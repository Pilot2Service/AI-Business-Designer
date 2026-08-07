# Data role heuristics — a broader collection

Background material for the skill
`../skills/data-role-diagnosis/SKILL.md`. This file gathers more
diagnostic questions and examples to support the two main perspectives
(enabler vs. strategic asset).

## Enabler vs. strategic asset — comparison table

| Dimension | Data as enabler | Data as strategic asset |
|---|---|---|
| Basic nature | Commodity, cost (necessary) | Asset whose value grows |
| Core question | "Does this help us do what we already do faster, cheaper, better?" | "Could we sell this, or use it to train a model a competitor can't replicate?" |
| Focus | Data governance, quality, integrations, operational efficiency | Monetization, data network effects (flywheel), new business models |
| Metric | Cost savings, fewer errors, process speed | ROI, new revenue, defensible competitive advantage |
| Typical example | Setting up a data governance model doesn't itself make money, but it enables e.g. automated customer reporting | Purchase-behavior data is used to build a "Next Best Action" recommendation algorithm sold as a service |
| Risk if the role isn't recognized | Monetization investment made without a working data foundation — fails on quality/reliability grounds | The value of data is underestimated, treated as a pure IT cost rather than a competitive advantage |

## Additional diagnostic questions

- Who in the organization "owns" this data today, and is that ownership
  tied to a budget (cost center) or to an outcome (P&L responsibility)?
  Data that sits only under a cost center is almost always treated as an
  enabler regardless of its actual potential.
- Has anyone in the organization ever asked "could we sell this?" about
  this data, and what was the answer? If the question has never even
  been raised, that's a sign the data has been framed by default as an
  enabler without a deliberate decision.
- Is there data that looks like an enabler in one business unit but like
  an asset in another (e.g. logistics data that's an operational cost
  for the logistics team but valuable forecasting data for sales)? The
  role isn't always a single shared truth across the whole organization
  — it can vary by perspective.

## The Offense/Defense framework in practice

The data strategy conversation often gets tangled because the same term
("data strategy") is used to mean two different things:

- **Defense:** data governance, quality, security, compliance. Goal:
  reduce risk and errors, enable trustworthy use. Doesn't directly
  produce new revenue.
- **Offense:** exploiting data as a source of new business, product, or
  competitive advantage. Goal: growth and differentiation. Requires a
  working defense foundation underneath it.

A common trap: an organization wants "offense"-level results (new
revenue streams, AI products) but its data is only at "defense"-level
maturity (siloed, inconsistent, not reliably available). In that case,
the correct first investment isn't offense but defense — only after that
do offense investments pay off.

## See also

- `../skills/data-role-diagnosis/SKILL.md` — the main skill that uses
  this background material
- `../skills/data-monetization-model-selection/SKILL.md` — the next step
  once the role has been validated as an asset
