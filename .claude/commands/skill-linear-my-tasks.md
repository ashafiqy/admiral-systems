<!-- bot-skill
name: linear-my-tasks
description: Show a person's active Linear tasks (live data)
type: query
tools: Read,Glob,Grep,mcp__linear-server__*
-->

Use the Linear MCP to find all issues assigned to "$ARGS".

Query Linear directly — do NOT read from CSV files.

Return:

*[Person] — Active Tasks*

List their issues grouped by project, showing:
• Issue title
• Priority (P0-P3)
• State (In Progress / Todo / Backlog)
• Due date (if set)

At the bottom, show:
• Total active issues: X
• In Progress: X
• Overdue: X

Format output for Slack mrkdwn (use *bold* headers, not ### markdown headers).
If no person matches "$ARGS", suggest checking the name spelling or list team members from the vault.
