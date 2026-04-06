# Admiral Systems — Company Vault

## About
Admiral Systems is a digital agency. This vault is the shared company knowledge base — everything here is visible to the team (PMs, founders, delivery leads).

**Rule: Do not put private or personal content here. Personal Admiral thoughts go in the sharkie vault.**

## Vault Structure

```
admiral-systems/
  inbox/              ← Quick capture for company items
  command/            ← Strategy, OKRs, leadership decisions, key meetings
    strategy.md
    okrs/                ← Quarterly OKRs
    decisions/           ← Strategic decision log
    meetings/            ← leadership/, all-hands/, retros/
  clients/            ← One folder per client
    _client-index.md     ← Master list of all clients
    _template-client/    ← Copy this for new clients
  delivery/           ← Sprint management, capacity, risks, processes
    sprint-current.md
    sprint-archive/
    capacity.md
    risks.md
    processes/           ← Delivery SOPs
  team/               ← Team roster, hiring, onboarding
    _team-roster.md
    _hiring/
    _onboarding/
  operations/         ← Internal tools and SOPs
    agent-playbooks/     ← Agent workflow definitions
    beta-workflow/       ← Beta engagement workflow
    sops/                ← Standard operating procedures
    tools/               ← Setup guides, scripts, architecture docs
  finance/            ← Revenue tracking, billing, budgets
  growth/             ← Pipeline, proposals, case studies, partnerships
  templates/          ← Company templates (tpl-*.md)
```

## Conventions

### File Naming
- **kebab-case**: `client-brief.md`, not `Client Brief.md`
- Meeting notes: `YYYY-MM-DD-{title}.md`
- Templates: `tpl-{type}.md`

### Frontmatter Standard
```yaml
---
title: Note Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
tags:
  - area/topic
status: active | draft | review | archived
---
```

### Tags
- `#client/{name}` — client-specific
- `#delivery/sprint`, `#delivery/risk`
- `#team/{name}` — team member specific
- `#type/meeting`, `#type/decision`, `#type/sop`
- `#finance/billing`, `#finance/revenue`
- `#growth/pipeline`, `#growth/proposal`

### Content Routing Rules
| Content Type | Destination |
|---|---|
| Strategy & OKRs | `command/` |
| Client work | `clients/{client-name}/` |
| Sprint & delivery | `delivery/` |
| Team management | `team/` |
| Tools & SOPs | `operations/` |
| Internal tools & setup guides | `operations/tools/` |
| Strategic decisions & vision docs | `command/decisions/` |
| Financial tracking | `finance/` |
| Sales & growth | `growth/` |

## Templates

**Always check `templates/` before creating new content.** Use the matching template when one exists.

| Template | Use When |
|---|---|
| `tpl-linear-task.md` | Creating Linear issues — RACI, acceptance criteria, blockers, dropoff (mandatory structure) |
| `tpl-linear-project.md` | Creating Linear projects — project brief, team, milestones, resources |
| `tpl-linear-milestone.md` | Creating Linear milestones — goal, in-scope issues, done-when criteria |
| `tpl-client-brief.md` | Setting up a new client folder — overview, contacts, scope, key dates |
| `tpl-meeting-notes.md` | Capturing meeting notes — agenda, discussion, decisions, action items |
| `tpl-sop.md` | Writing SOPs — purpose, when to use, steps, owner |
| `tpl-project-tracker.md` | Tracking a project in the vault — milestones, tasks, risks, log |
| `tpl-sprint-review.md` | Sprint reviews — completed, carry-over, metrics, next focus |
| `tpl-retro.md` | Retrospectives — went well, didn't go well, improvements, action items |

Also see `operations/agent-playbooks/` for agent-specific workflows (e.g. `client-feedback-playbook.md` for the full Linear issue creation flow).

### Linear Rules
- **Never create issues with status "Triage".** Always create new issues with status **"Backlog"** only. Do not set Todo, In Progress, or any other state — the team will manually move issues forward.
- **Every issue must have an estimate.** Use the scale: 1 pt = 1hr, 2 pts = 2hrs, 3 pts = 3hrs, 4 pts = 4hrs, 5 pts = 5hrs.

## System Architecture
See [[remote-claude-architecture]] for the remote access system design (bots, ETL, Agent Teams).
See [[admiral-systems-knowledge-vault-brief]] for the original ETL vision.

## Change History
See [[HISTORY]] for a log of structural changes to this vault.

## Team
See [[_team-roster]] for the current roster.

## Active Clients
See [[_client-index]] for the current client list.
