---
title: WSL2 + Claude Code + Slack Bot Setup Guide
created: 2026-03-22
updated: 2026-03-22
tags:
  - type/sop
  - ops/tooling
status: active
---

# WSL2 + Claude Code + Slack Bot Setup Guide

A complete guide to running Claude Code as a Slack bot on WSL2, with @mention-based interaction for team-visible, channel-based usage.

> See also: [[wsl-claude-telegram-setup]] for the Telegram bot companion guide (personal, /command-based), and [[remote-claude-architecture]] for the full system architecture.

---

## Table of Contents

1. [Prerequisites](#1-prerequisites)
2. [Create the Slack App](#2-create-the-slack-app)
3. [Get Your Allowed User IDs](#3-get-your-allowed-user-ids)
4. [Create the Bot Script](#4-create-the-bot-script)
5. [Run as systemd Service](#5-run-as-systemd-service)
6. [Testing](#6-testing)
7. [Troubleshooting](#7-troubleshooting)

---

## 1. Prerequisites

This guide assumes you already have WSL2 running with Claude Code installed. If not, follow [[wsl-claude-telegram-setup]] sections 1 through 6 first (WSL2 install, Node.js, Claude Code, GitHub SSH, repo cloning, and CLAUDE.md setup).

The only additional dependency needed is the Slack Bolt SDK:

```bash
pip3 install slack_bolt --break-system-packages
```

Verify the install:

```bash
python3 -c "from slack_bolt import App; print('slack_bolt installed')"
```

---

## 2. Create the Slack App

### Step 1: Create a new app

1. Go to [api.slack.com/apps](https://api.slack.com/apps)
2. Click **Create New App**
3. Select **From scratch**
4. App Name: `Claude WSL Bot` (or whatever you prefer)
5. Pick your workspace from the dropdown
6. Click **Create App**

### Step 2: Enable Socket Mode

Socket Mode lets the bot receive events over a WebSocket connection instead of requiring a public URL. This is ideal for running behind WSL2 on a local machine.

1. In the left sidebar, click **Socket Mode**
2. Toggle **Enable Socket Mode** to ON
3. You will be prompted to generate an App-Level Token
4. Token Name: `socket-mode-token`
5. Add the scope: `connections:write`
6. Click **Generate**
7. Copy and save the **App-Level Token** (starts with `xapp-`)

### Step 3: Add Bot Token Scopes

1. In the left sidebar, click **OAuth & Permissions**
2. Scroll down to **Scopes** > **Bot Token Scopes**
3. Click **Add an OAuth Scope** and add each of the following:
   - `app_mentions:read` — lets the bot see when someone @mentions it
   - `chat:write` — lets the bot send messages
   - `channels:history` — lets the bot read messages in public channels it is in
   - `groups:history` — lets the bot read messages in private channels it is in
   - `im:history` — lets the bot read direct messages
   - `im:read` — lets the bot see DM metadata
   - `channels:read` — lets the bot see public channel info
   - `groups:read` — lets the bot see private channel info

### Step 4: Subscribe to events

1. In the left sidebar, click **Event Subscriptions**
2. Toggle **Enable Events** to ON
3. Under **Subscribe to bot events**, click **Add Bot User Event** and add:
   - `app_mention` — fires when someone @mentions the bot in a channel
   - `message.im` — fires when someone sends a DM to the bot
4. Click **Save Changes**

### Step 5: Install to workspace

1. In the left sidebar, click **Install App**
2. Click **Install to Workspace**
3. Review the permissions and click **Allow**
4. Copy and save the **Bot User OAuth Token** (starts with `xoxb-`)

### Step 6: Invite the bot to channels

In Slack, go to each channel where you want the bot available and type:

```
/invite @Claude WSL Bot
```

The bot will only respond to @mentions in channels it has been invited to.

---

## 3. Get Your Allowed User IDs

The bot restricts who can interact with it using Slack user IDs. To find a user's ID:

1. In Slack, click on the person's profile picture or name
2. Click **View full profile**
3. Click the **three dots** menu (More)
4. Click **Copy member ID**

The ID looks like `U04A1B2C3D4`. Collect IDs for each person who should be allowed to use the bot.
```
Allowed IDs
# Valentine
U08SWUP0UDV
# Daz
U0142V7NALQ
# Rohan
U06PJG1EJ6T
# Davis
U019C2TKM4J
# Sean Ng
U02A4CF2QAW
# Shafiq
U0A8C0E3610
```

---

## 4. Create the Bot Script

Create the scripts and logs directories if they do not already exist:

```bash
mkdir -p ~/scripts ~/logs
```

Create the bot script. Replace the token values, allowed user IDs, repo path, and Claude path with your actual values. Find your Claude path with `which claude`.

```bash
cat > ~/scripts/slack-claude-bot.py << 'PYEOF'
import subprocess
import os
import re
import logging
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler

# ============================================================
# CONFIGURATION — UPDATE THESE VALUES
# ============================================================
SLACK_BOT_TOKEN = "xoxb-your-bot-token"
SLACK_APP_TOKEN = "xapp-your-app-token"
SLACK_USERS = [
    {"slack_id": "U08SWUP0UDV", "name": "Valentine"},
    {"slack_id": "U0142V7NALQ", "name": "Daz"},
    {"slack_id": "U06PJG1EJ6T", "name": "Rohan"},
    {"slack_id": "U019C2TKM4J", "name": "Davis"},
    {"slack_id": "U02A4CF2QAW", "name": "Sean Ng"},
    {"slack_id": "U0A8C0E3610", "name": "Shafiq"},
]
ALLOWED_USER_IDS = [user["slack_id"] for user in SLACK_USERS]
REPO_DIR = os.path.expanduser("~/repos/your-repo")
CLAUDE_PATH = "/usr/bin/claude"
MAX_MESSAGE_LENGTH = 3000  # Slack's limit is lower than Telegram

# ============================================================
# SKILLS REGISTRY — ADD YOUR SKILLS HERE
# ============================================================
SKILLS = {
    "sync": "Pull latest changes from GitHub and update submodules",
    "git-pull": "Pull latest changes from a specific repo in ~/repos/",
    "git-pull-sub": "Pull latest changes for a submodule within a repo",
    "vault-status": "Show vault health — last updated files, stale notes",
    "client-brief": "Pull a client summary from the vault",
    "etl-sync": "Trigger ETL processing for recent sources",
}

# ============================================================
# STATE — THREAD-AWARE CONVERSATION TRACKING
# ============================================================
# Key: (user_id, thread_ts) — each thread gets its own context
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
# SYSTEM PROMPT — SENT WITH EVERY CLAUDE INVOCATION
# ============================================================
SYSTEM_PROMPT = (
    "You are running in Slack read-only mode. "
    "You CANNOT use Bash, Edit, Write, or any write tools. "
    "Do not ask the user to approve or allow tool usage — "
    "you physically cannot run write commands. "
    "If a task requires file changes, git operations, or any write action, "
    "tell the user to mention you with 'skills' to see available skills. "
    "Keep responses concise."
)

# ============================================================
# INITIALIZE SLACK APP
# ============================================================
app = App(token=SLACK_BOT_TOKEN)

# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_thread_key(user_id, thread_ts):
    """Build a unique key for per-user, per-thread conversation tracking."""
    return (user_id, thread_ts)


def get_history(user_id, thread_ts):
    """Retrieve conversation history for a specific user and thread."""
    key = get_thread_key(user_id, thread_ts)
    if key not in conversation_history:
        conversation_history[key] = []
    return conversation_history[key]


def add_to_history(user_id, thread_ts, user_message, assistant_response):
    """Append an exchange to the thread's conversation history."""
    history = get_history(user_id, thread_ts)
    history.append({
        "user": user_message,
        "assistant": assistant_response
    })
    while len(history) > MAX_HISTORY:
        history.pop(0)


def strip_bot_mention(text):
    """Remove the <@BOT_ID> mention from the beginning of a message."""
    return re.sub(r"<@[A-Z0-9]+>\s*", "", text).strip()


def send_chunked(say, text, thread_ts):
    """Send a message in chunks that respect Slack's character limit."""
    if not text:
        text = "No output"
    for i in range(0, len(text), MAX_MESSAGE_LENGTH):
        chunk = text[i:i + MAX_MESSAGE_LENGTH]
        say(text=chunk, thread_ts=thread_ts)


def is_allowed(user_id):
    """Check whether a user is in the allowed list."""
    return user_id in ALLOWED_USER_IDS


def run_claude(prompt, thread_ts, user_id):
    """Invoke Claude Code in read-only mode and return the output."""
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

    add_to_history(user_id, thread_ts, prompt, output)
    return output


def execute_skill(skill_name, skill_args):
    """Execute a confirmed skill and return the output string."""
    try:
        if skill_name == "sync":
            result = subprocess.run(
                ["bash", "-c",
                 "git fetch --all --prune && git pull --ff-only && git submodule update --remote --recursive"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=120
            )
            output = result.stdout + result.stderr

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
            output = result.stdout + result.stderr

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
            output = result.stdout + result.stderr

        elif skill_name == "vault-status":
            result = subprocess.run(
                [CLAUDE_PATH, "-p",
                 "Show vault health: list the 10 most recently modified files, "
                 "any files not updated in over 90 days, and a count of files by top-level folder.",
                 "--output-format", "text",
                 "--allowedTools", "Read,Glob,Grep,Bash"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=300
            )
            output = result.stdout.strip() or result.stderr.strip() or "No output"

        elif skill_name == "client-brief":
            if not skill_args:
                return "Usage: `@bot skill client-brief <client-name>`\nExample: `@bot skill client-brief acme`"
            result = subprocess.run(
                [CLAUDE_PATH, "-p",
                 f"Pull a summary of client '{skill_args}' from the vault. "
                 "Include status, key contacts, active projects, and recent activity.",
                 "--output-format", "text",
                 "--allowedTools", "Read,Glob,Grep"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=300
            )
            output = result.stdout.strip() or result.stderr.strip() or "No output"

        elif skill_name == "etl-sync":
            result = subprocess.run(
                [CLAUDE_PATH, "-p",
                 "Trigger ETL processing: scan for recently added source files, "
                 "process them, and report what was synced.",
                 "--output-format", "text",
                 "--allowedTools", "Read,Glob,Grep,Bash"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=300
            )
            output = result.stdout.strip() or result.stderr.strip() or "No output"

        else:
            result = subprocess.run(
                [CLAUDE_PATH, "-p", f"Run the skill: {skill_name}",
                 "--output-format", "text"],
                cwd=REPO_DIR, capture_output=True, text=True, timeout=300
            )
            output = result.stdout.strip() or result.stderr.strip() or "No output"

    except subprocess.TimeoutExpired:
        output = "Skill timed out"
    except Exception as e:
        output = f"Error: {str(e)}"

    return output


def parse_command(text):
    """Parse the cleaned message text into a command and arguments.

    Returns a tuple of (command, args_string).
    Commands: 'skill', 'confirm', 'cancel', 'skills', 'repo', or None for freeform text.
    """
    text = text.strip()
    lower = text.lower()

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
    else:
        return (None, text, None)


def get_pending_key(user_id, thread_ts):
    """Build a key for tracking pending skills per user per thread."""
    return (user_id, thread_ts)

# ============================================================
# EVENT HANDLERS
# ============================================================

@app.event("app_mention")
def handle_mention(event, say):
    """Handle @mentions in channels and threads."""
    user_id = event.get("user", "")
    if not is_allowed(user_id):
        say(text="Sorry, you are not authorized to use this bot.", thread_ts=event.get("ts"))
        return

    raw_text = event.get("text", "")
    text = strip_bot_mention(raw_text)
    thread_ts = event.get("thread_ts", event.get("ts"))

    logger.info(f"Mention from {user_id} in thread {thread_ts}: {text}")

    command, arg1, arg2 = parse_command(text)

    if command == "skills":
        handle_skills_list(say, thread_ts)
    elif command == "skill":
        handle_skill_request(say, user_id, thread_ts, arg1, arg2)
    elif command == "confirm":
        handle_confirm(say, user_id, thread_ts)
    elif command == "cancel":
        handle_cancel(say, user_id, thread_ts)
    elif command == "repo":
        handle_repo(say, thread_ts)
    else:
        handle_freeform(say, user_id, thread_ts, arg1)


@app.event("message")
def handle_dm(event, say):
    """Handle direct messages to the bot."""
    # Ignore bot messages, message_changed events, etc.
    if event.get("subtype"):
        return

    user_id = event.get("user", "")
    if not is_allowed(user_id):
        say(text="Sorry, you are not authorized to use this bot.")
        return

    text = event.get("text", "").strip()
    thread_ts = event.get("thread_ts", event.get("ts"))

    logger.info(f"DM from {user_id} in thread {thread_ts}: {text}")

    command, arg1, arg2 = parse_command(text)

    if command == "skills":
        handle_skills_list(say, thread_ts)
    elif command == "skill":
        handle_skill_request(say, user_id, thread_ts, arg1, arg2)
    elif command == "confirm":
        handle_confirm(say, user_id, thread_ts)
    elif command == "cancel":
        handle_cancel(say, user_id, thread_ts)
    elif command == "repo":
        handle_repo(say, thread_ts)
    else:
        handle_freeform(say, user_id, thread_ts, arg1)

# ============================================================
# COMMAND IMPLEMENTATIONS
# ============================================================

def handle_skills_list(say, thread_ts):
    """List all registered skills."""
    if not SKILLS:
        say(text="No skills registered yet.", thread_ts=thread_ts)
        return
    lines = [f"*Available skills:*\n"]
    for name, description in SKILLS.items():
        lines.append(f"  `skill {name}` -- {description}")
    lines.append(f"\nUsage: `@bot skill <name>` (requires confirmation)")
    say(text="\n".join(lines), thread_ts=thread_ts)


def handle_skill_request(say, user_id, thread_ts, skill_name, skill_args):
    """Request a skill, pending confirmation."""
    if not skill_name:
        say(text="Usage: `@bot skill <name>`\nSay `@bot skills` to see the list.",
            thread_ts=thread_ts)
        return

    if skill_name not in SKILLS:
        say(text=f"Unknown skill: `{skill_name}`\nSay `@bot skills` to see available skills.",
            thread_ts=thread_ts)
        return

    pkey = get_pending_key(user_id, thread_ts)
    pending_skills[pkey] = {
        "name": skill_name,
        "args": skill_args
    }

    args_display = f"\n*Arguments:* `{skill_args}`" if skill_args else ""
    say(
        text=(
            f":warning: *SKILL CONFIRMATION REQUIRED*\n\n"
            f"*Skill:* `{skill_name}`\n"
            f"*Description:* {SKILLS[skill_name]}{args_display}\n\n"
            f"This skill CAN create, modify, or delete files.\n"
            f"Say `@bot confirm` to execute or `@bot cancel` to abort."
        ),
        thread_ts=thread_ts
    )


def handle_confirm(say, user_id, thread_ts):
    """Confirm and execute a pending skill."""
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
    """Cancel a pending skill."""
    pkey = get_pending_key(user_id, thread_ts)
    if pkey not in pending_skills:
        say(text="No pending skill to cancel in this thread.", thread_ts=thread_ts)
        return

    skill_data = pending_skills.pop(pkey)
    say(text=f"Cancelled skill: `{skill_data['name']}`", thread_ts=thread_ts)


def handle_repo(say, thread_ts):
    """Show git status of the configured repo."""
    try:
        result = subprocess.run(
            ["git", "status", "--short", "--branch"],
            cwd=REPO_DIR, capture_output=True, text=True, timeout=30
        )
        output = result.stdout.strip() or "No output"
    except Exception as e:
        output = f"Error: {str(e)}"
    say(text=f"```\n{output}\n```", thread_ts=thread_ts)


def handle_freeform(say, user_id, thread_ts, text):
    """Send freeform text to Claude for processing."""
    say(text="Thinking...", thread_ts=thread_ts)
    output = run_claude(text, thread_ts, user_id)
    send_chunked(say, output, thread_ts)

# ============================================================
# MAIN
# ============================================================

def main():
    logger.info("Slack Claude bot starting (READ-ONLY mode)...")
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()

if __name__ == "__main__":
    main()
PYEOF
```

---

## 5. Run as systemd Service

### Test manually first

```bash
python3 ~/scripts/slack-claude-bot.py
```

Go to Slack and @mention your bot in a channel it has been invited to. If it responds, stop the script with `Ctrl+C` and create the service.

### Find your Claude path

```bash
which claude
```

### Create the service file

Replace `YOUR_USERNAME` with your WSL username:

```bash
sudo tee /etc/systemd/system/slack-claude.service << 'EOF'
[Unit]
Description=Slack Claude Bot
After=network.target

[Service]
Type=simple
User=YOUR_USERNAME
WorkingDirectory=/home/YOUR_USERNAME
ExecStart=/usr/bin/python3 /home/YOUR_USERNAME/scripts/slack-claude-bot.py
Restart=always
RestartSec=10
Environment=PATH=/usr/local/bin:/usr/bin:/bin:/home/YOUR_USERNAME/.npm-global/bin
Environment=HOME=/home/YOUR_USERNAME

[Install]
WantedBy=multi-user.target
EOF
```

### Enable and start

```bash
sudo systemctl daemon-reload
sudo systemctl enable slack-claude
sudo systemctl start slack-claude
sudo systemctl status slack-claude
```

Status should show `active (running)`.

### Service management commands

```bash
sudo systemctl stop slack-claude              # stop the bot
sudo systemctl restart slack-claude            # restart (after editing the script)
sudo systemctl status slack-claude             # check status
sudo journalctl -u slack-claude -n 50 --no-pager   # view logs
sudo journalctl -u slack-claude -f            # live log tail
```

---

## 6. Testing

Invite the bot to a test channel first, then verify each interaction:

| Action | Expected Result |
|---|---|
| `@Claude WSL Bot skills` | Lists all registered skills with descriptions |
| `@Claude WSL Bot what files are in the root?` | Claude responds in read-only mode within the thread |
| Follow-up in same thread | Claude remembers the previous exchange in that thread |
| New thread | Claude starts fresh with no prior context |
| `@Claude WSL Bot repo` | Shows `git status` of the configured repo |
| `@Claude WSL Bot skill sync` | Asks for confirmation in the thread |
| `@Claude WSL Bot confirm` | Executes the sync, returns output in the thread |
| `@Claude WSL Bot cancel` | Cancels a pending skill in the thread |
| `@Claude WSL Bot skill git-pull sharkie` | Asks for confirmation, then pulls the repo |
| `@Claude WSL Bot skill git-pull-sub admiral-systems` | Asks for confirmation, then pulls the submodule |
| `@Claude WSL Bot skill client-brief acme` | Asks for confirmation, then pulls a client summary |
| DM to bot: `what is the current sprint?` | Claude responds in DM with read-only vault query |
| DM to bot: `skill vault-status` | Asks for confirmation, then shows vault health |
| Mention from unauthorized user | Bot replies with "not authorized" |

---

## 7. Troubleshooting

### Socket Mode not enabled

If the bot connects but never receives events, Socket Mode may not be turned on.

1. Go to [api.slack.com/apps](https://api.slack.com/apps) and select your app
2. Click **Socket Mode** in the sidebar
3. Verify the toggle is ON
4. Verify you have an App-Level Token with `connections:write` scope

### Wrong token type

The bot uses two different tokens. Mixing them up is a common mistake.

| Token | Starts with | Used for |
|---|---|---|
| Bot User OAuth Token | `xoxb-` | `SLACK_BOT_TOKEN` in the script — authenticates the bot to send messages |
| App-Level Token | `xapp-` | `SLACK_APP_TOKEN` in the script — establishes the Socket Mode connection |

If you see authentication errors, double-check that each token is in the correct variable.

### Bot not responding to @mentions

1. Verify the bot has been invited to the channel (`/invite @Claude WSL Bot`)
2. Check that **Event Subscriptions** are enabled with `app_mention` and `message.im` events
3. Check that Bot Token Scopes include `app_mentions:read` and `channels:history`
4. View the logs for errors:

```bash
sudo journalctl -u slack-claude -n 50 --no-pager
```

### Thread context not working

Each thread is tracked by `(user_id, thread_ts)`. If the bot is not remembering context:

1. Make sure you are replying **within the same thread** (not starting a new top-level message)
2. Check that `MAX_HISTORY` is not set too low
3. Note that conversation history is in-memory and resets when the service restarts

### Bot responds but Claude times out

Increase the timeout in the bot script (default is 300 seconds / 5 minutes):

```python
timeout=600  # 10 minutes
```

### "Permission denied (publickey)" when running git skills

The SSH key is not accessible to the systemd service. Ensure:

1. The SSH key has no passphrase: `ssh-keygen -p -f ~/.ssh/github_key`
2. Git is configured globally to use the key: `git config --global core.sshCommand "ssh -i /home/YOUR_USERNAME/.ssh/github_key -o IdentitiesOnly=yes"`
3. The service has `Environment=HOME=/home/YOUR_USERNAME` in the unit file

### "No such file or directory: claude"

Claude is not in the service's PATH. Find it with `which claude` and either:

- Add its directory to the service's `Environment=PATH=...` line
- Use the full path in the bot script's `CLAUDE_PATH` variable

### Slack rate limiting

If the bot hits Slack's rate limits (HTTP 429 responses), `slack_bolt` handles retries automatically. If you see persistent rate limit errors:

1. Reduce `MAX_HISTORY` to send less context per Claude invocation
2. Add a short delay between chunked messages if responses are very long
3. Check the logs for the specific endpoint being rate-limited

### Service keeps crashing

Check the logs for Python errors:

```bash
sudo journalctl -u slack-claude -n 100 --no-pager
```

Common causes:

- Missing `slack_bolt` package (run `pip3 install slack_bolt --break-system-packages`)
- Invalid token format (must be `xoxb-` for bot token, `xapp-` for app token)
- Syntax errors in the Python script (missing commas, wrong indentation)
- Port conflict if another Socket Mode handler is already running

### Running both Telegram and Slack bots

Both bots can run side-by-side as separate systemd services. They share the same repo directory and Claude installation but operate independently:

```bash
sudo systemctl status telegram-claude    # Telegram bot status
sudo systemctl status slack-claude       # Slack bot status
```

If both bots invoke Claude simultaneously, each gets its own subprocess. This is fine for light usage but may cause slowdowns under heavy load.
