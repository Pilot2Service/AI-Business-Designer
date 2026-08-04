# Opportunity Recognition

Systemaattinen liiketoimintamahdollisuuksien tunnistaminen ja arviointi (Kirzner, Shane & Venkataraman) — täydennetty omistajan (Tommi Järvinen) [redacted]-palvelun Opportunity Value Assessment -metodologialla.

## Skillit tässä pakissa

| Skilli | Kuvaus | Kypsyys |
|---|---|---|
| `market-and-signal-scanning` | Systemaattinen ympäristön skannaus (markkina, teknologia, sääntely, kilpailu) mahdollisuuksien tunnistamiseksi. | `scaffold` |
| `pattern-and-analogy-connector` | Yhdistää irrallisia havaintoja mielekkääksi mahdollisuudeksi tunnistamalla analogioita eri toimialojen/tilanteiden välillä. | `scaffold` |
| `opportunity-intake-elicitation` | Kerää jäsennellysti lähtötiedot tunnistetusta mahdollisuudesta hyvin muotoilluilla kysymyksillä. | `validated` |
| `opportunity-evaluation-and-judgment` | Arvioi tunnistetun mahdollisuuden elinkelpoisuuden jäsennellysti ennen resurssien sitomista (yleinen scaffold). | `scaffold` |
| `opportunity-value-assessment` | Sijoittaa mahdollisuuden houkuttelevuus × toteutettavuus -matriisiin ja arvioi sen 7 näkökulmasta — oma tuotteistettu kehys. | `validated` |
| `opportunity-brief-writing` | Kirjoittaa arvioinnin 1-2-sivuiseksi Opportunity Brief -raportiksi. | `validated` |
| `market-sizing-tam-sam-som` | Laskee markkinan koon ja aidosti saavutettavan osuuden kvantitatiivisesti. | `scaffold` |
| `competitive-and-five-forces-mapping` | Kartoittaa kilpailudynamiikan ja toimialan rakenteelliset voimat. | `scaffold` |

Kypsyys näkyy tarkasti `../skills_index.json`:ssa (frontmatterissa ei seurata
kypsyyttä, ks. `../meta/frontmatter_schema.md`). Tämä pakki on repon ensimmäinen
esimerkki ydinpakista, jossa yleiset tutkimuspohjaiset scaffold-skillit ja
omistajan validoitu, tuotteistettu metodologia elävät rinnakkain samassa pakissa.

## Skillien looginen kulku (oma metodologia)

```
opportunity-intake-elicitation → opportunity-value-assessment → opportunity-brief-writing
```

Ks. myös `market-sizing-tam-sam-som` ja `competitive-and-five-forces-mapping`
syventävinä tukiskilleinä `opportunity-value-assessment`-vaiheelle.

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
- [redacted] — Opportunity Value Assessment -palvelu (oma tuote,
  `opportunity-intake-elicitation`, `opportunity-value-assessment`,
  `opportunity-brief-writing`)
- Mullins' Seven Domains Model, Timmons-malli, POEM-matriisi, NABC-malli,
  Opportunity Canvas — ks. `references/[redacted]-frameworks-review.md`

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
