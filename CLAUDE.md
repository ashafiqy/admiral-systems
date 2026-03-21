# Admiral Systems — Company Vault

## About
Admiral Systems is a digital agency. This vault is the shared company knowledge base — everything here is visible to the team (PMs, founders, delivery leads).

**Rule: Do not put private or personal content here. Personal Admiral thoughts go in the sharkie vault.**

## Vault Structure

```
admiral-systems/
  00-inbox/              ← Quick capture for company items
  05-command/            ← Strategy, OKRs, leadership decisions, key meetings
    strategy.md
    okrs/                ← Quarterly OKRs
    decisions/           ← Strategic decision log
    meetings/            ← leadership/, all-hands/, retros/
  10-clients/            ← One folder per client
    _client-index.md     ← Master list of all clients
    _template-client/    ← Copy this for new clients
  15-delivery/           ← Sprint management, capacity, risks, processes
    sprint-current.md
    sprint-archive/
    capacity.md
    risks.md
    processes/           ← Delivery SOPs
  20-team/               ← Team roster, hiring, onboarding
    _team-roster.md
    _hiring/
    _onboarding/
  25-operations/         ← Internal tools and SOPs
  30-finance/            ← Revenue tracking, billing, budgets
  35-growth/             ← Pipeline, proposals, case studies, partnerships
  40-templates/          ← Company templates (tpl-*.md)
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
| Strategy & OKRs | `05-command/` |
| Client work | `10-clients/{client-name}/` |
| Sprint & delivery | `15-delivery/` |
| Team management | `20-team/` |
| Tools & SOPs | `25-operations/` |
| Financial tracking | `30-finance/` |
| Sales & growth | `35-growth/` |

## Team
See `20-team/_team-roster.md` for the current roster.

## Active Clients
See `10-clients/_client-index.md` for the current client list.
