# Opportunity Recognition

Systemaattinen liiketoimintamahdollisuuksien tunnistaminen ja arviointi (Kirzner, Shane & Venkataraman) — täydennetty omistajan oman palvelun Opportunity Value Assessment -metodologialla.

## Skillit tässä pakissa

| Skilli | Kuvaus | Kypsyys |
|---|---|---|
| `market-and-signal-scanning` | Systemaattinen ympäristön skannaus (markkina, teknologia, sääntely, kilpailu) mahdollisuuksien tunnistamiseksi. | `scaffold` |
| `pattern-and-analogy-connector` | Capability Pattern Mapping: abstrahoi pintapuolisesti erilaiset casejoukot yhdeksi nimetyksi, toimialariippumattomaksi patterniksi, joka toimii diagnostisena kysymyksenä uudessa kontekstissa. | `scaffold` |
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

`pattern-and-analogy-connector`-skillin Capability Pattern Mapping -menetelmästä
on konkreettinen, AI-ratkaisuihin sovellettu toteutus:
`../ai-strategy-and-governance/references/ai-capability-pattern-library.md`
(13 patternia) ja sen käyttöskilli
`../ai-strategy-and-governance/skills/ai-capability-pattern-matching/SKILL.md`.

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
- omistajan oma palvelu — Opportunity Value Assessment -palvelu (oma tuote,
  `opportunity-intake-elicitation`, `opportunity-value-assessment`,
  `opportunity-brief-writing`)
- Mullins' Seven Domains Model, Timmons-malli, POEM-matriisi, NABC-malli,
  Opportunity Canvas — ks. `references/opportunity-frameworks-review.md`

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
