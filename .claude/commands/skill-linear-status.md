<!-- bot-skill
name: linear-status
description: Show Linear project status from vault data
type: query
tools: Read,Glob,Grep,Bash
-->

Find the client or project matching "$ARGS" in the vault. Read any Linear-related files in the client's folder, delivery reports, or Linear exports in `delivery/linear/`. Return what you can find about issue counts, status breakdown, priority distribution, and recent completions. Note if data may be stale. Keep concise for chat.