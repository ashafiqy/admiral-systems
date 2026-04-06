---
title: Linear Formatting Standards
created: 2026-03-10
updated: 2026-04-06
tags:
  - operations/standards
  - delivery/linear
status: active
---

# Linear Formatting Standards

Evergreen reference for how Admiral Systems formats Linear projects, issues, and milestones. All playbooks and templates follow these standards.

---

## Project Description — 3 blocks only

1. **Header** — Client · Platform · Timeline · PM · Team (one line)
2. **Overview** — 2–3 sentences, what we're building + current status
3. **Milestones table** — phases with target dates + status emoji

Nothing else. SOWs, ICE scores, strategic objectives, and client background belong in Notion/Drive — linked from Linear, not embedded in the description.

Reference template: [[tpl-linear-project]]

---

## Issue (Task) — 4 blocks only, keep template structure as-is

- **Title** — verb phrase, specific
- **Task Overview** — 1 sentence
- **Additional Notes** — task-specific links only (Figma, Webflow, Drive). Client info goes in the Project document.
- **Acceptance Criteria** — max 5 checkboxes. If you need more, split into sub-tasks.
- **Task Dropoff** — links to delivered work (added when submitting for review)

Reference template: [[tpl-linear-task]]

---

## Milestone — 3 blocks only

1. **Goal** — 1–2 sentences: what this phase achieves
2. **In Scope** — list of issues assigned to this milestone
3. **Done When** — max 3 checkboxes

Reference template: [[tpl-linear-milestone]]

---

## Issue Status — Default on Creation

- **Never create issues with status "Triage".** Always create new issues with status **"Backlog"** only. Do not set Todo, In Progress, or any other state — the team will manually move issues forward.
- Triage is reserved for issues that enter Linear through external integrations or automations and need human review before being actioned.

## Estimates — Mandatory

- **Every issue must have an estimate.** No issue should be created without one.
- Scale: 1 pt = 1hr, 2 pts = 2hrs, 3 pts = 3hrs, 4 pts = 4hrs, 5 pts = 5hrs.
- If a task exceeds 5 pts (5hrs), split it into sub-tasks.
