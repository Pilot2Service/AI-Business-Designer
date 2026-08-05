---
status: validated
owner_input_needed: false
last_reviewed: 2026-08-05
---

# AI-Native Startup Design

Miten AI-natiivi tuote/liiketoiminta suunnitellaan alusta asti tekoälyn
aikakaudella: uudesta mindsetistä ja AI-mahdollisuuksien tunnistuksesta
asiakasymmärryksen kautta rakennettavaan PRD:hen, prosessien
closed-loop-suunnitteluun ja oikean AI-työkalupinon valintaan.

## Tila

Tämä pakki on rakennettu suoraan omistajan (Tommi Järvinen) fasilitoimasta
**AI-native Business Design** -työpajasta pre-startup-perustajille
([redacted] / firstkiss.co, pidetty 1.–2.6.2026,
[github.com/Pilot2Service/AI-training-P6](https://github.com/Pilot2Service/AI-training-P6)).
Se ei ole tutkimustason scaffold vaan omistajan pitämään, käytännön
työpajaan ankkuroitu sisältö — `source_layer: owner`, `maturity: validated`
kaikilla skilleillä (ks. `../../skills_index.json`).

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `ai-native-opportunity-scan` | Löytää ja priorisoi agenttisen/closed-loop-tason AI-mahdollisuuksia omassa startup-caseessa promptiketjulla. |
| `customer-vision-to-jtbd` | Jäsentää vapaamuotoisen vision ICP:ksi, Jobs-To-Be-Done-analyysiksi, tarveteemoiksi ja AI-advantage-pisteytykseksi. |
| `ai-buildable-prd-writing` | Kirjoittaa PRD:n AI-rakennusagentille annettavana työmääräyksenä, plus tukidokumentit ja tuotantosuunnitelman. |
| `closed-loop-process-and-human-oversight-design` | Jäsentää prosessit avoimiksi/suljetuiksi silmukoiksi ja päättää ihmisen valvonnan tason (in/on/outside-the-loop). |
| `ai-native-tool-stack-selection` | Valitsee pienimmän toimivan AI-natiivin työkalupinon 12 kategorian päätöspuulla. |

## Ankkurointi

- Omistajan AI-native Business Design -työpaja (Tommi Järvinen,
  [redacted]/firstkiss.co, 1.–2.6.2026) — ks.
  `references/workshop-source.md`
- Ideal Customer Profile (ICP) ja Jobs-To-Be-Done (JTBD) -tuotestrategia-
  kehykset, sellaisina kuin työpaja soveltaa niitä
- Open loop / closed loop -systeemiajattelu ja human-in/on/outside-the-loop
  -malli, sellaisina kuin työpaja esittää ne AI-agenttikontekstissa

## Skillien looginen kulku

```
ai-native-opportunity-scan
        │
        ▼
customer-vision-to-jtbd
        │
        ▼
ai-buildable-prd-writing ──► ai-native-tool-stack-selection
        │                           (kenelle PRD annetaan)
        ▼
closed-loop-process-and-human-oversight-design
   (syventää agenttisuuden tunnistusta, jota
    opportunity-scan käytti jo vaiheessa 1)
```

Skillit on suunniteltu käytettäviksi myös itsenäisesti (ks.
`../../meta/skill_design_principles.md` — independence-testi), mutta yllä
oleva polku vastaa työpajan Day 1 -etenemisjärjestystä (mindset →
mahdollisuus → asiakas → PRD → työkalut) ja sopii ensikertalaiselle.

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  promptikirjasto, työkalukategoriakartta, lähdetiedot
cases/                       (varattu — tulevat omat, anonymisoidut työpaja-/asiakastapaukset)
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
