---
status: validated
owner_input_needed: true
last_reviewed: 2026-08-05
---

# Business Model Canvas

Business Model Canvas (BMC) consulting expertise brought together into one
specialisation pack: a 159-pattern innovation library for reinventing a
business model, the owner's own variation and clarity logic, detection of
antipatterns and client misunderstandings, and research-based support for
session facilitation, diagnostic reading of a canvas, tool selection, and
interpreting client language.

## Status

This pack combines two sources supplied by the owner:

1. **A public, machine-readable 159-pattern innovation library** — see
   `references/bmc-innovation-pattern-library.md`.
2. **The owner's own, non-public research work** — an ongoing project to
   capture BMC consulting expertise. It contains both genuinely validated
   expert content drawn from a consulting interview conducted in April 2026,
   and a pre-filled, not-yet-completed research layer synthesized from
   well-known BMC sources (Jeffries, Williams, van der Linden,
   Blank/Strategyzer, Ash Maurya).

For this reason, three of the pack's seven skills are `validated`/`owner`
level and four are `scaffold`/`research` level — see `CLAUDE.md` and
`references/bmc-source-material-notes.md` for the full explanation of the
split.

## Client profile (anchored in the expert)

The consulting practice behind this pack targets **early-stage and
growth-stage companies** — not large enterprises or their innovation units.
Typically small companies where the founder or entrepreneur is closely
involved in the work. The expert's own definition of the BMC's role:
*"BMC is a thinking tool, not a complete business planning instrument. Its
purpose is to help the team think in new ways, see new opportunities, and
enable different perspectives."* The BMC does not replace: product
specifications, profitability calculations, growth and margin scenarios —
these require more precise tools.

## Skills in this pack

| Skill | Level | Description |
|---|---|---|
| `bmc-innovation-pattern-matching` | `validated` | Identifies 3-5 compatible innovation patterns from the 159-pattern library, using the expert's own four-part taxonomy. |
| `bmc-canvas-clarity-and-iteration` | `validated` | Variation logic, detecting when a team is stuck, clarity-before-depth readiness criteria. |
| `bmc-antipattern-and-misunderstanding-correction` | `validated` | Five working-method antipatterns + four client misunderstandings about the BMC's role, with direct corrective moves for each. |
| `bmc-session-facilitation-design` | `scaffold` | Session structure: starting point, fill-in order, length/team composition, evidence color-coding. |
| `bmc-canvas-diagnostic-reading` | `scaffold` | Six diagnostic rules (Hook Rule, etc.) + a four-dimension quality rubric. |
| `bmc-tool-switching-decisions` | `scaffold` | When to move to the VPC, Lean Canvas, Mission Model Canvas, or financial modeling. |
| `bmc-client-language-translation` | `scaffold` | Interpreting client phrases + the three most common conceptual misunderstandings. |

## Logical flow through the skills

```
bmc-session-facilitation-design (session design)
        │
        ▼
bmc-innovation-pattern-matching (innovation direction + patterns)
        │
        ▼
bmc-canvas-clarity-and-iteration (2-3 variants, clarity criterion)
        │
        ├──► bmc-canvas-diagnostic-reading (deeper internal analysis)
        │
        ├──► bmc-antipattern-and-misunderstanding-correction
        │     (use mid-work, when something gets stuck)
        │
        └──► bmc-tool-switching-decisions (when to move forward)

bmc-client-language-translation
   (use throughout — interpreting client language)
```

The skills are also designed to be used independently (see
`../../meta/skill_design_principles.md` — the independence test), but the
path above matches how a typical BMC engagement unfolds.

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  pattern library, source material background
cases/                       (reserved — future own, anonymised client cases)
```

## Relationship to other packs

- `business-design-frameworks` — generic, framework-independent structuring
  models. The BMC is one well-known framework among these, but this pack is
  its own specialisation area because of a broader, internally
  interdependent body of expertise (vocabulary, diagnostics, pattern
  library) — not just one structuring model among others.
- `ai-native-startup-design` — a lightweight, fast "prototype in two days"
  pack for AI-native pre-startup founders. Its `ai-buildable-prd-writing`
  skill follows BMC work in time but doesn't use the BMC itself — this pack
  produces the input that feeds it once the business model innovation has
  been done first.
- `research-commercialisation` — commercialising research-driven
  innovations; can use this pack's pattern library as one source of
  commercialisation options.

See `../../meta/maturity_levels.md` for an explanation of the maturity
levels and `../../AGENT_GUIDE.md` for how an agent should read and weigh
this pack's content.
