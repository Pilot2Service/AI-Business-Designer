# Data Strategy & Literacy — shared guardrails

General guardrails (disclaimer, no fabricated numbers, premise-checking, making
maturity visible) are collected in one place: **see
[`../meta/shared-guardrails.md`](../meta/shared-guardrails.md) — read that first.**
This file only contains what's genuinely specific to this pack.

---

## Data is a representation of reality, not reality itself

This pack's guiding principle: **never treat given data as unquestioned
truth.** Behind every data-based claim, model, or recommendation there are:

- choices about what was collected and what wasn't (coverage gaps, missing
  groups)
- historical biases in how the data came to exist (who got served, who was
  asked, what was measured and what wasn't)
- measurement choices that shape the outcome (which variable was used as a
  proxy for what you actually wanted to know)

Before this pack's skills produce a conclusion from data, they explicitly
ask: *what's missing from this data, and whose perspective is missing from
it?* See
[`skills/data-bias-and-quality-critical-reading/SKILL.md`](skills/data-bias-and-quality-critical-reading/SKILL.md).

## Two different questions: role and value

Don't conflate **the role of data** (enabler or strategic asset —
[`skills/data-role-diagnosis/SKILL.md`](skills/data-role-diagnosis/SKILL.md))
with **the value of data** (how much this is worth in euros or competitive
advantage — the business case and portfolio skills in other packs). The
role question answers WHAT KIND of business logic data can support; the
value question answers WHETHER this is worth it right now. Both are needed,
but in a specific order: role first, then value.

## Data strategy is not data governance, and vice versa

Data governance (governance model, quality, ownership, access control) is
**defense**: it reduces risk and enables trustworthy use, but doesn't by
itself produce new business. Data strategy (what new data to acquire, how
to monetize it, what business model it connects to) is **offense**: it
produces new value, but fails without a functioning governance foundation
underneath it. Don't present either as a substitute for the other to a
client — both are needed, for different reasons.

## Disclaimer in this pack — regulatory liability too

In addition to the general disclaimer (`shared-guardrails.md`): privacy and
regulatory questions related to data monetization and processing (e.g.
GDPR) require separate data-protection expertise — this pack does not
substitute for it.

## Maturity in this pack

This pack's skills are currently at `maturity: scaffold` (see
[`../skills_index.json`](../skills_index.json) and
[`../meta/maturity_levels.md`](../meta/maturity_levels.md)) — the structure
and research anchoring are solid (data literacy frameworks, the data value
chain and Data & AI strategy literature, a synthesis of monetization
models), but the owner's own validated consulting experience hasn't been
attached yet.

## Shared standards

See [`../meta/frontmatter_schema.md`](../meta/frontmatter_schema.md) (what's
allowed in a SKILL.md frontmatter) and
[`../meta/skill_design_principles.md`](../meta/skill_design_principles.md)
(what a good skill in this repo has to pass).
