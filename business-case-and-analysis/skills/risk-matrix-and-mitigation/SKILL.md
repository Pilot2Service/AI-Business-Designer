---
name: risk-matrix-and-mitigation
description: "Tunnistaa ja pisteyttää riskit (todennäköisyys × vaikutus) ja suunnittelee mitigoinnit. Käytä kun tarvitset business case & analysis-tason tukea vastaavaan tehtävään."
---

# Risk Matrix & Mitigation

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Tunnistaa ja pisteyttää riskit (todennäköisyys × vaikutus) ja suunnittelee mitigoinnit.

## Ankkurointi tutkimukseen

- ISO 31000
- PMI riskienhallinta

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
- Ei poista riskiä — tekee sen näkyväksi ja jäsentää mitigointivaihtoehdot.

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

- Kun tämä vaihe on valmis, siirry pakkiin `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
