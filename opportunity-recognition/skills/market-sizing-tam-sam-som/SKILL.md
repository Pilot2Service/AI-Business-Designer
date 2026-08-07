---
name: market-sizing-tam-sam-som
description: "Laskee markkinan koon ja aidosti saavutettavan osuuden kvantitatiivisesti. Käytä kun tarvitset opportunity recognition-tason tukea vastaavaan tehtävään."
---

# Market Sizing (TAM/SAM/SOM)

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Laskee markkinan koon ja aidosti saavutettavan osuuden kvantitatiivisesti.

## Ankkurointi tutkimukseen

- stratarts — market-opportunity-analyzer
- Business Opportunity Scout (buYoung)

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
- Ei vahvista markkinakokolukuja muistista — käyttää käyttäjän antamia lähtöarvoja tai merkitsee oletuksen [oletus — tarkista].

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

- Samassa pakissa seuraavaksi: `../competitive-and-five-forces-mapping/SKILL.md` — Kartoittaa kilpailudynamiikan ja toimialan rakenteelliset voimat.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
- `../../../meta/external-data-mcp.md` — valinnainen ulkoinen data-MCP (Market
  Sizing MCP Server / TAM-MCP-Server) laskelman pohjadataksi tai
  ristiintarkistukseksi, jos käyttäjän ympäristössä sellainen on kytkettynä. Ei
  riippuvuus — skilli toimii ilmankin.
- `../agents/market-sizing-cross-validator.md` — delegoitava agentti joka
  ristiintarkistaa tämän skillin tuottaman laskelman ennen kuin lukua käytetään
  business casessa
