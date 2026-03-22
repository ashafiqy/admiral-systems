<!-- bot-skill
name: client-brief
description: Pull a comprehensive client summary from the vault
type: query
tools: Read,Glob,Grep
-->

Find the client matching "$ARGS" in `clients/`. Read ALL files in the client's folder to build a comprehensive brief covering: project overview, commercial terms, scope and deliverables, timeline and milestones, team allocation, recent meetings, risks and blockers. If no client matches "$ARGS", list available client folders. Keep informative but concise for chat.