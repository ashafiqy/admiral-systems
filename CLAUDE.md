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
| Financial tracking | `finance/` |
| Sales & growth | `growth/` |

## Team
See `team/_team-roster.md` for the current roster.

## Active Clients
See `clients/_client-index.md` for the current client list.
