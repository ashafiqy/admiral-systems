---
title: "Beta Engagement Template"
created: 2026-02-18
updated: 2026-03-21
tags:
  - client/hop-lun
  - type/template
status: active
---

\# BETA ENGAGEMENT PLAYBOOK



\## Admiral Systems Website Development Framework



\### Engagement Value: $30K+ | Target Margin: 50-60% | Duration: 8-10 weeks



---



\## ENGAGEMENT OVERVIEW



Beta Engagement Definition: Website development and design system creation using Webflow as our primary platform. This engagement model focuses on creating high-performance, scalable digital experiences with enterprise-grade design systems.



Typical Client Profile:



\- Mid-market to enterprise companies  

\- Need for marketing website or platform  

\- Seeking Webflow expertise (we're Asia's first Enterprise partner)  

\- Budget: $25,000 \\- $75,000  

\- Timeline: 8-10 weeks



---



\## PHASE 1: PROJECT INITIATION (Week 0\\)



\### Duration: 2-3 days



\### Margin Impact: Critical for protecting 50-60% target



\#### 1.1 Linear Project Setup (ADM-001)



When: Within 2 hours of contract signing Who:



\- R: Project Manager (Sarah)  

\- A: Engagement Lead (Sean \\- Design Lead)  

\- C: Client Sponsor  

\- I: Team Members



Process:



```

1\. Access Linear.app

2\. Select "Beta Engagement Template"

3\. Configure:

&nbsp;  - Project prefix: \[CLIENT]-BETA

&nbsp;  - Custom fields: ICE scoring enabled

&nbsp;  - RACI matrix fields active

&nbsp;  - Client view: Read-only dashboard

4\. Add team (typically 4-6 members):

&nbsp;  - Design Lead (Sean)

&nbsp;  - 2x Webflow Developers

&nbsp;  - UX Designer

&nbsp;  - QA Specialist

5\. Set milestones:

&nbsp;  - Design System Complete (Week 3)

&nbsp;  - Development Sprint 1 (Week 5)

&nbsp;  - UAT \& Launch (Week 8)

```



Success Metrics:



\- Project configured within 2 hours  

\- All team members have access  

\- Client dashboard active



\#### 1.2 Tracking Time Configuration (ADM-002)



When: Same day as contract signing Who:



\- R: Finance Admin  

\- A: Project Manager  

\- C: COO (Daz)  

\- I: Team Members



Process:



```

1\. Create in Tracking Time:

&nbsp;  ClientName > Beta-Web > Sprint-01

2\. Set billing rates:

&nbsp;  - Sean (Design Lead): $350/hour

&nbsp;  - Senior Developer (SG): $250/hour

&nbsp;  - Developer (ID): $180/hour

&nbsp;  - Designer (ID): $200/hour

&nbsp;  - QA Specialist: $150/hour

3\. Configure 15-minute minimum billing

4\. Enable Linear sync (every 4 hours)

```



Budget Allocation Example ($50K project):



\- Design Phase: $15K (30%)  

\- Development: $25K (50%)  

\- QA \& Launch: $5K (10%)  

\- Project Management: $5K (10%)



---



\## PHASE 2: DESIGN SYSTEM (Weeks 1-3)



\### Target Hours: 120-150 hours



\### Margin Protection: Maintain 55% minimum



\#### 2.1 Figma Design System Creation (BET-001)



When: Week 1-3 Who:



\- R: Design Lead (Sean)  

\- A: Creative Director  

\- C: Client Brand Team  

\- I: Dev Team



Week 1 \\- Discovery \& Audit:



```

Day 1-2: Brand Asset Audit

\- Collect existing brand guidelines

\- Review current website/materials

\- Stakeholder interviews (ICE Score: 8.5)

\- Document in Linear with findings



Day 3-5: Figma Setup

\- Create team workspace

\- Set up file structure:

&nbsp; /01\_Discovery

&nbsp; /02\_Components

&nbsp; /03\_Templates

&nbsp; /04\_Prototypes

\- Import brand assets

```



Week 2 \\- Component Development:



```

Monday: Typography System

\- Define type scale (8-10 sizes)

\- Set line heights, weights

\- Create text styles in Figma

\- Document usage rules



Tuesday-Wednesday: Colour System

\- Primary, secondary, tertiary palettes

\- Semantic colours (success, warning, error)

\- Accessibility check (WCAG AA minimum)

\- Create colour styles



Thursday-Friday: Core Components

\- Buttons (5-6 variants)

\- Forms (all input types)

\- Cards (3-4 layouts)

\- Navigation patterns

```



Week 3 \\- Templates \& Documentation:



```

Monday-Tuesday: Page Templates

\- Homepage template

\- Landing page template

\- Content page template

\- Contact page template



Wednesday-Thursday: Prototyping

\- Link all screens

\- Add micro-interactions

\- Create user flows

\- Prepare for dev handoff



Friday: Documentation \& Training

\- Component usage guide

\- Spacing \& grid documentation

\- Handoff session with developers

\- Record Loom video for client

```



Deliverables:



\- Complete Figma design system  

\- 15-20 page designs  

\- Interactive prototype  

\- Usage documentation  

\- Dev handoff specs



---



\### Sub-Phase 2C: Webflow Foundation
\*\*When:\*\* Runs parallel to 2B (Visual Design), starting when design variables are 50% locked
\*\*RACI:\*\* Dev Lead (R), PM (A), Design Lead (C to confirm values), Client PM (I)
\*\*Trigger condition:\*\* Design Lead signals "colors and typography are locked" in Slack or Figma
before any variables are entered into Webflow.

\#### \[PROJECT-PREFIX\]-2C1: Webflow Project Setup (2 pts)
Triggered when: Design system 50% complete (primary colors + fonts confirmed)
\- \[ \] Webflow project created under agency workspace with correct client name
\- \[ \] Staging domain active: \[client-slug\].webflow.io
\- \[ \] Client-First naming convention applied to global style settings
\- \[ \] Brand fonts installed (or Google Fonts fallback if font files pending)
\- \[ \] Project shared with Design Lead (Designer role) and Dev team (Developer role)
\- \[ \] Staging URL posted in Slack \[#project-channel\] and added to project EPIC

\#### \[PROJECT-PREFIX\]-2C2: Design Variables Entry — Colors, Typography, Spacing (4 pts)
Triggered when: Each token category locked by Design Lead (enter in batches, not one-shot)
\- \[ \] Full color palette entered as Webflow variables (primary, secondary, semantic)
\- \[ \] Typography scale entered: all heading levels, body sizes, line heights, font weights
\- \[ \] Spacing scale entered (e.g. 4px base unit with 7 spacing steps)
\- \[ \] All variables cross-checked against Figma source by Design Lead and Dev Lead
\- \[ \] Style guide screenshot posted in Slack for team awareness

\#### \[PROJECT-PREFIX\]-2C3: CMS Collections Architecture (4 pts)
Triggered when: Page designs 60% complete (enough to define field requirements)
\- \[ \] All CMS collections created per EPIC scope (e.g. Blog, Team, Careers, Case Studies)
\- \[ \] Each collection has correct field types and names
\- \[ \] 1–2 sample content items entered per collection for dev testing
\- \[ \] Collection structure reviewed by Content Lead for field accuracy
\- \[ \] CMS structure documented in Google Drive: 05\_DEVELOPMENT/CMS\_Architecture.md

\*\*Capacity note:\*\* 2C tasks draw from Phase 3 Dev budget (~10 pts), not Phase 2 budget.
Moving setup earlier means Phase 3 Week 1 starts on page builds immediately.



---



\## PHASE 3: DEVELOPMENT (Weeks 4-7)



\### Target Hours: 200-250 hours



\### Critical: Daily time tracking compliance



\#### 3.1 Webflow Development Setup (BET-002)



When: Week 4-8 Who:



\- R: Webflow Developer  

\- A: Tech Lead  

\- C: Design Lead  

\- I: Client



Week 4 \\- Foundation:



```

Monday: Project Setup

1\. Create Webflow project

2\. Configure hosting plan

3\. Set up environments:

&nbsp;  - Development

&nbsp;  - Staging

&nbsp;  - Production

4\. Install client brand fonts

5\. Configure global styles



Tuesday-Wednesday: CMS Architecture

1\. Define collections:

&nbsp;  - Blog posts

&nbsp;  - Team members

&nbsp;  - Case studies

&nbsp;  - Resources

2\. Set up fields and references

3\. Create sample content

4\. Build CMS templates



Thursday-Friday: Component Building

1\. Create symbols for:

&nbsp;  - Header/navigation

&nbsp;  - Footer

&nbsp;  - Form components

&nbsp;  - CTA sections

2\. Build utility classes

3\. Set up interactions library

```



Week 5-6 \\- Page Development:



```

Sprint Planning (Monday AM):

\- Review designs in Figma

\- Break into Linear issues

\- Apply ICE scoring

\- Assign via RACI



Daily Development Rhythm:

\- 10 AM: Standup (15 mins)

\- 10:15 AM - 12:30 PM: Development

\- 2 PM - 5:30 PM: Development

\- 5:30 PM: Push to staging

\- 5:45 PM: Time tracking entry



Page Build Sequence:

1\. Homepage (3 days)

2\. Product/Service pages (2 days)

3\. About/Team pages (1 day)

4\. Blog/Resource centre (2 days)

5\. Contact/Forms (1 day)

6\. Legal pages (0.5 day)

```



\#### 3.2 SEO Optimisation (BET-003)



When: Week 6 Who:



\- R: SEO Specialist  

\- A: Tech Lead  

\- C: Marketing  

\- I: Client



Technical SEO Checklist:



```

1\. Page Speed Optimisation

&nbsp;  - Image compression (<100KB)

&nbsp;  - Lazy loading enabled

&nbsp;  - Minify CSS/JS

&nbsp;  - Target: <3s load time



2\. Schema Markup

&nbsp;  - Organisation schema

&nbsp;  - Product/Service schema

&nbsp;  - FAQ schema

&nbsp;  - Breadcrumb schema



3\. Technical Setup

&nbsp;  - XML sitemap generation

&nbsp;  - Robots.txt configuration

&nbsp;  - 301 redirect mapping

&nbsp;  - Google Search Console setup

&nbsp;  - Analytics implementation

```



\#### 3.3 Content Migration (BET-004)



When: Week 5-6 Who:



\- R: Content Lead  

\- A: Project Manager  

\- C: Client  

\- I: SEO Team



Migration Process:



```

1\. Content Audit (Day 1)

&nbsp;  - Export all existing content

&nbsp;  - Create migration spreadsheet

&nbsp;  - Flag outdated content

&nbsp;  - ICE score for priority



2\. Data Preparation (Day 2)

&nbsp;  - Clean up formatting

&nbsp;  - Optimise images

&nbsp;  - Update meta descriptions

&nbsp;  - Prepare redirect map



3\. Import Process (Day 3-4)

&nbsp;  - Batch import via CSV

&nbsp;  - Manual review each page

&nbsp;  - Set up 301 redirects

&nbsp;  - Verify all links



4\. QA Phase (Day 5)

&nbsp;  - Check all pages render

&nbsp;  - Verify SEO elements

&nbsp;  - Test forms and CTAs

&nbsp;  - Mobile responsiveness

```



---



\## PHASE 4: QUALITY \& LAUNCH (Week 8\\)



\### Target Hours: 40-50 hours



\### Focus: Zero defects, client satisfaction



\#### 4.1 UAT Management (QUA-003)



When: Week 8 Who:



\- R: QA Lead  

\- A: Project Manager  

\- C: Client Team  

\- I: Dev Team



UAT Process:



```

Monday - Test Planning:

1\. Create UAT scenarios (20-25 tests)

2\. Set up staging environment

3\. Provide client access

4\. Schedule training call



Tuesday-Wednesday - Testing:

Client Testing Checklist:

â–¡ Homepage journey complete

â–¡ All CTAs functional

â–¡ Forms submit correctly

â–¡ Mobile experience smooth

â–¡ Content accurate

â–¡ Analytics tracking working

â–¡ Page speed acceptable

â–¡ SEO elements present



Thursday - Issue Resolution:

\- P0 (Critical): Fix immediately

\- P1 (High): Fix within 4 hours

\- P2 (Medium): Fix by end of day

\- P3 (Low): Document for post-launch



Friday - Sign-off:

1\. Final walkthrough with client

2\. Get written approval

3\. Prepare launch sequence

```



\#### 4.2 Performance Testing (QUA-004)



When: Week 7-8 Who:



\- R: Performance Engineer  

\- A: Tech Lead  

\- C: Infrastructure  

\- I: Client



Performance Targets:



```

Metrics to Achieve:

\- First Contentful Paint: <1.5s

\- Largest Contentful Paint: <2.5s

\- Total Blocking Time: <300ms

\- Cumulative Layout Shift: <0.1

\- PageSpeed Score: >90 (mobile)

\- GTmetrix Grade: A

```



---



\## PHASE 5: HANDOVER \& SUPPORT (Week 9-10)



\### Success Metric: CSAT \\>9, Google Review secured



\#### 5.1 Client Handover (QUA-002)



When: Week 9 Who:



\- R: Delivery Lead  

\- A: Project Manager  

\- C: Client Team  

\- I: Account Manager



Handover Package Contents:



```

1\. Access Credentials

&nbsp;  - Webflow account transfer

&nbsp;  - Analytics access

&nbsp;  - Domain/DNS details

&nbsp;  - Third-party integrations



2\. Documentation

&nbsp;  - Site architecture diagram

&nbsp;  - CMS usage guide

&nbsp;  - SEO maintenance guide

&nbsp;  - Component library



3\. Training Materials

&nbsp;  - 60-min recorded training

&nbsp;  - Quick reference guides

&nbsp;  - FAQ document

&nbsp;  - Support contact info



4\. Working Files

&nbsp;  - Figma design files

&nbsp;  - Image assets (original)

&nbsp;  - Brand guidelines

&nbsp;  - Content spreadsheets

```



\#### 5.2 CSAT \& Review Collection (ADM-006, ADM-007)



When: Week 9-10 Who:



\- R: Account Manager (Rohan)  

\- A: Head of Revenue  

\- C: Delivery Team  

\- I: Leadership



Review Collection Sequence:



```

Day 1 (Post-Launch):

\- Send CSAT survey

\- Target: Response within 48 hours



Day 3 (If CSAT â‰¥9):

\- Request Google review

\- Provide direct link

\- Share suggested talking points



Day 7:

\- Follow-up if no review

\- Offer to schedule call

\- Address any concerns



Day 14:

\- Prepare Clutch submission

\- Schedule client interview

\- Brief client on process

```



---



\## FINANCIAL TRACKING \& MARGIN PROTECTION



\### Weekly Margin Check (FIN-001)



Every Friday at 4 PM SGT



```

Sample Week 5 Analysis:

Budget Allocated: $50,000

Hours Budgeted: 200 hours

Hours Used: 95 hours

Budget Consumed: 47.5%

Current Margin: 54%

Status: ON TRACK



Breakdown by Role:

\- Sean (10 hrs @ $350): $3,500

\- Senior Dev (30 hrs @ $250): $7,500

\- Developers (40 hrs @ $180): $7,200

\- Designer (15 hrs @ $200): $3,000

Total Spent: $21,200

```



\### Daily Time Tracking Compliance (ADM-003)



Every day by 5 PM SGT



```

Linear Issue: BETA-234: Build homepage hero section

Time Logged: 3.5 hours

Description: "Implemented hero section with Webflow interactions, 

optimised images, added responsive breakpoints"

Task Category: Development

Billable: Yes

```



---



\## RISK MITIGATION STRATEGIES



\### Common Beta Engagement Risks:



Risk 1: Scope Creep



\- Trigger: Client requests beyond signed SOW  

\- Mitigation:  

&nbsp; - Document all requests in Linear  

&nbsp; - ICE score for priority  

&nbsp; - Issue change order if \\>10% scope increase  

&nbsp; - Maintain margin above 50%



Risk 2: Design Revision Loops



\- Trigger: \\>3 rounds of major revisions  

\- Mitigation:  

&nbsp; - Lock design after Week 3  

&nbsp; - Additional revisions \\= new SOW  

&nbsp; - Clear sign-off at each milestone



Risk 3: Technical Complexity



\- Trigger: Custom functionality requests  

\- Mitigation:  

&nbsp; - Assess during Week 1  

&nbsp; - Propose Gamma engagement if needed  

&nbsp; - Use approved Webflow apps only  

&nbsp; - No custom code without change order



---



\## SUCCESS METRICS \& KPIs



\### Project Level Success:



\- On-Time Delivery: 95% milestones met  

\- Budget Adherence: \\<5% variance  

\- Quality Score: \\<2% defect rate  

\- Client Satisfaction: CSAT \\>9  

\- Team Utilisation: 75-80%  

\- Margin Achievement: 50-60%



\### Post-Launch Metrics (30 days):



\- Performance: PageSpeed \\>90  

\- Uptime: 99.9%  

\- SEO: Rankings maintained/improved  

\- Conversions: Baseline established  

\- Support Tickets: \\<5



---



\## TEAM COMMUNICATION RHYTHM



\### Daily:



\- 10 AM SGT: Team standup (15 mins)  

\- 5 PM SGT: Time entry deadline  

\- 6 PM SGT: Staging deployment



\### Weekly:



\- Monday 9 AM: Sprint planning  

\- Wednesday 3 PM: Client check-in  

\- Friday 4 PM: Margin review  

\- Friday 5 PM: Retrospective



\### Milestone:



\- Design Complete: Formal presentation  

\- Dev Complete: UAT kickoff  

\- Launch: Handover session  

\- Post-Launch: 30-day review



---



\## TOOLS \& INTEGRATIONS



\### Core Stack:



1\. Linear: Project management, ICE scoring, RACI matrix  

2\. Tracking Time: Time entry, budget tracking  

3\. Figma: Design system, prototypes  

4\. Webflow: Development platform  

5\. Slack: Team communication  

6\. Loom: Training videos  

7\. Google Drive: File storage



\### Integrations:



\- Linear â†” Tracking Time (4-hour sync)  

\- Linear â†” Slack (real-time notifications)  

\- Webflow â†” Analytics (GA4, PostHog)  

\- Figma â†” Webflow (design tokens)



---



\## CLIENT EXAMPLES \& CASE STUDIES



\### Recent Beta Engagements:



XCL Academy ($45K)



\- 25 pages migrated  

\- 3 language versions  

\- Custom admissions portal  

\- Delivered in 7 weeks  

\- Margin: 58%



CarTracker ($35K)



\- RMD platform setup  

\- Vehicle listing system  

\- Dealer portal  

\- 6-week delivery  

\- Margin: 55%



SendByte ($28K)



\- Marketing website  

\- Resource centre  

\- Lead generation forms  

\- 5-week delivery  

\- Margin: 52%



---



\## APPENDIX: TEMPLATES \& RESOURCES



\### Available Templates:



\- Beta engagement contract template  

\- Figma starter design system  

\- Webflow project boilerplate  

\- UAT test scenarios (25 standard tests)  

\- Client training deck  

\- Handover checklist  

\- CSAT survey template  

\- Review request templates



\### Training Resources:



\- Webflow University access  

\- Figma best practices guide  

\- SEO checklist (100+ items)  

\- Performance optimisation guide  

\- Client communication templates  

\- Scribe process recordings



---



\## ESCALATION \& SUPPORT



\### Escalation Matrix:



Level 1 (Team Lead \\- 4 hours):



\- Technical blockers  

\- Resource conflicts  

\- Minor scope questions



Level 2 (Sean/PM \\- 2 hours):



\- Design approval delays  

\- Budget concerns  

\- Timeline risks



Level 3 (Leadership \\- 1 hour):



\- Margin breach (\\<45%)  

\- Client escalation  

\- Scope \\>20% change



Level 4 (COO \\- Immediate):



\- Contract disputes  

\- Critical delivery risk  

\- CSAT \\<7



\### Support Contacts:



\- Technical: Davis (Solution Architect)  

\- Design: Sean (Creative Lead)  

\- Commercial: Rohan (Head of Revenue)  

\- Operations: Daz (COO)



---



\*This Beta Engagement Playbook is a living document. Updates required when:\*



\- \*New tools adopted\*  

\- \*Process improvements identified\*  

\- \*Client feedback received\*  

\- \*Margin targets adjusted\*



Last Updated: February 2026
Version: 2.1
Owner: Daz (COO)
Next Review: July 2026

---

## Using Claude to Generate Tasks

### One task per prompt run — not batches.

### Required inputs before generating a task
1. Project name + EPIC link
2. Team members + weekly point capacity for this phase
3. Phase brief summary (2–3 sentences)
4. Task number, name, owner, points, sprint week
5. One-sentence deliverable description
6. What this task depends on + what it blocks
7. RACI pre-filled — do NOT leave RACI for Claude to infer

### Claude prompt template (copy-paste, fill CONTEXT block, submit)

---
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
---

### Quality check before saving to Linear
- [ ] RACI all four fields filled (no blanks)
- [ ] Escalation line names a real person, not a role title
- [ ] "What We're Doing" is 3 sentences or fewer
- [ ] No Additional Notes section present
- [ ] No brand colors, reference websites, or training links in the body
- [ ] Acceptance Criteria ≤ 10 items, each binary
- [ ] Metadata has Depends On and Blocks filled
- [ ] Task body is under 250 words

