# Opportunity Recognition — shared guardrails

General guardrails (disclaimer, no fabricated numbers, premise-checking, making
maturity visible) are collected in one place: **see
`../meta/shared-guardrails.md` — read that first.** This file only contains
what's genuinely specific to this pack.

---

## Maturity in this pack

This pack's maturity is **mixed** (see `../skills_index.json` and
`../meta/maturity_levels.md`):

- `market-and-signal-scanning`, `pattern-and-analogy-connector`,
  `opportunity-evaluation-and-judgment`, `market-sizing-tam-sam-som`,
  `competitive-and-five-forces-mapping` are `maturity: scaffold` — the
  structure and research anchoring are solid, but the owner's own validated
  field experience hasn't been attached yet.
- `opportunity-intake-elicitation`, `opportunity-value-assessment`, and
  `opportunity-brief-writing` are `maturity: validated`,
  `source_layer: owner` — converted directly from the owner's own productized
  Opportunity Value Assessment methodology, used in real client work.

## Pack-specific note

Doesn't substitute for deep industry expertise — it surfaces opportunities
for assessment, it doesn't guarantee they're implementable.

This pack's `market-sizing-cross-validator` agent (see `agents/`)
cross-checks the calculation produced by the `market-sizing-tam-sam-som`
skill before the figure is used in a business case or presented to
leadership — see also `../meta/external-data-mcp.md` for the optional
external data sources the agent can draw on if they're connected.

## Shared standards

See `../meta/frontmatter_schema.md` (what's allowed in a SKILL.md
frontmatter) and `../meta/skill_design_principles.md` (what a good skill in
this repo has to pass).
