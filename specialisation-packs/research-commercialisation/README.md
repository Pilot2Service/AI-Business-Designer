---
status: validated
owner_input_needed: false
last_reviewed: 2026-08-04
---

# Research Commercialisation

How to turn a research result or IP into a commercialisable product, service,
or company: from opportunity recognition to IP strategy, TTO collaboration,
funding, team building, and the founder's readiness self-assessment.

## Status

This pack is built directly from the owner's published **owner's published
commercialisation guide** handbook (the owner's own service, 2025, 75 pages)
and its AFCA self-assessment tool. It is not a research-level scaffold but
content anchored in the owner's validated methodology, based on experience
from approximately 500 commercialisation projects — `source_layer: owner`,
`maturity: validated` for all skills (see `../../skills_index.json`).

## Skills in this pack

| Skill | Description |
|---|---|
| `research-opportunity-recognition` | Assess whether a research result has real commercial potential — market pull vs. technology push. |
| `spinout-vs-licensing-pathway` | Choose the commercialisation pathway: spin-out, licensing, or hybrid. |
| `ip-disclosure-and-ownership-check` | Establish IP ownership and make a timely invention disclosure. |
| `tto-engagement-strategy` | Use the Technology Transfer Office effectively, and recognise when extra support is needed. |
| `industry-specific-commercialisation-playbook` | Tailor strategy by industry: life sciences, deep tech, software, impact. |
| `funding-pathway-design` | Combine non-dilutive and dilutive funding, manage runway. |
| `commercialisation-journey-roadmap` | The full five-stage roadmap: opportunity → concept → validation → strategy → execution. |
| `founding-team-design-and-agreements` | Build a balanced founding team and a Founders' Agreement. |
| `industry-partner-engagement` | Bring industry partners on board early. |
| `academic-entrepreneur-role-choice` | Choose your own role: full-time founder, advisor, or part-time. |
| `commercialisation-readiness-check` | A mission, idea, and readiness test before starting out. |
| `founder-competence-self-assessment` | AFCA — a 10-area / 76-item self-assessment of founder readiness. |

## Anchored in

- the owner's published commercialisation guide (owner, 2025)
- AFCA — Founder's Competence Assessment (the owner's own tool), a synthesis
  of the EU's EntreComp and ResearchComp frameworks
- The handbook's own sources: see `references/sources.md`

## Logical flow of skills

```
research-opportunity-recognition
        │
        ▼
spinout-vs-licensing-pathway ──► ip-disclosure-and-ownership-check
        │                               │
        │                               ▼
        │                       tto-engagement-strategy
        │                               │
        ▼                               ▼
industry-specific-commercialisation-playbook ──► funding-pathway-design
        │
        ▼
commercialisation-journey-roadmap
        │
        ▼
founding-team-design-and-agreements ──► industry-partner-engagement
        │
        ▼
academic-entrepreneur-role-choice
        │
        ▼
commercialisation-readiness-check ──► founder-competence-self-assessment
```

The skills are also designed to be used independently (see
`../../meta/skill_design_principles.md` — the independence test), but the path
above matches the handbook's own sequence and suits a first-time user.

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  terminology, AFCA data, case studies, sources
cases/                       (reserved — future own, anonymised project cases)
```

See `../../meta/maturity_levels.md` for what the maturity levels mean, and
`../../AGENT_GUIDE.md` for how an agent should read and weight this pack's
content.
