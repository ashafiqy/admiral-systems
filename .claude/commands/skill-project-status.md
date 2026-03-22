<!-- bot-skill
name: project-status
description: Full project status — vault context + live Linear progress
type: query
tools: Read,Glob,Grep,mcp__linear-server__*
-->

Provide a comprehensive project status for "$ARGS" by combining vault context with live Linear data.

*Step 1: Read vault files*
Scan `clients/` for the matching client folder. Read project overview, brief, epic, milestone files, meeting notes, and risk documentation.

*Step 2: Query Linear MCP*
Find the matching Linear project and fetch:
• Issue completion percentage
• Issues by state (Backlog/Todo/In Progress/Done)
• Any overdue issues
• Recent project updates/status reports

*Step 3: Return combined status*

*[Client Name] — Project Status*

*Context* (from vault)
• Phase: current phase + progress description
• Team: who's assigned and their roles
• Key decisions: recent important decisions from meetings
• Risks/Blockers: any flagged risks

*Task Progress* (from Linear — live)
• Completion: X% (Y of Z issues done)
• In Progress: X issues
• Blocked/Overdue: X issues
• Recent completions: list last 3-5 completed issues

*Next Up*
• Next milestone + deadline
• Key upcoming deliverables

NEVER read from CSV files. Vault for context, Linear MCP for task progress.
Format output for Slack mrkdwn (use *bold* headers, not ### markdown headers).
If no client matches "$ARGS", list available client folders.
