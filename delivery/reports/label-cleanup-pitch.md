---
title: "Label Cleanup Pitch"
created: 2026-03-10
updated: 2026-03-21
tags:
  - delivery/linear
  - type/report
status: active
---

# Linear Label Cleanup — Leadership Pitch

**Date:** March 17, 2026
**Prepared by:** Operations
**For:** Daz, Rohan

---

## The Problem

We currently have **66 labels** in Linear. In practice, most of them are never used — and the ones that are used often duplicate information already captured elsewhere (the project name, the team, the status, the priority field). The result is inconsistency: some issues have 5 labels, most have 0, and nobody agrees on what any label actually means.

This creates noise, not signal.

---

## The Principle

Before deciding what to keep, we need a clear rule for what a label is *for*.

> **A label should only exist if it adds information that cannot be derived from any other Linear field.**

Linear already tracks: which project, which team, what status, what priority, who it's assigned to, when it's due, how big it is, and which sprint it belongs to.

If a label just repeats one of those things — it goes.

---

## Why Most of Our Labels Fail This Test

### Client tags are redundant

Labels like `admiral`, `rmd`, `sprklabs`, `cartracker`, `studioscents`, `levlup`, `rcg`, `xcl`, `rcgcanada`, `plume` are all client identifiers.

But every issue already lives **inside** a client project. If you open an issue on Cartracker, it's obviously a Cartracker issue. The label adds nothing. Creating a new retainer project? We create a new project and put the issues inside it — the project carries the client context, not the label.

**All 10 client labels: delete.**

---

### Entity labels are redundant

Labels like `admiral-systems`, `rmd-co`, `sprklabs` identify which company the work belongs to.

But the team already tells you this: Admiral-Projects, RMD-Projects, Sprklabs-Projects. The label is a duplicate.

**All 3 entity labels: delete.**

---

### Location labels are redundant

`remote`, `on-site`, `hybrid` — these describe where a person works, not what an issue is. Location is a property of the assignee, not the task.

**All 3 location labels: delete.**

---

### Engagement model labels are redundant

`fixed-price`, `retainer`, `discovery-project`, `starter-pack`, `growth-pack`, `enterprise-pack` describe the commercial model of a project.

Once we enforce the project naming convention (CLIENT-MODEL-TYPE-PERIOD), the engagement model is already in the project name. And even before that — this is project-level context, not issue-level context. Labels apply to issues only; they don't appear on projects or milestones.

**All 6 engagement model labels: delete.**

---

### `blocked` and `needs-review` are redundant

Linear has native statuses for both. `blocked` maps directly to Linear's **Client Blocked** status. `needs-review` maps to **In Review**. Using labels to replicate statuses creates a split source of truth — the issue can show as "In Progress" in status but "needs-review" in labels, with no way to know which is current.

**Both: delete.**

---

### Financial and scheduling labels are redundant

`invoiced`, `paid`, `invoice-pending`, `on-hold` — financial state doesn't belong in a project management tool at the issue level. Due date and urgency labels (`overdue`, `urgent`, `this-week`, `next-week`) are redundant with Linear's due date field and priority field.

**All 8: delete.**

---

### Legacy and miscellaneous labels

Labels like `critical`, `low` (standalone, without the p0-p3 prefix), `Bug`, `Feature`, `Improvement`, `task`, `milestone`, `finance`, `ops`, `marketing`, `partnership`, `tech`, `product`, `optimization`, `devstudio`, `internal`, `client-request` — most of these are either legacy carry-overs from a previous system, Linear defaults that were never cleaned up, or vague categories with no consistent usage.

**All: delete.**

---

## What We Keep — and Why

**14 labels total.**

### Priority Labels (4)

| Label | Meaning | SLA |
|---|---|---|
| `p0-critical` | Production down or blocking a client — drop everything | 24 hours |
| `p1-high` | Must be done this week | 48 hours |
| `p2-medium` | This sprint / within 1 week | 1 week |
| `p3-low` | Backlog — do when capacity allows | No fixed SLA |

**Why keep these when Linear has a native Priority field?**

The native Priority field (Urgent / High / Normal / Low) controls sorting and filtering in Linear views — but it carries no SLA meaning. The p0-p3 labels are the team's shared language for time commitment. They stay, and we sync them to the native Priority field so both work together.

---

### Work Discipline Labels (5)

| Label | Meaning |
|---|---|
| `design` | Visual/UX design work |
| `frontend` | Client-side / UI development |
| `backend` | Server-side / API / infrastructure |
| `data` | Data, analytics, reporting |
| `content` | Copy, content creation, documentation |

**Why:** This is the only information about an issue that no other Linear field captures. The project tells you *what* you're building. The discipline label tells you *what kind of work* is needed — which drives resourcing and capacity planning. It also makes it possible to filter across all projects by skill type.

---

### Project Phase Labels (4)

| Label | Meaning |
|---|---|
| `discovery` | Early-stage research and scoping |
| `design-phase` | Design iteration before development |
| `development` | Active build phase |
| `launch` | Go-live, deployment, release |

**Why:** The status field tracks individual issue progress. The phase label tags which stage of the *engagement* the issue belongs to — useful for cross-project capacity views and sprint planning by phase.

---

### QA Flag (1)

| Label | Meaning |
|---|---|
| `needs-qa` | Completed work requiring QA sign-off before closing |

**Why:** This is a sub-signal within the In Review status. An issue can be In Review for two very different reasons: waiting for client feedback, or waiting for internal QA. This label disambiguates the two without creating separate statuses.

---

## Impact on Team Workflow

**Current minimum:** The original plan called for at least 2 labels per issue (client + discipline). Client labels are being removed.

**New minimum:** Every active issue must have at least **1 discipline label** (`design`, `frontend`, `backend`, `data`, or `content`).

Phase labels and the QA flag are applied as relevant. Priority labels (p0-p3) are applied whenever a priority decision is made — and synced to the Linear Priority field at the same time.

No other labels need to be set.

---

## The Net Result

| | Before | After |
|---|---|---|
| Total labels | 66 | 14 |
| Labels deleted | — | ~52 |
| Required labels per issue | 2 (client + discipline) | 1 (discipline) |
| Priority labels | Exist but inconsistently synced | Kept + synced to native Priority field |
| Client context on issues | Duplicated via label | Already in the project — no label needed |

**One line:** We go from 66 labels that create confusion to 14 labels that each add something no other Linear field already tells you.

---

## Decision Required

Approve this label set so the cleanup can be executed. No changes will be made in Linear until this is signed off.

Labels to delete: ~52 (all client, entity, location, engagement model, financial, scheduling, and legacy labels)
Labels to keep: 14 (priority × 4, discipline × 5, phase × 4, QA flag × 1)
