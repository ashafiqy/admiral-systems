<!-- bot-skill
name: capacity
description: Team capacity — vault baseline + live Linear active issues
type: query
tools: Read,Glob,Grep,mcp__linear-server__*
-->

Build a team capacity report by combining vault baseline data with live Linear issue counts.

*Step 1: Read vault*
Read `delivery/reports/capacity-dashboard-snapshot.md` for the team's monthly throughput baseline. Also check `team/` for roster and roles.

*Step 2: Query Linear MCP*
For each team member, query Linear for their currently active issues (state = In Progress or Todo).

*Step 3: Return capacity report*

*Team Capacity*

Person | Active (Linear) | Baseline | Status
-------|----------------|----------|-------
...    | X              | Y/month  | :white_check_mark: Available / :warning: At capacity / :red_circle: Over

*Available for new work:*
• List people with room

*Over capacity:*
• List people who are overloaded with details

*Recommendation:*
• Brief note on whether the team can take on new work

NEVER read from CSV files. Use Linear MCP for current active issue counts.
Format output for Slack mrkdwn (use *bold* headers, not ### markdown headers).
