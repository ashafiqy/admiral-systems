---
title: "Playbook: Linear Quality Checker"
created: 2026-02-18
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# Linear Quality Checker

Agent playbook for verifying that a Linear project and its issues meet Admiral's standards. Run this after every `create-linear-project` or `create-issue-agent` execution.

---

## When to Run

- After creating a new project (post [[create-linear-project]])
- After adding new issues to an existing project (post [[create-issue-agent]])
- As a periodic health check on any active project
- Before handing a project over to a client or presenting it to the team

---

## Step 0 — Pull Project Data

```
get_project    →  read project description and metadata
list_milestones  →  confirm milestone objects exist
list_issues    →  pull all issues (use project identifier)
```

Collect all returned data before starting checks. Do not check incrementally — read everything first.

---

## Step 1 — Project Description Check

Read the project description and verify it follows the 3-block format from [[tpl-linear-project]]:

| Check | Pass Condition |
|---|---|
| Has **Project Brief** table | Client, Type, Platform, PM, Target Date, Hard Deadline, Live URL all present |
| Has **The Ask** section | 2–3 sentences max |
| Has **Team** table | Role, Name, Responsibility columns present |
| Has **Milestones** table | All 4 phases listed with target dates and status |
| Has **Resources** section | Google Drive and Figma links present (TBC is acceptable) |
| No RACI embedded | RACI must not appear in the project description |
| No SOW embedded | SOW, contract, or risk register must not be in the description |

---

## Step 2 — Milestone Objects Check

| Check | Pass Condition |
|---|---|
| 4 milestones exist | `list_milestones` returns exactly 4 results |
| Names match table | Milestone object names match the Milestones table exactly |
| Target dates set | Each milestone has a `targetDate` |

---

## Step 3 — Issue Quality Check

### Required Fields

| Field | Pass Condition |
|---|---|
| `state` | Is `"Todo"` |
| `estimate` | Is set (1, 2, 3, 5, or 8) |
| `dueDate` | Is set in ISO format |
| `labels` | Contains exactly one p0/p1/p2/p3 label |
| `priority` | Is set to 1, 2, 3, or 4 |
| `milestone` | Is assigned to one of the 4 project milestones |
| `assignee` | Is set |

### Priority Consistency Check

| Label | Expected priority value |
|---|---|
| p0-critical | 1 (Urgent) |
| p1-high | 2 (High) |
| p2-medium | 3 (Normal) |
| p3-low | 4 (Low) |

### Description Quality Check

| Check | Pass Condition |
|---|---|
| Title is a verb phrase | Starts with an action verb; specific not vague |
| Task Overview is 1 sentence | Present and concise |
| Acceptance Criteria present | At least 1 checkbox, max 5 |
| Task Blockers is empty | Should be blank on creation |
| Task Dropoff is empty | Should be blank on creation |
| No client context embedded | Client background should not appear in the issue |

---

## Step 4 — Duplicate Detection

Scan all issue titles for exact and semantic duplicates. Flag for human review — do not auto-resolve.

---

## Step 5 — Output Report

Produce a structured pass/fail report with specific issue identifiers and fixes for any failures.

---

## Reference

| | |
|---|---|
| Project description template | [[tpl-linear-project]] |
| Issue description template | [[tpl-linear-task]] |
| Create issue playbook | [[create-issue-agent]] |
| Create project playbook | [[create-linear-project]] |
