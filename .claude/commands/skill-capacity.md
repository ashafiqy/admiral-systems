<!-- bot-skill
name: capacity
description: Team capacity — who's available, who's overloaded
type: query
tools: Read,Glob,Grep
-->

Read `delivery/reports/capacity-dashboard-snapshot.md` for the latest capacity data. If that file doesn't exist or is empty, scan client project files to infer team allocations. Return a formatted capacity report showing each person's active issues vs monthly capacity and their status (available/at capacity/over). Note who has room for new work and who is critically over capacity. Keep concise for chat.