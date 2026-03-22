<!-- bot-skill
name: whats-due
description: Next deadlines and milestones across all projects
type: query
tools: Read,Glob,Grep
-->

Scan all `clients/*/` folders for deadline-related content. Look for phase gates with dates, milestone deadlines, target dates in project overviews, week numbers with associated deliverables. Return a chronologically sorted list of upcoming deadlines showing date, client, milestone/deliverable, and owner. Show the next 2 weeks. Keep concise for chat.