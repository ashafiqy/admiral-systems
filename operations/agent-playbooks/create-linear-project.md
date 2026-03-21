---
title: "Playbook: Create Linear Project"
created: 2026-02-18
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# How to Create a New Linear Project

Agent playbook for setting up a new Admiral project in Linear from scratch — including the project, milestone objects, and initial issues — following Admiral's templates and standards.

---

## Step 0 — Gather Info Before Touching Linear

Run these two lookups first so you have the correct names/IDs:

```
list_teams                    → confirm the team name (e.g. "DeliveryHQ")
list_users                    → get exact names for PM and team members
list_users filtered by team   → verify every issue assignee appears in that team's member list
```

> If any assignee is missing from the team, use a different team or resolve their membership **before proceeding**. Assigning issues to non-members will fail silently or error.

Then collect the following from the PM before creating anything:

- [ ] Project name (following naming convention: `{CLIENT}-{Phase}-{Type}`)
- [ ] Client name, project type (Retainer / Fixed-scope / Pro Bono), platform (Webflow / HubSpot / Custom)
- [ ] PM name + each team member's name, role, and key responsibility
- [ ] Start date + target date + hard deadline (if applicable)
- [ ] Phase names and target dates (expect 4 phases)
- [ ] Google Drive link + Figma link (may be TBC)
- [ ] Initial tasks to create per phase (title + 1-sentence overview + acceptance criteria)
- [ ] Confirm all issue assignees are members of the target team (verified via `list_users` filtered by team)

> For RACI role assignments, reference [[roles-responsibilities-2026-q1]] for the current team structure (Leadership / Senior / Junior tiers and responsibilities).

Do not proceed to Step 1 until all of the above is confirmed.

---

## Step 1 — Create the Project

**Tool:** `save_project`

**Required params:** `name`, `addTeams`, `startDate`, `targetDate`, `lead`

**Key params:**
| Param | What to set |
|---|---|
| `name` | Project slug e.g. `WLX-Beta-WebsiteRedesign` |
| `addTeams` | Team name from `list_teams` e.g. `"DeliveryHQ"` |
| `lead` | PM's name from `list_users` |
| `startDate` | ISO format: `YYYY-MM-DD` |
| `targetDate` | ISO format: `YYYY-MM-DD` (target, not hard deadline) |
| `summary` | 1 sentence, max 255 chars — this shows on project cards |
| `description` | Full markdown — see format below |

**Description format** — fill in [[tpl-linear-project]] exactly.

---

## Step 2 — Create Milestone Objects (one per phase)

**Tool:** `save_milestone` — run once per phase. 4 calls total.

**Required params:** `project`, `name`
**Optional but important:** `targetDate`

**Naming convention:** `Phase N: Focus Area Description`

After creating all 4, verify their names match what's in the Milestones table inside the project description.

---

## Step 3 — Create Initial Issues

**Tool:** `save_issue`

**Required params:** `title`, `team`
**Important params:** `project`, `milestone`, `assignee`, `priority`, `state`, `estimate`, `dueDate`, `labels`

> **Always set `state: "Todo"`** on every `save_issue` call. Omitting it defaults to Triage — issues land in a hidden inbox and won't appear on the project board.

**Issue title rules:**
- Verb phrase, specific — "Design Homepage Hero Section" not "Homepage"
- Never just a noun or vague label

**Estimates:** Use Fibonacci scale — 1 · 2 · 3 · 5 · 8 pts. 1 pt = 2 hrs deep work.

**Priority labels:** Use existing workspace labels. Derive from ICE score if available:
- `p0-critical` — ICE ≥ 450
- `p1-high` — ICE 340–449
- `p2-medium` — ICE 260–339
- `p3-low` — ICE < 260

**Priority field** (Linear's built-in sort/filter field — set this alongside the label):
- p0-critical → `priority: 1` (Urgent)
- p1-high → `priority: 2` (High)
- p2-medium → `priority: 3` (Normal)
- p3-low → `priority: 4` (Low)

> Always set both `labels` AND `priority` so the Linear board sorts correctly when filtered by priority.

**Due dates:** Derive from milestone target date + priority tier. P0 issues early in the window, P3 at the end.

**Description format** — follow [[tpl-linear-task]] exactly. RACI and ICE sections are **included when the project warrants it** (senior projects, internal workflow work, or when the PM requests it). Reference [[roles-responsibilities-2026-q1]] for RACI role lookups.

**Example call:**

```
save_issue
  title: "Design Homepage Hero Section"
  team: "DeliveryHQ"
  project: "{PROJECT-NAME}"
  milestone: "Phase 2: Wireframes & Visual Design"
  assignee: "Tiara"
  priority: 2
  state: "Todo"
  estimate: 3
  dueDate: "2026-02-20"
  labels: ["p1-high"]
  description: (use Task_Template format, filled in)
```

---

## Step 4 — What NOT to Do

**In the project description — never embed:**
- RACI matrix → add as a project-specific section only if seniors request it
- Sitemap or deliverables list → project-specific, not a template section
- Risk register or Dependencies table → belongs in Drive/SOW
- SOW or contract → seniors-only, never in the project description
- Communication channels → not needed in Linear

**In issue descriptions — never include:**
- Client background or project context → it lives in the project, not the issue
- More than 5 acceptance criteria checkboxes → split into sub-tasks
- Pre-filled Task Blockers or Task Dropoff → the team owns these

**Staging site link:** only add it once Webflow is actually set up. Leave as "TBC" until then.

---

## Reference

| | |
|---|---|
| Project description template | [[tpl-linear-project]] |
| Issue description template | [[tpl-linear-task]] |
| Milestone description template | [[tpl-linear-milestone]] |
| Team structure & RACI roles | [[roles-responsibilities-2026-q1]] |
| Good project description example | `SB-AST-JirehLaw` in Linear |
| Good milestone structure example | `HPL-BETA-RMD-2026` in Linear |
