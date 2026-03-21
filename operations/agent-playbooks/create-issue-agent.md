---
title: "Playbook: Add Issues to Existing Project"
created: 2026-02-18
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# How to Add New Issues to an Existing Linear Project

Agent playbook for creating one or more new issues inside an existing Admiral Linear project — without touching the project or milestone setup.

---

## Step 0 — Confirm Project Context

Before creating anything, read the project to confirm it exists and pull its current state:

```
get_project  →  confirm project name, ID, description, and milestone structure
list_milestones  →  get exact milestone names and IDs to assign issues to
list_users  →  confirm assignee names are valid members of the team
```

Do not proceed until you have:
- [ ] Confirmed the project exists and is active
- [ ] A list of all current milestones with names and IDs
- [ ] Confirmed all intended assignees appear in `list_users` for this team

---

## Step 1 — Duplicate Check (mandatory)

Run `list_issues` on the project and scan every existing issue title.

For each proposed new issue title:
- Check for **exact matches** — identical title
- Check for **semantic matches** — same verb + same subject, even if worded differently
  - e.g. "Document Step 2" vs "Write the Step 2 SOP" → same intent → flag it
  - e.g. "Set up Google Analytics" vs "Configure GA4 for Webflow" → same intent → flag it

**If a conflict is found:**
- Stop. Do not create the issue.
- Report: `DUPLICATE DETECTED: "{proposed title}" conflicts with existing "{existing title}" ({identifier})`
- Wait for the PM to resolve

Only proceed to Step 2 once all proposed titles are confirmed as unique.

---

## Step 2 — Gather Required Info Per Issue

For each new issue, collect:

| Field | Required | Notes |
|---|---|---|
| Title | Yes | Verb phrase, specific. "Design Homepage Hero" not "Homepage" |
| Milestone | Yes | Must match an existing milestone name exactly |
| Assignee | Yes | Must match a name from `list_users` |
| State | Yes | Always `"Todo"` — never omit |
| Estimate | Yes | Fibonacci: 1 · 2 · 3 · 5 · 8 pts (1 pt = 2 hrs deep work) |
| Priority label | Yes | p0-critical / p1-high / p2-medium / p3-low |
| Priority field | Yes | Must match label: p0→1, p1→2, p2→3, p3→4 |
| Due date | Yes | ISO format YYYY-MM-DD. Derive from milestone window + priority tier |
| RACI | When warranted | Senior projects, internal workflow work, or PM requests it |
| ICE Score | When warranted | Required if RACI is included |

> **Priority field and label must always be set together.**

---

## Step 3 — Create Issues

**Tool:** `save_issue` — one call per issue.

**Description format** — follow [[tpl-linear-task]] exactly.

> Task Blockers and Task Dropoff must be **left empty** on creation — the team fills these in during the work.

---

## Step 4 — Verify Each Issue

After creating each issue, run `get_issue` on its returned ID and confirm:

- [ ] `state` is `"Todo"` (not Triage or Backlog)
- [ ] `estimate` is set
- [ ] `dueDate` is set
- [ ] `labels` contains exactly one p0/p1/p2/p3 label
- [ ] `priority` field value matches the label (p0→1, p1→2, p2→3, p3→4)
- [ ] `milestone` is set to the correct phase

---

## What NOT to Do

- Never create an issue without first running the duplicate check (Step 1)
- Never omit `state: "Todo"` — issues default to Triage and disappear from the board
- Never set `priority` without also setting `labels`, or `labels` without `priority`
- Never pre-fill Task Blockers or Task Dropoff — leave both empty
- Never create more than 5 Acceptance Criteria checkboxes — split into sub-tasks instead
- Never embed client background or project context in the issue

---

## Reference

| | |
|---|---|
| Issue description template | [[tpl-linear-task]] |
| Full project creation playbook | [[create-linear-project]] |
| Quality checker (run after this) | [[linear-quality-checker]] |
