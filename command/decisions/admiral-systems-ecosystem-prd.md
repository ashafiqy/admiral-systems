---
title: "Admiral Systems — Ecosystem PRD"
created: 2026-04-06
updated: 2026-04-06
tags:
  - type/decision
  - operations/architecture
status: active
---

# Admiral Systems — Ecosystem PRD

## 1. Executive Summary

Admiral Systems is a digital agency running a unified operations platform built on four pillars:

1. **Vault** — Git-backed Obsidian knowledge base (this repo) storing all company knowledge
2. **Linear** — Task and project management (source of truth for delivery)
3. **Claude Code** — AI-powered assistant running on WSL2, accessible via terminal, Slack, and Telegram
4. **MCP Stack** — Model Context Protocol servers connecting Claude to Linear, Slack, Gmail, and future integrations

The system serves the Admiral Systems team (3 partners, 3 seniors, 5 juniors) across three entities: Admiral Systems (SG), RMD-HK, and Sprklabs (CH).

---

## 2. System Architecture

```
                          ┌─────────────────────────────────────────────────┐
                          │              TEAM INTERFACES                    │
                          │                                                 │
                          │   ┌─────────┐  ┌─────────┐  ┌──────────────┐  │
                          │   │ Slack   │  │Telegram │  │ Direct CLI   │  │
                          │   │ Bot     │  │ Bot     │  │ (Terminal)   │  │
                          │   │ "Davy   │  │         │  │              │  │
                          │   │ Jones"  │  │         │  │              │  │
                          │   └────┬────┘  └────┬────┘  └──────┬───────┘  │
                          └────────┼────────────┼──────────────┼──────────┘
                                   │            │              │
                                   ▼            ▼              ▼
                          ┌─────────────────────────────────────────────────┐
                          │           CLAUDE CODE (WSL2)                    │
                          │                                                 │
                          │   ┌──────────────────────────────────────────┐  │
                          │   │            Skills & Commands              │  │
                          │   │  /commit  /vault-sync  /history          │  │
                          │   │  /skill-linear-status  /skill-risks      │  │
                          │   │  /skill-all-projects   /admiral-ideas    │  │
                          │   │  /skill-digest-and-create  ...           │  │
                          │   └──────────────────────────────────────────┘  │
                          │                                                 │
                          │   ┌──────────────────────────────────────────┐  │
                          │   │          Agent Playbooks                  │  │
                          │   │  create-linear-project                   │  │
                          │   │  create-issue-agent                      │  │
                          │   │  client-feedback-playbook                │  │
                          │   │  linear-quality-checker                  │  │
                          │   │  context-sync-checker (deferred)         │  │
                          │   └──────────────────────────────────────────┘  │
                          └────────┬────────────┬──────────────┬──────────┘
                                   │            │              │
                          ┌────────▼────┐ ┌─────▼─────┐ ┌─────▼──────┐
                          │  MCP:       │ │  MCP:     │ │  MCP:      │
                          │  Linear     │ │  Slack    │ │  Gmail     │
                          │  ✅ Live    │ │  ✅ Live  │ │  🔲 Phase2 │
                          └────────┬────┘ └─────┬─────┘ └─────┬──────┘
                                   │            │              │
                          ┌────────▼────┐ ┌─────▼─────┐ ┌─────▼──────┐
                          │  LINEAR     │ │  SLACK    │ │  GMAIL     │
                          │             │ │           │ │            │
                          │ 20+ projects│ │ Channels: │ │ Client     │
                          │ 1100+ issues│ │ dept-     │ │ threads    │
                          │ 6 teams     │ │ delivery  │ │ Action     │
                          │ 13 users    │ │ _team     │ │ items      │
                          └─────────────┘ └───────────┘ └────────────┘
                                   │
                          ┌────────▼────────────────────────────────────────┐
                          │              VAULT (GitHub)                     │
                          │                                                 │
                          │  ┌──────────┐ ┌──────────┐ ┌──────────────┐   │
                          │  │ clients/ │ │delivery/ │ │ operations/  │   │
                          │  │ 6 active │ │ sprints  │ │ playbooks    │   │
                          │  │ folders  │ │ capacity │ │ sops         │   │
                          │  │          │ │ risks    │ │ tools        │   │
                          │  └──────────┘ └──────────┘ └──────────────┘   │
                          │  ┌──────────┐ ┌──────────┐ ┌──────────────┐   │
                          │  │ command/ │ │  team/   │ │ templates/   │   │
                          │  │ strategy │ │ roster   │ │ 9 templates  │   │
                          │  │ OKRs     │ │ roles    │ │              │   │
                          │  │ decisions│ │ hiring   │ │              │   │
                          │  └──────────┘ └──────────┘ └──────────────┘   │
                          └─────────────────────────────────────────────────┘
```

---

## 3. Component Inventory

### 3.1 Interfaces

| Component | Platform | Status | Purpose |
|-----------|----------|--------|---------|
| Davy Jones Slack Bot | Slack (`dept-delivery_team`) | Active | Standup, blockers, `/blocker` command, smart grouping, office hours |
| Telegram Bot | Telegram | Live | Personal query interface, skill execution, git operations |
| Direct CLI | WSL2 Terminal | Live | Full Claude Code access, Agent Teams, interactive sessions |

### 3.2 MCP Servers

| Server | Status | Read | Write | Purpose |
|--------|--------|------|-------|---------|
| Linear | Live | Yes | Yes | Issues, projects, comments, users, teams |
| Slack | Live | Yes | Yes | Messages, channels, search, notifications |
| Gmail | Phase 2 | Yes | No | Email threads, action item extraction |
| Google Drive | Phase 2 | Yes | No | Client files, meeting notes, Gemini summaries |
| Granola | Phase 2 | Yes | No | Meeting transcripts (machine-local) |
| GitHub (write) | Phase 3 | No | Yes | Vault commits with audit trail |

### 3.3 Vault Folders

| Folder | Purpose | Key Files |
|--------|---------|-----------|
| `inbox/` | Capture zone; archive after digestion | `archive/` for processed files |
| `command/` | Strategy, OKRs, leadership decisions | `strategy.md`, `decisions/`, `meetings/` |
| `clients/` | One folder per client (6 active) | `_client-index.md`, per-client `brief.md` + `HISTORY.md` |
| `delivery/` | Sprint management, capacity, risks | `sprint-current.md`, `capacity.md`, `risks.md` |
| `team/` | Team roster, roles, hiring, onboarding | `_team-roster.md`, `roles-responsibilities-2026-q1.md` |
| `operations/` | Tools, playbooks, SOPs, initiatives | `agent-playbooks/`, `sops/`, `tools/`, `ops-slack-bot/` |
| `finance/` | Revenue tracking, billing, budgets | `revenue-tracker.md` |
| `growth/` | Pipeline, proposals, case studies | `pipeline.md` |
| `templates/` | 9 standard templates | `tpl-linear-task.md`, `tpl-client-brief.md`, etc. |

### 3.4 Claude Code Skills & Commands

| Skill | Type | Purpose |
|-------|------|---------|
| `/commit` | Command | Stage, commit, and push vault changes |
| `/vault-sync` | Command | Git pull to sync vault across machines |
| `/history` | Command | Summarize vault change history |
| `/admiral-ideas` | Command | Scan vault and generate improvement ideas |
| `/skill-linear-status` | Bot Skill | Live Linear project status via MCP |
| `/skill-linear-my-tasks` | Bot Skill | Person's active Linear tasks |
| `/skill-all-projects` | Bot Skill | Dashboard of all active projects |
| `/skill-client-brief` | Bot Skill | Client brief summary |
| `/skill-client-contact` | Bot Skill | Client contact lookup |
| `/skill-capacity` | Bot Skill | Team capacity overview |
| `/skill-team-workload` | Bot Skill | Workload per team member |
| `/skill-risks` | Bot Skill | Active risks and blockers |
| `/skill-whats-due` | Bot Skill | Upcoming deadlines |
| `/skill-vault-status` | Bot Skill | Vault health check |
| `/skill-project-status` | Bot Skill | Single project deep-dive |
| `/skill-digest-and-create` | Bot Skill | Digest client input → vault + Linear + Slack |

### 3.5 Agent Playbooks

| Playbook | Purpose | Location |
|----------|---------|----------|
| `create-linear-project` | End-to-end project creation (project + 4 milestones + issues) | `operations/agent-playbooks/` |
| `create-issue-agent` | Add issues to existing project (duplicate check + template) | `operations/agent-playbooks/` |
| `client-feedback-playbook` | Client feedback → Linear issues + status update + Slack | `operations/agent-playbooks/` |
| `linear-quality-checker` | Post-creation validation of all Linear objects | `operations/agent-playbooks/` |
| `priority-mapping` | Label-to-priority mapping (p0-p3 → Urgent-Low) | `operations/agent-playbooks/` |
| `sync-priority` | Bulk sync between labels and priority field | `operations/agent-playbooks/` |
| `context-sync-checker` | Bridge context docs with Linear state (DEFERRED) | `operations/beta-workflow/` |

---

## 4. Data Flows

### 4.1 Standup → Blockers → Linear

```
9:00 AM SGT                    Team replies                Claude processes
┌──────────┐    <!channel>     ┌──────────┐    parse       ┌──────────┐
│ Davy     │───────────────────│ Juniors  │───────────────│ Claude   │
│ Jones    │    standup prompt  │ post     │    did/doing/  │ extracts │
│ Bot      │                   │ updates  │    blockers    │ items    │
└──────────┘                   └──────────┘               └─────┬────┘
                                                                │
                               ┌──────────┐                     │
                               │ Linear   │◄────────────────────┘
                               │ comment  │    if blocker links
                               │ + status │    to Linear issue
                               │ update   │
                               └──────────┘
```

### 4.2 Meeting Notes → Vault → Linear (ETL Pipeline)

```
Source                    Trigger                   Process                  Output
┌──────────┐             ┌──────────┐              ┌──────────┐           ┌──────────┐
│ Google   │             │ Slack:   │              │ Claude   │           │ Vault    │
│ Meet     │──Gemini───▶ │ @claude  │──────────────│ reads    │──────────│ entry    │
│ Granola  │  summary    │ etl-sync │   manual     │ via MCP  │           │ written  │
│ Gmail    │             │          │   trigger    │ extracts │           └─────┬────┘
│ Slack    │             └──────────┘              │ items    │                 │
└──────────┘                                       └─────┬────┘           ┌─────▼────┐
                                                         │               │ Linear   │
                                                         └──────────────▶│ issues   │
                                                              action     │ created  │
                                                              items      └─────┬────┘
                                                                               │
                                                                         ┌─────▼────┐
                                                                         │ Slack    │
                                                                         │ notify   │
                                                                         └──────────┘
```

### 4.3 Client Feedback → Linear → Slack

```
Input                     Playbook                  Linear                   Slack
┌──────────┐              ┌──────────┐              ┌──────────┐           ┌──────────┐
│ Client   │              │ digest-  │              │ Issues   │           │ Update   │
│ feedback │──────────────│ and-     │──────────────│ created  │──────────│ posted   │
│ (meeting,│   trigger    │ create   │   save_issue │ w/ RACI  │  Slack   │ to team  │
│ email,   │              │ skill    │              │ AC, est  │  MCP     │ channel  │
│ Slack)   │              └──────────┘              │ dropoff  │           └──────────┘
└──────────┘                   │                    └──────────┘
                               │
                          ┌────▼─────┐
                          │ Vault    │
                          │ staging  │
                          │ (inbox/) │
                          └──────────┘
```

---

## 5. Integration Map

### 5.1 Claude Code ↔ Linear

| Direction | Method | Operations |
|-----------|--------|------------|
| Read | `mcp__linear-server__list_*` | Teams, projects, users, issues, cycles, milestones |
| Read | `mcp__linear-server__get_*` | Single issue, project, user details |
| Write | `mcp__linear-server__save_issue` | Create/update issues (always as Backlog) |
| Write | `mcp__linear-server__save_comment` | Add comments to issues |
| Write | `mcp__linear-server__save_project` | Create/update projects |
| Write | `mcp__linear-server__save_milestone` | Create/update milestones |

### 5.2 Claude Code ↔ Slack

| Direction | Method | Operations |
|-----------|--------|------------|
| Read | `mcp__plugin_slack__slack_read_channel` | Read channel messages |
| Read | `mcp__plugin_slack__slack_search_*` | Search messages, channels, users |
| Write | `mcp__plugin_slack__slack_send_message` | Post to channels |
| Write | `mcp__plugin_slack__slack_send_message_draft` | Draft messages for review |
| Write | `mcp__plugin_slack__slack_schedule_message` | Schedule future messages |

### 5.3 Claude Code ↔ Vault

| Direction | Method | Operations |
|-----------|--------|------------|
| Read | `Read`, `Glob`, `Grep` | Browse vault files, search content |
| Write | `Write`, `Edit` | Create/modify vault files |
| Sync | `git pull/push` | Sync across machines via `/vault-sync` and `/commit` |

### 5.4 Davy Jones Bot ↔ Slack

| Feature | Channel | Trigger | Output |
|---------|---------|---------|--------|
| Standup prompt | `dept-delivery_team` | 9:00 AM SGT cron | `<!channel>` ping |
| Standup collection | `dept-delivery_team` | Team replies | Parse did/doing/blockers, reactions |
| `/blocker` command | Any channel | Slash command | Modal form → formatted message → Linear comment |
| Standup summary | `dept-delivery_team` | 11:15 AM SGT cron | Compiled summary (pending testing) |
| Smart grouping | `dept-delivery_team` | 3:15 PM SGT cron | Cross-project grouping (pending testing) |
| Office hours | `dept-delivery_team` | Scheduled | Senior availability (pending testing) |

---

## 6. Team & Governance

### 6.1 Team Structure

**Leadership & Partners**

| Name | Role | Entity | Responsibilities |
|------|------|--------|-----------------|
| Daz | COO | Admiral Systems (Devhaus) | Operations, client relationships, sales, financials |
| Rohan | Accounts & Commercial | Admiral + RMD-HK | SOW ownership, account management |
| Valentin | Partner | Sprklabs (CH) | Design direction, go-live QA, EU growth |

**Senior Team**

| Name | Role | Responsibilities |
|------|------|-----------------|
| Shafiq | Delivery Lead / PM | Linear management, issue creation, UAT, junior management, SOPs |
| Davis | Technical Lead | Webflow dev, technical QA, mentorship |
| Sean | Design Lead | Figma, UI/UX, component design |

**Junior Team**

| Name | Role | Responsibilities |
|------|------|-----------------|
| Tiara | Designer | Visual design, Figma, Relume wireframing, AI images |
| Elfajri | Developer | Front-end, animations, form/integration implementation |
| Luthfi | SEO / Data | Schema markup, SEO, analytics, FullStory |
| Haykal | AEO / SEO Support | AEO testing, AI search optimization |
| Mona | Design Support | Design workflow support, Webflow tasks |

### 6.2 Operational Rules

- **Issue creation** → Seniors only (not juniors)
- **Project direction** → Commercial (Rohan/Val) → Delivery (Shafiq/Davis) → Juniors
- **SOW approval** → Rohan/Val draft; Shafiq/Davis approve before work begins
- **Linear updates** → Seniors before Monday standup; juniors post Slack by 10AM daily
- **Scope changes** → Never accepted without Rohan/Val sign-off
- **Build environment** → All builds in Admiral's workspace; staging links only; transfer after payment

### 6.3 Blocker Visibility Routing

| Category | Always CC | Domain Expert |
|----------|-----------|---------------|
| All blockers | Shafiq + Daz | — |
| Design | Shafiq + Daz | Sean |
| Tech | Shafiq + Daz | Davis |
| Admiral/RMD entity | Shafiq + Daz | Rohan |
| Sprklabs entity | Shafiq + Daz | Valentin |

---

## 7. Standards & Templates

### 7.1 Vault Standards

| Standard | Rule |
|----------|------|
| File naming | kebab-case (`client-brief.md`) |
| Dates | ISO 8601 (`YYYY-MM-DD`) |
| Frontmatter | title, created, updated, tags, status (mandatory) |
| Tags | Hierarchical: `#client/{name}`, `#delivery/sprint`, `#type/meeting` |
| Cross-references | `[[wikilinks]]` for Obsidian |
| Templates | Always check `templates/` before creating content |

### 7.2 Linear Standards

| Standard | Rule |
|----------|------|
| Issue status on creation | Always **Backlog** (never Triage) |
| Estimates | Mandatory. 1pt=1hr, 2pt=2hr, 3pt=3hr, 4pt=4hr, 5pt=5hr |
| Issue title | Verb phrase, specific |
| Issue description | Follow `tpl-linear-task`: RACI + Overview + AC + Blockers + Dropoff |
| Acceptance criteria | Max 5 per issue (split if more needed) |
| Project description | 3 blocks only: Header, Overview, Milestones table |
| Milestone description | 3 blocks: Goal, In Scope issues, Done When (max 3) |
| Priority | p0-critical(1), p1-high(2), p2-medium(3), p3-low(4); label + field must match |
| Duplicate check | Semantic + exact match required before creating issues |

### 7.3 Template Inventory

| Template | File | Purpose |
|----------|------|---------|
| Linear Task | `tpl-linear-task.md` | Issue creation with RACI, AC, blockers, dropoff |
| Linear Project | `tpl-linear-project.md` | Project brief, team, milestones, resources |
| Linear Milestone | `tpl-linear-milestone.md` | Goal, in-scope issues, done-when |
| Client Brief | `tpl-client-brief.md` | New client folder setup |
| Meeting Notes | `tpl-meeting-notes.md` | Agenda, discussion, decisions, actions |
| SOP | `tpl-sop.md` | Purpose, when to use, steps, owner |
| Project Tracker | `tpl-project-tracker.md` | Milestones, tasks, risks, log |
| Sprint Review | `tpl-sprint-review.md` | Completed, carry-over, metrics |
| Retro | `tpl-retro.md` | Went well, didn't, improvements |

### 7.4 Sensitive Data Rules

Never include in Linear, Slack, or vault:
- Direct quotes from client emails
- Internal financial data (margins, budgets, contract values)
- HR / SAP system details
- Internal stakeholder hierarchy language
- Contract or SOW details

---

## 8. Current State vs Roadmap

### Phase 1 — Live Now

| Component | Status |
|-----------|--------|
| Vault structure & conventions | Live |
| Git-backed version control | Live |
| CLAUDE.md governance | Live |
| 9 standard templates | Live |
| 6 active client folders with HISTORY.md | Live |
| Linear MCP (read + write) | Live |
| Slack MCP (read + write) | Live |
| Claude Code skills (16 skills) | Live |
| Agent playbooks (7 playbooks) | Live |
| Davy Jones Slack bot — standup + blockers | Live |
| Telegram bot | Live |
| Direct CLI access | Live |
| Build environment SOP | Live |
| `/commit`, `/vault-sync`, `/history` commands | Live |

### Phase 2 — In Progress / Blocked

| Component | Status | Blocker |
|-----------|--------|---------|
| Standup summary compilation | Code exists | Needs testing |
| Smart grouping (3:15 PM) | Code exists | Needs testing |
| Office hours workflow | Code exists | Needs testing |
| EOD activity log (6:00 PM) | Code exists | Needs testing |
| Google Drive MCP | Planned | MCP not configured |
| Gmail MCP | Planned | MCP not configured |
| Granola MCP | Planned | Machine-local dependency |
| Full ETL pipeline | Planned | Blocked on Drive/Gmail MCPs |
| Context-sync-checker agent | Deferred | Needs consistent meeting note cadence |

### Phase 3 — Future

| Component | Status |
|-----------|--------|
| GitHub MCP (write) | Planned |
| Google Drive MCP (write) | Planned |
| Agent Teams for vault maintenance | Experimental |
| Notification cron (daily digest) | Planned |
| Confidence scoring on vault entries | Planned |
| Auto-ETL from Granola Enterprise | Planned |

---

## 9. Dependencies & Blockers

### Technical Dependencies

| Dependency | Blocks | Owner |
|------------|--------|-------|
| Google Drive MCP setup | Full ETL pipeline | Shafiq/Davis |
| Gmail MCP setup | Email thread extraction | Shafiq/Davis |
| Granola MCP setup | Meeting transcript ETL | Shafiq |
| Consistent meeting note cadence | Context-sync-checker | Team |
| Slack admin access | Bot slash commands in production | Shafiq |

### Known Limitations

| Limitation | Impact | Mitigation |
|------------|--------|------------|
| Bot conversation history is in-memory | Lost on service restart | Acceptable for query-based interactions |
| Granola is machine-local | Only works where installed | Manual export or Granola Enterprise (Phase 3) |
| SQLite single-writer | Scales to ~3GB / 2 years | Sufficient for current team size |
| Agent Teams require interactive session | Not available via bots | Use direct CLI for complex workflows |

---

## 10. File Index

### Governance & Standards
- `CLAUDE.md` — Master governance document
- `HISTORY.md` — Vault change log
- `operations/agent-playbooks/linear-standards.md` — Linear formatting standards
- `operations/agent-playbooks/priority-mapping.md` — Priority assignment rules
- `team/roles-responsibilities-2026-q1.md` — Team roles and operational rules

### Architecture & Setup
- `operations/tools/remote-claude-architecture.md` — System architecture (bots, ETL, Agent Teams)
- `operations/tools/wsl-claude-slack-setup.md` — Slack bot setup guide
- `operations/tools/wsl-claude-telegram-setup.md` — Telegram bot setup guide
- `command/decisions/admiral-systems-knowledge-vault-brief.md` — Original ETL vision
- `command/decisions/admiral-systems-ecosystem-prd.md` — This document
- `command/decisions/admiral-systems-ecosystem-diagram.html` — Interactive architecture diagram

### Playbooks
- `operations/agent-playbooks/create-linear-project.md` — Project creation workflow
- `operations/agent-playbooks/create-issue-agent.md` — Issue creation workflow
- `operations/agent-playbooks/client-feedback-playbook.md` — Feedback to Linear flow
- `operations/agent-playbooks/linear-quality-checker.md` — Quality validation
- `operations/agent-playbooks/sync-priority.md` — Priority sync workflow
- `operations/agent-playbooks/create-issue-step3b-google-sheet.md` — Google Sheet template

### SOPs
- `operations/sops/sop-build-environment.md` — Build environment policy

### Initiatives
- `operations/_initiative-index.md` — Internal initiative tracker
- `operations/beta-workflow/project-brief.md` — Beta engagement workflow
- `operations/ops-slack-bot/project-brief.md` — Davy Jones Slack bot

### Templates
- `templates/tpl-linear-task.md`
- `templates/tpl-linear-project.md`
- `templates/tpl-linear-milestone.md`
- `templates/tpl-client-brief.md`
- `templates/tpl-meeting-notes.md`
- `templates/tpl-sop.md`
- `templates/tpl-project-tracker.md`
- `templates/tpl-sprint-review.md`
- `templates/tpl-retro.md`

### Claude Code
- `.claude/commands/commit.md`
- `.claude/commands/vault-sync.md`
- `.claude/commands/history.md`
- `.claude/commands/admiral-ideas.md`
- `.claude/commands/skill-*.md` (12 bot skills)
