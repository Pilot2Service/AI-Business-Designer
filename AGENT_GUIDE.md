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

## 3. Maturity and trust — read skills_index.json, not the frontmatter

SKILL.md frontmatter contains **only** `name` and `description` (the
standard fields of the Claude Skill format). Maturity, source layer, and
whether owner input is still needed live in `skills_index.json`:

| Field | Values | What it means for the agent |
|---|---|---|
| `maturity` | `scaffold` / `draft` / `validated` / `canonical` | How much to lean on this as standalone truth |
| `source_layer` | `research` / `owner` / `derived` | `research` = public framework. `owner` = owner's validated experience, most valuable. |
| `owner_input_needed` | `true` / `false` | If `true`, the technique is still just a scaffold |

**Trust hierarchy:** `canonical` > `validated` > `draft` > `scaffold`.

## 4. What to do when a skill is `maturity: scaffold`

Most skills in this pack are at scaffold level: the structure and
anchoring are reliable, but the `[OWNER INPUT]` section doesn't yet
contain the owner's own experience.

1. Use the structure and anchoring normally.
2. Don't imagine the owner's personal experience, heuristics, or case
   examples. Say out loud that this part is missing.
3. Continue with what's available, but make the uncertainty visible.

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

- Must not fill `[OWNER INPUT]` sections with generic or imagined content
- Must not add new fields to SKILL.md frontmatter (only `name`+`description`
  are allowed)
- Must not treat `scaffold`-level content as equally authoritative as
  `validated`/`canonical`
- Must not mistake this pack for a finished answer — it's context on top of
  your own expertise
- Must not let an `agents/` subagent modify any file or make a final
  decision — they only return a findings table (see item 7)
