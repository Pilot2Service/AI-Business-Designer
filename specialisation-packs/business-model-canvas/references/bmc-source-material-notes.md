# Source material notes — Business Model Canvas pack

This pack is built from two complementary sources:

## 1. Innovation pattern library (machine-readable)

- A public business model innovation pattern library: 159 patterns in
  four groups (Financial/Operating/Value/Experience Model), 13 sub-models.
  The full library is in this pack: `bmc-innovation-pattern-library.md`.
- A usage guide for AI agents applying the patterns: contextual
  relevance, printing JSON paths, avoiding contradictory patterns,
  ethical compliance, feasibility assessment, output schema
  (`pattern_id`, `pattern_name`, `sub_model`, `rationale`).
- A task specification for context-based pattern recommendation: from
  context (ICP, solution category, market characteristics, cost
  structure) to a recommendation of 3-5 coherent patterns, output schema
  `{recommendations, conflicts_avoided, assumptions}`.

Together these form the technical backbone of the
`bmc-innovation-pattern-matching` skill.

## 2. The owner's private expertise layer

The owner's own, non-public research work to capture BMC consulting
expertise in a structured, machine-readable form. The content is split
into two clearly marked layers:

- **Research layer** — a pre-filled synthesis of well-known BMC sources
  (Jeffries, Williams, van der Linden, Blank/Strategyzer, Ash Maurya)
  containing open sections the owner has not yet filled in (expert
  sessions marked pending).
- **Expert layer** — genuinely completed methodology drawn from the
  owner's own consulting interview conducted in April 2026: an expert
  profile, cognitive signatures, iteration logic, the canvas-readiness
  quality model, guidance for applying innovation patterns, antipatterns,
  and the most common client misunderstandings.

This skills pack's `maturity`/`source_layer` values are set directly
according to this split: skills built from the expert layer are
`validated`/`owner`, skills built from the research layer are
`scaffold`/`research` — exactly the same principle this whole repo
follows elsewhere.

Some topics in the expert layer (intuition signals, red-flag sensitivity,
heuristics, situation-reading patterns, organizational identity) are
still entirely empty and haven't been used as the basis for any skill.
Once the owner fills these in later, this pack's skills should be
enriched again.

## 3. Why its own pack rather than part of business-design-frameworks

The `business-design-frameworks` pack is a deliberately loose collection
of independent, standalone structuring models (layers, value chain,
category, strategy map, service journey). BMC consulting expertise, by
contrast, is one unified, internally interdependent practice area — its
own vocabulary, diagnostics, and pattern library — much like
`research-commercialisation` and `ai-native-startup-design`. That's why
this is its own specialisation pack rather than an addition to
business-design-frameworks.
