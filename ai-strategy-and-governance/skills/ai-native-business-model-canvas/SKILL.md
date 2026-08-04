---
name: ai-native-business-model-canvas
description: "Suunnittelee siirtymän AI-enhanced-liiketoiminnasta AI-native-liiketoimintamalliin laajennetulla, tekoälyspesifillä Business Model Canvasilla. Käytä kun tarvitset ai strategy & governance-tason tukea vastaavaan tehtävään."
---

# AI-Native Business Model Canvas

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Suunnittelee siirtymän perinteisestä "AI-enhanced" (tekoälyllä parannellusta)
liiketoiminnasta "AI-native" (tekoälynatiiviin) liiketoimintamalliin —
liiketoimintamalliin, joka on rakennettu alusta alkaen tekoälyn varaan ja jonka
koko arvotarjooma riippuu ML-ekosysteemistä.

## Ankkurointi tutkimukseen

- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — laajennettu AI Business Model Canvas
- Business Model Canvas (Osterwalder & Pigneur) — pohjarakenne, jota tämä
  kehys laajentaa neljällä AI-spesifillä linssillä

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. **Arvolupaus (Value Proposition).** Määritä miten tekoäly personoi, skaalaa
   tai luo uutta arvoa reaaliajassa — ei vain nopeuta olemassa olevaa prosessia.
   Esimerkki: hyperpersonoitu oppimisalusta, joka mukauttaa sisältöä ja sävyä
   käyttäjän tunnetilan mukaan. Testaa: jos tekoäly poistettaisiin, romahtaisiko
   arvolupaus vai jäisikö se vain hitaammaksi? (Jälkimmäinen = AI-enhanced,
   ei AI-native.)
2. **Avainresurssit (Key Resources).** Tunnista proprietary data — uniikki data,
   jota kilpailijat eivät voi helposti kopioida tai hankkia. Kartoita
   algoritmit ja orkestrointikerros yrityksen ydinomaisuutena, ei
   tukiprosessina.
3. **Kustannusrakenne (Cost Structure).** Mallinna mallien kouluttamisen ja
   pyörittämisen (inference-kustannukset) talous: pilvilaskennan hinnoittelu,
   API-kustannukset skaalautuessa, ja miten nämä kustannukset käyttäytyvät
   käyttäjä-/transaktiomäärän kasvaessa (lineaarisesti vai alilineaarisesti).
4. **Ekosysteemi ja kumppanuudet.** Päätä mitä malleja/kyvykkyyksiä rakennetaan
   itse (Build), mitä hyödynnetään valmiina rajapintoina (Utilize) ja keiden
   kanssa partneroidutaan (Partner). Tähän päätökseen syvemmin:
   `../build-vs-buy-vs-partner-ai/SKILL.md`.
5. **Data flywheel -tarkistus.** Arvioi ruokkiiko käyttö dataa takaisin malliin
   niin, että tuote paranee itsestään käytön myötä — tämä on yksi keskeisimmistä
   eroista AI-enhanced- ja AI-native-mallin välillä.
6. Tuota jäsennelty tulos (canvas-taulukko tai vastaava, ks. `../../references/`
   kun lisätty) ja validoi se sidosryhmillä tai omalla kokemuspohjaisella
   tarkistuslistalla.

## Mitä tämä skilli EI tee

- Ei tee lopullista liiketoimintamallipäätöstä puolestasi — tuottaa jäsennellyn
  luonnoksen ihmisen päätöksenteon tueksi.
- Ei vahvista tarkkoja inference- tai pilvikustannuslukuja muistista — käyttää
  käyttäjän antamia lähtöarvoja tai merkitsee oletuksen selvästi
  (`[oletus — tarkista]`).
- Ei tee build-vs-buy-vs-partner-päätöstä lopullisesti — jäsentää sen osana
  canvasia mutta viittaa syvempään analyysiin toisessa skillissä.
- Ei arvioi teknistä toteutettavuutta tai PoC-rajausta — se on
  `ai-use-case-feasibility-and-poc-scoping`-skillin tehtävä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä
omaa kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt ja heuristiikat tässä tekniikassa
- konkreettiset mallipohjat (`../../references/`-kansioon, esim. canvas-template)
- referenssitapaukset / omat caset AI-native-liiketoimintamalleista
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../ai-opportunity-portfolio/SKILL.md` —
  Tunnistaa ja priorisoi AI-käyttötapaukset ennen liiketoimintamallin suunnittelua.
- Samassa pakissa seuraavaksi: `../ai-use-case-feasibility-and-poc-scoping/SKILL.md`
  — Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen.
- Syventävä skilli ekosysteemipäätökseen: `../build-vs-buy-vs-partner-ai/SKILL.md`
- Liittyvä skilli toisessa pakissa (kun malli on validoitu ja tarvitaan täysi
  liiketoimintaperustelu): `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
