---
title: "Ops Slack Bot - Project Brief"
created: 2026-04-05
updated: 2026-04-05
tags:
  - operations/ops-slack-bot
  - type/project-brief
status: active
---

# Ops Slack Bot (Davy Jones) — Project Brief

## Context

The delivery team needs structured, low-friction daily operations in `dept-delivery_team`. Juniors get lost without clear processes for standups, escalating blockers, and booking senior time. Seniors get ambushed with 1:1 questions that could be group sessions. Updates live in Slack and WhatsApp, not in any queryable system.

This initiative adds ops features to the existing Davy Jones Slack bot (`~/scripts/slack-claude-bot.py`) as an importable library (`~/scripts/ops/`), backed by a SQLite database for persistence and future context retrieval.

**Linear Initiative:** [Ops Slack Bot](https://linear.app/admiralhq/initiative/ops-slack-bot-540d59f3455e)
**Brief v3.1:** [Junior Operations Bot](https://linear.app/admiralhq/document/brief-v31-junior-operations-bot-slack-bot-48b66aa24c20)
**Target:** 2026-04-20
**Owner:** Shafiq Yussaini (build) + Davis (routing logic input)
**Requested by:** Daz

---

## RACI

| Letter | Meaning |
|---|---|
| **R** | Responsible — does the work |
| **A** | Accountable — owns the outcome |
| **C** | Consulted — input needed |
| **I** | Informed — kept in the loop |

| Area | Shafiq | Davis | Daz | Rohan | Valentin | Sean |
|---|---|---|---|---|---|---|
| Bot development | R | C | A | I | I | I |
| Standup workflow | R | I | A | I | I | I |
| Blocker routing logic | R | R | A | I | I | I |
| Office hours process | R | C | A | C | C | C |
| Testing & rollout | R | C | A | I | I | I |

---

## Architecture

- **Library:** `~/scripts/ops/` — imported by Davy Jones bot
- **Database:** SQLite (WAL mode) at `~/data/davy-jones/davy-jones.db`
- **Processing:** Two-phase — fast ingest (DB + reaction) → async Claude parsing via ThreadPoolExecutor
- **Channel:** Everything in `dept-delivery_team` (one channel for unified context)
- **Calendar:** None in v1 — juniors create Google Meet manually

---

## Feature Checklist

### Standup Collection
- [x] Daily standup prompt with `<!channel>` tag (9:00 AM SGT)
- [x] Reaction legend in prompt (👀 = received, ✅ = processed)
- [x] Standup reply ingestion with 👀 → ✅ reactions
- [x] Claude parsing (did / doing / blockers)
- [x] Slack clip + URL extraction and storage
- [x] Late standup handling (upsert, not duplicate)
- [x] Message edit detection and re-processing
- [x] Standup IDs (SU-001 format)
- [x] SQLite persistence with queue (raw → processing → done)
- [ ] Standup summary compilation (10:15 AM) — code exists, needs testing
- [ ] Standup reminder for non-submitters (9:45 AM) — code exists, needs testing
- [ ] Linear issue comment posting from standup data

### Blocker Routing
- [x] Auto-detect blockers from standup → post to channel with visibility tags
- [x] Visibility tagging: always CC Shafiq + Daz, domain expert, entity CCs (Rohan for Admiral/RMD, Valentin for Sprklabs)
- [ ] `/blocker` standalone command — code exists, needs testing

### Smart Grouping (3:15 PM)
- [ ] Question intake from channel messages — code exists, needs testing
- [ ] Claude classification (project / category / topic / domain / entity)
- [ ] Similarity grouping per Brief v3.1 format
- [ ] Group session suggestions

### Office Hours
- [ ] Senior response tracking (accept / decline / reschedule)
- [ ] 4:00 PM nudge for unbooked juniors + unresponsive seniors
- [ ] Escalation messages in channel

### End-of-Day
- [ ] 6:00 PM activity log — code exists, needs testing

---

## Visibility Tagging Rules

| Who | When tagged |
|---|---|
| Shafiq + Daz | Always (all blockers and questions) |
| Sean | Domain = design |
| Davis | Domain = tech |
| Rohan | Entity = admiral or rmd |
| Valentin | Entity = sprklabs only |

---

## Technical Details

| Component | Details |
|---|---|
| **Code** | `~/scripts/ops/` (config, models, worker, standup, blockers, questions, office_hours, prompts) |
| **Bot** | `~/scripts/slack-claude-bot.py` (Davy Jones — imports ops library) |
| **DB** | `~/data/davy-jones/davy-jones.db` (SQLite, WAL mode) |
| **Test channel** | `#test-ast-pm-bot` (C0AN10UUH6J) — private channel |
| **Production channel** | `#dept-delivery_team` — TBD |
| **Dependencies** | `slack_bolt`, `apscheduler` |
| **Slack scopes** | `chat:write`, `reactions:write`, `channels:history`, `groups:history`, `im:history`, `im:read`, `app_mentions:read`, `channels:read`, `groups:read` |
| **Slack events** | `app_mention`, `message.im`, `message.groups` |

---

## Related Documents

- [[wsl-claude-slack-setup]] — Original Slack bot setup guide
- [[remote-claude-architecture]] — System architecture (bots, ETL, Agent Teams)
- [[roles-responsibilities-2026-q1]] — Team structure and "10AM daily" rule
- [[linear-restructuring-plan-2026-03-10]] — Standup-to-Linear spec (section 3.7)
