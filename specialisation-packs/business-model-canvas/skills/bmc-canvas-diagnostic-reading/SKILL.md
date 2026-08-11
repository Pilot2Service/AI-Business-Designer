---
name: bmc-canvas-diagnostic-reading
description: "Reads a finished BMC canvas as a diagnostic instrument using six research-based rules (Hook Rule, value-cost consistency, segment specificity, evidence grade, defensive canvas, missing block) and a four-dimension quality rubric."
---

# BMC Canvas Diagnostic Reading

## Purpose

Provides a systematic way to read a finished (or nearly finished) BMC
canvas as a diagnostic instrument — not just a checklist of filled blocks,
but six questions about whether the canvas is internally consistent,
honest about evidence, and ready for the hypothesis-testing phase. Use
this ONCE the canvas (or a variant) is ready for assessment — not
mid-session while it's still being built (for that, see
`../bmc-session-facilitation-design/SKILL.md` and
`../bmc-canvas-clarity-and-iteration/SKILL.md`).

## Anchored in research

Based on the owner's private research layer (an April 2026 expert
interview)
(`30_domain_packs/bmc/diagnostics/bmc_diagnostic_rules.md`,
`canvas_quality_rubric.md`, `antipatterns/counterexamples.md` — all
`status: template`, `source: research_layer`), a synthesis drawing on
van der Linden, Jeffries, Williams, and general facilitation practice.
`[EXPERT INPUT]` sections are not yet filled in.

**Note:** This is different from
`../bmc-canvas-clarity-and-iteration/SKILL.md`'s owner-validated
"clarity > depth" readiness criterion. That criterion is deliberately
simpler and more opinionated ("does the canvas tell one thing clearly?").
This skill's six rules are more precise and analytical ("is the canvas
internally consistent and evidence-based?"). Use both — they answer
different questions.

## Method

1. **DR-01 — Hook Rule.** Every element on the right side needs a
   matching hook on the left — and vice versa. If customer relationships
   is defined as "dedicated personal service," key resources needs
   senior customer-facing staff and key activities needs relationship
   management. Trace the connections between related elements — orphan
   elements (without hooks) are assumption gaps. This mirrors a core
   consistency check in Osterwalder and Pigneur's original BMC
   methodology: the nine blocks aren't independent fields, they're a
   connected system, and a block that doesn't visibly connect to anything
   else is a warning sign.
2. **DR-02 — Value-cost consistency.** If the value proposition promises
   premium quality, uniqueness, or a high-touch service, the cost
   structure has to reflect that. A "best quality" + "cost leadership"
   combination is internally contradictory. A contradiction doesn't mean
   the business is wrong — it means the team hasn't resolved a
   fundamental strategic tension. Ask: "can we deliver this value at
   this cost?"
3. **DR-03 — Segment specificity test.** A segment is too broad when:
   it's defined only by demographics ("people aged 25-45"); it could
   include any competitor's any customer ("SMEs"); it lumps several
   distinct buying logics into one group; it includes both the user and
   the payer without distinguishing them. A segment is specific enough
   when a team member could walk outside and identify five specific
   people who fit it, and explain why those five share the same job,
   pain, and gain — a test in the spirit of Jobs-to-be-Done thinking
   (van der Linden, Jeffries) applied directly to segment definition.
4. **DR-04 — Evidence grade check.** Read every block and classify it:
   proven (tested with real customers/data), weakly proven (an internal
   assumption or secondhand information), assumed (an untested belief).
   The blocks with the most red are the testing priority. A canvas that's
   entirely green either describes a genuinely mature business model or
   hasn't been honest about what's actually known.
5. **DR-05 — Defensive canvas signal.** When a team fills in the canvas
   quickly, confidently, and without debate, two things are possible:
   (1) the model is genuinely mature and well understood (rare), or (2)
   the team is projecting certainty instead of examining it (common).
   Signals: no block was debated or changed during the session; every
   element is positive (no tensions or trade-offs named); the team
   refers to the canvas as "our story" rather than "our assumptions";
   customer segments are presented as facts, not hypotheses.
6. **DR-06 — A missing block tells you something.** When a block is
   left empty or marked "TBD," this is diagnostic information, not a
   formatting error. An empty revenue streams block means the team
   hasn't resolved how value gets captured. An empty key partners block
   usually means dependencies haven't been thought through yet. The most
   diagnostic empty block: customer relationships — teams often skip it
   by conflating it with channels, which reveals that the nature of the
   interaction (transactional vs. relational, high-touch vs. automated)
   hasn't been thought through yet.
7. **Use the four-dimension rubric for a final score** (each 1-5):
   segment specificity, value proposition quality, internal consistency,
   evidence honesty. Interpretation: 16-20 = strong canvas, ready for
   the testing phase. 11-15 = workable, needs fixes before testing.
   6-10 = significant rework needed. Below 6 = start over.
8. **Watch for two counterexamples that look like good work but
   aren't:** (C-01) a specific but still wrong segment — specificity
   doesn't guarantee validity if the segment is too small, internally
   heterogeneous, or limited to the founder's own network; test: can the
   team name three competitors chasing the same group? (C-02) an honest
   but still incomplete canvas — honesty about uncertainty doesn't mean
   the RIGHT uncertainties have been identified; test: when asked "what
   would kill this business model?", do the risks named match anything
   visible on the canvas?

## What this skill does NOT do

- Doesn't contain the owner's own take on the most common hook error,
  value-cost contradiction, or segment specificity test seen in their own
  practice — these remain open as `[EXPERT INPUT]` sections in the source
  files.
- Doesn't replace `../bmc-canvas-clarity-and-iteration/SKILL.md`'s
  simpler, owner-validated readiness criterion — use both alongside each
  other, not one instead of the other.
- Doesn't make the final proceed/return decision for you — it provides
  scoring and diagnostics; the decision to move to the testing phase is a
  human one.

## Refinement notes

- What's the most common hook error (DR-01) you find in practice?
- What's the most common value-cost contradiction (DR-02) you see, and
  how do you raise it without triggering defensiveness?
- What's your own segment specificity test (DR-03)?
- How do you run the evidence grade check (DR-04) live in a session? Do
  clients push back on being marked red?
- How do you tell genuine confidence apart from defensive certainty
  (DR-05)?
- Which empty block (DR-06) tells you the most, in your experience?
- How does your own quality assessment work — which dimension weighs
  the most?

## Continue from here

- Previous skill in the same pack:
  `../bmc-canvas-clarity-and-iteration/SKILL.md` — the owner's own,
  lighter-weight readiness criterion, use first.
- Next skill in the same pack:
  `../bmc-tool-switching-decisions/SKILL.md` — when the diagnostics
  reveal that the BMC is no longer the right tool.
- This pack's shared guardrails: `../../CLAUDE.md`

## References

- `../../references/bmc-source-material-notes.md` — source material background
- `../../CLAUDE.md` — this pack's shared guardrails
