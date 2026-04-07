---
title: Vault Change History
created: 2026-03-22
updated: 2026-04-07
tags:
  - type/reference
status: active
---

# Vault Change History

Reverse-chronological log of structural changes to the Admiral Systems vault. Future sessions should append to this file when making significant vault changes.

---

## 2026-04-07

- Digested Delivery Team Sync Up notes (`inbox/7th April Delivery Team Sync Up.md` → archived) — 2 Linear issues for Haykal and Luthfi; see RCG client HISTORY.md
- Routed Label-Cleanup-Pitch from `inbox/` → `command/decisions/label-cleanup-pitch.md`

## 2026-04-06

- Digested Granola sprint planning notes (`inbox/Granola Action items 06 Apr 2026.md` → archived to `inbox/archive/`) — 7 Linear issues created, 3 comments added; see per-client HISTORY.md files for details
- Created client vault folders for ORG (`clients/admiral-gamma-org/`) and Wallex (`clients/admiral-retainer-wallex/`)
- Populated `clients/_client-index.md` with all 6 active clients
- Created build environment SOP (`operations/sops/sop-build-environment.md`) — all builds must start in Admiral's workspace
- Added Templates section to [[CLAUDE]] with lookup table for all 9 vault templates
- Added Linear Rules to [[CLAUDE]] and [[linear-standards]] — issues always created as Backlog with mandatory estimates
- Added `/vault-sync` Claude Code slash command — git pull for syncing vault across machines
- Created ecosystem PRD (`command/decisions/admiral-systems-ecosystem-prd.md`) — comprehensive system architecture, data flows, integration map, standards, and roadmap
- Created interactive HTML architecture diagram (`command/decisions/admiral-systems-ecosystem-diagram.html`)
- Created migration plan: GitHub → Google Drive (`command/decisions/vault-migration-github-to-drive.md`)
- Created `/changelog` skill to replace `/commit` post-migration

## 2026-04-05

- Added limited-allow Slack IDs for junior team members (Tiara, Elfajri, Luthfi, Mona, Haykal) to [[wsl-claude-slack-setup]]
- Added `/commit` and `/history` Claude Code slash commands
- Fixed markdown table formatting in [[roles-responsibilities-2026-q1]]

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
