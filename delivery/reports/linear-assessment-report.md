---
title: "Linear Assessment Report"
created: 2026-03-07
updated: 2026-03-21
tags:
  - delivery/linear
  - type/report
status: active
---

# Linear Project Management Assessment
## Admiral Systems — March 2026

**Assessment Date:** March 8, 2026
**Data Source:** Linear Export (939 issues, 22 projects, 12 teams)
**Period Analyzed:** August 2025 – March 2026
**Prepared for:** Commercial & Delivery Leadership

---

## Executive Summary

**Overall Grade: C+ / Needs Significant Improvement**

Admiral Systems' Linear workspace shows a team that started with good intentions but has outgrown its setup. Client delivery projects (ORG, Cartracker, XCL) are reasonably well-managed, but internal operations and resource planning are breaking down. The data reveals systemic issues in five critical areas:

1. **Overdue Crisis** — 24.8% of all issues are past due
2. **Priority Inflation** — 56% of issues marked Urgent/High
3. **Resource Overload** — Top 3 people have 78 active issues combined
4. **Process Gaps** — Less than half of issues are estimated or in sprints
5. **Shadow Work** — Unlogged tasks make all capacity planning fictional

The commercial team currently has **zero quantitative inputs** to answer "can we take on this new project?" This assessment provides the data foundation and a 4-phase action plan to fix that.

---

## Table of Contents

1. [Overdue Crisis](#1-overdue-crisis-critical)
2. [Priority Inflation](#2-priority-inflation-high)
3. [Resource Overload & Imbalance](#3-resource-overload--imbalance-critical)
4. [Process Gaps](#4-process-gaps)
5. [Project Health Overview](#5-project-health-varies-wildly)
6. [Throughput & Trends](#6-throughput--trends)
7. [Shadow Work / Unlogged Tasks](#7-shadow-work--unlogged-tasks-critical)
8. [Project Setup & Structure Issues](#8-project-setup--structure-issues)
9. [Per-Project Deep Dive](#9-per-project-deep-dive)
10. [Sprint/Cycle Velocity Analysis](#10-sprintcycle-velocity-analysis)
11. [Cycle Time Analysis](#11-cycle-time-analysis)
12. [Estimation Accuracy Analysis](#12-estimation-accuracy-analysis)
13. [The Resource/Capacity Problem](#13-the-resourcecapacity-problem)
14. [Recommendations](#14-recommendations)
15. [Verification Metrics](#15-verification-metrics)

---

## 1. Overdue Crisis (CRITICAL)

**233 of 939 issues (24.8%) are overdue** — past their due date and still open.

| Project | Overdue Issues |
|---|---|
| AST-Internal-Operations | 120 |
| (no project assigned) | 28 |
| [ARCHIVED] HPL-BetaEngagement-RMD | 17 |
| ANI6-Beta-AST | 12 |
| SB-StudioScents | 9 |
| UTV-Beta-P_RMD-2026 | 8 |
| All others | 39 |

### Why This Matters

When nearly **1 in 4 issues** is overdue, due dates lose all meaning. The team stops trusting them, the commercial team can't use them for client timelines, and clients get surprised. This is likely the root cause of the "last-minute updates" problem.

### The Internal Ops Problem

AST-Internal-Operations alone has **120 overdue issues** — more than half of all overdue items. This project is a dumping ground: 182 total issues, only 25% done, 91 still in backlog. Internal work is being deprioritized for client work (understandable for an agency), but the sheer volume creates organizational debt.

### Important Caveat: Recurring Tasks

**101 of the 233 overdue issues (43.3%) are recurring tasks** that were never completed/closed (see Section 8A for full breakdown). Without recurring tasks, the true overdue rate drops from 24.8% to **13.4%** — still too high, but the crisis is partly manufactured by poor recurring task management.

---

## 2. Priority Inflation (HIGH)

**56.1% of all issues are marked Urgent or High priority.** Only 5.1% are Low priority.

| Priority | Count | % of Total | Healthy Target |
|---|---|---|---|
| Urgent | 141 | 15.0% | <5% |
| High | 386 | 41.1% | 20-25% |
| Medium | 190 | 20.2% | 40-50% |
| Low | 48 | 5.1% | 20-30% |
| No priority | 174 | 18.5% | <5% |

### Why This Matters

When everything is urgent, nothing is urgent. If over half the board is Urgent/High, the team has no way to differentiate what actually needs immediate attention vs. what can wait. This directly causes the "always says yes" problem — every task looks critical, so they try to do everything.

### Recommended Priority Definitions

- **Urgent** (<5%): Client SLA breach, production down, revenue at risk
- **High** (20-25%): Current sprint commitments, client-facing deadlines this week
- **Medium** (40-50%): Planned upcoming work, next sprint candidates
- **Low** (20-30%): Nice-to-haves, internal improvements, backlog items

---

## 3. Resource Overload & Imbalance (CRITICAL)

### Active Workload (In Progress + In Review)

| Person | Active Issues | Total Assigned | % of All Issues |
|---|---|---|---|
| daz@ | 36 | 296 | 31.5% |
| elfajri@ | 21 | 96 | 10.2% |
| haykal@ | 21 | 68 | 7.2% |
| prj-website-rev@ (external) | 8 | 16 | 1.7% |
| sean@ | 8 | 113 | 12.0% |
| luthfi@ | 4 | 39 | 4.2% |
| rohan@ | 3 | 14 | 1.5% |
| tiara.almira@ | 3 | 75 | 8.0% |
| shafiq@ | 2 | 18 | 1.9% |
| davis@ | 1 | 126 | 13.4% |

### Key Problems

1. **daz@ has 36 active issues.** No individual can meaningfully make progress on 36 things simultaneously. This person is a bottleneck across the entire organization — 296 total issues assigned, spanning 15 projects and 11 teams.

2. **elfajri@ and haykal@ each have 21 active issues** — also unsustainable. However, haykal's count is inflated by recurring weekly SEO content tasks.

3. **No WIP limits exist.** There's no mechanism to prevent overloading.

4. **132 issues (14%) are unassigned**, including 6 already in active states (In Progress/In Review).

5. **Time in "In Progress" averages 50 days** (median 40 days). Healthy sprints close issues in days, not weeks.

6. **Time in "In Review" averages 59 days.** Work sits in review for nearly 2 months on average — a massive bottleneck.

### The Direct Cause of the Capacity Problem

The commercial team asks "can we take this on?" and gets a yes, but people already have 20+ active items. Nothing new gets done quickly.

---

## 4. Process Gaps

| Process Area | Current | Healthy Target | Gap |
|---|---|---|---|
| Issues with estimates | 48.2% | >90% (client work) | Severe |
| Issues in cycles/sprints | 46.6% | >90% (client work) | Severe |
| Issues with labels | 28.2% (90 unique labels) | >80% (15-20 labels) | Moderate |
| Issues stuck in Triage | 34 (avg 116 days) | 0 (triage in <48hrs) | Severe |
| Sub-task usage | 20.2% | >40% | Moderate |

### Estimation Gap
Less than half of issues are estimated. Without estimates, you cannot calculate team capacity or forecast delivery dates. This is the missing link between "do we have capacity?" and reality.

### Sprint/Cycle Gap
Less than half of issues are assigned to cycles. Without cycle discipline, there's no forcing function to limit WIP or plan capacity per sprint. Work is effectively unbounded.

### Label Chaos
90 unique labels with only 28.2% coverage. Labels mix issue types, project phases, and priorities (e.g., "p1-high" as a label when priority is already a field). The taxonomy needs consolidation to ~15-20 meaningful labels.

### Triage Bottleneck
34 issues stuck in Triage for an average of **116 days** — nearly 4 months. Triage should be a 24-48 hour waypoint, not a parking lot.

---

## 5. Project Health Varies Wildly

### Well-Managed Projects (Client Delivery)

| Project | Total | Done % | Active | Assessment |
|---|---|---|---|---|
| ORG-Gamma-CDPEngineering | 59 | 89% | 0 | Excellent — ready to archive |
| CT-Beta-P_RMD-Q3 | 67 | 82% | 3 | Strong — wrapping up well |
| PLU-Beta-P_SPL | 55 | 82% | 7 | Good — healthy active project |

### Struggling Projects

| Project | Total | Done % | Backlog | Overdue | Assessment |
|---|---|---|---|---|---|
| AST-Internal-Operations | 178 | 25% | 91 | 120 | Out of control |
| [ARCHIVED] HPL-BetaEngagement-RMD | 40 | 0% | 33 | 17 | Abandoned, not cleaned up |
| HPL-BETA-RMD-2026 | 34 | 19% | 24 | 3 | Barely started |
| SPL-Internal-Operations | 35 | 44% | 0 | 4 | Slow triage process |

### Key Insight

Client projects get reasonable attention, but internal and transition projects are neglected. The archived HPL project still having active issues is a red flag for workspace hygiene.

---

## 6. Throughput & Trends

### Issues Created Per Month

```
Aug 2025:  76  ████████
Sep 2025: 119  ████████████
Oct 2025: 193  ████████████████████  <-- spike (new client engagements)
Nov 2025: 129  █████████████
Dec 2025: 125  █████████████
Jan 2026:  75  ████████
Feb 2026: 185  ███████████████████  <-- spike (new client engagements)
Mar 2026:  37  ████ (partial month)
```

### Analysis

- Overall completion rate (48.2% done) vs. creation rate suggests the team is keeping up overall
- Backlog is growing in specific projects (AST-Internal-Ops, HPL)
- The Oct and Feb spikes likely correspond to new client engagement kickoffs
- Total throughput: ~60-70 completed issues per month across the team

---

## 7. Shadow Work / Unlogged Tasks (CRITICAL)

Seniors and the commercial team assign tasks verbally or via Slack/email that never make it into Linear. This is arguably **the most damaging problem** because:

### Impact

1. **It makes all capacity planning fictional.** Even with perfect estimation and sprint planning, unlogged tasks consume real time that isn't accounted for. Someone looks "available" in Linear but is actually buried in off-the-books work.

2. **It creates a quality death spiral.** Team takes on logged client work + unlogged senior requests -> not enough time for either -> quality drops -> team ships something subpar instead of requesting a delay -> client trust erodes.

3. **It prevents honest conversations.** The commercial team can't see the real workload, so they keep saying yes. The delivery team can't point to a concrete "I'm full" signal.

### Data Evidence

The average "In Progress" time of 50 days and daz's 36 active issues almost certainly include work that was originally unlogged and got retroactively created, if at all.

---

## 8. Project Setup & Structure Issues

### 8A. Recurring Tasks Are Massively Inflating Numbers

There are **7 recurring task types** being manually duplicated every week/fortnight:

| Recurring Task | Instances | Assignee | Overdue | Done | Done % |
|---|---|---|---|---|---|
| Weekly content production (SEO) | 23 | haykal | 18 | 4 | 17% |
| Weekly Issue Management | 21 | daz | 18 | 2 | 10% |
| Set Sprint Setting for the week | 14 | daz | 13 | 0 | 0% |
| Weekly Closing | 14 | daz | 13 | 0 | 0% |
| Run QA checks across the org | 14 | daz | 13 | 0 | 0% |
| Check Active Projects Pipeline Status | 14 | daz | 13 | 0 | 0% |
| Check Cashflow Risks | 14 | daz | 13 | 0 | 0% |
| Fortnightly Client Sync Meeting | 9 | daz | 0 | 8 | 89% |
| **TOTAL** | **123** | | **101** | **14** | **11%** |

**Critical impact:**
- 123 recurring tasks = **14.1% of all issues** — not real project work
- 101 of 233 overdue issues (**43.3%**) are recurring tasks — nearly half the overdue crisis is manufactured
- Without recurring tasks: overdue rate drops from 24.8% to **13.4%**
- daz's adjusted numbers: total issues 257 -> 157, active 36 -> ~17
- haykal's adjusted numbers: most "In Progress" items are weekly SEO tasks

**The pattern:** Tasks are created weekly with a due date, put in Backlog or left In Progress, and never completed. daz's 5 weekly ops tasks have **0% completion rate** going back to Dec 2025 — either the work is done but tickets aren't closed, or the work isn't being done at all.

**Fix:** Use Linear's built-in recurring issue feature, or track as a weekly checklist within a single ops task. The Fortnightly Client Sync (Cartracker, 89% completion) is the only recurring task managed properly.

### 8B. Project Structure Inconsistencies

| Issue | Count | Examples |
|---|---|---|
| Projects with no milestones | 7 | CT-Beta, WLX-Retainer, SPL-Internal-Ops |
| Projects with no target end date | 8 | Multiple active client projects |
| Projects with no summary | 5 | AST-Internal-Ops (178 issues!) |
| Projects past target date (still "In Progress") | 3 | XCL, SPL-Ops, ORG |
| Projects with wrong target dates | 2 | UTV (says 2024), XCL (says Feb 2025) |
| Duplicated projects in export | 6 | Team-level vs workspace-level duplication |

### 8C. Calendar Invite Noise

~20+ calendar invitations from Google Calendar were auto-imported into Linear as issues then canceled (DLVRY-196 through DLVRY-216). This is workspace noise from a misconfigured email-to-Linear integration that should be disabled.

### 8D. Archived Project with Active Work

[ARCHIVED] HPL-BetaEngagement-RMD has 40 issues, 3 in progress, 0 completed. HPL-BETA-RMD-2026 was created as the replacement but the old project was never properly closed — issues weren't migrated, just left behind.

### 8E. Stale Project Health Reporting

| Health Status | Projects | Notes |
|---|---|---|
| No updates | 7 | Including active ones (SB-StudioScents, AST-Account Care) |
| Off track | 1 (RCG) | 3-4 more should be marked off track |
| Updates >3 months old | 4+ | SPL-Ops, AST-Internal-Ops (both Aug 2025) |

### 8F. Naming Convention Inconsistencies

Projects use at least 4 different naming schemes:
- `{CLIENT}-{Greek}-{Team}` — RCG-Epsilon-P_SPL, ORG-Gamma-CDPEngineering
- `{CLIENT}-Beta-{Suffix}` — ANI6-Beta-AST, CT-Beta-P_RMD-Q3
- `AST-Internal-{Dept}` — AST-Internal-Operations, AST-Internal-Commercial
- `{CODE}-{Type}` — WLX-Retainer-MarTechSupport

No documentation exists for what Greek letters signify (likely engagement phases: Alpha/Beta/Gamma/Epsilon).

Issue IDs span multiple prefixes within one project (e.g., CT-Beta has PCT-*, DLVRY-*, and AST-* issues), indicating cross-team issue creation.

---

## 9. Per-Project Deep Dive

### Active Client Projects

#### ANI6-Beta-AST (Animoca Brands) — 82 issues, 56% done
- **Strengths:** Well-structured with milestones, cycles, and estimates (65% coverage). Good team distribution across sean (design), davis (dev), prj-website-rev (client), elfajri (dev), tiara (design). Scope changes handled properly (12 canceled).
- **Concerns:** 9 still active including client-side items stuck in review. Target end date says May 2025 — clearly wrong.
- **Risk Level:** Medium

#### XCL-Beta-WebflowMigration-Q3 — 79 issues, 65% done
- **Strengths:** Good sprint discipline (most issues in cycles). Clean design -> dev -> QA handoff pattern visible.
- **Concerns:** 8 active items, sean carrying most of the load. Target date Feb 2025 is a data entry error.
- **Risk Level:** Medium

#### CT-Beta-P_RMD-Q3 (Cartracker) — 67 issues, 82% done
- **Strengths:** Best-managed project overall. High completion rate, good cycle usage. Clear milestone progression.
- **Concerns:** rohan's 3 active issues include one overdue since Jan 2026.
- **Risk Level:** Low

#### ORG-Gamma-CDPEngineering — 59 issues, 89% done
- **Strengths:** Excellent project management. davis drove this to near-completion. Good use of parent/child hierarchy.
- **Action:** Should be marked Completed and archived (53/59 completed, 0 active).
- **Risk Level:** None (complete)

#### PLU-Beta-P_SPL (LevelUp) — 55 issues, 82% done
- **Strengths:** High completion rate, milestones defined.
- **Concerns:** Marked Completed but still has 7 active issues in review (elfajri owns most).
- **Action:** Should not be marked Completed until review items are closed.
- **Risk Level:** Low

#### RCG-Epsilon-P_SPL (Red Centre Global) — 54 issues, 67% done
- **Status:** Only project explicitly marked "Off track" — data confirms it.
- **Concerns:** 3 overdue milestones (Lead Magnet Creation 1, 2, 3). 2 Blocker issues (new enquiry flow + email notification linking).
- **Strengths:** Recent UAT and bug fix activity shows the team is pushing to deliver.
- **Risk Level:** High

#### HPL-BETA-RMD-2026 (Hop Lun) — 34 issues, 19% done
- **Status:** Early-stage (started Jan 2026), currently in Phase 2 (Wireframes).
- **Strengths:** Well-structured with numbered tasks and clear phases.
- **Concerns:** Most backlog is unassigned. Bulk of dev work (Phase 3-4) has no assignee. Lots of 8-point issues with no cycle.
- **Risk Level:** Medium (resource allocation needed)

#### SB-StudioScents — 21 issues, 50% done
- **Owner:** luthfi (sole developer) — clean ownership.
- **Concern:** Marked "Completed" but has 5 active issues still in progress.
- **Risk Level:** Low

#### SPI-Epsilon-WebApp (Spireworks) — 5 issues, 0% done
- **Status:** All 5 issues stuck in "In Review." elfajri is sole assignee. Legacy project (started 2022). No health updates.
- **Risk Level:** Low (legacy maintenance)

### Internal Projects

#### AST-Internal-Operations — 178 issues, 25% done, 120 overdue
**The most problematic project.** A catch-all for weekly ops tasks, learning initiatives, tool setup, and everything else. ~60% of issues are pre-created recurring weekly tasks that inflate the count. daz owns 126 of 178 issues. No milestones, no target dates, no summary.

**Recommendation:** Split into distinct projects (Weekly Ops Cadence, Tool/Platform Setup, Learning & Growth) and archive the recurring task backlog.

#### SPL-Internal-Operations — 35 issues, 44% done
Partnership operations between Admiral and SparkLabs. daz owns 32/35 issues. Mix of partnership management, CRM setup, and lead gen strategy. 8 issues in review since Aug 2025.

#### Internal-AI-Generation-Workflow — 14 issues, 0% done
All 14 assigned to haykal. 10 in "In Review" with no reviewer assigned. 3 overdue milestones. Who is reviewing this work?

#### Internal-Learning and Development — 18 issues
Onboarding tasks for team members. Mostly completed — good onboarding structure.

---

## 10. Sprint/Cycle Velocity Analysis

**411 issues are assigned to sprints across 26 cycles (Aug 2025 - Mar 2026).**

### Historical Sprint Performance

Cycles 1-18 show strong completion rates — most are 95-100%. The team generally finishes what it commits to in properly-sized sprints.

### Recent Sprint Collapse

| Cycle | Dates | Planned | Done | Done % | Carryover | Pts Planned | Pts Done | Pts % |
|---|---|---|---|---|---|---|---|---|
| 19 | Jan 11 - Mar 8 | 18 | 8 | 44% | 10 | 26 | 8 | 31% |
| 25 | Feb 22 - Mar 8 | 22 | 14 | 64% | 5 | 29 | 12 | 41% |
| **26** | **Mar 1 - Mar 8** | **70** | **14** | **20%** | **53** | **104** | **7** | **7%** |

### Cycle 26 Analysis (Current Sprint)

**70 issues planned, only 14 done (20%), 53 carrying over, only 7 of 104 points completed (7%).**

This sprint has **70 issues** — more than any previous sprint by 2-3x (compare to cycle 6, the previous largest at 41). Issues are being dumped into the current sprint without capacity planning.

### Key Insight for the Commercial Team

The team **CAN deliver** when sprints are sized properly (10-25 issues). But when sprints are overloaded, completion collapses.

**Realistic sprint capacity: ~15-20 issues / 30-50 points per sprint across the whole team.**

---

## 11. Cycle Time Analysis

### Overall Timing (completed issues only, n=447)

| Metric | Average | Median | P75 | P90 |
|---|---|---|---|---|
| **Lead Time** (Created -> Done) | 24.9 days | 13.9 days | 32.0 days | 57.9 days |
| **Queue Time** (Created -> Started) | 10.2 days | 1.2 days | 6.1 days | 26.4 days |
| **Cycle Time** (Started -> Done) | 14.4 days | 8.9 days | 18.9 days | 37.1 days |

**Interpretation:** Half of all issues take 2+ weeks from creation to completion. Once started, work typically takes 9 days to finish. The main bottleneck isn't doing the work — it's the queue time (P90 is 26 days, meaning 10% of issues wait nearly a month before anyone starts).

### Lead Time Distribution

```
< 1 day     |  25 (  5.6%)  ##
1-3 days    |  36 (  8.1%)  ####
3-7 days    |  71 ( 15.9%)  ########
1-2 weeks   | 100 ( 22.4%)  ###########
2-4 weeks   |  96 ( 21.5%)  ###########
1-2 months  |  75 ( 16.8%)  ########
2-3 months  |  20 (  4.5%)  ##
3+ months   |  24 (  5.4%)  ##
```

~10% of issues take 2+ months — these are the ones that cause client surprise.

### Lead Time by Project (median, completed only)

| Project | Median Lead Time | Assessment |
|---|---|---|
| Internal-Learning & Dev | 0.8 days | Quick onboarding tasks |
| HPL-BETA-RMD-2026 | 3.5 days | New project, early tasks |
| RCG-Epsilon-P_SPL | 5.0 days | Bug fixes/UAT — fast turnaround |
| SB-StudioScents | 6.5 days | Small project, single owner |
| XCL-Beta-WebflowMigration | 11.3 days | Decent for design+dev |
| ORG-Gamma-CDPEngineering | 12.1 days | Reasonable for data engineering |
| ANI6-Beta-AST | 14.9 days | Large website project |
| SPL-Internal-Operations | 18.7 days | Internal — deprioritized |
| CT-Beta-P_RMD-Q3 | 22.0 days | 3 weeks — getting slow |
| PLU-Beta-P_SPL | 26.0 days | Nearly a month per issue |

### Lead Time by Person (median, completed only)

| Person | Completed | Median Lead Time | Assessment |
|---|---|---|---|
| shafiq | 5 | 1.3 days | Small sample, quick tasks |
| luthfi | 25 | 3.6 days | Fast executor |
| tiara.almira | 48 | 7.9 days | Consistent, reasonable |
| haykal | 21 | 12.8 days | ~2 weeks |
| sean | 69 | 12.9 days | ~2 weeks, solid for design |
| daz | 81 | 16.1 days | Over 2 weeks — overloaded |
| davis | 103 | 19.0 days | ~3 weeks — high volume |
| elfajri | 40 | 32.2 days | Over a month — too many projects |
| ghifari | 22 | 42.0 days | 6 weeks — before departure? |

**Key finding:** elfajri's 32-day median lead time correlates with being spread across 5 projects simultaneously. davis has high volume (103 completed) but 19-day median — acceptable given complex data/dev work.

---

## 12. Estimation Accuracy Analysis

### Do Estimates Predict Actual Time?

| Estimate | Count | Median Actual | Avg Actual | Days/Point |
|---|---|---|---|---|
| 1 point | 45 | 7.2 days | 8.6 days | 8.6 |
| 2 points | 35 | 10.0 days | 12.8 days | 6.4 |
| 3 points | 43 | 11.0 days | 15.0 days | 5.0 |
| 5 points | 26 | 21.1 days | 22.1 days | 4.4 |
| 8 points | 12 | 40.1 days | 34.2 days | 4.3 |

**Pearson correlation: 0.463 (moderate)** — estimates have some predictive value but are far from reliable.

### The Ratio Problem

A 1-point issue takes 8.6 days on average, while an 8-point issue takes 34.2 days. If perfectly calibrated, 8-point should take 8x a 1-point — instead it takes ~4x. Most likely: 1-point issues sit in queue/review just as long as larger issues, inflating their actual time disproportionately.

### Practical Timeline Guide for the Commercial Team

| Estimate | Expected Duration |
|---|---|
| 1-2 points | ~1-2 weeks |
| 3 points | ~2 weeks |
| 5 points | ~3 weeks |
| 8 points | ~5-6 weeks |

### Estimation Accuracy by Person

| Person | n | Avg Estimate | Avg Actual | Days/Point | Assessment |
|---|---|---|---|---|---|
| davis | 50 | 3.1 pt | 12.4 days | 4.0 | Most consistent estimator |
| tiara.almira | 20 | 2.8 pt | 11.2 days | 4.0 | Equally consistent |
| sean | 37 | 2.6 pt | 12.1 days | 4.7 | Slightly under-estimates |
| daz | 9 | 4.2 pt | 28.0 days | 6.6 | Significantly under-estimates |
| elfajri | 20 | 3.3 pt | 22.7 days | 6.9 | Under-estimates (too much WIP) |
| luthfi | 11 | 1.9 pt | 16.6 days | 8.7 | Under-estimates substantially |
| ghifari | 5 | 2.8 pt | 31.3 days | 11.2 | Worst ratio (small sample) |

**Calibration baseline:** davis and tiara.almira at 4.0 days/point are the most reliable estimators. Use this ratio for capacity planning.

### Estimation Coverage

| Status | Estimated % | Target |
|---|---|---|
| In Progress | 69% | >95% |
| Backlog | 72% | >90% |
| Done (historical) | 43% | n/a |

The trend is improving — recent issues are more likely to have estimates.

---

## 13. The Resource/Capacity Problem

### Team Throughput (completed issues/month, last 3 months)

| Person | Dec | Jan | Feb | Avg/mo | Active Now | Projects |
|---|---|---|---|---|---|---|
| davis | 11 | 24 | 15 | **17** | 1 | 11 |
| elfajri | 24 | 8 | 7 | **13** | 21 | 8 |
| sean | 9 | 3 | 11 | **8** | 8 | 9 |
| luthfi | 5 | 1 | 15 | **7** | 4 | 4 |
| daz | 16 | 1 | 3 | **7** | 36 | 15 |
| tiara.almira | 6 | 5 | 5 | **5** | 3 | 9 |
| haykal | 5 | 3 | 3 | **4** | 21 | 5 |
| shafiq | 0 | 0 | 4 | **1** | 2 | 4 |

**Total agency throughput: ~60-70 completed issues per month.** That's the real capacity ceiling. Any new project intake must fit within this envelope.

### The Three Root Causes

**1. daz is a catastrophic bottleneck**
- 296 total issues (31.5% of all work), 36 active, 15 projects, 11 teams
- Throughput collapsed: 16 in Dec -> 1 in Jan -> 3 in Feb
- 143 overdue issues — more overdue items than any other person has total items
- This isn't a prioritization problem — it's structural. One person cannot own 15 projects.

**2. Multi-project context-switching is killing velocity**
- elfajri: 21 active across 5 projects
- haykal: 21 active across 2 projects
- daz: 36 active across 7 projects
- Research shows 3+ simultaneous projects drops productivity by 40-60%. The data confirms it.

**3. No capacity model exists**
- Only 48% of issues have estimates -> can't calculate remaining effort
- Only 47% of issues are in cycles -> can't forecast sprint-level delivery
- Work types barely labeled (61/939) -> can't assess capability-specific availability
- The commercial team has **zero quantitative inputs** to answer "can we take this project?"

---

## 14. Recommendations

### Phase 1: Emergency Triage (Week 1)

| # | Action | Owner | Target |
|---|---|---|---|
| R1 | Triage daz's 36 active issues: delegate, defer, or cancel each one | daz + leadership | Max 7 active issues, 2-3 projects |
| R2 | Triage all 233 overdue issues: update date, remove date, or cancel | All assignees | <30 overdue remaining |
| R3 | Close [ARCHIVED] HPL project: bulk-cancel or migrate 3 active issues | daz | 0 open issues on archived project |

### Phase 2: Build the Capacity Model (Weeks 2-3)

| # | Action | Owner | Target |
|---|---|---|---|
| R4 | Establish per-person throughput baselines using historical data | Delivery lead | Published capacity per person |
| R5 | Make estimation mandatory for all client work | All | >90% estimation coverage |
| R6 | Add work type custom field (Design/Dev/Data/Strategy) to all issues | All | >90% coverage on client work |
| R7 | Implement "No Ticket, No Work" policy with Slack->Linear shortcut | Leadership | 100% of work logged |

### Phase 3: Process Discipline (Weeks 3-4)

| # | Action | Owner | Target |
|---|---|---|---|
| R8 | Sprint discipline: hard WIP limits, capacity-based sprint loading | Delivery lead | 15-20 issues per sprint max |
| R9 | Create Commercial Capacity Dashboard (see companion document) | Delivery lead | Weekly updates for commercial team |
| R10 | Re-triage all priorities using defined thresholds | All | <5% Urgent, 20-25% High |

### Phase 4: Workspace Hygiene (Ongoing)

| # | Action | Owner | Target |
|---|---|---|---|
| R11 | Consolidate 90 labels to ~15-20 | Delivery lead | Clean label taxonomy |
| R11 | Archive completed projects (close issues first) | All PMs | 0 "completed" projects with active issues |
| R11 | Clear 34 Triage items | All | <48hr triage cycle |
| R11 | Weekly backlog grooming | All teams | 0 issues >90 days in backlog without review |

---

## 15. Verification Metrics

Track weekly after implementing changes:

| Metric | Current | 30-Day Target | 90-Day Target |
|---|---|---|---|
| Overdue issues | 233 (24.8%) | <100 (<11%) | <30 (<5%) |
| Avg active issues per person | 12.2 | <9 | <7 |
| Max active issues (any person) | 36 (daz) | <15 | <10 |
| Estimation coverage (client work) | 48% | >70% | >90% |
| Work type field coverage | 6.5% | >50% | >90% |
| Issues in cycles | 46.6% | >70% | >90% |
| Avg time in "In Review" | 59 days | <20 days | <5 days |
| Avg time in "In Progress" | 50 days | <25 days | <14 days |
| Sprint completion rate | 20% (cycle 26) | >60% | >80% |

### Monthly Capacity Review

Run a monthly capacity review with the commercial team using the Capacity Dashboard. The question to answer each month:

> **"Given our throughput baselines and current commitments, which capabilities have room for new projects, and which are already over capacity?"**

---

## Companion Documents

- **Capacity Dashboard Snapshot** — `Capacity-Dashboard-Snapshot.md`
- **Phased Action Plan & Checklists** — `Action-Plan-Checklists.md`
- **Overdue Issues Triage Worksheet** — `Overdue-Issues-Triage.csv`
- **daz Workload Triage Worksheet** — `Daz-Active-Issues-Triage.csv`
- **Weekly Health Metrics Tracker** — `Weekly-Health-Metrics-Tracker.md`

---

*Assessment generated from Linear data export of March 7, 2026. All statistics are based on 939 issues across 22 projects and 12 teams.*
