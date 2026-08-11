# Human-AI Collaboration Design

How an AI Business Designer moves human-AI oversight from a vague promise
("a human checks it") to an intentional, accountable architecture: what
maturity level a process's human oversight is actually at (not the level
it's assumed to be at), how the AI should behave in tone and under
pressure, how its outputs stay grounded against a source of truth instead
of agreeably wrong, whether the human-AI partnership is actually working
over time, and how to protect the pipeline that produces the next
generation of experts able to catch the AI's mistakes at all. Answers the
question "is this AI process actually supervised the way we think it is,
and will it stay that way" — the accountability layer underneath the
opportunities identified in `ai-strategy-and-governance` and the products
designed in `specialisation-packs/ai-native-startup-design`.

## Skills in this pack

| Skill | Description |
|---|---|
| `hitl-maturity-and-confidence-routing` | Classifies a process against a four-level HITL maturity model (Smoke-and-Mirrors → Reactive → Intentionally Designed → Collaborative Intelligence) and designs a confidence-score routing table with a named accountable calibration owner. |
| `ai-behavioral-specification-design` | Specifies an AI's sentiment, tone, and precision (temperature) as an explicit design artifact — a "Behavioral Document" — including how it redirects rather than goes silent when it hits a guardrail. |
| `ai-accuracy-guardrails-and-grounding-design` | Designs absolute guardrails and grounds AI outputs against a named source of truth to counter sycophancy, weighed against "tokonomics" — the cost/latency price of every added guardrail instruction. |
| `hitl-override-metrics-and-feedback-audit` | Audits a human-AI partnership's health with override-rate and override-accuracy metrics, and designs the feedback loop that turns human corrections into model improvement (the AI Flywheel). |
| `expert-agency-and-apprenticeship-protection` | Draws the boundary around decisions AI may never make autonomously, and protects the pipeline that trains junior experts against being silently automated away. |

## Logical flow of the skills

```
hitl-maturity-and-confidence-routing   (where is oversight actually at, and where should work route?)
              │
    ┌─────────┼─────────────────┐
    ▼         ▼                 ▼
ai-behavioral-  ai-accuracy-      expert-agency-and-
specification-  guardrails-and-   apprenticeship-
design          grounding-design  protection
(how it should  (how it stays     (what it must never
 sound & flex)   honest)           decide alone)
    │         │
    └────┬────┘
         ▼
hitl-override-metrics-and-feedback-audit
   (is the whole partnership actually
    working — measured, not assumed)
```

The skills are also designed to be usable independently (see
`../meta/skill_design_principles.md` — the independence test), but the
flow above matches a typical sequence: first place the process on the
maturity model and design its routing, then specify how the AI behaves and
stays grounded, then draw the hard boundary around what it may never
decide, and throughout — audit whether it's actually working with real
usage data rather than a one-time design decision.

## Relationship to other packs

- **`specialisation-packs/ai-native-startup-design/closed-loop-process-and-human-oversight-design`**
  — the earlier, simpler three-tier model (in/on/outside-the-loop) for
  early-stage process design. This pack's `hitl-maturity-and-confidence-routing`
  is the deeper, operational layer to reach for once the process is live —
  not a replacement.
- **`ai-strategy-and-governance/ai-output-curation-and-quality-control`**
  — applies the same simple three-tier model specifically to content
  quality. This pack's `hitl-override-metrics-and-feedback-audit` deepens
  its step 7 ("track quality over time") into a full audit methodology,
  and `ai-behavioral-specification-design` gives its curators an explicit
  tone/guardrail spec to check against instead of a subjective "feels
  right."
- **`ai-strategy-and-governance/responsible-ai-and-governance-check`** — a
  legal/regulatory risk lens (EU AI Act tiers). This pack's skills are
  complementary: responsible-AI governance asks "is this legally and
  ethically allowed," this pack asks "is the human-AI working relationship
  itself sound, day to day."
- **`ai-strategy-and-governance/task-level-decomposition-and-automation-fit`**
  — its SML error-tolerance criterion (deterministic vs. probabilistic
  tasks) is the upstream task-classification input that this pack's
  routing, behavioral-spec, and agency-boundary skills build on.
- **`prototyping-and-demonstration/rapid-prototype-and-vibe-coding-craft`**
  — a prototype that passes still needs a designed human-oversight model
  before production; this pack picks up exactly where that skill's
  fidelity-level prototype leaves off.

## Anchored in

- Su Belagodu — public HITL commentary and advisory work (a four-level
  HITL maturity model, confidence-score routing, override-rate
  diagnostics). Some specific quotes attributed to her in the source
  material could not be independently verified word-for-word — see each
  skill's "Anchored in research" section for exactly what's confirmed vs.
  caveated.
- Databricks engineering blog, "What is Human-in-the-Loop (HITL)?" — an
  independent industry anchor for the general HITL maturity concept,
  beyond a single named source.
- Named 2026 AI product-design practitioners (Vitaly Friedman, Jasmine
  Orange, Joshua Ebner) — real, identifiable people whose general work
  area matches the attributed concepts; specific quotes flagged as
  unconfirmed where that's the case.
- Independent 2026 discourse on AI's "apprenticeship risk" to junior
  expertise pipelines (American Recruiting & Consulting Group, SPARK6,
  peer-reviewed novice-risk research) — used in place of an unverifiable
  named attribution ("Curt Strovink") that could not be confirmed as an
  identifiable person.
- Atlassian's public adoption of the Agent Skills / SKILL.md open standard
  and its own design-system AI skills — an independently verifiable case
  for the skills-file-as-expertise-interface concept in
  `expert-agency-and-apprenticeship-protection`.
- The human-in/on/outside-the-loop model already used elsewhere in this
  repo (see "Relationship to other packs" above) as this pack's simpler
  predecessor layer.

Full sourcing and grounding-strength notes, including everything that was
excluded from this pack and why:
[`references/hitl-partnership-heuristics-research.md`](references/hitl-partnership-heuristics-research.md).

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  background material, sourcing notes
```

See `../meta/maturity_levels.md` for what the maturity levels mean, and
`../AGENT_GUIDE.md` for how an agent should read and weight this pack's
content.
