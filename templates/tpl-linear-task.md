---
title: "Template: Linear Task/Issue Description"
created: 2026-02-18
updated: 2026-03-21
tags:
  - type/template
  - delivery/linear
status: active
---

<!-- TEMPLATE USAGE RULES
- Task body target: 150–250 words (excluding Metadata block and blockquotes)
- RACI is mandatory — fill all four fields; use "—" only if genuinely no one applies
- "Task Overview": 2–3 sentences only; NO background, brand references, or training links
- Additional Notes: ALLOWED — use only for task-specific reference links (Figma, Drive, staging URLs, tool URLs). Max 5 bullets under "Reference Materials:". DO NOT add: brand colors, competitor sites, general training videos — those belong in the EPIC
- Acceptance Criteria: max 15 items; each must be binary (checkable yes/no)
- Metadata: do not duplicate fields Linear auto-tracks (Status, URL, Created, Updated)
-->

# [Phase.Number]: [Task Title]

**Points:** [X] pts | **Sprint:** Week [X] | **Phase:** Phase [X] – [Phase Name]

## RACI

> _Who owns this task. R = does the work, A = signs off on output, C = consulted for input, I = kept informed. All four fields are required — use "—" only if genuinely not applicable._

| R (Does work)    | A (Approves) | C (Input needed) | I (Kept updated) |
| ---------------- | ------------ | ---------------- | ---------------- |
| [Name ([X] pts)] | [Name]       | [Name]           | [Name]           |

**Escalation:** Tag @[name] for [design/dev/content] questions. Tag @[PM] only for PM decisions.

## Task Overview

> _2–3 sentences only. What is being built or delivered, and what the outcome looks like. Background and rationale belong in the EPIC — link it below._

[2–3 sentences maximum. State the deliverable and outcome — not the background or rationale.
Context and strategic reasoning belongs in the EPIC. See: [EPIC Link →]]

## Acceptance Criteria

> _Pass/fail checklist — each item must be independently verifiable (done or not done). Maximum 15 items._

- [ ] [(Assignee) if parallel workstreams] [Specific, binary, pass/fail item]

## Blockers

> _List anything preventing progress. Mark the task as Blocker in Linear and tag the Accountable person above if you're stuck._

## Dropoff

> _Where to deliver the finished work — Figma link, Drive folder, staging URL, etc. Mark the task In Review once all items below are delivered._

- [Deliverable 1: e.g. Figma link, Google Drive folder, Webflow staging URL]

## Additional Notes

> _Task-specific reference links only — not brand context, training materials, or competitor sites._

**Reference Materials:**

- [link type]: [URL or placeholder]

## Metadata

> _Linear tracking fields. Do not duplicate fields Linear auto-tracks (Status, URL, Created, Updated)._

- Identifier: [PROJECT-PREFIX-Number]
- Assignee: [Name ([X] pts)][, Name ([Y] pts) if multiple]
- Labels: Phase-[X], [Topic-Tag], Week-[X]
- Depends on: [Task ID or prerequisite condition]
- Blocks: [Task ID or downstream task]
- Estimate: [X] points

---

> **Playbooks:** [[create-issue-agent]] · **Standards:** [[linear-standards]]
