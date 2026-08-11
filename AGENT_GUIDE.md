---
id: meta.agent_guide.001
title: Agent Guide
status: canonical
---

# Agent Guide — AI Business Designer Skills

This file is written for **agents** (Claude Code, Cowork, other
skill-compatible agents) that use this pack as context for a business
analysis, strategy, or AI-strategy task. Pack-specific `CLAUDE.md` files
complement this with skill-specific guardrails — read both.

## 1. What this is

A skills pack, not a finished answer. Every SKILL.md teaches one precisely
scoped technique and states which academic or professional framework it's
anchored to.

## 2. Two levels of guidance

1. **`<pack>/skills/<skill>/SKILL.md`** — what to do, step by step.
   Narrow, task-specific.
2. **`<pack>/CLAUDE.md`** — the pack's shared guardrails: disclaimer, no
   fabricated numbers, premise check, making maturity visible. Always read
   before running a skill.

## 3. Maturity — an internal working note, not a public disclaimer

SKILL.md frontmatter contains **only** `name` and `description` (the
standard fields of the Claude Skill format). `skills_index.json` privately
tracks `maturity`, `source_layer`, and `owner_input_needed` — this is the
owner's own refinement and backlog tool, not a completeness rating to
recite to the person you're helping. Every skill in this pack, at every
maturity level, is grounded in either the owner's own consulting practice
or a named, professionally used framework (see each skill's "Anchored in
research" section) — none of it is speculative or invented.

| Field | Values | What it means internally |
|---|---|---|
| `maturity` | `scaffold` / `draft` / `validated` / `canonical` | Whether the owner has personally run this specific technique through a real engagement yet |
| `source_layer` | `research` / `owner` / `derived` | `research` = built from a named public framework. `owner` = converted from the owner's own field-tested experience |
| `owner_input_needed` | `true` / `false` | Whether the skill's "Refinement notes" section still has open prompts |

## 4. Using a skill regardless of its internal maturity tag

Use the technique as written — it's real, usable methodology at every
maturity level. Don't fabricate the owner's personal case examples, war
stories, or heuristics that aren't actually in the skill file — if a
"Refinement notes" section is still open, work with what the skill
actually contains rather than inventing content to fill the gap. If the
person you're helping specifically asks how validated a technique is,
check `skills_index.json` and answer honestly — but don't volunteer a
maturity disclaimer unprompted, as if the technique itself were
incomplete.

## 5. How to retrieve from this pack

Don't load the whole repo at once. Use `skills_index.json` to select the
2-5 most relevant skills. Read that pack's `CLAUDE.md` at the same time.

## 6. Task-based navigation

| Task type | Primary pack |
|---|---|
| Identifying/assessing a business opportunity | `opportunity-recognition` |
| ROI/risk case for an investment | `business-case-and-analysis` |
| Prioritizing AI use cases | `ai-strategy-and-governance` |
| Leadership presentation / change communication | `change-and-communication` |
| Structuring a larger problem | `strategic-thinking` |
| Multi-step task | `playbooks/` — a ready-made skill chain |

## 7. Delegatable agents — a second opinion before a decision

Four packs include their own `agents/` folder (`business-case-and-analysis`,
`opportunity-recognition`, `business-design-frameworks`,
`ai-strategy-and-governance`). These are **read-only** subagents invoked
via the Task tool, not SKILL.md techniques: they don't build an analysis
from scratch — they review/challenge an analysis that's already been done,
before it moves into a decision (see `meta/shared-guardrails.md` item 5
and each agent's own `.md`). Use them once a skill's output is assembled
but before it's presented to a human for approval — they don't replace
human approval, they improve what the human sees before deciding.

## 8. What an agent must not do

- Must not fill a skill's "Refinement notes" section with generic or
  imagined content, or invent owner experience that isn't actually there
- Must not add new fields to SKILL.md frontmatter (only `name`+`description`
  are allowed)
- Must not volunteer an unprompted maturity disclaimer that undersells a
  skill's actual, usable content — every skill is real methodology, not a
  rough draft
- Must not mistake this pack for a finished answer — it's context on top of
  your own expertise
- Must not let an `agents/` subagent modify any file or make a final
  decision — they only return a findings table (see item 7)
