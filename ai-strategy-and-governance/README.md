# AI Strategy & Governance

Identifying, prioritizing, and responsibly adopting AI opportunities in a
business.

## Skills in this pack

| Skill | Description |
|---|---|
| `ai-reshuffle-opportunity-framing` | Tests whether an AI opportunity is framed as automating an existing process or as a genuine value-chain reshuffle, before it enters scoring. |
| `task-level-decomposition-and-automation-fit` | Breaks roles/processes down to task level (People Path + Process Path) and classifies every task as Automate/Augment/Human-Only using SML criteria. |
| `ai-capability-pattern-matching` | Uses a library of 13 AI capability patterns (research-based, cross-checked against two independent industry AI use-case reports) to pose diagnostic questions — a top-down alternative to task-level decomposition for assembling a raw list. |
| `ai-opportunity-portfolio` | Identifies, scores (5D model), and prioritizes AI use cases with a 2x2 matrix; separates incremental and transformative (Value Play taxonomy) opportunities. |
| `ai-native-business-model-canvas` | Designs the transition from an AI-enhanced business to an AI-native business model using an extended Business Model Canvas (VP, data moat, Human-AI Interaction Model, compute costs). |
| `capability-commoditization-tracking` | Tracks which capabilities are commoditizing vs. becoming newly complementary under AI, and redirects investment accordingly. |
| `conways-law-ai-architecture-check` | Diagnoses whether the organization's communication structure will get mirrored in its AI system, and forces the resequencing decision (structure before build). |
| `ai-use-case-feasibility-and-poc-scoping` | Determines the technical boundary conditions of an AI use case and scopes the PoC phase. |
| `responsible-ai-and-governance-check` | Checks the regulatory, risk, and ethics dimensions of an AI initiative. Deeper EU AI Act compliance analysis requires separate regulatory expertise. |
| `build-vs-buy-vs-partner-ai` | Structures the decision to build in-house, buy off a platform, or partner on an AI solution. |
| `ai-capability-roadmap` | Builds the organization's AI capability map and roadmap across three horizons (0–6/6–18/18–36 months) + ATOM/Readiness Scorecard. |
| `ai-discovery-engagement-design` | Productizes the entire discovery process into a paid/internal discovery engagement — phases, service products, deliverables. |
| `workshop-to-agent-productization` | Converts a company's own recorded/written expert material into an interactive AI agent for Q&A and upsell, instead of leaving it static. |
| `shadow-ai-response-and-safe-adoption` | Identifies unauthorized AI tool usage (Shadow AI) and replaces it with a safe, ROI-justified official solution. |
| `ai-output-curation-and-quality-control` | Designs a quality-control and curation process for AI outputs — the shift from creator to curator. |

## Anchored in

- EU AI Act (Regulation (EU) 2024/1689)
- LinkedIn 2026 — Risk & Compliance Management
- LinkedIn Skills on the Rise 2026 — AI Business Strategy
- Perplexity research — PoC scoping through to productionization
- Anthropic product lead Dianne Penn — the "evals are the new PRDs"
  failing-transcript-to-eval-set technique, added to
  `ai-use-case-feasibility-and-poc-scoping`'s golden-test-set step
  (source video transcript supplied by the user)
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
- Sangeet Paul Choudary, *Reshuffle: Who Wins When AI Restacks the
  Knowledge Economy* (2025, 2025 Thinkers50 Strategy Award) —
  `ai-reshuffle-opportunity-framing` and
  `capability-commoditization-tracking`
- Howard Yu's LEAP thesis (IMD, 2023 Thinkers50 Strategy Award) —
  a second, independent source for `capability-commoditization-tracking`
- Conway's Law (Melvin Conway, 1967) and its active 2026 extension to
  AI system architecture — `conways-law-ai-architecture-check`
- Verified 2026 case examples (Perplexity AI, Shutterstock) used as
  worked illustrations across several skills — see
  `references/ai-native-reshuffle-heuristics-research.md` for full
  sourcing and selection notes
- Industry-specific AI use-case report (2026 edition) — 130 AI use
  cases across six industries, a responsible-AI risk framework. 81
  text-extracted and verified cases were used as the basis for
  `references/ai-capability-pattern-library.md`.
- A second, independent AI use-case digest (63 use cases, 16
  functions) — used as a cross-check for the pattern library

## Logical flow of the skills

```
ai-reshuffle-opportunity-framing  (premise check — is this automation or reshuffle?)
        │
        ▼
task-level-decomposition-and-automation-fit    ai-capability-pattern-matching
   (bottom-up: task-level raw list)          (top-down: pattern library's
        │                                     diagnostic questions)
        └──────────────────┬──────────────────────────┘
                            ▼
ai-opportunity-portfolio  (5D scoring → 2x2 matrix → prioritized backlog)
        │
        ├──► ai-native-business-model-canvas  (if transformative)
        ├──► ai-use-case-feasibility-and-poc-scoping  (technical validation)
        ├──► conways-law-ai-architecture-check  (will org structure distort this?)
        └──► ai-capability-roadmap  (Horizon 1/2/3 scheduling)
                    │
                    ▼
        responsible-ai-and-governance-check, build-vs-buy-vs-partner-ai
                    │
                    ▼
        shadow-ai-response-and-safe-adoption, ai-output-curation-and-quality-control
             (post-adoption maintenance and quality control)

capability-commoditization-tracking, workshop-to-agent-productization
   (used on a recurring cadence / opportunistically — not a single-pass step)
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
