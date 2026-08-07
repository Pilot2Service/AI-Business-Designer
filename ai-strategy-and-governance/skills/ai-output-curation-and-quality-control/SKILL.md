---
name: ai-output-curation-and-quality-control
description: "Designs a quality-control and curation process for AI-generated content or decisions — the shift from 'creator' to 'curator': what gets checked, who checks it, and against what criteria before publication or use."
---

# AI Output Curation & Quality Control

*Status: `scaffold` — see `../../../skills_index.json` and `../../../meta/maturity_levels.md`.*

## Purpose

Designs a process for assessing, correcting, and approving AI-generated
content or decisions before use — a role in which the human no longer
produces content from scratch ("creator") but evaluates and steers the
AI's output toward an on-brand, coherent, reliable result ("curator").

## Anchored in research

- A research report supplied by the user, "AI Business Designer in the
  Age of AI" (2026) — "curation and quality control: the shift from
  creator to curator," part of the modeling and design competency
  area.
- The human-in/on/outside-the-loop model, see
  `../../../specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design/SKILL.md`
  — this skill applies the same model specifically to content/output
  quality, rather than general process design.

## Method (draft — to be expanded)

1. Define what the AI produces (text, code, image, decision
   recommendation, classification) and what it's used for — an
   internal purpose or a customer-facing one?
2. Define quality criteria before the AI starts producing: what does
   "good" mean for this output (factual accuracy, on-brand fit, tone,
   correctness, coherence)?
3. Choose the level of checking using the human-in/on/outside-the-loop
   model (see
   `../../../specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design/SKILL.md`):
   high-stakes/high-risk outputs are always checked before
   publication, lower-risk outputs can be monitored with spot checks.
4. Name the curator(s) — who owns quality, and what's their role: they
   no longer produce content from scratch, but assess, correct, and
   approve/reject the AI's output.
5. Build a checklist or rubric that the curator uses consistently — a
   subjective "feels right" doesn't scale.
6. Design a feedback loop: how the curator's corrections are fed back
   into the prompt or system so the same mistakes don't recur
   (closed-loop thinking).
7. Track quality over time: what share of AI outputs pass through
   without correction — this tells you whether the process is maturing
   toward less human oversight or not.

## What this skill does NOT do

- Doesn't assess the AI model's technical performance (e.g. accuracy/
  recall metrics) — that's a technical/data-science task; this skill
  is a business quality-assurance process.
- Doesn't remove the need for human oversight on high-risk outputs
  just because the process exists — the curation process complements,
  it doesn't replace, responsible-AI principles (see
  `../responsible-ai-and-governance-check/SKILL.md`).
- Doesn't make the final approve/reject decision for you on an
  individual output.

## [OWNER INPUT — to be completed]

This skill is a structural draft (`maturity: scaffold`). It doesn't yet
contain your own experience, heuristics, or case examples. Fill in
here:

- your own rules of thumb for when spot-check oversight is enough vs.
  when 100% checking is needed
- concrete templates (into `../../references/`, e.g. a curation
  rubric)
- reference cases / your own examples of quality control for AI
  outputs
- what this skill deliberately does *not* do (guardrails, common
  mistakes) — add to the list above

Once this section is filled in and validated in practice, update the
`maturity` field in `skills_index.json` to `draft`, `validated`, or
`canonical` (see `../../../meta/maturity_levels.md`). **Don't add new
fields to the frontmatter** — `name` and `description` are the only
ones allowed (see `../../../meta/frontmatter_schema.md`).

## Continue from here

- In this pack: `../responsible-ai-and-governance-check/SKILL.md`
- Related skill in another pack:
  `../../../specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design/SKILL.md`,
  `../../../change-and-communication/skills/workshop-and-facilitation-design/SKILL.md`
  (training the curator team).
- A ready-made skill chain for this situation: see `../../../playbooks/`
- This pack's shared guardrails: `../../CLAUDE.md`

## References

- `../../references/` — the pack's shared background material
- `../../CLAUDE.md` — the pack's shared guardrails
