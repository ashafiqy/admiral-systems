---
title: "Linear Views Recommendations"
created: 2026-03-10
updated: 2026-03-21
tags:
  - delivery/linear
  - type/report
status: active
---

# Linear Views — Recommendations

**Created:** March 16, 2026
**Purpose:** Custom views to create manually in Linear to surface ongoing workspace health issues.

All views should be saved at **workspace level** so leadership can access them. Favorite the top 4 operational views for quick sidebar access.

---

## Problems → Views Mapping

| Problem             | Current Metric               | Target             | View                 |
| ------------------- | ---------------------------- | ------------------ | -------------------- |
| Resource overload   | daz@ at 48 active issues     | ≤12                | WIP per Person       |
| Stuck in Triage     | 34 issues, avg 116 days      | <48hr residence    | Triage Queue         |
| Overdue issues      | 233 overdue (24.8%)          | <5%                | Overdue Issues       |
| Stuck in Review     | avg 59 days                  | <5 days            | In Review Bottleneck |
| Priority inflation  | 56% Urgent+High              | <40%               | Priority Health      |
| No priority set     | 176 issues (17%)             | 0                  | No Priority Set      |
| Unestimated         | 52% of issues                | >90% estimated     | Missing Estimates    |
| Outside sprints     | 53% of issues                | >90% in cycles     | Floating Issues      |
| Per-company clarity | 3 companies in one workspace | —                  | Company Overviews ×3 |
| Capacity visibility | —                            | See who is at 80%+ | Capacity View        |

---

## Recommended Creation Order

Create in this order — highest operational impact first:

1. WIP per Person
2. Triage Queue
3. Overdue Issues
4. In Review Bottleneck
5. Priority Health
6. No Priority Set
7. Missing Estimates
8. Floating Issues
9. Company Overviews ×3
10. Capacity View (Leadership)

---

## View Configurations

### 1. WIP per Person ✅

**Purpose:** Spot overloaded assignees. Target: daz@ ≤12 active, team average ≤9.

| Setting            | Value                             |
| ------------------ | --------------------------------- |
| Layout             | Board                             |
| Filter             | `Status` is In Progress           |
| Group by           | Assignee                          |
| Sub-group by       | Priority                          |
| Sort within groups | Priority ascending (Urgent first) |
| Share              | Workspace-level                   |

> **Why Priority (not Project) as sub-group:** This view answers "how heavy and how urgent is this person's load?" Breaking by Project would dilute that signal. Sort by Priority within each Assignee column so the most critical tasks surface at the top.

---

### 2. Triage Queue ✅

**Purpose:** Catch issues stuck in Triage — target <48 hour residence time.

| Setting  | Value                                 |
| -------- | ------------------------------------- |
| Layout   | List                                  |
| Filter   | `Status` is Triage                    |
| Group by | Project                               |
| Sort     | Created date ascending (oldest first) |
| Share    | Workspace-level                       |

> **Why Project as group:** Triage issues need to be routed to the right project owner. Grouping by Project makes it immediately clear which PM is responsible for clearing each backlog.

---

### 3. Overdue Issues ✅

**Purpose:** Daily check — anything past due date that isn't done.

| Setting      | Value                                                       |
| ------------ | ----------------------------------------------------------- |
| Layout       | List                                                        |
| Filter       | `Due date` before today AND `Status` is not Done, Cancelled |
| Group by     | Assignee                                                    |
| Sub-group by | Project                                                     |
| Sort         | Priority ascending (Urgent first) within groups             |
| Share        | Workspace-level                                             |

> **Why Project (not Priority) as sub-group:** The due date already conveys urgency — oldest overdue is most critical. What's missing is _which project_ the issue belongs to, so a PM can immediately identify and act on their own project's overdue items. Sort by Priority within each group so the most critical overdue issues surface first.

---

### 4. In Review Bottleneck ✅

**Purpose:** Surface issues stuck in review (current avg: 59 days, target: <5 days).

| Setting      | Value                                                 |
| ------------ | ----------------------------------------------------- |
| Layout       | List                                                  |
| Filter       | `Status` is In Review                                 |
| Group by     | Project                                               |
| Sub-group by | Assignee                                              |
| Sort         | Updated date ascending (least recently touched first) |
| Share        | Workspace-level                                       |

> **Why Project → Assignee:** You need to see which project has the biggest review backlog, then drill down to who owns the stuck issues within that project. This lets a project lead chase their own reviewers without noise from other projects.

---

### 5. P0 & P1 Health Check ✅

**Purpose:** Monitor Urgent+High ratio — target below 40%.

| Setting      | Value                                                            |
| ------------ | ---------------------------------------------------------------- |
| Layout       | Board                                                            |
| Filter       | `Priority` is Urgent OR High AND `Status` is not Done, Cancelled |
| Group by     | Priority                                                         |
| Sub-group by | Assignee                                                         |
| Share        | Workspace-level                                                  |

> **Why Priority (not Project) as primary group:** This view exists to show workspace-wide priority distribution. Adding Project would fragment the columns and hide the big picture. The ratio of Urgent vs. High columns is the signal leadership is watching.

---

### 6. No Priority Set ✅

**Purpose:** Issues with no Priority field set — currently 176 (17%).

| Setting  | Value                                                         |
| -------- | ------------------------------------------------------------- |
| Layout   | List                                                          |
| Filter   | `Priority` is No priority AND `Status` is not Done, Cancelled |
| Group by | Project                                                       |
| Share    | Workspace-level                                               |

> **Why Project as group:** Priority needs to be set by the PM or lead on a project-by-project basis. Grouping by Project shows which projects have the most unclassified issues and makes it easy to hand off the cleanup task to the right owner.

---

### 7. Missing Estimates ✅

**Purpose:** Enforce estimation coverage target (currently 48%, target >90%).

| Setting      | Value                                                   |
| ------------ | ------------------------------------------------------- |
| Layout       | List                                                    |
| Filter       | `Estimate` is empty AND `Status` is not Done, Cancelled |
| Group by     | Project                                                 |
| Sub-group by | Status                                                  |
| Share        | Workspace-level                                         |

> **Why Project as group:** Estimation is a project-level responsibility. Grouping by Project shows which projects are most under-estimated and lets the PM batch-estimate their own issues in one focused session.

---

### 8. Floating Issues (No Cycle) ✅

**Purpose:** Issues not assigned to any sprint — currently 53%.

| Setting            | Value                                     |
| ------------------ | ----------------------------------------- |
| Layout             | List                                      |
| Filter             | `Cycle` is empty AND `Status` is not Done |
| Group by           | Assignee                                  |
| Sub-group by       | Project                                   |
| Sort within groups | Priority ascending (Urgent first)         |
| Share              | Workspace-level                           |

> **Why Project (not Priority) as sub-group:** When assigning floating issues to a sprint, the person needs to know which project each issue belongs to — that determines which team's cycle to put it in. Priority alone doesn't help with routing. Sort by Priority within groups so the most urgent unassigned issues are visible at the top of each project bucket.

---

### 9a–9c. Company Overviews (×3)

**Purpose:** Per-company status board for leadership. Create one view per company.

| Setting      | AdmiralSystems                                                 | RMD                                                        | Sprklabs                                                        |
| ------------ | -------------------------------------------------------------- | ---------------------------------------------------------- | --------------------------------------------------------------- |
| Layout       | Board                                                          | Board                                                      | Board                                                           |
| Filter       | `Team` is Admiral-Projects AND `Status` is not Done, Cancelled | `Team` is RMD-Projects AND `Status` is not Done, Cancelled | `Team` is Sprklabs-Projects AND `Status` is not Done, Cancelled |
| Group by     | Project                                                        | Project                                                    | Project                                                         |
| Sub-group by | Status                                                         | Status                                                     | Status                                                          |
| Share        | Workspace-level                                                | Workspace-level                                            | Workspace-level                                                 |

> **Why the Done filter was added:** Without `Status is not Done, Cancelled`, completed projects (e.g., SB-StudioScents, UTV-Beta-P_RMD-2026, PLU/TM-Beta-P_SPL) and all their closed issues would appear on the board, cluttering the active project view that leadership needs.

---

### 10. Capacity View (Leadership)

**Purpose:** Show who is at or near 80% capacity.

**Capacity rules:**

- 1 Linear point = 2 hours
- 40hr work week = **20 points** per person
- 80% threshold = **16 points**
- Issues with no estimate = counted as **1 point**

#### Option A — Cycle Capacity (Goal State, Recommended)

Linear Cycles natively track points assigned vs. capacity per member. This is the proper solution.

Setup steps:

1. Go to the active Cycle for each team
2. Open Cycle settings → set capacity per member to **20 points**
3. Linear will display `X / 20 pts` per person in the Cycle view
4. Anyone above **16 points** is at ≥80% capacity

> Use sprint review sessions to make Cycle capacity tracking the team norm.

#### Option B — Proxy View (Use Now, Bridge Until Cycles Are Adopted)

| Setting            | Value                                                       |
| ------------------ | ----------------------------------------------------------- |
| Layout             | List                                                        |
| Filter             | `Status` is not Done, Cancelled AND `Assignee` is not empty |
| Group by           | Assignee                                                    |
| Sub-group by       | Priority                                                    |
| Display            | Show Estimate column                                        |
| Sort within groups | Priority ascending (Urgent first)                           |
| Share              | Workspace-level (or Leadership team)                        |

> **Why Priority (not Project) as sub-group:** The capacity view answers "is this person at 80%?" — you need the total load per person and the urgency breakdown. Breaking by Project would show per-project load which is a different (less useful) question for capacity management.

> Leadership reads this view by scanning each Assignee group. Sum the estimates (blanks = 1pt each). If a person's total ≥ 16pts, they are at capacity. Note: Linear does not show a running total per assignee group — this requires a manual count unless using Cycles (Option A).

**Important:** For capacity numbers to be reliable, all active issues must have estimates set. "No estimate = 1pt" should be a team norm enforced during sprint planning, not just a view assumption.

---

## Slack Subscriptions (Optional)

Consider subscribing these two views to a Slack channel for daily async visibility:

- **WIP per Person** — flags overload before it becomes a blocker
- **Overdue Issues** — daily accountability without a standup
