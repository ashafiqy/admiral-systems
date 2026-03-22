<!-- bot-skill
name: digest-and-create
description: Digest client input into vault, draft Linear updates, and ping PM chat
type: action
tools: Read,Glob,Grep,Edit,Write,mcp__linear-server__*,mcp__plugin:slack:slack__*
-->

Process new client input and stage it for PM review.

*Step 1: Identify the client*
Read the input provided in "$ARGS". Determine which client this relates to by matching against `clients/` folders.

*Step 2: Digest into vault (staging)*
Synthesize the input into a structured vault entry. Write it to `inbox/` as a staging file — NOT directly to the client folder.

Use the appropriate format:
• Meeting notes → follow [[tpl-meeting-notes]] structure
• Client request/scope change → structured summary with decisions, commitments, action items
• General update → contextual summary

Include frontmatter:
```yaml
---
title: [descriptive title]
created: [today's date]
updated: [today's date]
tags:
  - client/[client-name]
status: draft
target: clients/[client-folder]/[filename]
---
```

*Step 3: Draft Linear project update*
Write a summary of what changed that would be posted as a Linear project update. Do NOT create it yet — just draft the text.

*Step 4: Draft Linear tasks*
If the input contains action items or new work, draft Linear tasks following the [[tpl-linear-task]] template from the vault. Include:
• Title (verb-first)
• Description (RACI, acceptance criteria, blockers, dropoff)
• Suggested assignee, priority, estimate, milestone

Do NOT create them yet — just draft the text.

*Step 5: Post to Slack for review*
Post to the #claude-actionables channel with:

*:clipboard: New Client Input — [Client Name]*

*Vault Entry* (staged in inbox/)
> [preview of what was written]

*Drafted Linear Project Update*
> [the update text]

*Drafted Linear Tasks*
> [list of drafted tasks with titles, assignees, priorities]

_Reply in this thread:_
• `@bot confirm` — file vault entry, create Linear update + tasks
• `@bot [add corrections]` — I'll update everything and re-post
• `@bot cancel` — discard everything

*On confirm:*
• Move vault entry from `inbox/` to `clients/{client}/`
• Create the Linear project update via MCP
• Create the Linear tasks via MCP following [[create-issue-agent]] playbook

*On corrections:*
• Update the `inbox/` entry with new info
• Revise all drafted Linear content
• Re-post the updated draft for another review

*On cancel:*
• Delete the `inbox/` entry
• Discard all drafts

Format all Slack messages using Slack mrkdwn (use *bold* headers, not ### markdown headers).
