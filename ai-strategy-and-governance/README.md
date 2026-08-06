# AI Strategy & Governance

AI-mahdollisuuksien tunnistaminen, priorisointi ja vastuullinen käyttöönotto liiketoiminnassa.

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `task-level-decomposition-and-automation-fit` | Pilkkoo roolit/prosessit tehtävätasolle (People Path + Process Path) ja luokittelee jokaisen tehtävän Automate/Augment/Human-Only SML-kriteereillä. |
| `ai-capability-pattern-matching` | Käyttää 13 AI-kyvykkyyspatternin kirjastoa (tutkimuspohjainen, kahdesta riippumattomasta toimialan AI-käyttötapausraportista ristiintarkistettu) diagnostisten kysymysten esittämiseen — top-down-vaihtoehto tehtävätason pilkkomiselle raakalistan kokoamisessa. |
| `ai-opportunity-portfolio` | Tunnistaa, pisteyttää (5D-malli) ja priorisoi AI-käyttötapaukset 2x2-matriisilla; erottelee inkrementaaliset ja transformatiiviset (Value-Play-taksonomia) mahdollisuudet. |
| `ai-native-business-model-canvas` | Suunnittelee siirtymän AI-enhanced-liiketoiminnasta AI-native-liiketoimintamalliin laajennetulla Business Model Canvasilla (VP, data moat, Human-AI Interaction Model, compute-kustannukset). |
| `ai-use-case-feasibility-and-poc-scoping` | Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen. |
| `responsible-ai-and-governance-check` | Tarkistaa AI-aloitteen sääntely-, riski- ja eettisyysnäkökulmat. Syvempään EU AI Act -compliance-analyysiin tarvitaan erillinen sääntely-asiantuntemus. |
| `build-vs-buy-vs-partner-ai` | Jäsentää päätöksen rakentaa itse, ostaa alustalta vai kumppanoitua AI-ratkaisussa. |
| `ai-capability-roadmap` | Rakentaa organisaation AI-kyvykkyyskartan ja roadmapin kolmella horisontilla (0-6/6-18/18-36kk) + ATOM/Readiness Scorecard. |
| `ai-discovery-engagement-design` | Tuotteistaa koko tunnistamisprosessin maksulliseksi/sisäiseksi discovery-toimeksiannoksi — vaiheet, palvelutuotteet, luovutettava aineisto. |
| `shadow-ai-response-and-safe-adoption` | Tunnistaa luvattoman AI-työkalujen käytön (Shadow AI) ja korvaa sen turvallisella, ROI-perustellulla virallisella ratkaisulla. |
| `ai-output-curation-and-quality-control` | Suunnittelee laadunvalvonta- ja kuratointiprosessin AI:n tuotoksille — siirtymä tekijästä kuraattoriksi. |

Kaikki `maturity: scaffold` — ks. `../skills_index.json` kypsyystilalle (frontmatterissa
ei seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Ankkurointi

- EU AI Act (asetus (EU) 2024/1689)
- LinkedIn 2026 — Risk & Compliance Management
- LinkedIn Skills on the Rise 2026 — AI Business Strategy
- Perplexity-tutkimus — PoC-määrittely tuotannollistamiseen asti
- Perplexity-tutkimus — roadmapit ja liiketoimintakyvykkyyskartat
- Markkinatutkimus: avoimet "Senior AI Business Designer" -tyyppiset rekrytointi-ilmoitukset
- strategic-options-evaluation -logiikka sovellettuna AI-päätöksiin
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — AI-soveltuvuuden triagi, data flywheel, AI-native
  Business Model Canvas, Shadow AI, AI-tuotosten kuratointi ja
  laadunvalvonta
- Tutkimuskooste "Tekoälymahdollisuuksien ja -kapasiteetin
  tunnistamismenetelmät, viitekehykset ja osaamiset liiketoiminnassa"
  (2026) — SML/Dual Decomposition -tehtäväpilkkominen, process/task
  mining, 5-ulotteinen pisteytysmalli, 2x2-priorisointimatriisi,
  Value-Play-taksonomia, Deploy-Reshape-Invent-taksonomia, kolmihorisonttinen
  roadmap, ATOM/Readiness Scorecard, discovery-toimeksiantojen rakenne ja
  tuotteistus (synteesi useista toimialan AI-kyvykkyysraporteista ja
  Brynjolfsson & Mitchell -tutkimuksesta)
- Yleinen "Shadow IT" -kirjallisuus ja -käytäntö, laajennettuna
  AI-työkalujen kontekstiin
- Toimialakohtainen AI-käyttötapausraportti (2026-painos) — 130
  AI-käyttötapausta kuudella toimialalla, vastuullisen AI:n riskikehys.
  81 tekstipohjaisesti poimittua ja tarkistettua casea käytetty
  `references/ai-capability-pattern-library.md`:n pohjana.
- Toinen, riippumaton AI-käyttötapauskooste (63 käyttötapausta, 16
  funktiota) — käytetty patternikirjaston ristiintarkistuksena

## Skillien looginen kulku

```
task-level-decomposition-and-automation-fit    ai-capability-pattern-matching
   (bottom-up: tehtävätason raakalista)      (top-down: patternikirjaston
        │                                     diagnostiset kysymykset)
        └──────────────────┬──────────────────────────┘
                            ▼
ai-opportunity-portfolio  (5D-pisteytys → 2x2-matriisi → priorisoitu backlog)
        │
        ├──► ai-native-business-model-canvas  (jos transformatiivinen)
        ├──► ai-use-case-feasibility-and-poc-scoping  (tekninen validointi)
        └──► ai-capability-roadmap  (Horisontti 1/2/3 -aikataulutus)
                    │
                    ▼
        responsible-ai-and-governance-check, build-vs-buy-vs-partner-ai
                    │
                    ▼
        shadow-ai-response-and-safe-adoption, ai-output-curation-and-quality-control
             (käyttöönoton jälkeinen ylläpito ja laadunvalvonta)
```

`ai-discovery-engagement-design` on tämän kulun "meta-skilli" — se
jäsentää koko yllä olevan ketjun yhdeksi ajoitetuksi, luovutettavaksi
konsultointitoimeksiannoksi, kun tunnistamisprosessi tehdään
muodollisena projektina eikä ad hoc -analyysinä.

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
