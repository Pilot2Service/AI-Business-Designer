---
name: ai-buildable-prd-writing
description: "Writes a PRD (Product Requirements Document) as a work order for an AI build agent — problem, vision, core features, scope boundaries, and success criteria — plus supporting documents and a build plan."
---

# AI-Buildable PRD Writing

*Status: `validated`, `source_layer: owner` — see `../../../skills_index.json` and
`../../../../meta/maturity_levels.md`.*

## Purpose

Write a PRD (Product Requirements Document) that serves as a clear work
order for an AI build agent (e.g. Lovable, Bolt, v0) — in the same way a
contractor builds from blueprints. Core principle: building is fast now,
which means building in the wrong direction is also fast. Design is what
keeps that speed pointed in the right direction. A good PRD makes
decisions; a bad PRD is a wish list that leaves the important choices for
the AI to guess.

## Based on

- The owner's AI-native Business Design workshop
  (the owner's own workshop), run 1–2 June 2026, Day 1 —
  Session 2 "Planning in the AI Era", steps 4–6 (PRD structure,
  supporting documents, build plan, handoff to the build agent).
- The workshop's core principle: the **Spec → Plan → Implement → Test**
  workflow; the PRD states *what* and *why*, not *how*.

## Method

1. **Assemble the inputs.** Vision + ICP/JTBD/Need Themes/NMB score/AI
   wedge (from the `../customer-vision-to-jtbd/SKILL.md` skill), any deep
   research background, and — if there were multiple candidate solution
   directions — the chosen MVP direction with its rationale (the RICE
   selection and MVP synthesis from
   `../rice-scoring-and-mvp-synthesis/SKILL.md`). If the solution
   direction was clear from the start and the ideation/RICE stage wasn't
   used, the `customer-vision-to-jtbd` input alone is enough.
2. **Write the PRD with five mandatory sections**
   (`../../references/prompt-library.md`, prompt 7):
   - **Problem & customer** — who this is for, and what pain it solves.
   - **Product vision** — describe the experience in the customer's own
     words.
   - **Core features** — list only the features the first version needs.
     Describe each as an outcome the user achieves ("the user can…"), not
     as a technical implementation.
   - **Scope boundaries / Out of scope** — what is DELIBERATELY not being
     built in this version. As important a section as the feature list.
   - **Success criteria** — how we'll know the prototype works.
3. **Apply MVP discipline.** Cut scope ruthlessly: one customer, one core
   job, the fewest features that prove the idea. An MVP spec is the same
   PRD, with scope mercilessly trimmed.
4. **Test the PRD's quality.** Does it make decisions — is it specific
   about the customer, ruthless about scope, explicit about what's left
   out? Or is it a wish list that leaves the important choices for the AI
   to guess? The latter is a sign that the design isn't finished.
5. **Write the necessary supporting documents:**
   - **Brand style & personality** — tone, voice, what the product should
     feel like.
   - **Design system** — colors, fonts, basic UI components, so the
     result is coherent.
   - **Skills plan** — what ready-made, reusable capabilities (skills) to
     hand the build agent(s), instead of explaining the same workflow
     again each time.
6. **Build the production plan.** Decide the build order. Typical
   pattern: scaffolding first (login, database, empty shell), then one
   feature at a time on top of it.
7. **Hand the PRD and supporting documents to the build agent**
   (see `../ai-native-tool-stack-selection/SKILL.md` for who). Confirm the
   build plan and the main structural choices with the agent before
   building begins in earnest.

## What this skill does NOT do

- Does not include technical architecture decisions or specific
  technology choices — the PRD states WHAT and WHY, not HOW; technical
  implementation is left to the build phase and the build agent.
- Does not guarantee the prototype's success — a good PRD reduces the
  risk of building in the wrong direction, it doesn't remove it.
- Does not replace the `business-case-builder` or
  `requirements-and-scope-framing` skills in the `business-case-and-
  analysis` pack for a bigger business justification requiring funding or
  formal organizational approval — this is a lightweight, fast spec for
  building one prototype on a week's timeline.

## Continue from here

- Preceding skill in this pack: `../customer-vision-to-jtbd/SKILL.md`,
  possibly `../ai-differentiator-solution-ideation/SKILL.md` and
  `../rice-scoring-and-mvp-synthesis/SKILL.md` (if multiple solution
  directions were weighed before this).
- Related skill in this pack: `../ai-native-tool-stack-selection/SKILL.md`
  — who the PRD is handed to for building. If the MVP is a
  conversational/agentic product, see also
  `../ai-native-conversational-os-design/SKILL.md` for deepening the
  PRD's "Core Features" section.
- Related skill in another pack:
  `../../../../opportunity-recognition/skills/opportunity-brief-writing/SKILL.md`,
  `../../../../business-case-and-analysis/skills/requirements-and-scope-framing/SKILL.md`
- The pack's shared guardrails: `../../CLAUDE.md`

## References

- `../../references/prompt-library.md` — prompt 7 + PRD checklist
- `../../references/workshop-source.md` — source information
- `../../CLAUDE.md` — the pack's shared guardrails
