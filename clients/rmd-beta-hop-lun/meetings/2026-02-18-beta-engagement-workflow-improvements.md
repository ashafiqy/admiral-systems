---
title: "Beta Engagement Workflow Improvements"
created: 2026-02-18
updated: 2026-03-21
tags:
  - client/hop-lun
  - type/meeting
status: active
---

# Session: Beta Engagement Workflow Improvements
**Date:** 2026-02-18
**Session type:** Template revision + process improvement
**Files changed:** `artifacts/Task Template.md`, `artifacts/BetaEngagement Template.md`
**Files created:** `sessions/README.md`, `sessions/2026-02-18_beta-engagement-workflow-improvements.md`

---

## Session Summary

The Beta Engagement automation system was producing tasks that were too long, missing task-level RACI, and starting Webflow setup later than necessary. This session addressed all three problems by revising the Task Template, inserting a new Sub-Phase 2C into the BetaEngagement Template, and adding a structured Claude prompt template with a quality checklist. A `sessions/` folder was established as a permanent changelog for future improvements.

---

## Artifacts Analyzed

| File | Key Findings |
|---|---|
| `artifacts/Task Template.md` | No RACI block; "Additional Notes" section had no guardrails; no word count guidance; Metadata duplicated Linear auto-tracked fields (URL, Status, Created, Updated) |
| `artifacts/BetaEngagement Template.md` | Phase 2 (Design) and Phase 3 (Development) were fully sequential — Webflow setup not starting until Week 4; no AI task generation guidance |
| `artifacts/Example AI Generated Task.md` | 600+ word output; included brand colors, reference websites, training links in task body; no RACI block |

---

## Pain Points Identified

1. **No task-level RACI** — team had to cross-reference the phase brief to find who to escalate to; escalation paths were unclear inside each task
2. **AI tasks were too verbose** — Claude filled "Additional Notes" with brand colors, reference sites, and training links that belong in the EPIC, not individual tasks; default output was 600+ words
3. **No word count guardrails** — nothing in the template told Claude (or humans) how long a task should be; 250-word target was never established
4. **Webflow setup started too late** — Phase 3 Week 1 was wasted on project setup and variable entry that could have been done in parallel with late Phase 2 design work

---

## Decisions Made

| Workstream | Decision | Rationale |
|---|---|---|
| Task Template | Add RACI block as mandatory section | Escalation paths must live inside each task, not just the phase brief |
| Task Template | Add template usage rules comment block at top | Gives Claude (and humans) explicit constraints before the template fields |
| Task Template | Remove "Additional Notes" section entirely | Context belongs in the EPIC; the section was being misused for brand and training content |
| Task Template | Set 150–250 word target for task body | Establishes a testable constraint; current output was 3–4× longer than needed |
| Task Template | Simplify Metadata | Remove URL, Status, Created, Updated — Linear auto-tracks these; duplication creates maintenance debt |
| BetaEngagement Template | Insert Sub-Phase 2C: Webflow Foundation | 3 tasks (project setup, variables entry, CMS architecture) run parallel to Phase 2B; ~10 pts drawn from Phase 3 budget; Phase 3 Week 1 then begins on page builds immediately |
| BetaEngagement Template | Add Claude task generation section | Structured prompt template + required inputs + quality checklist; reduces AI output variance and eliminates common failure modes |
| Repo structure | Create `sessions/` folder | Running changelog committed to GitHub; decisions are traceable alongside the files they describe |

---

## Changes Made

### `artifacts/Task Template.md` — full rewrite

**Removed:**
- `# Task Overview` section with freeform description field
- `## Additional Notes` section
- Metadata fields: URL, Status, Created, Updated, Project (with HPL-specific hardcoded link), Sub-issues

**Added:**
- Template usage rules comment block (word count target, RACI rules, section restrictions)
- `## RACI` section with 4-column table (R/A/C/I) + Escalation line
- Phase/sprint/points header line
- `## What We're Doing` (labeled 2–3 sentence limit)
- `## Blockers` with escalation instruction + common blockers placeholder
- `## Dropoff` with "In Review" trigger instruction
- Simplified Metadata: Identifier, Assignee, Labels, Depends on, Blocks, Estimate only

### `artifacts/BetaEngagement Template.md` — two insertions

**Insertion 1:** Sub-Phase 2C: Webflow Foundation (inserted between Phase 2 and Phase 3)
- 2C1: Webflow Project Setup (2 pts) — triggered at 50% design system completion
- 2C2: Design Variables Entry — Colors, Typography, Spacing (4 pts) — triggered per token category lock
- 2C3: CMS Collections Architecture (4 pts) — triggered at 60% page designs complete
- Capacity note: draws from Phase 3 budget; Phase 3 Week 1 opens on page builds

**Insertion 2:** "Using Claude to Generate Tasks" section (appended after handover section)
- Required inputs list (7 items) — establishes what must be known before generating a task
- Claude prompt template (copy-paste ready, with CONTEXT block to fill)
- Quality checklist (8 binary items to check before saving to Linear)

**Updated:** Version bumped from 2.0 → 2.1, Last Updated from December 2024 → February 2026, Next Review from January 2025 → July 2026

---

## Claude Prompt Template

The following prompt is embedded in `artifacts/BetaEngagement Template.md` under "Using Claude to Generate Tasks." It is duplicated here for quick access without opening the playbook.

```
You are generating a single Linear task for an Admiral Systems Beta Engagement project.
Follow these rules exactly. Do not add sections not listed in the format below.

FORMAT RULES:
- Task body: maximum 250 words (excluding Metadata block)
- Sections allowed: RACI, What We're Doing, Acceptance Criteria, Blockers, Dropoff, Metadata
- Sections NOT allowed: Additional Notes, Background, Context, Brand Colors, Reference Websites,
  Training Materials — these belong in the EPIC and Phase Brief, not the task
- RACI: all four fields must be filled; use "—" only if genuinely no one applies
- "What We're Doing": 2–3 sentences only; state the deliverable; link to EPIC for context
- Acceptance Criteria: maximum 10 items; each must be binary (pass/fail testable)
- If parallel workstreams: prefix each criterion with (Name) in parentheses

OUTPUT FORMAT:
# [Phase.Number]: [Task Title]
**Points:** [X] pts | **Sprint:** Week [X] | **Phase:** Phase [X] – [Phase Name]

## RACI
| R (Does work) | A (Approves) | C (Input needed) | I (Kept updated) |
|---|---|---|---|
| [Name ([X] pts)] | [Name] | [Name] | [Name] |

**Escalation:** Tag @[name] for [type] questions. Tag @[PM name] only for PM decisions.

## What We're Doing
[2–3 sentences. State deliverable and outcome. End with: "See [EPIC/Phase Brief] for context →"]

## Acceptance Criteria
- [ ] [Binary, testable item — max 10]

## Blockers
> Mark as **Blocker** and tag Accountable person from RACI above.
> Common blockers: [1–2 specific items]

## Dropoff
- [Deliverable link 1]
- [Deliverable link 2 if applicable]
> Mark **In Review** when [specific condition].

## Metadata
- Identifier: [PROJECT-PREFIX-Number]
- Assignee: [Name ([X] pts)]
- Labels: Phase-[X], [Topic], Week-[X]
- Depends on: [Task ID or condition]
- Blocks: [Task ID or condition]
- Estimate: [X] points

CONTEXT (fill this in before submitting):
Project: [Project name + EPIC link]
Team + weekly capacities: [Name: X pts/week, Name: Y pts/week]
Phase summary: [2–3 sentences]
Task: [Number, name, owner, points, sprint week]
Deliverable: [One sentence]
Depends on: [Task ID or condition]
Blocks: [Task ID or condition]
RACI: R=[Name], A=[Name], C=[Name], I=[Name]

Do not generate any text outside the task format above. Begin with the # heading.
```

---

## Next Steps

### For the next session
- [ ] Run the new Claude prompt template against a hypothetical new client (not HPL) to validate output is ≤250 words with RACI filled
- [ ] Compare output against `artifacts/Example AI Generated Task.md` — confirm 60%+ word reduction with no operational clarity lost
- [ ] Confirm only `[PROJECT-PREFIX]`, `[DESIGN-LEAD]`, `[DEV-LEAD]` placeholders need changing between engagements

### For the next client engagement
- [ ] When Phase 2 kicks off: brief Dev Lead on Sub-Phase 2C trigger conditions before design starts
- [ ] Add 2C1/2C2/2C3 tasks to Linear at project setup, with "waiting for trigger" status
- [ ] Design Lead to signal "colors and typography locked" in writing (Slack or Figma comment) before any Webflow variables are entered

### Backlog (not time-sensitive)
- [ ] Create a Linear template for Sub-Phase 2C tasks that auto-populates from the BetaEngagement playbook
- [ ] Evaluate whether the Claude prompt template should be stored as a Claude Project prompt (persistent) vs. copy-paste per session
