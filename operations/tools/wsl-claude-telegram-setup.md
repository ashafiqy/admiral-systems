---
title: WSL2 + Claude Code + Telegram Bot Setup Guide
created: 2026-03-22
updated: 2026-03-22
tags:
  - type/sop
  - ops/tooling
status: active
---

# WSL2 + Claude Code + Telegram Bot Setup Guide

A complete guide to running Claude Code 24/7 on Windows 11 via WSL2, with a Telegram bot interface for sending commands and managing skills.

> See also: [[wsl-claude-slack-setup]] for the Slack bot companion guide, and [[remote-claude-architecture]] for the full system architecture.

---

## Table of Contents

1. [Install WSL2](#1-install-wsl2)
2. [Install Node.js and Claude Code](#2-install-nodejs-and-claude-code)
3. [Authenticate Claude Code](#3-authenticate-claude-code)
4. [Set Up GitHub SSH Access](#4-set-up-github-ssh-access)
5. [Clone Your Repos](#5-clone-your-repos)
6. [Create the CLAUDE.md File](#6-create-the-claudemd-file)
7. [Create the Telegram Bot](#7-create-the-telegram-bot)
8. [Create the Bot Script](#8-create-the-bot-script)
9. [Run the Bot as a Systemd Service](#9-run-the-bot-as-a-systemd-service)
10. [Keep WSL Alive 24/7](#10-keep-wsl-alive-247)
11. [Set Up tmux for Persistent Sessions](#11-set-up-tmux-for-persistent-sessions)
12. [Testing](#12-testing)
13. [Troubleshooting](#13-troubleshooting)

---

## 1. Install WSL2

Open PowerShell as Administrator:

```powershell
wsl --install -d Ubuntu-24.04
```

After installation, set your username and password when prompted. Then reboot if required.

---

## 2. Install Node.js and Claude Code

Open WSL (search "Ubuntu" in Start menu) and run:

```bash
# Update packages
sudo apt update && sudo apt upgrade -y

# Install essentials
sudo apt install -y git curl tmux openssh-server jq python3 python3-pip

# Install Node.js 20
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt install -y nodejs

# Verify Node
node --version
npm --version

# Install Claude Code globally
npm install -g @anthropic-ai/claude-code

# Verify Claude Code
claude --version
```

If `which claude` returns a Windows path (e.g. `/mnt/c/...`), the WSL npm global bin isn't in your PATH:

```bash
echo 'export PATH="$(npm config get prefix)/bin:$PATH"' >> ~/.bashrc
source ~/.bashrc
which claude
```

It should now return a Linux path like `/usr/bin/claude` or `/usr/local/bin/claude`.

---

## 3. Authenticate Claude Code

If you have a Claude Pro/Max subscription, use OAuth (no API key needed):

```bash
claude login
```

This opens a browser-based login flow. Authenticate with your Anthropic account.

If using the API instead, set your key:

```bash
echo 'export ANTHROPIC_API_KEY="sk-ant-your-key-here"' >> ~/.bashrc
source ~/.bashrc
```

---

## 4. Set Up GitHub SSH Access

### Generate an SSH key

```bash
mkdir -p ~/.ssh
chmod 700 ~/.ssh
ssh-keygen -t ed25519 -C "your-email@example.com" -f ~/.ssh/github_key
```

When prompted for a passphrase, press Enter twice (no passphrase). This is important — a passphrase will prevent the systemd service from authenticating.

### Configure SSH

```bash
cat >> ~/.ssh/config << 'EOF'
Host github.com
  HostName github.com
  User git
  IdentityFile ~/.ssh/github_key
  IdentitiesOnly yes
EOF
```

### Set Git to use the SSH key globally

This ensures the key works even when invoked from systemd services:

```bash
git config --global core.sshCommand "ssh -i /home/YOUR_USERNAME/.ssh/github_key -o IdentitiesOnly=yes"
```

Replace `YOUR_USERNAME` with your WSL username.

### Add the public key to GitHub

```bash
cat ~/.ssh/github_key.pub
```

1. Copy the output
2. Go to [github.com/settings/keys](https://github.com/settings/keys)
3. Click **New SSH key**
4. Title: "WSL2 Claude"
5. Paste the key, click **Add SSH key**

### Test the connection

```bash
ssh -T git@github.com
```

Type `yes` when asked about the host fingerprint. You should see: `Hi YourUsername! You've successfully authenticated...`

### Set default pull strategy

```bash
git config --global pull.ff only
```

---

## 5. Clone Your Repos

```bash
mkdir -p ~/repos && cd ~/repos

# Clone your repo (with submodules if any)
git clone --recurse-submodules git@github.com:YourUsername/your-repo.git
```

### Submodule setup

If your repo has submodules, verify the submodule remote is correct:

```bash
cd ~/repos/your-repo/your-submodule
git remote -v
```

If the remote URL is wrong, fix it:

```bash
git remote set-url origin git@github.com:YourUsername/your-submodule.git
```

Also update `.gitmodules` in the parent repo to use SSH URLs:

```bash
cd ~/repos/your-repo
nano .gitmodules
```

Change HTTPS URLs to SSH format:

```
[submodule "your-submodule"]
        path = your-submodule
        url = git@github.com:YourUsername/your-submodule.git
```

Then sync:

```bash
git submodule sync
```

### Verify branch tracking

Make sure your local branch tracks the correct remote branch:

```bash
git branch -a
git branch --set-upstream-to=origin/main main
```

---

## 6. Create the CLAUDE.md File

Create a `CLAUDE.md` in your repo root. Claude Code reads this automatically when invoked from that directory.

```bash
cat > ~/repos/your-repo/CLAUDE.md << 'EOF'
# Persona & Tone

Your persona instructions go here.

---

# Claude Guardrails

## Telegram Bot Mode

When invoked from the Telegram bot (non-interactive / -p flag):

### READ-ONLY by default

- You can ONLY read files, search code, and respond with information
- You CANNOT create, edit, delete, or modify any files
- You CANNOT run git push, git commit, or any write operations
- You CANNOT run npm install, pip install, or any install commands
- You CANNOT execute shell commands that modify the system

### Skills & Commands

- Write operations are ONLY permitted when explicitly invoked through a registered skill
- Skills require user confirmation via /confirm before execution
- Never attempt to bypass read-only restrictions
- If a user's question would require file modifications, explain what changes would be needed and suggest using the appropriate skill
EOF
```

---

## 7. Create the Telegram Bot

1. Open Telegram, search for **@BotFather**
2. Send `/newbot`
3. Give it a name (e.g., "Claude WSL Bot")
4. Give it a username (e.g., `claude_wsl_bot`)
5. Save the bot token (format: `7123456789:AAH...`)

### Get your Telegram user ID

1. Search for **@userinfobot** on Telegram
2. Send it any message
3. Save the user ID it returns (a number like `123456789`)

### Install Python dependencies

```bash
pip3 install python-telegram-bot --break-system-packages
```

---

## 8. Create the Bot Script

```bash
mkdir -p ~/scripts ~/logs
```

Create the bot script. Replace `YOUR_BOT_TOKEN_HERE` and `123456789` with your actual values. Replace `/usr/bin/claude` with the output of `which claude`. Replace `REPO_DIR` with your repo path.

```bash
cat > ~/scripts/telegram-claude-bot.py << 'PYEOF'
import subprocess
import os
import asyncio
from telegram import Update
from telegram.ext import Application, MessageHandler, CommandHandler, filters, ContextTypes

# ============================================================
# CONFIGURATION — UPDATE THESE VALUES
# ============================================================
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"
ALLOWED_USER_ID = 123456789
REPO_DIR = os.path.expanduser("~/repos/your-repo")
CLAUDE_PATH = "/usr/bin/claude"
MAX_MESSAGE_LENGTH = 4096

# ============================================================
# SKILLS REGISTRY — ADD YOUR SKILLS HERE
# ============================================================
SKILLS = {
    "sync": "Pull latest changes from GitHub and update submodules",
    "git-pull": "Pull latest changes from a specific repo in ~/repos/",
    "git-pull-sub": "Pull latest changes for a submodule within a repo",
}

# State
pending_skills = {}
conversation_history = []
MAX_HISTORY = 20

# ============================================================
# SYSTEM PROMPT — SENT WITH EVERY CLAUDE INVOCATION
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
# HANDLERS
# ============================================================

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return
    skills_list = "\n".join([f"  /skill {k} - {v}" for k, v in SKILLS.items()])
    await update.message.reply_text(
        "Claude WSL Bot (READ-ONLY MODE)\n\n"
        "Any message you send will be answered by Claude.\n"
        "Claude can ONLY read files and respond.\n"
        "It CANNOT create, edit, or delete anything.\n\n"
        "Commands:\n"
        "/repo - show repo status\n"
        "/skills - list available skills\n"
        f"/skill <name> - request a skill (requires confirmation)\n\n"
        f"Available skills:\n{skills_list}"
    )

async def handle_claude(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return

    user_message = update.message.text
    await update.message.reply_text("Thinking...")

    # Build conversation context from history
    context_parts = []
    if conversation_history:
        context_parts.append("Previous conversation:")
        for entry in conversation_history:
            context_parts.append(f"[You]: {entry['user']}")
            context_parts.append(f"[Bobbly]: {entry['assistant']}")
        context_parts.append("---")

    context_parts.append(f"Current message: {user_message}")
    full_prompt = "\n".join(context_parts)

    try:
        result = subprocess.run(
            [CLAUDE_PATH, "-p", full_prompt,
             "--output-format", "text",
             "--allowedTools", "Read,Glob,Grep,WebSearch,WebFetch",
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

    # Save this exchange to history
    conversation_history.append({
        "user": user_message,
        "assistant": output
    })

    # Trim to last MAX_HISTORY exchanges
    while len(conversation_history) > MAX_HISTORY:
        conversation_history.pop(0)

    # Send response, splitting if too long for Telegram
    for i in range(0, len(output), MAX_MESSAGE_LENGTH):
        chunk = output[i:i + MAX_MESSAGE_LENGTH]
        await update.message.reply_text(chunk)

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
    if not SKILLS:
        await update.message.reply_text("No skills registered yet.")
        return
    skills_list = "\n".join([f"• {k} - {v}" for k, v in SKILLS.items()])
    await update.message.reply_text(f"Available skills:\n\n{skills_list}\n\nUse /skill <name> to request one.")

async def request_skill(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_user.id != ALLOWED_USER_ID:
        return

    parts = update.message.text.split(maxsplit=2)
    if len(parts) < 2:
        await update.message.reply_text("Usage: /skill <name>\nUse /skills to see available skills.")
        return

    skill_name = parts[1].strip().lower()
    if skill_name not in SKILLS:
        await update.message.reply_text(f"Unknown skill: {skill_name}\nUse /skills to see available skills.")
        return

    skill_args = parts[2].strip() if len(parts) > 2 else None

    pending_skills[update.effective_user.id] = {
        "name": skill_name,
        "args": skill_args
    }

    args_display = f"\nArguments: {skill_args}" if skill_args else ""
    await update.message.reply_text(
        f"SKILL CONFIRMATION REQUIRED\n\n"
        f"Skill: {skill_name}\n"
        f"Description: {SKILLS[skill_name]}{args_display}\n\n"
        f"This skill CAN create, modify, or delete files.\n"
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

    try:
        if skill_name == "sync":
            result = subprocess.run(
                ["bash", "-c", "git fetch --all --prune && git pull --ff-only && git submodule update --remote --recursive"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=120
            )
            output = result.stdout + result.stderr

        elif skill_name == "git-pull":
            if not skill_args:
                output = "Usage: /skill git-pull <repo-name>\nExample: /skill git-pull sharkie"
            elif ".." in skill_args or "/" in skill_args:
                output = "Invalid repo name."
            else:
                repo_path = os.path.join(os.path.expanduser("~/repos"), skill_args)
                if not os.path.isdir(repo_path):
                    output = f"Repo not found: ~/repos/{skill_args}"
                else:
                    result = subprocess.run(
                        ["bash", "-c", "git pull --ff-only && git submodule update --remote --recursive"],
                        cwd=repo_path, capture_output=True, text=True, timeout=120
                    )
                    output = result.stdout + result.stderr

        elif skill_name == "git-pull-sub":
            if not skill_args:
                output = "Usage: /skill git-pull-sub <submodule-name>\nExample: /skill git-pull-sub admiral-systems"
            elif ".." in skill_args or "/" in skill_args:
                output = "Invalid submodule name."
            else:
                sub_path = os.path.join(REPO_DIR, skill_args)
                if not os.path.isdir(sub_path):
                    output = f"Submodule not found: {skill_args}"
                else:
                    result = subprocess.run(
                        ["bash", "-c", "git pull origin main --ff-only"],
                        cwd=sub_path, capture_output=True, text=True, timeout=120
                    )
                    output = result.stdout + result.stderr

        else:
            result = subprocess.run(
                [CLAUDE_PATH, "-p", f"Run the skill: {skill_name}", "--output-format", "text"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=300
            )
            output = result.stdout.strip() or result.stderr.strip()

    except subprocess.TimeoutExpired:
        output = "Skill timed out"
    except Exception as e:
        output = f"Error: {str(e)}"

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

# ============================================================
# MAIN
# ============================================================

def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("repo", repo_status))
    app.add_handler(CommandHandler("skills", list_skills))
    app.add_handler(CommandHandler("skill", request_skill))
    app.add_handler(CommandHandler("confirm", confirm_skill))
    app.add_handler(CommandHandler("cancel", cancel_skill))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_claude))

    print("Bot started (READ-ONLY mode)...")
    app.run_polling()

if __name__ == "__main__":
    main()
PYEOF
```

---

## 9. Run the Bot as a Systemd Service

First test the bot manually:

```bash
python3 ~/scripts/telegram-claude-bot.py
```

Send `/start` to your bot in Telegram. If it responds, stop it with `Ctrl+C` and create the service.

Find your Claude path (needed for the service PATH):

```bash
which claude
```

Create the service file (replace `YOUR_USERNAME` with your WSL username):

```bash
sudo tee /etc/systemd/system/telegram-claude.service << 'EOF'
[Unit]
Description=Telegram Claude Bot
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/scripts/telegram-claude-bot.py
Restart=always
RestartSec=10
Environment=PATH=/usr/local/bin:/usr/bin:/bin:/home/YOUR_USERNAME/.npm-global/bin
Environment=HOME=/home/YOUR_USERNAME

[Install]
WantedBy=multi-user.target
EOF
```

Enable and start:

```bash
sudo systemctl daemon-reload
sudo systemctl enable telegram-claude
sudo systemctl start telegram-claude
sudo systemctl status telegram-claude
```

Status should show `active (running)`.

### Service management commands

```bash
sudo systemctl stop telegram-claude        # stop the bot
sudo systemctl restart telegram-claude      # restart (after editing the script)
sudo systemctl status telegram-claude       # check status
sudo journalctl -u telegram-claude -n 50 --no-pager   # view logs
sudo journalctl -u telegram-claude -f      # live log tail
```

---

## 10. Keep WSL Alive 24/7

From **Windows PowerShell (Run as Admin)**:

### Create a startup task

Replace `Ubuntu-24.04` with your distro name if different:

```powershell
$action = New-ScheduledTaskAction -Execute "wsl.exe" -Argument "-d Ubuntu-24.04 -- bash -c 'sudo service ssh start && sleep infinity'"
$trigger = New-ScheduledTaskTrigger -AtStartup
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable
Register-ScheduledTask -TaskName "WSL2-KeepAlive" -Action $action -Trigger $trigger -Settings $settings -RunLevel Highest -User "$env:USERNAME"
```

### Prevent Windows from sleeping

```powershell
powercfg /change standby-timeout-ac 0
powercfg /change hibernate-timeout-ac 0
powercfg /change monitor-timeout-ac 30
```

---

## 11. Set Up tmux for Persistent Sessions

Inside WSL:

```bash
cat >> ~/.bashrc << 'EOF'

# Auto-create persistent Claude tmux session
if ! tmux has-session -t claude 2>/dev/null; then
  tmux new-session -d -s claude -c "$HOME/repos/your-repo"
fi
EOF
```

### tmux usage

```bash
tmux attach -t claude          # attach to your Claude session
tmux ls                        # list all sessions
```

### Running multiple Claude sessions

```bash
# Multiple tmux sessions
tmux new-session -d -s session1 -c "$HOME/repos/repo1"
tmux new-session -d -s session2 -c "$HOME/repos/repo2"
tmux attach -t session1

# Or use windows within one session (inside tmux):
# Ctrl+B then C      → new window
# Ctrl+B then 0-9    → switch windows
# Ctrl+B then W      → list windows

# Or split panes:
# Ctrl+B then %      → split vertically
# Ctrl+B then "      → split horizontally
# Ctrl+B then arrow  → switch panes

# Detach (leave running):
# Ctrl+B then D
```

---

## 12. Testing

From Telegram, test each feature:

| Command | Expected Result |
|---|---|
| `/start` | Shows help menu with available commands and skills |
| Any text message | Claude responds in read-only mode with conversation context |
| Follow-up message | Claude remembers the previous exchange |
| `/repo` | Shows `git status` of the repo |
| `/skills` | Lists all registered skills |
| `/skill git-pull your-repo` | Asks for confirmation |
| `/confirm` | Executes git pull, returns output |
| `/cancel` | Cancels a pending skill |
| `/skill git-pull-sub your-submodule` | Asks for confirmation, then pulls submodule |

---

## 13. Troubleshooting

### Bot keeps crashing (activating/auto-restart)

Check the logs for Python errors:

```bash
sudo journalctl -u telegram-claude -n 50 --no-pager
```

Common causes: missing commas, unclosed parentheses, wrong indentation in the Python script.

### "Permission denied (publickey)" when pulling from Telegram

The SSH key isn't accessible to the systemd service. Ensure:

1. The SSH key has **no passphrase**: `ssh-keygen -p -f ~/.ssh/github_key` (enter old passphrase, then Enter twice for empty)
2. Git is configured globally to use the key: `git config --global core.sshCommand "ssh -i /home/YOUR_USERNAME/.ssh/github_key -o IdentitiesOnly=yes"`
3. The service has `Environment=HOME=/home/YOUR_USERNAME` in the unit file

### "No such file or directory: claude"

Claude isn't in the service's PATH. Find it with `which claude` and either:
- Add its directory to the service's `Environment=PATH=...` line
- Use the full path in the bot script (replace `"claude"` with `"/usr/bin/claude"`)

### Local branch diverged from remote

```bash
cd ~/repos/your-repo
git reset --hard origin/main
```

### Submodule pointing to wrong remote

```bash
cd ~/repos/your-repo/your-submodule
git remote set-url origin git@github.com:YourUsername/correct-repo.git
cd ..
nano .gitmodules  # update the URL
git submodule sync
```

### Branch tracking misconfigured

```bash
git branch -a                                    # see all branches
git branch --set-upstream-to=origin/main main    # fix tracking
```

### WSL not staying alive after reboot

Verify the scheduled task exists in PowerShell (Admin):

```powershell
Get-ScheduledTask -TaskName "WSL2-KeepAlive"
```

If missing, re-create it (see Step 10).

### Bot responds but Claude times out

Increase the timeout in the bot script (default is 300 seconds / 5 minutes):

```python
timeout=600  # 10 minutes
```

### Conversation history too large causing timeouts

Reduce `MAX_HISTORY` in the bot script:

```python
MAX_HISTORY = 10  # 10 exchanges instead of 20
```
