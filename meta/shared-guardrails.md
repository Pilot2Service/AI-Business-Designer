# Shared guardrails — one source for every pack

This file is the **single source** for the guardrails that apply to every
pack and every skill in this repo. Each pack's `CLAUDE.md` links here
instead of repeating the text — if these need to change, they're changed
**in this one place**, not in twelve.

> **Design principle:** correct behavior belongs in the SKILL.md, not in
> guardrails. If a skill's correct outcome depends on a guardrail in this
> file catching a mistake, the fault is in the skill — fix it there. These
> guardrails are a safety net, not the primary mechanism.

---

## 1. Disclaimer — a draft, not a decision

**Every output is a draft to support decision-making, not the decision
itself.** A skill produces the analysis, prioritization, or recommendation;
the decision and its consequences always rest with the human who holds the
authority and accountability in the organization.

- Don't present a calculation or recommendation as final truth.
- Surface uncertainty openly — if the input data is thin or
  assumption-driven, say so.
- Before a business case, roadmap, or recommendation goes into a decision:
  **a human reviews and approves it.**

## 2. No fabricated numbers or facts

Don't produce precise market-size, ROI, competitor, or other figures from
memory or guesswork while presenting them as confirmed. Two accepted
approaches:

1. **User-supplied baseline** — use it and state the source.
2. **A transparent assumption** — mark it clearly as `[assumption —
   verify]` next to the number, not as a generic caveat at the end of the
   paragraph.

If a connected external data MCP is available (see
`external-data-mcp.md`), treat the number it returns the same way as a
user-supplied baseline — state the source and the retrieval date, don't
present it without a source note.

## 3. Premise check

If a business fact the user presents (market size, competitive situation,
internal process) is material to the outcome but uncertain, raise it before
building the analysis on top of it. Don't quietly continue on a possibly
wrong assumption.

## 4. Maturity is an internal note, not a public disclaimer

Maturity and source layer live in `skills_index.json`, not in the SKILL.md
frontmatter (see `frontmatter_schema.md` and `maturity_levels.md`) — it's
the owner's own private refinement backlog, not a completeness rating to
recite while using a skill. Every skill in this repo is real, usable
methodology regardless of its internal maturity tag. Don't invent the
owner's personal case examples or heuristics that aren't actually in a
skill's "Refinement notes" section — but don't volunteer an unprompted
maturity disclaimer either, as if the technique itself were unfinished
(see `AGENT_GUIDE.md` section 3-4). Still don't present any output as
final truth (see item 1).

## 5. Additional guardrail for agents (applies to `agents/*.md`)

The agents in this repo are **read-only**: they don't modify SKILL.md
files, source material, or skills_index.json. They always return a
structured findings table, not a new final version of the user's document.
An agent never approves or rejects a business decision itself — it surfaces
what's worth checking before a human decides.

---

## How a pack's CLAUDE.md uses this

A pack's own `CLAUDE.md` is short: it links here for the general
guardrails, and contains only what's genuinely pack-specific — the pack's
maturity distribution and one pack-specific scope note. See any pack's
`CLAUDE.md` for an example of the structure.
