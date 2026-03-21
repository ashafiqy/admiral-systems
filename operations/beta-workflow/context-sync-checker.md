---
title: "Context Sync Checker"
created: 2026-03-01
updated: 2026-03-21
tags:
  - operations/beta-workflow
  - type/tool
status: active
---

# TODO: Context Sync Checker Agent

> Status: Not started. Not needed now or soon. Build when the team has a regular cadence of meeting notes and client updates flowing into the repo and Linear needs to stay in sync with them.

---

## What This Agent Does

Given a new input document (meeting notes, client email, updated brief), this agent reads the relevant Linear project and flags which issues are now stale, affected, or need updating — and which new issues need to be created.

It acts as the bridge between "new information arrived" and "Linear reflects current reality."

---

## Inputs Required

- Path to the new context document (e.g. `Meetings/Weekly seniors alignment - 09 Mar 2026.md`)
- The Linear project identifier to check against (e.g. `AST-Internal-BetaWorkflow`)

---

## Process

### Step 1 — Read New Context
Read the input document in full. Extract:
- New decisions made
- Scope changes (additions or removals)
- New action items assigned
- Any blockers or risks surfaced
- Any deadlines changed

### Step 2 — Pull Current Linear State
```
list_issues on the project  →  all current issues with title, assignee, status, description
get_project  →  project description, milestones
```

### Step 3 — Cross-Reference
For each new decision/change/action item from the context document:
- Find the matching issue (if any) — match by title intent, not just keyword
- Determine the impact:
  - **Update needed** — issue exists but its description, AC, assignee, or due date is now wrong
  - **New issue needed** — action item not covered by any existing issue
  - **Close/deprioritise** — scope item was removed or cancelled

### Step 4 — Output Report

Produce a structured action list:

```
CONTEXT SYNC REPORT — {PROJECT-NAME}
Source document: {file path or description}
Run on: {date}

ISSUES TO UPDATE ({N})
  - {AST-XXX} "{title}"
    What changed: {specific field or context that changed}
    Suggested update: {what to change in the issue}

NEW ISSUES TO CREATE ({N})
  - "{suggested title}"
    Source: {quote or summary from context document}
    Suggested milestone: {phase}
    Suggested assignee: {name}

ISSUES TO CLOSE OR DEPRIORITISE ({N})
  - {AST-XXX} "{title}"
    Reason: {why it's no longer needed or should be deprioritised}

NO ACTION NEEDED
  - All other existing issues remain valid.
```

### Step 5 — Human Review Gate
This agent **only produces a report** — it does not auto-update, auto-create, or auto-close any issues. All changes require human review and approval before execution.

To action the report:
- Use `create-issue-agent.md` to create new issues
- Use `save_issue` directly to patch existing issues
- Use `save_issue` with state change to close or archive issues

---

## When to Run

- After every client meeting where decisions were recorded
- After an updated brief or SOW is added to the repo
- After any `Meetings/` file is added or updated
- Before a sprint planning session to ensure Linear reflects the latest context

---

## Dependencies

- Requires meeting notes or client updates to be stored in the repo (under `Meetings/` or `Plans/`)
- Requires Linear MCP to be connected (`list_projects` returns results)
- Works best when issue descriptions follow `templates/Task_Template.md` — structured descriptions make cross-referencing more reliable

---

## Why This Was Deferred

The team does not yet have a consistent cadence of structured meeting notes flowing into the repo. Once that cadence is established and the workflow is proven on a live client project, this agent will provide high value. Building it before the input format is stable would result in a brittle checker that needs constant revision.

Build trigger: when `Meetings/` folder has at least 3 structured notes following a consistent format and the team is actively maintaining Linear as the source of truth for a live client project.
