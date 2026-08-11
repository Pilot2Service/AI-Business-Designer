# Business Model Canvas

Business Model Canvas (BMC) consulting expertise brought together into one
specialisation pack: a 159-pattern innovation library for reinventing a
business model, the owner's own variation and clarity logic, detection of
antipatterns and client misunderstandings, research-based support for
session facilitation, diagnostic reading of a canvas, tool selection, and
interpreting client language — plus a set of resilience and risk-reading
heuristics that use the BMC as more than a static planning template:
pricing/economics prototyping, organizational-resistance mapping, revenue
and channel economics, operational risk scanning, and experiment design.

## Sources

This pack combines four sources:

1. **A public, machine-readable 159-pattern innovation library** — see
   `references/bmc-innovation-pattern-library.md`.
2. **The owner's own, non-public research work** — an ongoing project to
   capture BMC consulting expertise, including expert content drawn from a
   consulting interview conducted in April 2026 and a research layer
   synthesized from well-known BMC sources (Jeffries, Williams, van der
   Linden, Blank/Strategyzer, Ash Maurya). See `CLAUDE.md` and
   `references/bmc-source-material-notes.md` for the full background.
3. **A set of resilience/risk heuristics the owner collected from
   practitioner sources**, each independently grounded and selected
   against this pack's existing content — see
   `references/bmc-resilience-heuristics-research.md` for the full
   selection process, sourcing, and the heuristics deliberately left out
   (client-profile mismatch or overlap with existing skills).
4. **Two AI-native facilitation techniques** (`bmc-ai-assisted-draft-starting`,
   `bmc-ai-scaled-customer-interviewing`), selected from a second batch
   of owner-collected material together with several skills that landed
   in `ai-strategy-and-governance` instead — see
   `../../ai-strategy-and-governance/references/ai-native-reshuffle-heuristics-research.md`
   for the full selection and sourcing, including why these two
   specifically fit this pack rather than that one.

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

### Core BMC consulting skills

| Skill | Description |
|---|---|
| `bmc-innovation-pattern-matching` | Identifies 3-5 compatible innovation patterns from the 159-pattern library, using the expert's own four-part taxonomy. |
| `bmc-canvas-clarity-and-iteration` | Variation logic, detecting when a team is stuck, clarity-before-depth readiness criteria. |
| `bmc-antipattern-and-misunderstanding-correction` | Five working-method antipatterns + four client misunderstandings about the BMC's role, with direct corrective moves for each. |
| `bmc-session-facilitation-design` | Session structure: starting point, fill-in order, length/team composition, evidence color-coding. |
| `bmc-canvas-diagnostic-reading` | Seven diagnostic rules (Hook Rule, gravity/lock-in check, etc.) + a four-dimension quality rubric. |
| `bmc-tool-switching-decisions` | When to move to the VPC, Lean Canvas, Mission Model Canvas, or financial modeling. |
| `bmc-client-language-translation` | Interpreting client phrases + the three most common conceptual misunderstandings. |

### Resilience and risk heuristics

| Skill | Description |
|---|---|
| `bmc-hunting-zone-definition` | Sets a one-sentence direction (megatrend × assets × segment) before exploration starts, so BMC experiments stay bounded and comparable. |
| `bmc-economic-prototyping` | Forces pricing and unit economics into a live, testable prototype at the start of BMC work, with a willingness-to-pay test menu. |
| `bmc-revenue-quality-scoring` | Scores Revenue Streams -3 to +3 on predictability/resilience, not just size. |
| `bmc-channel-economics-check` | Puts a real CAC and payback period against every Channel, checked against actual budget and runway. |
| `bmc-antibody-and-sandbox-design` | Maps where a new model will trigger organizational resistance and designs a protected sandbox for it. |
| `bmc-operational-risk-scanning` | Reads Key Partners/Activities/Resources as a third-party access and operational risk surface. |
| `bmc-tech-level-repositioning` | Tests whether the model can win by deliberately moving up or down the technology-sophistication axis. |
| `bmc-experiment-method-selection` | Decides whether to build and test now (roughly two weeks) or use a cheaper proxy method instead. |
| `bmc-proxy-expert-validation` | Uses adjacent professionals (not the target customer directly) as a fast, cheap validation source. |
| `bmc-sensemaking-question-mapping` | Builds the canvas as open questions rather than filled-in answers, distinguishing missing-data gaps from unresolved-interpretation gaps. |
| `bmc-ai-assisted-draft-starting` | Starts a session from an AI-generated first-draft canvas and brand audit instead of a blank page — the team edits rather than generates. |
| `bmc-ai-scaled-customer-interviewing` | Uses AI-moderated interviews to run customer discovery at a scale no human team could match, then filters for outliers worth a personal follow-up. |

## Logical flow through the skills

```
bmc-hunting-zone-definition (set the direction before exploring — new)
        │
        ▼
bmc-session-facilitation-design (session design)
        │
        ▼
bmc-innovation-pattern-matching (innovation direction + patterns)
   ├──► bmc-tech-level-repositioning (a direction outside the pattern library)
        │
        ▼
bmc-canvas-clarity-and-iteration (2-3 variants, clarity criterion)
        │
        ├──► bmc-economic-prototyping (price/margin, live from minute zero)
        │        │
        │        ├──► bmc-revenue-quality-scoring (score the streams priced here)
        │        └──► bmc-channel-economics-check (CAC vs. that price/margin)
        │
        ├──► bmc-canvas-diagnostic-reading (deeper internal analysis, incl. gravity/lock-in)
        │
        ├──► bmc-operational-risk-scanning (left-side risk/access surface)
        │
        ├──► bmc-antibody-and-sandbox-design (will the client's own org kill this?)
        │
        ├──► bmc-antipattern-and-misunderstanding-correction
        │     (use mid-work, when something gets stuck)
        │
        └──► bmc-tool-switching-decisions (when to move forward)
                 │
                 ▼
        bmc-experiment-method-selection (build now, or a cheaper proxy?)

bmc-client-language-translation, bmc-sensemaking-question-mapping,
bmc-proxy-expert-validation, bmc-ai-scaled-customer-interviewing
   (use throughout — interpreting client language, framing the canvas as
   open questions, and sharpening/scaling hypothesis testing)

bmc-ai-assisted-draft-starting
   (optional, immediately before bmc-session-facilitation-design —
   start the session from an AI-generated draft instead of a blank page)
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
- `business-case-and-analysis` — `bmc-economic-prototyping` and
  `bmc-channel-economics-check` hand off to
  `roi-npv-sensitivity-model` once numbers need to move past a fast
  prototype into a full model; `bmc-operational-risk-scanning` hands off
  to `risk-matrix-and-mitigation` for formal risk scoring.
- `prototyping-and-demonstration` — `bmc-experiment-method-selection`
  hands off to `rapid-prototype-and-vibe-coding-craft` once the decision
  is to build rather than use a cheaper proxy test.
- `ai-strategy-and-governance` — `bmc-ai-assisted-draft-starting` and
  `bmc-ai-scaled-customer-interviewing` were selected from the same
  research pass as that pack's `ai-reshuffle-opportunity-framing`,
  `capability-commoditization-tracking`,
  `conways-law-ai-architecture-check`, and
  `workshop-to-agent-productization` — see that pack's
  `references/ai-native-reshuffle-heuristics-research.md` for why each
  landed where it did.

See `../../meta/maturity_levels.md` for an explanation of the maturity
levels and `../../AGENT_GUIDE.md` for how an agent should read and weigh
this pack's content.
