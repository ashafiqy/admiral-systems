import subprocess
import os
import re
import glob
import random
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

# ============================================================
# CONFIGURATION — UPDATE THESE VALUES
# ============================================================
BOT_TOKEN = "YOUR-TELEGRAM-BOT-TOKEN"
ALLOWED_USER_ID = 54462035
REPO_DIR = os.path.expanduser("~/repos/sharkie/admiral-systems")
CLAUDE_PATH = "/usr/bin/claude"
MAX_MESSAGE_LENGTH = 4096

# ============================================================
# SHELL SKILLS — HARDCODED (execute shell commands, not Claude)
# ============================================================
SHELL_SKILLS = {
    "sync": {
        "description": "Pull latest changes from GitHub and update submodules",
        "type": "action",
    },
    "git-pull": {
        "description": "Pull latest changes from a specific repo in ~/repos/",
        "type": "action",
    },
    "git-pull-sub": {
        "description": "Pull latest changes for a submodule within a repo",
        "type": "action",
    },
}

# ============================================================
# CLAUDE SKILLS — DYNAMICALLY LOADED FROM .claude/commands/
# ============================================================
CLAUDE_SKILLS = {}


def load_claude_skills():
    global CLAUDE_SKILLS
    CLAUDE_SKILLS = {}
    pattern = os.path.join(REPO_DIR, ".claude", "commands", "skill-*.md")
    for filepath in sorted(glob.glob(pattern)):
        try:
            with open(filepath, "r") as f:
                content = f.read()
            match = re.search(r"<!--\s*bot-skill\s*(.*?)-->", content, re.DOTALL)
            if not match:
                continue
            meta = {}
            for line in match.group(1).strip().split("\n"):
                if ":" in line:
                    key, val = line.split(":", 1)
                    meta[key.strip()] = val.strip()
            if "name" in meta:
                prompt_text = content.split("-->", 1)[1].strip() if "-->" in content else ""
                CLAUDE_SKILLS[meta["name"]] = {
                    "description": meta.get("description", "No description"),
                    "type": meta.get("type", "query"),
                    "tools": meta.get("tools", "Read,Glob,Grep"),
                    "filepath": filepath,
                    "prompt": prompt_text,
                }
        except Exception as e:
            print(f"Failed to load skill from {filepath}: {e}")


def get_all_skills():
    skills = {}
    for name, info in SHELL_SKILLS.items():
        skills[name] = info["description"]
    for name, info in CLAUDE_SKILLS.items():
        skills[name] = info["description"]
    return skills


def get_skill_type(skill_name):
    if skill_name in SHELL_SKILLS:
        return "shell"
    if skill_name in CLAUDE_SKILLS:
        return CLAUDE_SKILLS[skill_name]["type"]
    return None


# ============================================================
# STATE
# ============================================================
pending_skills = {}
conversation_history = []
MAX_HISTORY = 20

# ============================================================
# SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = (
    "You are running in Telegram read-only mode. "
    "You CANNOT use Bash, Edit, Write, or any write tools. "
    "Do not ask the user to approve or allow tool usage — "
    "you physically cannot run write commands. "
    "If a task requires file changes, git operations, or any write action, "
    "tell the user to use /skills to see available skills. "
    "Keep responses concise."
)

# ============================================================
# HELPER FUNCTIONS
# ============================================================


def run_claude(prompt, tools="Read,Glob,Grep,WebSearch,WebFetch"):
    context_parts = []
    if conversation_history:
        context_parts.append("Previous conversation:")
        for entry in conversation_history:
            context_parts.append(f"[You]: {entry['user']}")
            context_parts.append(f"[Claude]: {entry['assistant']}")
        context_parts.append("---")
    context_parts.append(f"Current message: {prompt}")
    full_prompt = "\n".join(context_parts)

    try:
        result = subprocess.run(
            [CLAUDE_PATH, "-p", full_prompt,
             "--output-format", "text",
             "--allowedTools", tools,
             "--system-prompt", SYSTEM_PROMPT],
            cwd=REPO_DIR,
            capture_output=True,
            text=True,
            timeout=300
        )
        output = result.stdout.strip() or result.stderr.strip() or "No output"
    except subprocess.TimeoutExpired:
        output = "Timed out after 5 minutes"
    except Exception as e:
        output = f"Error: {str(e)}"
    return output


def execute_shell_skill(skill_name, skill_args):
    try:
        if skill_name == "sync":
            result = subprocess.run(
                ["bash", "-c",
                 "git fetch --all --prune && git pull --ff-only && git submodule update --remote --recursive"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=120
            )
            return result.stdout + result.stderr

        elif skill_name == "git-pull":
            if not skill_args:
                return "Usage: /skill git-pull <repo-name>\nExample: /skill git-pull sharkie"
            if ".." in skill_args or "/" in skill_args:
                return "Invalid repo name."
            repo_path = os.path.join(os.path.expanduser("~/repos"), skill_args)
            if not os.path.isdir(repo_path):
                return f"Repo not found: ~/repos/{skill_args}"
            result = subprocess.run(
                ["bash", "-c",
                 "git pull --ff-only && git submodule update --remote --recursive"],
                cwd=repo_path, capture_output=True, text=True, timeout=120
            )
            return result.stdout + result.stderr

        elif skill_name == "git-pull-sub":
            if not skill_args:
                return "Usage: /skill git-pull-sub <submodule-name>\nExample: /skill git-pull-sub admiral-systems"
            if ".." in skill_args or "/" in skill_args:
                return "Invalid submodule name."
            sub_path = os.path.join(REPO_DIR, skill_args)
            if not os.path.isdir(sub_path):
                return f"Submodule not found: {skill_args}"
            result = subprocess.run(
                ["bash", "-c", "git pull origin main --ff-only"],
                cwd=sub_path, capture_output=True, text=True, timeout=120
            )
            return result.stdout + result.stderr

    except subprocess.TimeoutExpired:
        return "Skill timed out"
    except Exception as e:
        return f"Error: {str(e)}"
    return "Unknown shell skill"


def execute_claude_skill(skill_name, skill_args):
    skill = CLAUDE_SKILLS[skill_name]
    prompt = skill["prompt"].replace("$ARGS", skill_args or "all")
    try:
        result = subprocess.run(
            [CLAUDE_PATH, "-p", prompt,
             "--output-format", "text",
             "--allowedTools", skill["tools"]],
            cwd=REPO_DIR, capture_output=True, text=True, timeout=300
        )
        return result.stdout.strip() or result.stderr.strip() or "No output"
    except subprocess.TimeoutExpired:
        return "Skill timed out"
    except Exception as e:
        return f"Error: {str(e)}"


def execute_skill(skill_name, skill_args):
    if skill_name in SHELL_SKILLS:
        return execute_shell_skill(skill_name, skill_args)
    elif skill_name in CLAUDE_SKILLS:
        return execute_claude_skill(skill_name, skill_args)
    return f"Unknown skill: {skill_name}"


# ============================================================
# TELEGRAM HANDLERS
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    all_skills = get_all_skills()
    skills_list = "\n".join([f"  /skill {k} - {v}" for k, v in all_skills.items()])

    query_cmds = [f"  {name}" for name, info in CLAUDE_SKILLS.items() if info["type"] == "query"]
    query_list = "\n".join(query_cmds) if query_cmds else "  (none loaded)"

    await update.message.reply_text(
        "Claude WSL Bot (READ-ONLY MODE)\n\n"
        "Query commands (instant, no confirmation):\n"
        f"{query_list}\n\n"
        "Action skills (require /confirm):\n"
        f"{skills_list}\n\n"
        "Other commands:\n"
        "/repo - show repo status\n"
        "/skills - list all skills\n"
        "/reload - reload skills from disk\n"
    )


async def handle_claude(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    user_message = update.message.text

    # Check if it matches a query skill name
    lower = user_message.strip().lower()
    for skill_name, info in CLAUDE_SKILLS.items():
        if info["type"] == "query" and (lower == skill_name or lower.startswith(skill_name + " ")):
            args = user_message.strip()[len(skill_name):].strip() or None
            await update.message.reply_text(f"Running {skill_name}...")
            output = execute_claude_skill(skill_name, args)
            for i in range(0, len(output), MAX_MESSAGE_LENGTH):
                await update.message.reply_text(output[i:i + MAX_MESSAGE_LENGTH])
            return

    # Regular freeform message
    replies = ["Thinking...", "Pondering...", "Wondering...", "Dreaming..."]
    await update.message.reply_text(random.choice(replies))

    output = run_claude(user_message)

    conversation_history.append({"user": user_message, "assistant": output})
    while len(conversation_history) > MAX_HISTORY:
        conversation_history.pop(0)

    for i in range(0, len(output), MAX_MESSAGE_LENGTH):
        await update.message.reply_text(output[i:i + MAX_MESSAGE_LENGTH])


async def repo_status(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    result = subprocess.run(
        ["git", "status", "--short", "--branch"],
        cwd=REPO_DIR, capture_output=True, text=True
    )
    await update.message.reply_text(f"```\n{result.stdout}\n```", parse_mode="Markdown")


async def list_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    all_skills = get_all_skills()
    if not all_skills:
        await update.message.reply_text("No skills registered yet.")
        return

    lines = ["Available skills:\n"]

    query_skills = {k: v for k, v in CLAUDE_SKILLS.items() if v["type"] == "query"}
    if query_skills:
        lines.append("Query (instant, no confirmation):")
        for name, info in query_skills.items():
            lines.append(f"  {name} — {info['description']}")
        lines.append("")

    action_skills = {}
    for name, info in SHELL_SKILLS.items():
        action_skills[name] = info["description"]
    for name, info in CLAUDE_SKILLS.items():
        if info["type"] == "action":
            action_skills[name] = info["description"]
    if action_skills:
        lines.append("Action (require /confirm):")
        for name, desc in action_skills.items():
            lines.append(f"  /skill {name} — {desc}")

    await update.message.reply_text("\n".join(lines))


async def request_skill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    parts = update.message.text.split(maxsplit=2)
    if len(parts) < 2:
        await update.message.reply_text("Usage: /skill <name>\nUse /skills to see available skills.")
        return

    skill_name = parts[1].strip().lower()
    all_skills = get_all_skills()
    if skill_name not in all_skills:
        await update.message.reply_text(f"Unknown skill: {skill_name}\nUse /skills to see available skills.")
        return

    skill_args = parts[2].strip() if len(parts) > 2 else None

    # Query skills execute immediately
    skill_type = get_skill_type(skill_name)
    if skill_type == "query":
        await update.message.reply_text(f"Running {skill_name}...")
        output = execute_claude_skill(skill_name, skill_args)
        for i in range(0, len(output), MAX_MESSAGE_LENGTH):
            await update.message.reply_text(output[i:i + MAX_MESSAGE_LENGTH])
        return

    pending_skills[update.effective_user.id] = {"name": skill_name, "args": skill_args}
    args_display = f"\nArguments: {skill_args}" if skill_args else ""
    await update.message.reply_text(
        f"SKILL CONFIRMATION REQUIRED\n\n"
        f"Skill: {skill_name}\n"
        f"Description: {all_skills[skill_name]}{args_display}\n\n"
        f"This skill CAN modify files or external systems.\n"
        f"Type /confirm to execute or /cancel to abort."
    )


async def confirm_skill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    user_id = update.effective_user.id
    if user_id not in pending_skills:
        await update.message.reply_text("No pending skill to confirm.")
        return
    skill_data = pending_skills.pop(user_id)
    skill_name = skill_data["name"]
    skill_args = skill_data.get("args")
    await update.message.reply_text(f"Running skill: {skill_name}...")
    output = execute_skill(skill_name, skill_args)
    for i in range(0, len(output), MAX_MESSAGE_LENGTH):
        await update.message.reply_text(output[i:i + MAX_MESSAGE_LENGTH])


async def cancel_skill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    if update.effective_user.id in pending_skills:
        skill_data = pending_skills.pop(update.effective_user.id)
        await update.message.reply_text(f"Cancelled skill: {skill_data['name']}")
    else:
        await update.message.reply_text("No pending skill to cancel.")


async def reload_skills(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    load_claude_skills()
    count = len(CLAUDE_SKILLS)
    await update.message.reply_text(f"Reloaded skills. Found {count} Claude skill(s).")


# ============================================================
# MAIN
# ============================================================

def main():
    load_claude_skills()
    print(f"Loaded {len(CLAUDE_SKILLS)} Claude skills + {len(SHELL_SKILLS)} shell skills")
    print("Bot started (READ-ONLY mode)...")

    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("repo", repo_status))
    app.add_handler(CommandHandler("skills", list_skills))
    app.add_handler(CommandHandler("skill", request_skill))
    app.add_handler(CommandHandler("confirm", confirm_skill))
    app.add_handler(CommandHandler("cancel", cancel_skill))
    app.add_handler(CommandHandler("reload", reload_skills))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_claude))

    app.run_polling()


if __name__ == "__main__":
    main()
