---
status: validated
owner_input_needed: true
last_reviewed: 2026-08-05
---

# Business Model Canvas

Business Model Canvas (BMC) -konsultointiosaaminen yhdeksi erikoistumispakiksi:
159 patternin innovaatiokirjasto liiketoimintamallin uudistamiseen, omistajan
oma variointi- ja selkeyslogiikka, antipatternien ja asiakkaan väärinkäsitysten
tunnistus, sekä tutkimuspohjainen tuki session fasilitointiin, canvasin
diagnostiseen lukemiseen, työkaluvalintaan ja asiakaspuheen tulkintaan.

## Tila

Tämä pakki yhdistää kaksi omistajan toimittamaa lähdettä:

1. **Julkinen 159 patternin koneluettava innovaatiokirjasto** — ks.
   `references/bmc-innovation-pattern-library.md`.
2. **Omistajan oma, ei-julkinen tutkimustyö** — kesken oleva projekti
   BMC-konsultointiasiantuntijuuden kaappaamiseksi. Sisältää sekä
   huhtikuussa 2026 tehdystä konsulttihaastattelusta poimitun, aidosti
   validoidun asiantuntijasisällön että tunnettujen BMC-lähteiden (Jeffries,
   Williams, van der Linden, Blank/Strategyzer, Ash Maurya) esitäytetyn,
   vielä täydentämättömän tutkimuskerroksen.

Tästä syystä pakin seitsemästä skillistä kolme on `validated`/`owner`-tasoa ja
neljä `scaffold`/`research`-tasoa — ks. `CLAUDE.md` ja
`references/bmc-source-material-notes.md` täydellinen selitys jaosta.

## Asiakasprofiili (ankkuroitu asiantuntijaan)

Tämän pakin taustalla oleva konsultointikäytäntö kohdistuu **varhaisen
vaiheen ja kasvuvaiheen yrityksiin** — ei suuriin yrityksiin tai niiden
innovaatioyksiköihin. Tyypillisesti pieniä yrityksiä, joissa perustaja tai
yrittäjä on tiiviisti mukana työssä. Asiantuntijan oma määritelmä BMC:n
roolista: *"BMC is a thinking tool, not a complete business planning
instrument. Its purpose is to help the team think in new ways, see new
opportunities, and enable different perspectives."* BMC ei korvaa:
tuotespesifikaatioita, kannattavuuslaskelmia, kasvu- ja marginaaliskenaarioita
— nämä vaativat tarkempia työkaluja.

## Skillit tässä pakissa

| Skilli | Taso | Kuvaus |
|---|---|---|
| `bmc-innovation-pattern-matching` | `validated` | 3-5 yhteensopivan innovaatiopatternin tunnistus 159 patternin kirjastosta, asiantuntijan neliosaisella taksonomialla. |
| `bmc-canvas-clarity-and-iteration` | `validated` | Variointilogiikka, jumissa-olon tunnistus, selkeys-ennen-syvyyttä-valmiuskriteeri. |
| `bmc-antipattern-and-misunderstanding-correction` | `validated` | Viisi työtavan antipatternia + neljä asiakkaan väärinkäsitystä BMC:n roolista, suorat korjausliikkeet. |
| `bmc-session-facilitation-design` | `scaffold` | Session rakenne: aloituskohta, täyttöjärjestys, pituus/tiimikoostumus, evidenssin värikoodaus. |
| `bmc-canvas-diagnostic-reading` | `scaffold` | Kuusi diagnostista sääntöä (Hook Rule ym.) + nelidimensioinen laaturubriikki. |
| `bmc-tool-switching-decisions` | `scaffold` | Milloin siirtyä VPC:hen, Lean Canvasiin, Mission Model Canvasiin tai taloudelliseen mallinnukseen. |
| `bmc-client-language-translation` | `scaffold` | Asiakaslauseiden tulkinta + kolme yleisintä käsiteväärinkäsitystä. |

## Skillien looginen kulku

```
bmc-session-facilitation-design (session-suunnittelu)
        │
        ▼
bmc-innovation-pattern-matching (innovaatiosuunta + patternit)
        │
        ▼
bmc-canvas-clarity-and-iteration (2-3 varianttia, selkeyskriteeri)
        │
        ├──► bmc-canvas-diagnostic-reading (syvempi sisäinen analyysi)
        │
        ├──► bmc-antipattern-and-misunderstanding-correction
        │     (käytä kesken työn, kun jokin juuttuu)
        │
        └──► bmc-tool-switching-decisions (milloin siirtyä eteenpäin)

bmc-client-language-translation
   (käytä koko ajan rinnalla — asiakaspuheen tulkinta)
```

Skillit on suunniteltu käytettäviksi myös itsenäisesti (ks.
`../../meta/skill_design_principles.md` — independence-testi), mutta yllä
oleva polku vastaa tyypillistä BMC-toimeksiannon etenemistä.

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  patternkirjasto, lähdeaineiston tausta
cases/                       (varattu — tulevat omat, anonymisoidut asiakastapaukset)
```

## Suhde muihin pakkeihin

- `business-design-frameworks` — geneeriset, kehysriippumattomat
  jäsentämismallit. BMC on yksi tunnettu kehys näiden joukossa, mutta tämä
  pakki on oma erikoistumisalueensa laajemman, sisäisesti riippuvaisen
  asiantuntijuuden (sanasto, diagnostiikka, patternkirjasto) vuoksi — ei
  vain yksi jäsentämismalli muiden joukossa.
- `ai-native-startup-design` — kevyt, nopea "prototyyppi kahdessa
  päivässä" -pakki AI-natiiveille pre-startup-perustajille. Sen
  `ai-buildable-prd-writing`-skilli seuraa BMC-työtä ajallisesti, mutta ei
  käytä BMC:tä itse — tämä pakki tuottaa syötteen sinne kun liiketoiminta­
  mallin innovaatio on ensin tehty.
- `research-commercialisation` — tutkimuslähtöisten innovaatioiden
  kaupallistaminen; voi käyttää tämän pakin patternkirjastoa yhtenä
  kaupallistamisvaihtoehtojen lähteenä.

Katso `../../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän
pakin sisältöä.
