<!-- bot-skill
name: project-status
description: Show current status of a specific project
type: query
tools: Read,Glob,Grep
-->

Scan the `clients/` folder for a client matching "$ARGS". Read the client's project overview, project brief, epic, milestone files, and any risk documentation. Return a formatted summary with: current phase + progress, team allocation, next milestone + deadline, risks/blockers, key metrics. Keep concise for chat. If no client matches "$ARGS", list available client folders.