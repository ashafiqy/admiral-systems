<!-- bot-skill
name: team-workload
description: What a person is working on — vault roles + live Linear tasks
type: query
tools: Read,Glob,Grep,mcp__linear-server__*
-->

Show a comprehensive workload view for "$ARGS" by combining vault and Linear data.

*Step 1: Read vault*
Search `clients/*/` project overviews for their team allocation, `team/` for their role, and `delivery/reports/` for their capacity baseline.

*Step 2: Query Linear MCP*
Fetch all issues assigned to this person from Linear. Group by project.

*Step 3: Return workload report*

*[Person] — Workload*

*Role & Projects* (from vault)
• Role: their title/position
• Projects: list of projects they're assigned to with their responsibility

*Active Tasks* (from Linear — live)
• Total: X issues
• By project:
  - [Project 1]: X issues (Y in progress)
  - [Project 2]: X issues (Y in progress)

*Capacity*
• Baseline: X issues/month
• Currently active: Y issues
• Status: Available / At capacity / Over

*Key items needing attention:*
• List any overdue or high-priority items

NEVER read from CSV files. Vault for roles, Linear MCP for tasks.
Format output for Slack mrkdwn (use *bold* headers, not ### markdown headers).
