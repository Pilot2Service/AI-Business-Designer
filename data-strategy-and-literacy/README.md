# Data Strategy & Literacy

How an AI Business Designer "reads" data: works out the true role of data
(enabler vs. strategic asset), assesses an organization's data literacy,
reads a dataset critically before it drives decisions, translates the
data/model logic into a business story, designs a Data & AI strategy
holistically, and selects the right monetization model. Answers the
question "what does the organization's data actually consist of, and how
should it be treated" — the foundation on which the AI/business decisions
of the `ai-strategy-and-governance`, `business-case-and-analysis`, and
`business-model-canvas` packs are built.

## Skills in this pack

| Skill | Description |
|---|---|
| `data-role-diagnosis` | Diagnoses whether data functions as an enabler or a strategic asset — resale, flywheel, and defensibility tests, the Offense/Defense framework. |
| `data-literacy-competency-assessment` | Assesses an organization's data literacy with a four-quadrant framework (Understanding, Acting, Engaging, Ethics), role by role. |
| `data-bias-and-quality-critical-reading` | Reads a dataset critically: bias taxonomy (selection, survivorship, historical, measurement, aggregation), vanity vs. actionable metrics. |
| `data-storytelling-and-business-translation` | Translates data/model logic into a story that drives a decision, using the Data→Information→Insight→Action ladder. |
| `data-ai-strategy-design-and-prioritization` | Designs a Data & AI strategy with a Driver Tree tool and prioritizes investments with a Data Readiness × Strategic Value matrix. |
| `data-monetization-model-selection` | Selects a direct (DaaS, Insight-as-a-Service, data exchange) or indirect (product enrichment, optimization, risk mitigation, Data Flywheel) monetization model with a decision tree. |

## Logical flow of the skills

```
data-literacy-competency-assessment   (optional starting point: where's the competency gap)
              │
              ▼
data-bias-and-quality-critical-reading   (confirm the data is trustworthy before using it)
              │
              ▼
data-role-diagnosis                      (enabler or strategic asset?)
              │
        ┌─────┴─────┐
        ▼           ▼
data-ai-strategy-   data-monetization-
design-and-         model-selection
prioritization      (if the asset role
(prioritize what     validated, choose
data/AI investment   how to monetize it)
to make now/later)
        │           │
        └─────┬─────┘
              ▼
data-storytelling-and-business-translation
   (use alongside all of the above — every
    finding needs to be translated into a
    story that drives a decision)
```

The skills are also designed to be usable independently (see
`../meta/skill_design_principles.md` — the independence test), but the path
above matches how a typical data strategy engagement usually unfolds: first
confirm competency and data trustworthiness, then diagnose the role, then
prioritize and select a model, and throughout, translate every finding into
a story that drives a decision.

## Relationship to other packs

- **`ai-strategy-and-governance/ai-opportunity-portfolio`** — receives the
  prioritized data/AI opportunities produced by this pack's
  `data-ai-strategy-design-and-prioritization` skill as input to its
  broader 5-dimension scoring (in particular the Data Readiness
  dimension).
- **`business-case-and-analysis/roi-npv-sensitivity-model`** — receives
  the model chosen by this pack's `data-monetization-model-selection`
  skill as input for the financial calculation.
- **`change-and-communication/executive-narrative-and-storyline`** —
  the general executive storyline structure that
  `data-storytelling-and-business-translation` specializes for data
  findings.
- **`specialisation-packs/business-model-canvas`** — its innovation
  pattern library's Financial Model section has data monetization
  patterns (e.g. `financial.rev.data_monetization`); this pack's
  `data-monetization-model-selection` deepens the choice behind them.
- **`strategic-thinking/hypothesis-driven-strategy`** — the same issue
  tree logic as this pack's Driver Tree tool, applied more generally to
  strategic questions.

## Anchored in

- The enabler vs. strategic asset distinction and the Data & AI Design
  Thinking tradition (Driver Tree, Agile Value Assessment, "Systems over
  Objects") — industry consulting practice, a synthesis of multiple
  sources, 2026.
- A DALI-type data literacy framework (a citizen- and professional-level
  four-quadrant data literacy model: Understanding, Acting, Engaging,
  Ethics & Privacy).
- Ackoff, Russell L. — the DIKW hierarchy (1989), applied here as a
  Data → Information → Insight → Action ladder.
- Davenport, Thomas H. & Bean, Randy — the Offense/Defense framework for
  data strategy.
- Minto, Barbara — the Pyramid Principle (1996) as the structure for data
  storytelling.
- Collins, Jim — the flywheel concept (*Good to Great*, 2001), applied to
  the data/AI context.
- The established bias taxonomy from statistics and machine learning
  (selection/survivorship/historical/measurement/aggregation bias).
- Direct and indirect data monetization models — industry consulting
  practice, a synthesis of multiple sources, 2026.

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  background material, heuristic collections
```

See `../meta/maturity_levels.md` for what the maturity levels mean, and
`../AGENT_GUIDE.md` for how an agent should read and weight this pack's
content.
