---
status: validated
owner_input_needed: false
last_reviewed: 2026-08-06
---

# AI-Native Startup Design

How to design an AI-native product/business from the ground up in the age
of AI: from a new mindset and AI opportunity identification through
customer understanding, need-theme scoring, and solution ideation to a
RICE-selected MVP, a buildable PRD, a conversational UI architecture,
closed-loop process design, and choosing the right AI tool stack.

## Status

This pack combines two sources the owner has applied in practice:

1. The **AI-native Business Design** workshop for pre-startup founders
   (the owner's own service, run for multiple participants
   1–2 June 2026,
   [owner's private material](https://owner's private material))
   — see `references/workshop-source.md`. Skills built on this are
   `maturity: validated` (multi-participant session).
2. The **external "AI-first SaaS Product" workshop** — a methodology the
   owner has applied to one own case (the owner's own "Decision Coach" MVP
   service) — see `references/ai-first-saas-workshop-source.md` and the
   worked example `cases/ai-decision-coach-mvp-case.md`. Skills built and
   deepened on this basis are `maturity: draft` (applied once, not yet
   broadly validated across multiple cases) — see the table below.

All skills are `source_layer: owner` (see `../../skills_index.json`).

## Skills in this pack

| Skill | Level | Description |
|---|---|---|
| `ai-native-opportunity-scan` | `validated` | Finds and prioritizes agentic/closed-loop-level AI opportunities in your own startup case via a prompt chain. |
| `customer-vision-to-jtbd` | `validated` | Structures a free-form vision into an ICP, a verb-driven Jobs-To-Be-Done analysis, 5+2 need themes, a 5-criteria NMB+AI-advantage score, and selects an AI differentiator need (AI wedge). |
| `ai-differentiator-solution-ideation` | `draft` | Ideates 3 distinct AI-native solution directions for the chosen AI wedge through three lenses. |
| `rice-scoring-and-mvp-synthesis` | `draft` | Scores solution directions with the RICE model, selects the MVP, and writes the MVP definition, a positioning statement, and "why we win" claims. |
| `ai-buildable-prd-writing` | `validated` | Writes the PRD as a work order for an AI build agent, plus supporting documents and a build plan. |
| `ai-native-conversational-os-design` | `draft` | Designs the conversational UI architecture for an AI-native product (Intent → Strategy Cards → Clarification → Output Cards → Mission → Agent Execution) and 5 AI-first product principles. |
| `closed-loop-process-and-human-oversight-design` | `validated` | Structures processes as open/closed loops and decides the level of human oversight (in/on/outside-the-loop). |
| `ai-native-tool-stack-selection` | `validated` | Selects the smallest workable AI-native tool stack using a 12-category decision tree. |

## Anchored in

- The owner's AI-native Business Design workshop (
  the owner's own service, 1–2 June 2026) — see
  `references/workshop-source.md`
- The external AI-first SaaS Product workshop's methodology, applied to
  the owner's own case — see `references/ai-first-saas-workshop-source.md`
  and `cases/ai-decision-coach-mvp-case.md`
- Ideal Customer Profile (ICP) and Jobs-To-Be-Done (JTBD) product-strategy
  frameworks, as applied by the workshops
- The RICE prioritization model (generally known, not the owner's own)
- Open loop / closed loop systems thinking and the human-in/on/
  outside-the-loop model, as presented by the workshop in the AI agent
  context

## Logical flow of the skills

```
ai-native-opportunity-scan
        │
        ▼
customer-vision-to-jtbd  (ICP → JTBD → Need Themes → NMB scoring → AI wedge)
        │
        ▼
ai-differentiator-solution-ideation  (3 solution directions for the chosen wedge)
        │
        ▼
rice-scoring-and-mvp-synthesis  (RICE selection → MVP definition → positioning)
        │
        ▼
ai-buildable-prd-writing ──► ai-native-tool-stack-selection
        │                           (who the PRD is handed to)
        ▼
ai-native-conversational-os-design
   (if the MVP is a conversational/agentic product —
    deepens the PRD's Core Features section)
        │
        ▼
closed-loop-process-and-human-oversight-design
   (deepens the agentic-ness identification that
    opportunity-scan already used in stage 1, and
    the oversight level for the Agent Execution stage)
```

The skills are also designed to be used independently (see
`../../meta/skill_design_principles.md` — the independence test). If the
solution direction is clear from the start, you can jump straight from
`customer-vision-to-jtbd` to `ai-buildable-prd-writing`, skipping the
ideation/RICE stage — the ideation chain is meant for situations where
there are genuinely multiple competing solution directions to weigh.

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   a single skill (name + description frontmatter)
references/                  prompt library, tool category map, source info
cases/                       worked example: ai-decision-coach-mvp-case.md
                              (add more of your own anonymized cases here going forward)
```

## Relationship to other packs

This pack is deliberately lightweight and fast ("prototype in two days"),
unlike:

- `ai-strategy-and-governance` — a broader, systematic assessment of an
  existing company's AI portfolio, build/buy/partner decisions, and
  governance. `ai-native-opportunity-scan` references its
  `ai-opportunity-portfolio` skill, but is lighter and faster.
- `business-case-and-analysis` — a more formal business justification
  requiring funding or organizational approval.
  `ai-buildable-prd-writing` is a lightweight spec for a one-week
  prototype, not a replacement for the `business-case-builder` skill in a
  bigger decision.
- `business-design-frameworks` — generic, AI-independent structuring
  models (layers, value chain, categories, strategy maps).
  `closed-loop-process-and-human-oversight-design` is a structuring
  approach from the same family, but tied to the AI agent context.

See `../../meta/maturity_levels.md` for an explanation of maturity levels
and `../../AGENT_GUIDE.md` for how an agent should read and weigh this
pack's content.
