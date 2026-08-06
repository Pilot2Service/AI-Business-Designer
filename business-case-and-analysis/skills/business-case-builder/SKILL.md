---
name: business-case-builder
description: "Rakentaa täyden business casen: ongelma, ratkaisu, talous (ROI/NPV/IRR), riskit, aikataulu, sidosryhmät, suositus. Käytä kun tarvitset business case & analysis-tason tukea vastaavaan tehtävään."
---

# Business Case Builder

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Rakentaa täyden business casen: ongelma, ratkaisu, talous (ROI/NPV/IRR), riskit, aikataulu, sidosryhmät, suositus.

## Ankkurointi tutkimukseen

- IIBA BABOK
- PMI Business Analysis
- w95/awesome-claude-corporate-skills — business-case-builder-rakenne

## Rakenne (luonnos — täydennettävä)

1. Määritä tilanne/konteksti, johon tätä skilliä sovelletaan.
2. Käy läpi ankkuroinnin mukainen tekniikka vaihe vaiheelta.
3. Tuota jäsennelty tulos (ks. `../../references/` kun lisätty).
4. Validoi tulos sidosryhmillä tai omalla kokemuspohjaisella tarkistuslistalla.

## Mitä tämä skilli EI tee

- Ei tee lopullista päätöstä puolestasi — tuottaa jäsennellyn luonnoksen ihmisen
  päätöksenteon tueksi.
- Ei vahvista lukuja, markkinatietoa tai kilpailijadataa muistista — käyttää käyttäjän
  antamia lähtöarvoja tai merkitsee oletuksen selvästi (`[oletus — tarkista]`).
- Ei hyväksy budjettia tai tee investointipäätöstä — tuottaa päätöksentekoaineiston hyväksyjälle.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt ja heuristiikat tässä tekniikassa
- konkreettiset mallipohjat (`../../references/`-kansioon)
- referenssitapaukset / omat caset
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa seuraavaksi: `../roi-npv-sensitivity-model/SKILL.md` — Laskee ROI:n, NPV:n ja IRR:n sekä herkkyysanalyysin eri skenaarioissa.
- Ennen tätä (jos taustalla on demo tai PoC jonka tuloksia käytetään
  syötteenä): `../../../prototyping-and-demonstration/skills/demo-to-business-case-bridge/SKILL.md`
  — kääntää demon tulokset validoiduiksi, oletusketjultaan läpinäkyviksi
  ROI-syötteiksi ennen kuin niitä käytetään tässä.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
