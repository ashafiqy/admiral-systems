---
title: "Ops Slack Bot - Change History"
created: 2026-04-05
updated: 2026-04-05
tags:
  - operations/ops-slack-bot
  - type/history
status: active
---

# Ops Slack Bot — Change History

## 2026-04-05 — Initial Build

### Foundation
- Created `~/scripts/ops/` library package (config, models, worker, standup, blockers, questions, office_hours, prompts)
- Integrated with Davy Jones bot (`slack-claude-bot.py`) via `ops.register(app, client, scheduler)`
- SQLite database at `~/data/davy-jones/davy-jones.db` with WAL mode
- Background worker with ThreadPoolExecutor (3 threads) for async Claude processing
- APScheduler for daily scheduled jobs (standup, reminder, summary, grouping, nudge, EOD)

### Standup Flow (tested and working)
- Daily standup prompt with `<!channel>` tag and reaction legend
- Two-phase processing: immediate 👀 reaction → Claude parses → ✅ reaction added
- Standup IDs (SU-001 format) stored in DB
- Slack clip (mp4) and URL extraction from message events
- Late standup handling via upsert (update existing record, not duplicate)
- Message edit detection (`message_changed` subtype) triggers re-processing

### Visibility Tagging
- Always CC: Shafiq + Daz
- Domain experts: Sean (design), Davis (tech)
- Entity CCs: Rohan (Admiral/RMD), Valentin (Sprklabs only)
- Claude classifies blockers by domain + entity to determine tags

### Configuration
- Team: 5 juniors + 6 seniors with Slack IDs
- Test channel: `#test-ast-pm-bot` (C0AN10UUH6J, private)
- Slack app scopes: added `reactions:write`, `message.groups` event subscription

### Architecture Decisions
- SQLite over PostgreSQL — single-writer, single-machine, ~1-3GB at 2 years, zero maintenance
- Library pattern (not separate bot) — shares Slack app, event loop, and infrastructure with Davy Jones
- Two-phase message processing — fast ingest + async Claude via thread pool
- Reactions only, no text replies in standup thread (except blocker alerts to channel)

### Vault
- Created `operations/ops-slack-bot/` with project-brief.md and HISTORY.md
- Created `operations/_initiative-index.md` for internal initiative tracking
