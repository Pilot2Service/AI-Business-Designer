---
status: validated
owner_input_needed: false
last_reviewed: 2026-08-06
---

# AI-Native Startup Design

Miten AI-natiivi tuote/liiketoiminta suunnitellaan alusta asti tekoälyn
aikakaudella: uudesta mindsetistä ja AI-mahdollisuuksien tunnistuksesta
asiakasymmärryksen, tarveteemapisteytyksen ja ratkaisuideoinnin kautta
RICE-valittuun MVP:hen, rakennettavaan PRD:hen, keskustelevaan
käyttöliittymäarkkitehtuuriin, prosessien closed-loop-suunnitteluun ja
oikean AI-työkalupinon valintaan.

## Tila

Tämä pakki yhdistää kaksi omistajan (Tommi Järvinen) itse käytäntöön
soveltamaa lähdettä:

1. **AI-native Business Design** -työpaja pre-startup-perustajille
   ([redacted] / firstkiss.co, pidetty useille osallistujille
   1.–2.6.2026,
   [github.com/Pilot2Service/AI-training-P6](https://github.com/Pilot2Service/AI-training-P6))
   — ks. `references/workshop-source.md`. Tämän pohjalta rakennetut
   skillit ovat `maturity: validated` (useamman osallistujan sessio).
2. **[redacted]n "AI-first SaaS Product" -työpaja** — omistajan itse
   soveltama menetelmä yhteen omaan caseen ([redacted] "Decision
   Coach" MVP) — ks. `references/[redacted]-workshop-source.md` ja
   worked example `cases/[redacted]-decision-coach-mvp.md`. Tämän pohjalta
   rakennetut ja syvennetyt skillit ovat `maturity: draft` (sovellettu
   kerran, ei vielä laajasti validoitu useammalla caseella) — ks.
   taulukko alla.

Kaikki skillit ovat `source_layer: owner` (ks. `../../skills_index.json`).

## Skillit tässä pakissa

| Skilli | Taso | Kuvaus |
|---|---|---|
| `ai-native-opportunity-scan` | `validated` | Löytää ja priorisoi agenttisen/closed-loop-tason AI-mahdollisuuksia omassa startup-caseessa promptiketjulla. |
| `customer-vision-to-jtbd` | `validated` | Jäsentää vapaamuotoisen vision ICP:ksi, verbivetoiseksi Jobs-To-Be-Done-analyysiksi, 5+2 tarveteemaksi, 5-kriteeriseksi NMB+AI-advantage-pisteytykseksi ja valitsee AI-differentiaattoritarpeen (AI wedge). |
| `ai-differentiator-solution-ideation` | `draft` | Ideoi 3 keskenään erilaista AI-natiivia ratkaisusuuntaa valitulle AI wedgelle kolmella linssillä. |
| `rice-scoring-and-mvp-synthesis` | `draft` | Pisteyttää ratkaisusuunnat RICE-mallilla, valitsee MVP:n, kirjoittaa MVP-määritelmän, positiointilauseen ja "miksi voitamme" -väittämät. |
| `ai-buildable-prd-writing` | `validated` | Kirjoittaa PRD:n AI-rakennusagentille annettavana työmääräyksenä, plus tukidokumentit ja tuotantosuunnitelman. |
| `ai-native-conversational-os-design` | `draft` | Suunnittelee AI-natiivin tuotteen keskustelevan käyttöliittymäarkkitehtuurin (Intent → Strategy Cards → Clarification → Output Cards → Mission → Agent Execution) ja 5 AI-first-tuoteperiaatetta. |
| `closed-loop-process-and-human-oversight-design` | `validated` | Jäsentää prosessit avoimiksi/suljetuiksi silmukoiksi ja päättää ihmisen valvonnan tason (in/on/outside-the-loop). |
| `ai-native-tool-stack-selection` | `validated` | Valitsee pienimmän toimivan AI-natiivin työkalupinon 12 kategorian päätöspuulla. |

## Ankkurointi

- Omistajan AI-native Business Design -työpaja (Tommi Järvinen,
  [redacted]/firstkiss.co, 1.–2.6.2026) — ks.
  `references/workshop-source.md`
- [redacted]n AI-first SaaS Product -työpajan menetelmä, sovellettu [redacted]-
  caseen — ks. `references/[redacted]-workshop-source.md` ja
  `cases/[redacted]-decision-coach-mvp.md`
- Ideal Customer Profile (ICP) ja Jobs-To-Be-Done (JTBD) -tuotestrategia-
  kehykset, sellaisina kuin työpajat soveltavat niitä
- RICE-priorisointimalli (yleisesti tunnettu, ei omistajan oma)
- Open loop / closed loop -systeemiajattelu ja human-in/on/outside-the-loop
  -malli, sellaisina kuin työpaja esittää ne AI-agenttikontekstissa

## Skillien looginen kulku

```
ai-native-opportunity-scan
        │
        ▼
customer-vision-to-jtbd  (ICP → JTBD → Need Themes → NMB-pisteytys → AI wedge)
        │
        ▼
ai-differentiator-solution-ideation  (3 ratkaisusuuntaa valitulle wedgelle)
        │
        ▼
rice-scoring-and-mvp-synthesis  (RICE-valinta → MVP-määritelmä → positiointi)
        │
        ▼
ai-buildable-prd-writing ──► ai-native-tool-stack-selection
        │                           (kenelle PRD annetaan)
        ▼
ai-native-conversational-os-design
   (jos MVP on keskusteleva/agenttinen tuote —
    syventää PRD:n Core-ominaisuudet-osiota)
        │
        ▼
closed-loop-process-and-human-oversight-design
   (syventää agenttisuuden tunnistusta, jota
    opportunity-scan käytti jo vaiheessa 1, ja
    Agent Execution -vaiheen valvontatasoa)
```

Skillit on suunniteltu käytettäviksi myös itsenäisesti (ks.
`../../meta/skill_design_principles.md` — independence-testi). Jos
ratkaisusuunta on alusta asti selvä, voi hypätä suoraan
`customer-vision-to-jtbd`:stä `ai-buildable-prd-writing`:iin ohittaen
ideointi-/RICE-vaiheen — ideointiketju on tarkoitettu tilanteisiin, joissa
on aidosti useampi kilpaileva ratkaisusuunta puntaroitavana.

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  promptikirjasto, työkalukategoriakartta, lähdetiedot
cases/                       worked example: [redacted]-decision-coach-mvp.md
                              (lisää omia anonymisoituja tapauksia tähän jatkossa)
```

## Suhde muihin pakkeihin

Tämä pakki on tarkoituksella kevyt ja nopea ("prototyyppi kahdessa
päivässä") toisin kuin:

- `ai-strategy-and-governance` — laajempi, olemassa olevan yrityksen
  AI-portfolion, build/buy/partner-päätösten ja hallinnon systemaattinen
  arviointi. `ai-native-opportunity-scan` viittaa sen
  `ai-opportunity-portfolio`-skilliin, mutta on kevyempi ja nopeampi.
- `business-case-and-analysis` — muodollisempi, rahoitusta tai
  organisaation hyväksyntää vaativa liiketoimintaperustelu.
  `ai-buildable-prd-writing` on kevyt spec yhden viikon prototyypille, ei
  korvaa `business-case-builder`-skilliä isommassa päätöksessä.
- `business-design-frameworks` — geneeriset, AI-riippumattomat
  jäsentämismallit (kerrokset, arvoketju, kategoriat, strategiakartat).
  `closed-loop-process-and-human-oversight-design` on saman perheen
  jäsentämistapa, mutta AI-agenttikontekstiin sidottuna.

Katso `../../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän
pakin sisältöä.
