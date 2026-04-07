# (REMINDER) Junior Team - Office hours

Tue, 07 Apr 26 · elfajri@admiralsystems.io, haykal@admiralsystems.io, luthfi@admiralsystems.io, mona@admiralsystems.io, shafiq@admiralsystems.io, tiara.almira@admiralsystems.io, davis@admiralsystems.io, sean@admiralsystems.io

### Scott (RCG) — Clay ICP Build

- Target: 3 ICPs total for Scott; 1 already built (UK Real Estate SMEs — ~3,800 companies, decision makers found, emails not pulled to save credits)
- Haykal to build the remaining 2 ICPs:
    - Mid-sized consulting companies (managing directors, able to pay ~£200k/year)
    - Boutique finance firms — private equity, venture capital, hedge funds, wealth management (11–50 employees, ~$500k–$5M revenue)
- All three ICPs are boutique-sized; revenue filter not recommended — use company size from LinkedIn instead
- Goal for tomorrow 3PM: show Scott the ICPs, let him choose which persona/segment to go after first
    - Scott has 5 inboxes → ~250 sends/day max, so lead volume must be manageable
- Once Scott chooses, enrich leads and pull emails (numbers typically drop after enrichment)
- Start at [https://university.clay.com](https://university.clay.com/) — watch the 101 course, focus on finding leads, not sending emails yet
- Daz to create a Linear issue with a proper guide for Haykal

### Scott (RCG) — Klaviyo → Loops Migration

- Luthfi has already migrated the 3 live Klaviyo flows into Loops ([https://loops.so](https://loops.so/))
- Blocker: Loops audience groups are capped at 1,000 contacts; current list is ~1,500
- Resolution: use AI (NotebookLM / Gemini) to filter down to the best 1,000 contacts using clear rationale
    - Filter criteria: (1) contacts with Stripe invoices = paying customers; (2) contacts who never opted in (came via Scott’s events)
    - Pick whichever segment is larger and most defensible to present to Scott
- Decision: go with Loops at $49/month (up to 5,000 contacts); not Klaviyo (B2C tool), not [Customer.io](http://customer.io/) ([https://customer.io](https://customer.io/)) at $100/month unless Scott decides otherwise
- Framing for Scott: show that data has been cleaned and migrated; raw file of ~1,500 contacts preserved so he knows nothing was lost when Klaviyo is cancelled
- Luthfi to chase Haykal to ensure the Clay work is done by 3PM tomorrow

### Wallex — Webflow & Site Build (Elfajri)

- Case studies in Webflow CMS:
    - Case studies live inside the articles collection (not a separate collection) — differentiated by type only
    - Action: open Wallex resources project in Webflow admin → check CMS schema for articles → confirm how article types (articles vs. case studies) are structured; if it ends up under articles, so be it
- Currency pages: do not build individual CMS pages for every currency pair (50×49 combinations = too many)
    - Solution: build one page and use 301 redirects from all currency-pair URLs to that single page

### Design Workflow — Paper/Pencil + MCP (Davis & Sean)

- Exploring replacing Reloom + Figma with an AI-driven wireframing workflow (Paper/Pencil or Cloud Code + MCP) to reduce tooling costs
    - Figma org plan is expensive; if removed, Daz can cover everyone’s Claude plan
- Sean demoed Paper/Pencil (Figma-based beta): types a prompt → MCP generates a wireframe directly in the design tool
    - Works with Claude; Gemini MCP integration less reliable
- Davis’s use case built on Cloud Code (not client-first conventions yet, but doable via PDF → skill)
- Key open question: how easily can MCP-generated designs be pushed to Webflow
    - Webflow MCP beta launched this week — Daz has a call with Webflow team (Jacqueline + Rohan) tomorrow at 8:30PM; Sean and Shafiq invited to join

### Hopland — Status & Blockers (Tiara & Mona)

- Not finished yet; Tiara focusing on Figma (Reloom had a permission/export issue — identified as a Mac folder permissions setting, not a Reloom bug)
- Contents and copy assignments are finalised with the brief; copy generated via Gemini/Reloom is not final-quality
- Images: use the Google Drive folder shared via email thread as the source for all images
- If Daz and Rohan can complete their part tonight, Tiara and Mona will start on Jira Law tomorrow morning (separate briefing call, juniors only)

### Action Items

- Haykal
    - Build 2 remaining Clay ICP workbooks (mid-sized consulting MDs; boutique finance firms) by 3PM tomorrow
    - Start with [https://university.clay.com](https://university.clay.com/) — 101 course, leads focus only
    - Chase Luthfi on the Loops work to confirm it’s ready by 3PM tomorrow
- Luthfi
    - Filter ~1,500 Loops contacts down to 1,000 using AI (Stripe invoice holders vs. non-opt-in contacts)
    - Present cleaned segments to Scott tomorrow alongside the migrated campaigns
    - Daz to create Linear issue with guide before Luthfi starts
- Elfajri
    - Open Wallex resources project in Webflow admin → inspect articles CMS schema → confirm case study type structure
    - Implement 301 redirect for currency pages (one page, redirect all pairs to it)
- Tiara & Mona
    - Upload all images to Reloom/Figma tonight using images from the Google Drive email thread
    - Await briefing from Daz tomorrow morning on Jira Law next steps (contingent on Daz + Rohan finishing tonight)
- Sean
    - Join Webflow team call tomorrow at 8:30PM (Jacqueline + Rohan); request Webflow MCP beta access
- Shafiq
    - Optional: join Webflow team call tomorrow at 8:30PM
- Daz
    - Create Linear issue with Clay guide for Haykal before end of day
    - Webflow call with Jacqueline + Rohan tomorrow 8:30PM
    - Senior-only calendar/process sync immediately after this call

---

Chat with meeting transcript: [https://notes.granola.ai/t/46ca1b23-2896-463e-a1d0-9b0f5f266a36-00demib2](https://notes.granola.ai/t/46ca1b23-2896-463e-a1d0-9b0f5f266a36-00demib2)