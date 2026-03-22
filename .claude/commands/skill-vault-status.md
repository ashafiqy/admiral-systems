<!-- bot-skill
name: vault-status
description: Vault health — recent files, stale notes, file counts
type: query
tools: Read,Glob,Grep,Bash
-->

Analyze vault health: list the 10 most recently modified .md files, count files by top-level folder, flag any important files not updated recently (sprint-current.md, capacity.md, risks.md, _client-index.md). Keep concise for chat.