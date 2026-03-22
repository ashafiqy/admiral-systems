<!-- bot-skill
name: linear-status
description: Live Linear project status — issues, priorities, completion
type: query
tools: Read,Glob,Grep,mcp__linear-server__*
-->

Use the Linear MCP to find the project matching "$ARGS".

First, read the vault `clients/` folder to identify the correct client and any Linear project references. Then query Linear MCP directly for live data.

Return:

*[Project Name] — Linear Status*

*Overview*
• Total issues: X
• Completion: X% done

*By State*
• Backlog: X
• Todo: X
• In Progress: X
• Done: X

*By Priority*
• P0 Critical: X
• P1 High: X
• P2 Medium: X
• P3 Low: X

*Overdue*
• List any issues past their due date

*Recent Completions (last 7 days)*
• List recently completed issues

NEVER read from CSV files in the vault. Always query Linear MCP for live data.
Format output for Slack mrkdwn (use *bold* headers, not ### markdown headers).
If no project matches "$ARGS", list available projects from Linear.
