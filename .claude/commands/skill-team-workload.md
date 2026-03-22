<!-- bot-skill
name: team-workload
description: Show what a specific person is working on
type: query
tools: Read,Glob,Grep
-->

Find all references to "$ARGS" across the vault. Search in `clients/*/` project overviews and briefs (team allocation sections), `team/` roster and roles files, `delivery/reports/` capacity data. Return their projects with roles, capacity baseline vs current active work, status (available/at capacity/over), and key responsibilities. Keep concise for chat.