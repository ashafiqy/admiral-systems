<!-- bot-skill
name: all-projects
description: Dashboard summary of all active projects
type: query
tools: Read,Glob,Grep
-->

Scan ALL folders in `clients/` (skip folders starting with `_`). For each client folder, read the project overview or project brief to extract: client name, current phase, PM/lead, risk level, next deadline. Return a summary table. Keep concise for chat.