# AI Strategy & Governance

AI-mahdollisuuksien tunnistaminen, priorisointi ja vastuullinen käyttöönotto liiketoiminnassa.

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `task-level-decomposition-and-automation-fit` | Pilkkoo roolit/prosessit tehtävätasolle (People Path + Process Path) ja luokittelee jokaisen tehtävän Automate/Augment/Human-Only SML-kriteereillä. |
| `ai-opportunity-portfolio` | Tunnistaa, pisteyttää (5D-malli) ja priorisoi AI-käyttötapaukset 2x2-matriisilla; erottelee inkrementaaliset ja transformatiiviset (Value-Play-taksonomia) mahdollisuudet. |
| `ai-native-business-model-canvas` | Suunnittelee siirtymän AI-enhanced-liiketoiminnasta AI-native-liiketoimintamalliin laajennetulla Business Model Canvasilla (VP, data moat, Human-AI Interaction Model, compute-kustannukset). |
| `ai-use-case-feasibility-and-poc-scoping` | Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen. |
| `responsible-ai-and-governance-check` | Tarkistaa AI-aloitteen sääntely-, riski- ja eettisyysnäkökulmat. Syvempään EU AI Act -compliance-analyysiin käytä tämän workspacen tekoalysaantely-plugineja (tekoaly-luokittelu, tekoaly-velvoitteet, tekoaly-vaatimustenmukaisuus). |
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
- Perplexity-tutkimus: Senior AI Business Designer (Solita/HP)
- strategic-options-evaluation -logiikka sovellettuna AI-päätöksiin
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — AI-soveltuvuuden triagi, data flywheel, AI-native
  Business Model Canvas, Shadow AI, AI-tuotosten kuratointi ja
  laadunvalvonta
- Käyttäjän toimittama tutkimusraportti "Tekoälymahdollisuuksien ja
  -kapasiteetin tunnistamismenetelmät, viitekehykset ja osaamiset
  liiketoiminnassa" (2026) — SML/Dual Decomposition -tehtäväpilkkominen,
  process/task mining, 5-ulotteinen pisteytysmalli, 2x2-priorisointi-
  matriisi, Value-Play-taksonomia, BCG:n Deploy-Reshape-Invent, kolmi-
  horisonttinen roadmap, ATOM/Readiness Scorecard, discovery-
  toimeksiantojen rakenne ja tuotteistus ([redacted], [redacted], McKinsey
  [redacted], BCG, Brynjolfsson & Mitchell -synteesi)
- Yleinen "Shadow IT" -kirjallisuus ja -käytäntö, laajennettuna
  AI-työkalujen kontekstiin

## Skillien looginen kulku

```
task-level-decomposition-and-automation-fit  (tehtävätason raakalista)
        │
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
