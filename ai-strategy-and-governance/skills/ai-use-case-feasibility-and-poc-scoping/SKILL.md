---
name: ai-use-case-feasibility-and-poc-scoping
description: "Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen. Käytä kun tarvitset ai strategy & governance-tason tukea vastaavaan tehtävään."
---

# AI Use Case Feasibility & PoC Scoping

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen.

## Ankkurointi tutkimukseen

- Perplexity-tutkimus — PoC-määrittely tuotannollistamiseen asti

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

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
- Ei tee teknistä arkkitehtuurisuunnittelua tai mallivalintaa puolestasi — rajaa PoC:n laajuuden ja onnistumiskriteerit.

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

- Samassa pakissa seuraavaksi: `../responsible-ai-and-governance-check/SKILL.md` — Tarkistaa AI-aloitteen sääntely-, riski- ja eettisyysnäkökulmat. Syvempään EU AI Act -compliance-analyysiin käytä tämän workspacen tekoalysaantely-plugineja (tekoaly-luokittelu, tekoaly-velvoitteet, tekoaly-vaatimustenmukaisuus).
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
