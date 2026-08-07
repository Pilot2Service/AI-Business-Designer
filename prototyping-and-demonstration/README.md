# Prototyping & Demonstration

How an AI consultant quickly builds a working concept, frames it correctly
for the customer, delivers it convincingly, and ties the result back into a
business case and ROI calculation. Answers the question "how do we make an
opportunity concrete and credible" — complementing the `opportunity-recognition`
and `ai-strategy-and-governance` packs' "what opportunity is this" question
and the `business-case-and-analysis` pack's "is this economically worth it"
question.

## Skills in this pack

| Skill | Description |
|---|---|
| `opportunity-visioning-with-pr-faq` | Communicates and shows an AI opportunity using Amazon's Working Backwards / PR-FAQ method before anything has been built. |
| `rapid-prototype-and-vibe-coding-craft` | Builds a fast-enough, credible-enough working prototype using AI-assisted coding ("vibe coding") — the right fidelity level, a tight iteration cycle, known risks. |
| `demo-framing-and-expectation-setting` | Frames the demo/PoC with the right term (PoC vs. Pilot vs. MVP) and a "proves/doesn't prove" pair before presenting it — prevents over-interpretation and "pilot purgatory". |
| `demo-delivery-and-storytelling` | Builds and delivers the demo using the Great Demo! methodology (Situation Slide, critical business issue, "do the last thing first"). |
| `demo-to-business-case-bridge` | Translates demo/PoC results into business-case-ready ROI inputs — technical performance vs. business impact, making the assumption chain visible, checking that the ROI mechanism fits the customer's organization. |

All `maturity: scaffold` — see [`../skills_index.json`](../skills_index.json)
for current maturity (maturity isn't tracked in the frontmatter — see
[`../meta/frontmatter_schema.md`](../meta/frontmatter_schema.md)).

## Logical flow through the skills

```
opportunity-visioning-with-pr-faq   (optional: put the vision into words before code)
              │
              ▼
rapid-prototype-and-vibe-coding-craft   (build a narrow, hypothesis-proving proto)
              │
              ▼
demo-framing-and-expectation-setting    (name it PoC/Pilot/MVP, "proves/doesn't prove")
              │
              ▼
demo-delivery-and-storytelling          (Great Demo! delivery)
              │
              ▼
demo-to-business-case-bridge            (make the assumption chain visible → ROI inputs)
              │
              ▼
   business-case-and-analysis/business-case-builder, roi-npv-sensitivity-model
```

`opportunity-visioning-with-pr-faq` is an optional first step — use it when
the vision isn't yet clear, or when prototyping isn't yet feasible or
worthwhile. `demo-framing-and-expectation-setting` should always be done
BEFORE the demo, not after.

## Relationship to other packs

- **`ai-strategy-and-governance/ai-use-case-feasibility-and-poc-scoping`** —
  defines the TECHNICAL boundaries of a PoC before prototyping. This pack's
  `demo-framing-and-expectation-setting` frames that same scoping for
  CUSTOMER COMMUNICATION — a different question, use both together.
- **`change-and-communication/executive-narrative-and-storyline`** —
  translates analysis into an executive narrative more generally. This
  pack's `demo-delivery-and-storytelling` and `opportunity-visioning-with-pr-faq`
  are its more specialized applications to a demo/visioning situation.
- **`business-case-and-analysis/business-case-builder` and
  `roi-npv-sensitivity-model`** — receive the validated inputs produced by
  this pack's `demo-to-business-case-bridge` skill.
- **`opportunity-recognition/pattern-and-analogy-connector` and
  `ai-strategy-and-governance/ai-capability-pattern-matching`** —
  produce the raw list of opportunities that this pack makes concrete and
  credible.

## Anchored in

- Cohan, Peter E. — *Great Demo! How To Create And Execute Stunning
  Software Demonstrations* and Paul Pearce's "Great Demo! Five Imperatives"
  application (Discovery, Demo Prep, Demo Delivery, Documentation, Debrief;
  Situation Slide, Critical Business Issue, "do the last thing first")
- Bryar, Colin & Carr, Bill — *Working Backwards: Insights, Stories, and
  Secrets from Inside Amazon* (2021) — the Working Backwards method and
  the PR-FAQ document
- Vibe coding best practices 2026 (synthesis of multiple sources) —
  tool selection, iteration cycle, PRD-first principle, known risks
- Prototype fidelity research (UX research tradition) — when to use
  low- vs. high-fidelity prototypes
- The PoC vs. Pilot vs. MVP distinction (synthesis of multiple 2026 sources)
- "Pilot purgatory" research (McKinsey/BCG/IDC/MIT syntheses) —
  why a large share of enterprise AI pilots never reach production
- Research synthesis (2026) on translating demo/PoC results into
  business language

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  background material, sources, own templates (to be filled in)
```

See [`../meta/maturity_levels.md`](../meta/maturity_levels.md) for what the
maturity levels mean, and
[`../AGENT_GUIDE.md`](../AGENT_GUIDE.md) for how an agent should read and
weight this pack's content.
