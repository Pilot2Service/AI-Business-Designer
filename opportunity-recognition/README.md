# Opportunity Recognition

Systemaattinen liiketoimintamahdollisuuksien tunnistaminen ja arviointi (Kirzner, Shane & Venkataraman).

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `market-and-signal-scanning` | Systemaattinen ympäristön skannaus (markkina, teknologia, sääntely, kilpailu) mahdollisuuksien tunnistamiseksi. |
| `pattern-and-analogy-connector` | Yhdistää irrallisia havaintoja mielekkääksi mahdollisuudeksi tunnistamalla analogioita eri toimialojen/tilanteiden välillä. |
| `opportunity-evaluation-and-judgment` | Arvioi tunnistetun mahdollisuuden elinkelpoisuuden jäsennellysti ennen resurssien sitomista. |
| `market-sizing-tam-sam-som` | Laskee markkinan koon ja aidosti saavutettavan osuuden kvantitatiivisesti. |
| `competitive-and-five-forces-mapping` | Kartoittaa kilpailudynamiikan ja toimialan rakenteelliset voimat. |

Kaikki `maturity: scaffold` — ks. `../skills_index.json` kypsyystilalle (frontmatterissa
ei seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Ankkurointi

- Business Opportunity Scout (buYoung)
- Kirzner (1973/1979) — entrepreneurial alertness
- Opportunity recognition as pattern recognition -kirjallisuus
- PESTLE
- Porter's Five Forces
- SFIA — Business Situation Analysis
- Tang, Kacmar & Busenitz — association and connection
- Tang, Kacmar & Busenitz — evaluation and judgment
- stratarts — market-opportunity-analyzer

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
