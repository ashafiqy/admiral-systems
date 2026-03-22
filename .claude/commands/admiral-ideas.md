Scan the Admiral Systems vault and generate actionable ideas for tools, agents, and commands that would improve project management, delivery, and context sharing with the team.

This is a read-only command — do not create or modify any files.

## Process

1. **Scan key vault areas** for patterns, gaps, and opportunities:
   - `clients/` — client structure, briefs, meetings, deliverables
   - `delivery/` — sprint tracking, capacity, risks, processes
   - `operations/agent-playbooks/` — existing agent definitions
   - `operations/sops/` — standard operating procedures
   - `operations/beta-workflow/` — experimental workflows
   - `team/` — team structure, onboarding, hiring
   - `templates/` — available templates
   - `command/` — strategy, OKRs, decisions, meetings
   - `.claude/commands/` — existing slash commands

2. **Cross-reference** what exists against common agency needs:
   - Are there repetitive manual processes that could be automated?
   - Are there missing agent playbooks for common workflows?
   - Are there gaps in slash commands for team operations?
   - Are there templates that should exist but don't?
   - Are there delivery patterns that could benefit from tooling?
   - Are there missing guardrails in `CLAUDE.md`?
   - Could existing or new agents/commands/skills benefit from safety rules, constraints, or validation steps?

3. **Generate categorized ideas** based on actual vault content.

## Output format

### Tools to build
Scripts, integrations, and automations that would save time or reduce errors.

### Agents to create or improve
Claude agent playbooks for the `operations/agent-playbooks/` directory — automated workflows the team can invoke.

### Commands & skills
New `/slash` commands for the vault workflow that would help the team.

### Guardrails & constraints
Rules, validation steps, or safety boundaries to add to `CLAUDE.md` files, agent playbooks, or command prompts — things that prevent mistakes, protect sensitive data, or enforce quality standards.

---

For each idea, use this format:

**[Idea Name]**
_One-line description_
- Rationale: [specific vault signal — reference actual files or patterns you found]
- Effort: quick / medium / large

---

End with a **"Top 3 highest-impact ideas"** summary that picks the most valuable ideas across all categories, with a one-sentence justification for each.
