# AI Strategy & Governance — shared guardrails

General guardrails (disclaimer, no fabricated numbers, premise-checking, the
principle of making maturity visible) are collected in one place: **see
`../meta/shared-guardrails.md` — read that first.** This file only contains
what's genuinely specific to this pack.

---

## Maturity in this pack

This pack's skills are currently at `maturity: scaffold` (see
`../skills_index.json` and `../meta/maturity_levels.md`) — the structure and
research anchoring are solid, but the owner's own validated experience
hasn't been attached yet.

## Pack-specific note

Does not replace a legal EU AI Act compliance assessment — deeper analysis
requires separate regulatory expertise.

This pack contains several similar three-/four-way classifications that
answer DIFFERENT questions — don't confuse them with each other:

- **Automate/Augment/Human-Only** (`task-level-decomposition-and-
  automation-fit`) — answers "does THIS TASK suit AI, and at what
  level."
- **Quick Wins/Strategic Bets/Hard-Low Value/Deprioritize**
  (`ai-opportunity-portfolio`) — answers "is THIS OPPORTUNITY worth
  pursuing, and is it easy to implement."
- **Deploy/Reshape/Invent** (`ai-opportunity-portfolio`) — answers
  "how DEEPLY does this implementation touch the organization."
- **Horizon 1/2/3** (`ai-capability-roadmap`) — answers "WHEN
  is this implemented."

When you refer to one of these, use the correct term and don't use them
as synonyms for one another — they correlate but they are not the same
classification.

There are two complementary, NOT competing, approaches to assembling a raw
list — don't present one as "better" without context:

- **Bottom-up** (`task-level-decomposition-and-automation-fit`) — works
  through an existing process one task at a time. Strong when the
  process is already precisely described.
- **Top-down** (`ai-capability-pattern-matching`) — poses the diagnostic
  questions of a ready-made capability pattern library
  (`references/ai-capability-pattern-library.md`) before a detailed
  process description exists. Faster first-pass mapping, requires
  validation before scoring.

This pack's `ai-initiative-readiness-auditor` agent (see `agents/`) audits
an initiative against the 5 dimensions of the `ai-opportunity-portfolio`
skill and the `responsible-ai-and-governance-check` checklist before the
initiative goes to approval — it does not replace the legal compliance
assessment mentioned above.

## Shared standards

See `../meta/frontmatter_schema.md` (what's allowed in a SKILL.md
frontmatter) and `../meta/skill_design_principles.md` (what a good skill in
this repo has to pass).
