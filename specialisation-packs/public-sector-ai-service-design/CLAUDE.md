# Public Sector AI Service Design — shared guardrails

The general guardrails (disclaimer, no invented figures, premise checking,
the principle of keeping maturity as an internal note) are collected in one
place: **see `../../meta/shared-guardrails.md` — read it first.** This file
contains only what's genuinely pack-specific here.

---

## This pack is a lens, not a rebuild

Every skill in this pack assumes the user already has (or is separately
using) the relevant core-pack skill — `ai-opportunity-portfolio`,
`business-case-builder`, `stakeholder-analysis-and-raci`,
`responsible-ai-and-governance-check`. Don't re-derive those skills'
methods from scratch inside a skill in this pack; reference them and add
only the public-sector-specific delta. If a user's question is actually
generic AI-strategy or business-case work with no public-sector-specific
angle, point them to the relevant core pack instead of stretching a skill
in this pack to cover it.

## Not legal or procurement advice

`ps-procurement-and-public-funding-navigation` and
`ps-regulatory-and-ethical-guardrails-for-public-ai` are **awareness and
triage** skills — they help a user recognize when a question has crossed
into procurement-law, funding-compliance, or AI-regulation territory that
needs a specialist. They do not answer procurement-law or regulatory
questions themselves, and don't cite specific national or EU legal
provisions as if the skill were qualified to give that advice. If the user
needs an actual legal or regulatory answer (e.g. Finnish procurement law,
EU AI Act classification), say so explicitly and suggest they use a
dedicated legal resource — don't improvise a citation.

## Source discipline for the public-sector-specific material

The public-sector-specific framing in this pack (most directly,
`ps-decision-readiness-and-public-communication`'s six-element model) is
adapted from the owner's own commercialisation methodology for public
sector pilots — a separate, commercially licensed product (see
`references/source-notes.md`). It is rewritten here as transferable
method and principle, not reproduced from the source workbook's exact
questions, task lists, or worked examples. Don't reconstruct the
source's step-by-step workbook content (20 planning modules, 3-sprint
project model, deliverable templates) inside this pack or any skill in
it — that is out of scope by design, not an oversight.

## Shared standards

See `../../meta/frontmatter_schema.md` (what's allowed in a SKILL.md
frontmatter) and `../../meta/skill_design_principles.md` (what a good
skill in this repo needs to pass).
