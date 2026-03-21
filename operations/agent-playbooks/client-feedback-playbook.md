---
title: "Playbook: Client Feedback to Linear"
created: 2026-03-09
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# Client Feedback Agent — Playbook

This agent handles the end-to-end workflow for turning client feedback into Linear tasks, a project status update, and a Slack message for the team.

## Execution Order

1. **Look up label IDs** — call `list_issue_labels` for the relevant team. Find IDs for "Design" and "Development". If missing, call `create_issue_label` to create them.

2. **Create Linear issues** — use `save_issue` for each task derived from client feedback. Follow [[tpl-linear-task]] for description structure. Required params per issue:
   - `title`: verb-phrase, descriptive
   - `team`: confirmed team ID (never use Test-DeliveryHQ)
   - `project`: confirmed project ID
   - `milestone`: confirmed milestone ID
   - `assignee`: confirmed user ID
   - `priority`: 1 (Urgent) for client-driven tasks
   - `dueDate`: ISO format (YYYY-MM-DD)
   - `labels`: array with relevant label ID(s)
   - `blockedBy`: array of issue identifiers (e.g. `["DLVRY-634", "DLVRY-635"]`) for dependent tasks
   - Capture returned issue URL for each

3. **Post project status update** — use `save_status_update` on the project. Include:
   - What the client confirmed
   - Links to newly created issues (with identifiers)
   - Key workflow steps (e.g. Relume → Webflow export workflow)
   - Useful links (prototype, meeting recording, Relume project)
   - Deadlines
   - Resource plan and any blockers
   - Do NOT include: client email quotes, internal financials, "big big boss" language, contract details
   - Capture returned status update URL

4. **Write Slack update MD file** — save to `/client_feedback/slack-update-[name]-[date].md`. Replace all `{LINK}` placeholders with actual URLs from steps 2–3 before writing.

5. **Create this agent folder** (one-time setup — already done if this file exists).

---

## Key Rules

- NEVER use Test-DeliveryHQ or any test team/project
- Always verify project team before creating issues (`get_project` to confirm team)
- Always use `get_issue` with the issue identifier (e.g. `RCG-19`) to look up specific issues — `list_issues` may return empty even if issues exist
- Task descriptions must follow [[tpl-linear-task]]: Overview → Additional Notes → Acceptance Criteria (max 5) → Task Blockers → Task Dropoff
- Slack message must replace all `{LINK}` placeholders with real URLs before writing the file
- Status update and Slack message must mirror all critical workflow details (account, project name, export rules, deadlines)
- When tasks have dependencies, use `blockedBy` on the dependent task and reference the blocking issue identifiers in the Task Blockers section of the description
- For RACI role assignments, reference [[roles-responsibilities-2026-q1]] for the current team structure

---

## Sensitive Info — Never Include

The following must never appear in Linear (issues, status updates) or Slack messages:
- Direct quotes from client emails
- Internal financial data (margins, budget, contract values)
- HR / SAP system details
- Internal stakeholder hierarchy language (e.g. "big big boss")
- Contract or SOW details

---

## Reference Files

| File | Purpose |
|---|---|
| [[tpl-linear-task]] | Template for Linear issue descriptions |
| [[create-linear-project]] | Full project + milestone + issue creation playbook |
| [[linear-standards]] | Linear formatting standards |
