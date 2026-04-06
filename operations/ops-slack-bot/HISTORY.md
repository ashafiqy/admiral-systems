---
title: "Ops Slack Bot - Change History"
created: 2026-04-05
updated: 2026-04-06
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

---

## 2026-04-05 — Standup Refinements & Testing

### Standup Prompt
- Added `<!channel>` tag to notify the full channel
- Added reaction legend: 👀 = received, ✅ = processed
- Standup header includes date: "Daily Standup — 2026-04-05"

### Standup Summary (11:15 AM SGT)
- Changed summary time from 10:15 to 11:15 SGT (= 10:15 WIB, aligns with Indonesia junior timezone)
- Summary tags both Shafiq + Daz (via `SUMMARY_CC` config)
- Each person's name links to their original standup message in the thread (deep link with `thread_ts`)
- Always shows Did / Doing / Blockers fields (empty shows "—")
- Removed Claude-generated summary — using deterministic formatter for consistent Slack mrkdwn output
- Lists all missing juniors who haven't submitted

### Bot Reply Policy (refined)
- Bot reacts with 👀 on receipt, adds ✅ when processed — both reactions stay (no swap)
- No text replies in the standup thread
- On message edit: removes ✅, re-processes, adds ✅ back when done
- Only posts to channel when blockers are detected

### Event Handling Fixes
- Fixed slack_bolt single-handler issue: `handle_message` in main bot now delegates to `ops.handle_delivery_message()` directly instead of registering a duplicate `@app.event("message")`
- Added `file_share` subtype handling — Slack clips were being dropped because they come as `file_share` not a bare `message`
- Added `message.groups` event subscription for private channels (was only listening to `message.channels`)
- Allowed seniors to submit standups for testing (not just juniors)

### DB Fixes
- Rebuilt FTS5 tables as standalone (not content-linked) to fix corruption from schema migrations
- Added `links TEXT` column to standups table for Slack clip + URL storage
- Added `processed_at TEXT` column to blockers table

---

## 2026-04-06 — /blocker Slash Command

### Modal Form
- Registered `/blocker` as a Slack slash command (Interactivity enabled, Socket Mode)
- Opens a modal form with 5 fields:
  - Description (required, multiline text)
  - Linear Issue Link (optional, URL input)
  - Project (required, dropdown: HopLun, RCG, 4Walls, Jireh Law, Internal, Other)
  - Category (required, multi-select: Design, Tech, PM/Process, Operations, Commercial)
  - Tag seniors (optional, multi-user picker for manual tagging)
- Form submission posts to `dept-delivery_team` with clean format + 👀✅ reactions
- No async Claude needed — structured form data gives project, category, and tags directly

### Blocker Message Format
- Clean, scannable format: `:red_circle: *Name* — Project  •  LINEAR-ID`
- Description on next line, tags below
- Thread reply prompts: "_Drop a Slack clip here if you want to add more context._"

### Linear Integration
- On form submit with Linear issue link: posts a comment on the Linear issue with blocker details, tagged seniors, and Slack thread link
- Updates Linear issue status to "Blocker"
- Runs in background thread so Slack response isn't delayed

### Visibility Tagging (from form)
- Always CC: Shafiq + Daz
- Domain experts added per selected category (multi-select, so multiple domains tag multiple experts)
- Entity CCs added per selected project (Rohan for Admiral/RMD, Valentin for Sprklabs)
- Manual tags from user picker merged on top — no duplicates

### Bug Fixes
- Fixed `handle_blocker_submission` — `user` is in `body`, not `view` (KeyError fix)
- Fixed duplicate bot processes causing double messages — ensured single process on restart
- Disabled channel message listener temporarily to avoid spam during development

### Slack Admin Setup (documented)
- Step-by-step guide for `/blocker` slash command setup (Interactivity, Slash Commands, reinstall)
- Required scopes: `reactions:write`, `message.groups`, `chat:write`
