---
name: risk-matrix-and-mitigation
description: "Identifies and scores risks (probability × impact) and designs mitigations. Use when you need business-case-and-analysis-level support for a comparable task."
---

# Risk Matrix & Mitigation

*Status: `scaffold` — see [`../../../skills_index.json`](../../../skills_index.json) and [`../../../meta/maturity_levels.md`](../../../meta/maturity_levels.md).*

## Purpose

Identifies and scores risks (probability × impact) and designs mitigations.

## Anchored in research

- ISO 31000
- PMI risk management

## Method (draft — to be expanded)

1. **Establish context and criteria first** (ISO 31000): what's the scope of
   this risk assessment, and what probability/impact scale and
   risk-acceptance threshold will be used? Skipping this step produces a risk
   matrix that can't be compared across projects.
2. **Identify risks systematically, not just the ones top of mind** — walk
   through each project phase, stakeholder group, and dependency (PMI
   identification techniques: brainstorming, checklists, assumption
   analysis, SWOT) and log each one as a discrete entry in a risk register
   with a clear risk statement (cause → risk event → effect).
3. **Score each risk on probability and impact on a defined scale** (e.g. 1–5
   on each axis) and plot it on a 5×5 matrix — the score, not gut feel,
   ranks which risks get attention first.
4. **For each risk above the acceptance threshold, select a PMI response
   strategy:** avoid (eliminate the cause), mitigate (reduce probability or
   impact), transfer (insurance, contract, third party), or accept (with a
   documented rationale, appropriate for low-priority risks) — and assign an
   owner and a trigger condition for each.
5. **Distinguish residual risk (what remains after mitigation) from the
   original score** — a mitigation plan that isn't re-scored against the
   same criteria understates what's still open.
6. **Set a monitoring and review cadence** (ISO 31000's continuous-review
   loop) — a risk register is a living document; a matrix built once at
   project start and never revisited misses new and materialized risks.

## What this skill does NOT do

- Doesn't make the final decision for you — it produces a structured draft to
  support a human decision.
- Doesn't confirm figures, market data, or competitor data from memory — it
  uses the inputs you provide, or marks an assumption clearly
  (`[assumption — verify]`).
- Doesn't eliminate risk — it makes it visible and structures the mitigation
  options.

## [OWNER INPUT — to be completed]

This skill is a structural draft (`maturity: scaffold`). It doesn't yet
contain your own experience, heuristics, or case examples. Fill in here:

- your own rules of thumb and heuristics for this technique
- concrete templates (into [`../../references/`](../../references/))
- reference cases / your own examples
- what this skill deliberately does *not* do (guardrails, common mistakes) —
  add to the list above

Once this section is filled in and validated in practice, update the
`maturity` field in `skills_index.json` to `draft`, `validated`, or
`canonical` (see
[`../../../meta/maturity_levels.md`](../../../meta/maturity_levels.md)).
**Don't add new fields to the frontmatter** — `name` and `description` are
the only ones allowed (see
[`../../../meta/frontmatter_schema.md`](../../../meta/frontmatter_schema.md)).

## Continue from here

- When this step is done, move to
  [`../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`](../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md)
- A ready-made skill chain for this situation: see [`../../../playbooks/`](../../../playbooks/)
- This pack's shared guardrails: [`../../CLAUDE.md`](../../CLAUDE.md)

## References

- [`../../references/`](../../references/) — the pack's shared background material
- [`../../CLAUDE.md`](../../CLAUDE.md) — the pack's shared guardrails
