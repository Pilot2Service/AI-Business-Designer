# Business Design Frameworks

A growing collection of ways to structure and model business, value creation,
value chains, and positioning. Unlike the other core packs, this pack is
deliberately open-ended — new structuring and modeling approaches will be
added over time as they're identified and refined.

## Skills in this pack

| Skill | Description |
|---|---|
| `layer-based-business-structuring` | Structures a business into layers (OSI-model-like), from infrastructure to brand — deciding which layers to build in-house and which to source through partners. |
| `value-chain-mapping` | Structures a business according to Porter's value chain model into primary and support activities — showing where value and margin actually come from. |
| `category-definition-and-modeling` | Models a product or business relative to market categories: associating with one, expanding one, or creating an entirely new one. |
| `strategy-canvas-and-value-curve` | Structures competitors/alternatives on shared competitive factors (Blue Ocean Strategy Canvas), identifies the industry's "as-is curve," and looks for ways to break away from it using the ERRC grid. |
| `customer-journey-and-ai-touchpoint-mapping` | Maps the customer's service journey and its friction points, and places AI on the journey only where it genuinely creates value. |
| `taste-emulation-heuristic` | Predicts a specific, narrowly-defined in-group's emotional/aesthetic reaction to a concept — a trainable judgment skill built through deliberate exposure hours, mental simulation, and correction against real feedback. |

`strategy-canvas-and-value-curve` is additionally anchored in the owner's
own 360 Comparison Factors tool, used in real client work.

## How the skills flow together

```
layer-based-business-structuring ──┐
                                    ├──► category-definition-and-modeling
value-chain-mapping ────────────────┘              ▲
                                                     │
strategy-canvas-and-value-curve ────────────────────┘
   (differentiation as an input to the category decision)

customer-journey-and-ai-touchpoint-mapping
   (a complementary, outside-in customer perspective —
    can be used together with any of the above)

taste-emulation-heuristic
   (a different question — predicted in-group reaction, not
    structural positioning — usable alongside any of the above,
    especially before committing to build or test a concept)
```

All can also be used independently (see
`../meta/skill_design_principles.md` — the independence test) — they are
alternative, partly complementary lenses on the same business.

## Anchored in

- The OSI model (telecommunications) — the original inspiration for the
  layer principle
- Hagel & Singer (1999) — "Unbundling the Corporation" (HBR)
- Baldwin & Clark (2000) — *Design Rules: The Power of Modularity*
- Porter, M. (1985) — *Competitive Advantage*, the value chain model
- Ramadan, Peterson, Lochhead & Maney (2016) — *Play Bigger*, category design
- Kim & Mauborgne (2005) — *Blue Ocean Strategy* (Strategy Canvas, Value
  Curve, Four Actions Framework/ERRC, Six Paths Framework)
- Ries & Trout — positioning theory
- The owner's 360 Comparison Factors comparison tool (the owner's own product)
- Notion product lead Max Schoening — taste as a trainable prediction
  skill (source video transcript supplied by the user)

## Structure

```
CLAUDE.md                    the pack's shared guardrails (always read first)
skills/<skill-id>/SKILL.md   an individual skill (name + description frontmatter)
references/                  background material, sources, own templates (to be filled in)
```

## How to add a new structuring approach to this pack

1. Create `skills/<new-skill-id>/SKILL.md` following the same structure as
   the existing skills (see `../templates/skill-template/SKILL.md`).
2. Anchor it in a known framework or your own validated experience — mark
   `source_layer` and `maturity` honestly in `skills_index.json`
   (`python3 ../scripts/generate_index.py` generates the skeleton; update
   maturity by hand as needed).
3. Add a row to this README's skill table and cross-link it in the
   "Continue from here" section to the closest related skills in this and
   other packs.
4. Run `python3 ../scripts/validate.py` before committing.

See `../meta/maturity_levels.md` for what the maturity levels mean, and
`../AGENT_GUIDE.md` for how an agent should read and weight this pack's
content.
