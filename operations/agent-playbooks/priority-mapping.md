---
title: "Priority Mapping: Labels to Linear Priority Field"
created: 2026-03-10
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# Priority Mapping: Labels → Linear Priority Field

## Overview

Admiral Systems uses a custom **p0–p3 label system** to tag issues with priority in Linear. These labels coexist with Linear's native Priority field. Both are set simultaneously — labels provide semantic context and team-facing SLA clarity, while the native Priority field enables Linear's built-in sorting, filtering, and priority views.

**Do not remove labels when syncing priority. Labels stay on the issue permanently.**

---

## Priority Mapping Table

| Label | Meaning | SLA | Linear Priority | MCP Integer |
|---|---|---|---|---|
| `p0-critical` | Drop everything — production down or blocking a client | 24 hours | Urgent | `1` |
| `p1-high` | Must be done this week | 48 hours | High | `2` |
| `p2-medium` | This sprint / within 1 week | 1 week | Normal | `3` |
| `p3-low` | Backlog — do when possible | No fixed SLA | Low | `4` |

---

## Key Rules

1. **Labels are canonical** — the p0–p3 labels are the source of truth for priority, not the Linear Priority field. When there is a conflict, trust the label.
2. **Both must be set** — always sync the Linear Priority field to match the label so issues can be sorted in Linear views.
3. **No-label issues → no priority change** — if an issue has no p0–p3 label, leave the Priority field untouched.
4. **Older labels are not canonical** — a standalone `critical` label (without the `p0-` prefix) is legacy and should not be used for mapping. Only use `p0-critical`, `p1-high`, `p2-medium`, `p3-low`.
5. **Archived team issues** — issues from archived teams (e.g., old Sprklabs `SPL-*` issues) may be inaccessible via MCP. Skip any `Entity not found` errors and continue.

---

## Company Context

The workspace runs 3 companies under the Admiral umbrella:

- **AdmiralSystems** — main company, client projects tracked in `Admiral-Projects` team
- **RMD** — sub-company, client projects tracked in `RMD-Projects` team
- **Sprklabs** — sub-company, client projects tracked in `Sprklabs-Projects` team

All internal work lives in the `Internal` team. Priority labels apply workspace-wide across all companies.

---

## Why Both Label + Priority Field?

Linear's built-in Priority field (Urgent / High / Normal / Low) controls:
- Column ordering in Board view
- Sort order in List view
- Priority filter in the sidebar
- Priority-based reporting in Insights

Labels alone do not drive these views. By syncing both, issues are correctly surfaced in all Linear views without removing the human-readable SLA context the labels provide.
