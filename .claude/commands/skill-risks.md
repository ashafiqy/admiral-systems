<!-- bot-skill
name: risks
description: Aggregate risk register across all projects
type: query
tools: Read,Glob,Grep
-->

Scan all `clients/*/` folders for risk-related content. Look for risk sections in project overviews or epics, files with "risk" in the name, sections titled "Risks", "Blockers", "Bottlenecks", or "Critical Path". Aggregate all risks into a single prioritized report. Sort by priority (critical first). Keep concise for chat.