import subprocess
import os
import re
import glob
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ============================================================
# CONFIGURATION — UPDATE THESE VALUES
# ============================================================
SLACK_BOT_TOKEN = "YOUR-SLACK-BOT-TOKEN"
SLACK_APP_TOKEN = "YOUR-SLACK-APP-TOKEN"
SLACK_USERS = [
    {"slack_id": "U08SWUP0UDV", "name": "Valentine"},
    {"slack_id": "U0142V7NALQ", "name": "Daz"},
    {"slack_id": "U06PJG1EJ6T", "name": "Rohan"},
    {"slack_id": "U019C2TKM4J", "name": "Davis"},
    {"slack_id": "U02A4CF2QAW", "name": "Sean Ng"},
    {"slack_id": "U0A8C0E3610", "name": "Shafiq"},
]
ALLOWED_USER_IDS = [user["slack_id"] for user in SLACK_USERS]
REPO_DIR = os.path.expanduser("~/repos/sharkie/admiral-systems")
CLAUDE_PATH = "/usr/bin/claude"
MAX_MESSAGE_LENGTH = 3000

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
    """Scan .claude/commands/skill-*.md and parse bot-skill metadata."""
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
            logger.error(f"Failed to load skill from {filepath}: {e}")


def get_all_skills():
    """Return merged dict of skill_name -> description for display."""
    skills = {}
    for name, info in SHELL_SKILLS.items():
        skills[name] = info["description"]
    for name, info in CLAUDE_SKILLS.items():
        skills[name] = info["description"]
    return skills


def get_skill_type(skill_name):
    """Return the type of a skill: 'query', 'action', or 'shell'."""
    if skill_name in SHELL_SKILLS:
        return "shell"
    if skill_name in CLAUDE_SKILLS:
        return CLAUDE_SKILLS[skill_name]["type"]
    return None


# ============================================================
# STATE — THREAD-AWARE CONVERSATION TRACKING
# ============================================================
conversation_history = {}
pending_skills = {}
MAX_HISTORY = 20

# ============================================================
# LOGGING
# ============================================================
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler(os.path.expanduser("~/logs/slack-claude-bot.log")),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# ============================================================
# SYSTEM PROMPT
# ============================================================
SYSTEM_PROMPT = (
    "You are running in Slack read-only mode. "
    "You CANNOT use Bash, Edit, Write, or any write tools. "
    "Do not ask the user to approve or allow tool usage — "
    "you physically cannot run write commands. "
    "If a task requires file changes, git operations, or any write action, "
    "tell the user to mention you with 'skills' to see available skills. "
    "Keep responses concise. "
    "IMPORTANT: Format all responses using Slack mrkdwn syntax, NOT markdown. "
    "Slack formatting rules: "
    "Use *bold* for headers and emphasis (not ## or ###). "
    "Use _italic_ for secondary emphasis. "
    "Use `code` for inline code and ```code``` for code blocks. "
    "Use > for block quotes. "
    "Use bullet points with • or -. "
    "Use blank lines between sections for visual separation. "
    "Use emoji like :white_check_mark: :warning: :red_circle: for status indicators. "
    "NEVER use # headers, --- dividers, or **double asterisk bold** (use *single asterisk* instead). "
    "Keep lines short — Slack wraps awkwardly on mobile with long lines."
)

# ============================================================
# INITIALIZE SLACK APP
# ============================================================
app = App(token=SLACK_BOT_TOKEN)

# ============================================================
# HELPER FUNCTIONS
# ============================================================


def get_thread_key(user_id, thread_ts):
    return (user_id, thread_ts)


def get_history(user_id, thread_ts):
    key = get_thread_key(user_id, thread_ts)
    if key not in conversation_history:
        conversation_history[key] = []
    return conversation_history[key]


def add_to_history(user_id, thread_ts, user_message, assistant_response):
    history = get_history(user_id, thread_ts)
    history.append({"user": user_message, "assistant": assistant_response})
    while len(history) > MAX_HISTORY:
        history.pop(0)


def strip_bot_mention(text):
    return re.sub(r"<@[A-Z0-9]+>\s*", "", text).strip()


def send_chunked(say, text, thread_ts):
    if not text:
        text = "No output"
    for i in range(0, len(text), MAX_MESSAGE_LENGTH):
        chunk = text[i:i + MAX_MESSAGE_LENGTH]
        say(text=chunk, thread_ts=thread_ts)


def is_allowed(user_id):
    return user_id in ALLOWED_USER_IDS


def run_claude(prompt, thread_ts, user_id, tools="Read,Glob,Grep,WebSearch,WebFetch"):
    """Invoke Claude Code and return the output."""
    history = get_history(user_id, thread_ts)

    context_parts = []
    if history:
        context_parts.append("Previous conversation in this thread:")
        for entry in history:
            context_parts.append(f"[User]: {entry['user']}")
            context_parts.append(f"[Assistant]: {entry['assistant']}")
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

    add_to_history(user_id, thread_ts, prompt, output)
    return output


def execute_shell_skill(skill_name, skill_args):
    """Execute a hardcoded shell skill."""
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
                return "Usage: `@bot skill git-pull <repo-name>`\nExample: `@bot skill git-pull sharkie`"
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
                return "Usage: `@bot skill git-pull-sub <submodule-name>`\nExample: `@bot skill git-pull-sub admiral-systems`"
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
    """Execute a dynamically loaded Claude skill."""
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
    """Route to shell or Claude skill execution."""
    if skill_name in SHELL_SKILLS:
        return execute_shell_skill(skill_name, skill_args)
    elif skill_name in CLAUDE_SKILLS:
        return execute_claude_skill(skill_name, skill_args)
    else:
        return f"Unknown skill: {skill_name}"


def parse_command(text):
    """Parse cleaned message text into (command, arg1, arg2)."""
    text = text.strip()
    lower = text.lower()

    # Direct query skill invocation (no "skill" prefix needed)
    for skill_name in CLAUDE_SKILLS:
        if CLAUDE_SKILLS[skill_name]["type"] == "query":
            if lower == skill_name or lower.startswith(skill_name + " "):
                args = text[len(skill_name):].strip() or None
                return ("query_skill", skill_name, args)

    if lower.startswith("skill "):
        remainder = text[6:].strip()
        parts = remainder.split(maxsplit=1)
        skill_name = parts[0].lower() if parts else ""
        skill_args = parts[1].strip() if len(parts) > 1 else None
        return ("skill", skill_name, skill_args)
    elif lower == "skills":
        return ("skills", None, None)
    elif lower == "confirm":
        return ("confirm", None, None)
    elif lower == "cancel":
        return ("cancel", None, None)
    elif lower == "repo":
        return ("repo", None, None)
    elif lower == "reload":
        return ("reload", None, None)
    else:
        return (None, text, None)


def get_pending_key(user_id, thread_ts):
    return (user_id, thread_ts)


# ============================================================
# EVENT HANDLERS
# ============================================================

@app.event("app_mention")
def handle_mention(event, say):
    user_id = event.get("user", "")
    if not is_allowed(user_id):
        say(text="Sorry, you are not authorized to use this bot.", thread_ts=event.get("ts"))
        return

    raw_text = event.get("text", "")
    text = strip_bot_mention(raw_text)
    thread_ts = event.get("thread_ts", event.get("ts"))

    logger.info(f"Mention from {user_id} in thread {thread_ts}: {text}")

    command, arg1, arg2 = parse_command(text)

    if command == "query_skill":
        handle_query_skill(say, user_id, thread_ts, arg1, arg2)
    elif command == "skills":
        handle_skills_list(say, thread_ts)
    elif command == "skill":
        handle_skill_request(say, user_id, thread_ts, arg1, arg2)
    elif command == "confirm":
        handle_confirm(say, user_id, thread_ts)
    elif command == "cancel":
        handle_cancel(say, user_id, thread_ts)
    elif command == "repo":
        handle_repo(say, thread_ts)
    elif command == "reload":
        handle_reload(say, thread_ts)
    else:
        handle_freeform(say, user_id, thread_ts, arg1)


@app.event("message")
def handle_dm(event, say):
    if event.get("subtype"):
        return
    user_id = event.get("user", "")
    if not is_allowed(user_id):
        return
    text = event.get("text", "").strip()
    thread_ts = event.get("thread_ts", event.get("ts"))

    logger.info(f"DM from {user_id} in thread {thread_ts}: {text}")

    command, arg1, arg2 = parse_command(text)

    if command == "query_skill":
        handle_query_skill(say, user_id, thread_ts, arg1, arg2)
    elif command == "skills":
        handle_skills_list(say, thread_ts)
    elif command == "skill":
        handle_skill_request(say, user_id, thread_ts, arg1, arg2)
    elif command == "confirm":
        handle_confirm(say, user_id, thread_ts)
    elif command == "cancel":
        handle_cancel(say, user_id, thread_ts)
    elif command == "repo":
        handle_repo(say, thread_ts)
    elif command == "reload":
        handle_reload(say, thread_ts)
    else:
        handle_freeform(say, user_id, thread_ts, arg1)


# ============================================================
# COMMAND IMPLEMENTATIONS
# ============================================================

def handle_query_skill(say, user_id, thread_ts, skill_name, skill_args):
    """Execute a query skill immediately — no confirmation needed."""
    say(text=f"Running `{skill_name}`...", thread_ts=thread_ts)
    logger.info(f"Query skill '{skill_name}' for user {user_id} (args: {skill_args})")
    output = execute_claude_skill(skill_name, skill_args)
    send_chunked(say, output, thread_ts)


def handle_skills_list(say, thread_ts):
    """List all registered skills, grouped by type."""
    all_skills = get_all_skills()
    if not all_skills:
        say(text="No skills registered yet.", thread_ts=thread_ts)
        return

    lines = ["*Available skills:*\n"]

    query_skills = {k: v for k, v in CLAUDE_SKILLS.items() if v["type"] == "query"}
    if query_skills:
        lines.append("*Query skills* (instant, no confirmation):")
        for name, info in query_skills.items():
            lines.append(f"  `{name}` — {info['description']}")
        lines.append("")

    action_skills = {}
    for name, info in SHELL_SKILLS.items():
        action_skills[name] = info["description"]
    for name, info in CLAUDE_SKILLS.items():
        if info["type"] == "action":
            action_skills[name] = info["description"]
    if action_skills:
        lines.append("*Action skills* (require `confirm`):")
        for name, desc in action_skills.items():
            lines.append(f"  `skill {name}` — {desc}")
        lines.append("")

    lines.append("_Query: `@bot project-status hop-lun`_")
    lines.append("_Action: `@bot skill sync` → `@bot confirm`_")
    lines.append("_Reload skills: `@bot reload`_")

    say(text="\n".join(lines), thread_ts=thread_ts)


def handle_skill_request(say, user_id, thread_ts, skill_name, skill_args):
    """Request an action/shell skill, pending confirmation."""
    all_skills = get_all_skills()
    if not skill_name:
        say(text="Usage: `@bot skill <name>`\nSay `@bot skills` to see the list.",
            thread_ts=thread_ts)
        return

    if skill_name not in all_skills:
        say(text=f"Unknown skill: `{skill_name}`\nSay `@bot skills` to see available skills.",
            thread_ts=thread_ts)
        return

    skill_type = get_skill_type(skill_name)
    if skill_type == "query":
        handle_query_skill(say, user_id, thread_ts, skill_name, skill_args)
        return

    pkey = get_pending_key(user_id, thread_ts)
    pending_skills[pkey] = {"name": skill_name, "args": skill_args}

    args_display = f"\n*Arguments:* `{skill_args}`" if skill_args else ""
    say(
        text=(
            f":warning: *SKILL CONFIRMATION REQUIRED*\n\n"
            f"*Skill:* `{skill_name}`\n"
            f"*Description:* {all_skills[skill_name]}{args_display}\n\n"
            f"This skill CAN modify files or external systems.\n"
            f"Say `@bot confirm` to execute or `@bot cancel` to abort."
        ),
        thread_ts=thread_ts
    )


def handle_confirm(say, user_id, thread_ts):
    pkey = get_pending_key(user_id, thread_ts)
    if pkey not in pending_skills:
        say(text="No pending skill to confirm in this thread.", thread_ts=thread_ts)
        return
    skill_data = pending_skills.pop(pkey)
    skill_name = skill_data["name"]
    skill_args = skill_data.get("args")
    say(text=f"Running skill: `{skill_name}`...", thread_ts=thread_ts)
    logger.info(f"Executing skill '{skill_name}' for user {user_id} (args: {skill_args})")
    output = execute_skill(skill_name, skill_args)
    send_chunked(say, output, thread_ts)


def handle_cancel(say, user_id, thread_ts):
    pkey = get_pending_key(user_id, thread_ts)
    if pkey not in pending_skills:
        say(text="No pending skill to cancel in this thread.", thread_ts=thread_ts)
        return
    skill_data = pending_skills.pop(pkey)
    say(text=f"Cancelled skill: `{skill_data['name']}`", thread_ts=thread_ts)


def handle_repo(say, thread_ts):
    try:
        result = subprocess.run(
            ["git", "status", "--short", "--branch"],
            cwd=REPO_DIR, capture_output=True, text=True, timeout=30
        )
        output = result.stdout.strip() or "No output"
    except Exception as e:
        output = f"Error: {str(e)}"
    say(text=f"```\n{output}\n```", thread_ts=thread_ts)


def handle_reload(say, thread_ts):
    """Reload Claude skills from disk (after git pull)."""
    load_claude_skills()
    count = len(CLAUDE_SKILLS)
    say(text=f"Reloaded skills from `.claude/commands/`. Found {count} Claude skill(s).",
        thread_ts=thread_ts)


def handle_freeform(say, user_id, thread_ts, text):
    say(text="Thinking...", thread_ts=thread_ts)
    output = run_claude(text, thread_ts, user_id)
    send_chunked(say, output, thread_ts)


# ============================================================
# MAIN
# ============================================================

def main():
    load_claude_skills()
    logger.info(f"Loaded {len(CLAUDE_SKILLS)} Claude skills + {len(SHELL_SKILLS)} shell skills")
    logger.info("Slack Claude bot starting (READ-ONLY mode)...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()


if __name__ == "__main__":
    main()
