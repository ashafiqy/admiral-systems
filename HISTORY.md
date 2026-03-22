---
title: Vault Change History
created: 2026-03-22
updated: 2026-03-22
tags:
  - type/reference
status: active
---

# Vault Change History

Reverse-chronological log of structural changes to the Admiral Systems vault. Future sessions should append to this file when making significant vault changes.

---

## 2026-03-22

- Connected skills to Linear MCP for live task data — 5 skills now query Linear directly
- Added [[skill-digest-and-create]] — full workflow for digesting client input into vault + Linear
- Removed `delivery/linear/` folder — CSV exports replaced by live Linear MCP queries
- Updated Slack bot system prompt for proper Slack mrkdwn formatting
- Added unified bot skill system with 11 query skills + dynamic loading from `.claude/commands/`
- Added [[remote-claude-architecture]] — full system architecture doc (bots, ETL, Agent Teams)
- Added [[wsl-claude-slack-setup]] — Slack bot setup guide with full Python script
- Moved [[wsl-claude-telegram-setup]] from `dump/` to `operations/tools/`
- Moved [[admiral-systems-knowledge-vault-brief]] from `dump/` to `command/decisions/` as reference doc
- Created this [[HISTORY]] file for session continuity
- Added [[admiral-ideas]] command and initial vault tooling ideas (`ideas/`)
- Updated [[CLAUDE]] with architecture references, routing table, and structure tree

## 2026-03-21

- Migrated content from temp staging into live vault
- Stopped tracking `.obsidian/` files and normalized `dump/` ignore
- Updated `.gitignore` for plugin binaries, cache, and crash dumps
- Removed number prefixes from all folder names
- Added [[CLAUDE]], templates, seed files, and `.gitignore`
- Initialized admiral-systems company vault
