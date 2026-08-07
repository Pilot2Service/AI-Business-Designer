# AI Strategy & Governance

Identifying, prioritizing, and responsibly adopting AI opportunities in a
business.

## Skills in this pack

| Skill | Description |
|---|---|
| `task-level-decomposition-and-automation-fit` | Breaks roles/processes down to task level (People Path + Process Path) and classifies every task as Automate/Augment/Human-Only using SML criteria. |
| `ai-capability-pattern-matching` | Uses a library of 13 AI capability patterns (research-based, cross-checked against two independent industry AI use-case reports) to pose diagnostic questions — a top-down alternative to task-level decomposition for assembling a raw list. |
| `ai-opportunity-portfolio` | Identifies, scores (5D model), and prioritizes AI use cases with a 2x2 matrix; separates incremental and transformative (Value Play taxonomy) opportunities. |
| `ai-native-business-model-canvas` | Designs the transition from an AI-enhanced business to an AI-native business model using an extended Business Model Canvas (VP, data moat, Human-AI Interaction Model, compute costs). |
| `ai-use-case-feasibility-and-poc-scoping` | Determines the technical boundary conditions of an AI use case and scopes the PoC phase. |
| `responsible-ai-and-governance-check` | Checks the regulatory, risk, and ethics dimensions of an AI initiative. Deeper EU AI Act compliance analysis requires separate regulatory expertise. |
| `build-vs-buy-vs-partner-ai` | Structures the decision to build in-house, buy off a platform, or partner on an AI solution. |
| `ai-capability-roadmap` | Builds the organization's AI capability map and roadmap across three horizons (0–6/6–18/18–36 months) + ATOM/Readiness Scorecard. |
| `ai-discovery-engagement-design` | Productizes the entire discovery process into a paid/internal discovery engagement — phases, service products, deliverables. |
| `shadow-ai-response-and-safe-adoption` | Identifies unauthorized AI tool usage (Shadow AI) and replaces it with a safe, ROI-justified official solution. |
| `ai-output-curation-and-quality-control` | Designs a quality-control and curation process for AI outputs — the shift from creator to curator. |

All `maturity: scaffold` — see `../skills_index.json` for current maturity
(maturity isn't tracked in the frontmatter, see
`../meta/frontmatter_schema.md`).

## Anchored in

- EU AI Act (Regulation (EU) 2024/1689)
- LinkedIn 2026 — Risk & Compliance Management
- LinkedIn Skills on the Rise 2026 — AI Business Strategy
- Perplexity research — PoC scoping through to productionization
- Perplexity research — roadmaps and business capability maps
- Market research: open "Senior AI Business Designer"-type job postings
- `strategic-options-evaluation` logic applied to AI decisions
- A research report supplied by the user, "AI Business Designer in the Age
  of AI" (2026) — AI-fit triage, the data flywheel, the AI-native
  Business Model Canvas, Shadow AI, and curation and quality control of
  AI outputs
- Research digest "Methods, Frameworks, and Competencies for Identifying
  AI Opportunities and Capacity in Business" (2026) — SML/Dual
  Decomposition task breakdown, process/task mining, the 5-dimensional
  scoring model, the 2x2 prioritization matrix, the Value Play
  taxonomy, the Deploy-Reshape-Invent taxonomy, the three-horizon
  roadmap, the ATOM/Readiness Scorecard, and the structure and
  productization of discovery engagements (a synthesis of several
  industry AI capability reports and Brynjolfsson & Mitchell research)
- General "Shadow IT" literature and practice, extended to the context
  of AI tools
- Industry-specific AI use-case report (2026 edition) — 130 AI use
  cases across six industries, a responsible-AI risk framework. 81
  text-extracted and verified cases were used as the basis for
  `references/ai-capability-pattern-library.md`.
- A second, independent AI use-case digest (63 use cases, 16
  functions) — used as a cross-check for the pattern library

## Logical flow of the skills

```
task-level-decomposition-and-automation-fit    ai-capability-pattern-matching
   (bottom-up: task-level raw list)          (top-down: pattern library's
        │                                     diagnostic questions)
        └──────────────────┬──────────────────────────┘
                            ▼
ai-opportunity-portfolio  (5D scoring → 2x2 matrix → prioritized backlog)
        │
        ├──► ai-native-business-model-canvas  (if transformative)
        ├──► ai-use-case-feasibility-and-poc-scoping  (technical validation)
        └──► ai-capability-roadmap  (Horizon 1/2/3 scheduling)
                    │
                    ▼
        responsible-ai-and-governance-check, build-vs-buy-vs-partner-ai
                    │
                    ▼
        shadow-ai-response-and-safe-adoption, ai-output-curation-and-quality-control
             (post-adoption maintenance and quality control)
```

`ai-discovery-engagement-design` is this flow's "meta-skill" — it
structures the entire chain above into a single scheduled, deliverable
consulting engagement, for when the discovery process is run as a formal
project rather than as ad hoc analysis.

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  background material, sources, own templates (to be filled in)
```

See `../meta/maturity_levels.md` for what the maturity levels mean, and
`../AGENT_GUIDE.md` for how an agent should read and weight this pack's
content.
