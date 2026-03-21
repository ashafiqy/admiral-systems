---
title: "Prompt: Build Master Google Sheet Template (Step 3b)"
created: 2026-03-15
updated: 2026-03-21
tags:
  - operations/playbook
  - delivery/linear
status: active
---

# Issue Creation Prompt — Step 3b: Build Master Google Sheet Template

> **How to use:** Paste the prompt below into your `create-issue-agent`. The agent will run a duplicate check against the existing issues in `AST-Internal-BetaWorkflow` before creating — if it flags a conflict with AST-328, see the note at the bottom.

---

## Prompt

Create a new issue in `AST-Internal-BetaWorkflow` under the milestone **Phase 3: Claude AI Prompts & Automation**.

**Title:** Build Step 3b Master Google Sheet Template

**Task Overview:** Design and build the master Google Sheet template that captures all per-page data from the approved sitemap, serving as the single handoff artefact between Step 3 (sitemap sign-off) and Step 3c (Linear project creation via Claude).

**RACI:**
- R — Responsible: Shafiq
- A — Accountable: Daz
- C — Consulted: Davis
- I — Informed: Val, Sean, Rohan

**The Sheet must have the following columns per page row:**
1. Finalized page slug
2. Page type — Static / CMS Template Page / Folder
3. CMS items (for CMS pages — referenced from Step 2 audit)
4. CMS fields (required fields per collection)
5. Progress checker (are/should Webflow build tasks be done for this page?)
6. Creative direction (tone, imagery, layout intent per page)
7. SEO title + meta description
8. JSON-LD / schema types and value mappings (where needed for AEO)
9. Claude prompt template column — a base prompt per page for generating Linear issues in Step 3c

**Acceptance Criteria:**
- [ ] Sheet template created with all 9 columns, correctly labelled with instructions per column
- [ ] At least one example row completed to demonstrate the expected format
- [ ] CMS items column references the Step 2 audit output format
- [ ] Claude prompt template column includes enough context to generate a Linear issue (title, description, AC, estimate, assignee, due date)
- [ ] Template is stored in Google Drive and linked from the AST-Internal-BetaWorkflow project document

**Assignee:** Shafiq · **Milestone:** Phase 3: Claude AI Prompts & Automation · **Priority:** p3-low · **Estimate:** 5 pts · **Due:** 2026-03-30

---

## Duplicate Conflict Note

The agent may flag this against **AST-328** (Build Step 3b Claude Agent and Create Master Google Sheet Template). If it does, confirm this distinction:

- **AST-328** — builds the Claude agent that *populates* the Sheet automatically from sitemap data
- **This issue** — designs the *template structure* itself (columns, labels, example row, instructions)

They are separate deliverables. AST-328 cannot be built until the template structure (this issue) is agreed and locked. Keep them as separate issues.
