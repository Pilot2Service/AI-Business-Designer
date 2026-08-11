# HITL & human-AI partnership heuristics — research and grounding notes

Source material for this pack: two owner-supplied documents ("Chief
Calibration: AI Business Design Heuristics and Operating Models" and "HITL
AI Design and Partnership Architecture") plus a pasted five-section
overview text ("AI's business design: strategic heuristics, operating
models, and design guidelines"), all reviewed August 2026. This document
records which items became skills, which became enhancements to existing
skills, which were excluded, and the source-verification work behind each
decision — so a reader can see exactly what's confirmed, what's
attributed-with-caveat, and what was re-grounded.

## What became this pack's five skills

The second source document is itself structured as five named
sub-documents (`HITL_Maturity_Routing.md`, `Behavioral_Mapping_Sentiment.md`,
`Accuracy_Guardrails_FactChecking.md`, `Collaboration_Metrics_Audit.md`,
`Systemic_Constraints_Agency.md`) — this mapped directly onto five skills:

| Source sub-document | Skill | Core content taken |
|---|---|---|
| HITL_Maturity_Routing.md | `hitl-maturity-and-confidence-routing` | 4-level maturity model, confidence-score routing table, Chief Calibration Officer framing, one-click override, Clippy 2.0 anti-pattern |
| Behavioral_Mapping_Sentiment.md | `ai-behavioral-specification-design` | Sentiment/tone, prompt trees, temperature vs. precision, "what would the human have done" framing |
| Accuracy_Guardrails_FactChecking.md | `ai-accuracy-guardrails-and-grounding-design` | Sycophancy risk, absolute guardrails, grounding/source-of-truth, tokonomics |
| Collaboration_Metrics_Audit.md | `hitl-override-metrics-and-feedback-audit` | Override rate (both directions), override accuracy, AI Flywheel, feedback-into-fine-tuning |
| Systemic_Constraints_Agency.md | `expert-agency-and-apprenticeship-protection` | High-stakes agency boundaries, apprenticeship risk, skills-files-as-interface |

## Source-verification results (web-checked August 2026)

| Named source | Verification result | How it's used |
|---|---|---|
| **Su Belagodu** | Real, identifiable: Managing Partner, Intellectus Advisors; former product leadership at Pegasystems, IBM, Wipro; runs a public "Humans + AI = Impact" HITL video series. Her general focus on HITL maturity and override-rate diagnostics is confirmed. The exact quotes attributed to her in the source material could not be independently located word-for-word. | Attributed with a caveat on exact quotes; the model structure itself is treated as reliably sourced. |
| **Vitaly Friedman** | Real, well-known (Smashing Magazine, "Design Patterns for AI Interfaces" 2026 course/training). The specific "AI amplifies existing weaknesses" quote attributed to him was not found verbatim. | Not used as a direct citation. The underlying claim is instead grounded in independent 2026 sources found directly: Forbes Technology Council, "AI Won't Fix Organizational Weaknesses — It Will Amplify Them" (Aug 2026), and a ScienceDirect article on AI as a "strategic amplifier" (June 2026). Used in the `ai-reshuffle-opportunity-framing` enhancement (see below), not attributed to Friedman by name. |
| **Jasmine Orange** | Real UX/experience designer (EY XD practice, conference speaker, podcast guest on AI and design). General public work matches the attributed framing; specific quotes not confirmed verbatim. | Attributed with a caveat in `ai-behavioral-specification-design`. |
| **Joshua Ebner** | Real, identifiable (LinkedIn: AI engineering & AI integration strategy). Specific quotes ("AI Flywheel," "kill mandate," "prototype reduces strategic uncertainty") not confirmed verbatim. | Attributed with a caveat in `hitl-override-metrics-and-feedback-audit` (AI Flywheel) and in the `rapid-prototype-and-vibe-coding-craft` enhancement (kill mandate). |
| **Curt Strovink** | **Not found.** No identifiable person by this name turned up in available search results. | **Attribution dropped entirely** from `expert-agency-and-apprenticeship-protection`. The "apprenticeship risk" concept is kept, re-grounded in independently confirmed 2026 sources instead: American Recruiting & Consulting Group ("AI is hollowing out the apprenticeship layer"), SPARK6 ("The Death of the Junior Analyst"), and a 2025 ScienceDirect peer-reviewed paper on novice-risk learning failures with emerging technologies. This is the same treatment this repo has previously applied to unverifiable attributions (e.g. the "Paris Thomas" two-week-rule exclusion from an earlier phase of this repo's BMC work). |
| **Ida Rimpiläinen / Topi Ahava / "CallUp AI"** | Both people are real and identifiable (Solita-affiliated, LinkedIn-verified). No public "CallUp AI" model or framework was found under that name. | **No dedicated skill built on this.** Folded as a light, ungrounded-attribution enhancement into `change-and-communication/workshop-and-facilitation-design` (see below) without naming the model, the people, or their employer — consistent with this repo's earlier decision to genericize other single-company-sourced material. |
| **Alja Lepistö, Yasemin Cenberoglu** | Not found in available search results. | No dedicated skill built on this material either. The underlying concepts ("slowing down to speed up," "prompt trees" replacing static service blueprints) are independently well documented in 2026 UX/product literature (e.g. Smashing Magazine, "Designing With Uncertainty: How AI Supercharges Probabilistic Thinking," June 2026) and are used in `ai-behavioral-specification-design` with the named-person attribution flagged as unconfirmed rather than dropped, since the underlying claim (not just a tangential one) is central to that skill. |
| **Whoop example** (absolute topical guardrails), **IMDb example** (grounding), **"Project VIN" example** (hallucination case) | Not independently verified against the named companies' own documentation. "Project VIN" in particular is too vague in the source material to use meaningfully (no confirmable referent). | Whoop and IMDb kept as illustrative examples of a pattern, explicitly flagged as unverified citations in `ai-accuracy-guardrails-and-grounding-design`. "Project VIN" dropped entirely — insufficient detail to responsibly use even as an illustration. |
| **Atlassian skills-file example** | Independently confirmed and *more specific than the source material claimed*: Atlassian is a real, current adopter of the open Agent Skills / SKILL.md standard (agentskills.io, opened December 2025) and has published its own design-system AI skills (an "ADS MCP server" plus detailed skill files) that its own team reports reduced AI token costs and improved output accuracy. | Used directly in `expert-agency-and-apprenticeship-protection` with the stronger, verified detail in place of the vaguer original claim. |

## Enhancements applied to existing skills (not new skills)

Four items from the source material overlapped enough with existing
skills that a new skill would have duplicated territory rather than filled
a gap. Each was added as a Method step or "Anchored in research" addition
instead:

- **`ai-strategy-and-governance/skills/task-level-decomposition-and-automation-fit`**
  — added the deterministic/probabilistic worked example table (billing
  logic and access permissions as deterministic; content summarization and
  creative ideation as probabilistic) to the existing "Error tolerance" SML
  criterion.
- **`prototyping-and-demonstration/skills/rapid-prototype-and-vibe-coding-craft`**
  — added the "kill mandate" principle (a prototyping team needs explicit
  authority to kill a failing experiment early) and the framing "a
  prototype is a tool to reduce strategic uncertainty, not a pre-version of
  the product," attributed to Joshua Ebner with the same verification
  caveat as above; sharpened the existing high-fidelity-prototype-trap
  guidance with the "stakeholders debating button colors instead of
  strategic value" framing.
- **`ai-strategy-and-governance/skills/ai-reshuffle-opportunity-framing`**
  — added a caution that AI amplifies an organization's existing
  weaknesses rather than fixing them, grounded in the independent Forbes
  Technology Council and ScienceDirect sources found above rather than in
  the unverified Vitaly Friedman attribution.
- **`change-and-communication/skills/workshop-and-facilitation-design`** —
  added a brief note on a real-time, cross-disciplinary "everyone working
  in the same room or shared digital space" collaboration format as an
  alternative to a staged, scheduled workshop when the pace of AI
  prototyping calls for it — without naming a specific model, company, or
  the two individuals from the unverified source, per the note above.

## Deliberately excluded — no action taken

- **SMART four-axis prioritization** (Feasibility / Desirability /
  Viability / Sustainability) from the source material's Section 1. Not
  built as a skill and not folded into an enhancement:
  `ai-strategy-and-governance/skills/ai-opportunity-portfolio`'s existing
  5-dimensional scoring model already covers this ground more rigorously
  (including an explicit regulatory/EU AI Act dimension), and adding a
  second, competing prioritization framework into the pack risked creating
  confusion about which one a user should reach for.
- **"Slowing down to speed up" discovery-phase heuristic** (stakeholder
  discussions, context analysis, assumption validation before a large
  investment) from Section 1. Judged to be sufficiently covered in spirit
  by the existing `strategic-thinking` pack's issue-tree work and
  `ai-strategy-and-governance/skills/ai-discovery-engagement-design`; no
  new skill or enhancement was made for this specifically.
- **"Above the algorithm" positioning and value-shift-to-bottleneck**
  (Section 4 of the pasted overview text) — already substantively covered
  by `ai-strategy-and-governance/skills/ai-reshuffle-opportunity-framing`
  and `ai-strategy-and-governance/skills/ai-output-curation-and-quality-control`'s
  creator-to-curator framing, both added to this repo in an earlier phase
  grounded in Sangeet Paul Choudary's *Reshuffle*. No further action
  needed beyond the weakness-amplification caution noted above.

## A note on this pack's relationship to two earlier skills

This repo already had two skills touching human-AI oversight before this
pack existed:
`specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design`
and
`ai-strategy-and-governance/skills/ai-output-curation-and-quality-control`.
Both use a simpler three-tier in/on/outside-the-loop model. Neither was
superseded, rewritten, or deleted — this pack's four-level maturity model
with confidence-score routing is materially more operationally specific
(named accountable owner, measured override-rate thresholds in both
directions, a designed feedback loop), and is positioned in both this
pack's own `CLAUDE.md` and in cross-references from the two earlier skills
as the deeper layer to reach for once a process has gone live and needs
real operational governance — not a replacement for the earlier, lighter
model at the design stage.
