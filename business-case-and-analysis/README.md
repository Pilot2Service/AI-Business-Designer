# Business Case & Analysis

Päätöksentekokelpoisten liiketoimintaperustelujen ja analyysien laadinta (BABOK, PMI).

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `requirements-and-scope-framing` | Rajaa ongelman ja vaatimukset selkeäksi, testattavaksi kokonaisuudeksi. |
| `stakeholder-analysis-and-raci` | Kartoittaa sidosryhmät valta/intressi-matriisilla ja määrittää vastuut RACI:lla. |
| `assumption-and-evidence-audit` | Testaa oletukset ja tunnistaa evidenssiaukot ennen suosituksen lukitsemista. |
| `business-case-builder` | Rakentaa täyden business casen: ongelma, ratkaisu, talous (ROI/NPV/IRR), riskit, aikataulu, sidosryhmät, suositus. |
| `roi-npv-sensitivity-model` | Laskee ROI:n, NPV:n ja IRR:n sekä herkkyysanalyysin eri skenaarioissa. |
| `risk-matrix-and-mitigation` | Tunnistaa ja pisteyttää riskit (todennäköisyys × vaikutus) ja suunnittelee mitigoinnit. |

Kaikki `maturity: scaffold` — ks. `../skills_index.json` kypsyystilalle (frontmatterissa
ei seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Ankkurointi

- 45ck — assumption-extractor / evidence-gap-review
- 45ck — raci-matrix / power-interest-grid
- BABOK — requirements
- BABOK — stakeholder analysis
- IEEE 830
- IIBA BABOK
- ISO 31000
- PMI Business Analysis
- PMI riskienhallinta
- WEF Future of Jobs 2025 — analytical thinking #1
- aj-geddes — business-case-development
- w95 business-case-builder
- w95/awesome-claude-corporate-skills — business-case-builder-rakenne

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
