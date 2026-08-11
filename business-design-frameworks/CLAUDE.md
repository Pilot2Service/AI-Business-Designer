# Business Design Frameworks — shared guardrails

General guardrails (disclaimer, no fabricated numbers, premise-checking, keeping maturity as an internal note) are collected in one place: **see
`../meta/shared-guardrails.md` — read that first.** This file only contains
what's genuinely specific to this pack.

---

## This pack is an open collection — not a closed list

Unlike the other core packs, this pack is designed to **keep growing**. It
brings together different ways of structuring and modeling business,
value creation, value chains, and positioning — layer models, value chain
analysis, category modeling, and new structuring approaches to be added
later. When a new skill is added to this pack:

- It gets its own `skills/<skill-id>/SKILL.md` file following the same
  minimal frontmatter pattern (`name` + `description`, nothing else).
- It's added to this pack's `README.md` skill table and, where relevant,
  cross-linked to other skills in the same pack ("Continue from here").
- Its maturity (`maturity`) defaults to `scaffold` unless it's the user's
  own validated method (like, for example, the owner skills in the
  research-commercialisation or opportunity-recognition packs).

## Disclaimer in this pack — a structuring approach, not a finished analysis

In addition to the general disclaimer (`shared-guardrails.md`): these are
thinking aids (mental models). Don't present the output of a modeling exercise
as the final truth or the one correct structure — several models can produce
different, equally valid perspectives on the same business.

## Pack-specific note

These are general, industry-agnostic structuring models — they always need
to be adapted to context. Don't force a business into a model that isn't
producing insight; try another model from the same collection, or combine
several.

This pack's `competitive-blind-spot-scanner` agent (see `agents/`) looks for
blind spots in any competitive/positioning analysis — it works on top of
both this pack's `strategy-canvas-and-value-curve` output and, for example,
the `opportunity-recognition` pack's `competitive-and-five-forces-mapping`
output. Use it before a competitive-situation analysis is presented as a
finished picture of the industry.

## Shared standards

See `../meta/frontmatter_schema.md` (what's allowed in a SKILL.md frontmatter)
and `../meta/skill_design_principles.md` (what a good skill in this repo has
to pass).
