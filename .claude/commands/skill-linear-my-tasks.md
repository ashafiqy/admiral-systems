<!-- bot-skill
name: linear-my-tasks
description: Show a person's tasks from vault data
type: query
tools: Read,Glob,Grep,Bash
-->

Find tasks assigned to "$ARGS" by searching Linear export files in `delivery/linear/`, project overviews in `clients/*/`, and the capacity dashboard. Return a table of their tasks with project, priority, status, and due date. Note if data comes from exports (may be stale). Keep concise for chat.