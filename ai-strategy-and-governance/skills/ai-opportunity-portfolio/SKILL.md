---
name: ai-opportunity-portfolio
description: "Tunnistaa ja priorisoi AI-käyttötapaukset liiketoiminta-arvon ja toteutettavuuden mukaan. Käytä kun tarvitset ai strategy & governance-tason tukea vastaavaan tehtävään."
---

# AI Opportunity Portfolio

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Tunnistaa ja priorisoi AI-käyttötapaukset liiketoiminta-arvon ja toteutettavuuden mukaan.

## Ankkurointi tutkimukseen

- LinkedIn Skills on the Rise 2026 — AI Business Strategy
- Perplexity-tutkimus: Senior AI Business Designer (Solita/HP)
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — AI-mahdollisuuksien tunnistaminen strategisella tasolla

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. Määritä tilanne/konteksti, johon tätä skilliä sovelletaan. Lähde liikkeelle
   olemassa olevista kitkakohdista (pain points) ja arvoketjun pullonkauloista —
   ei teknologiasta.
2. **AI-soveltuvuuden triagi.** Kysy jokaisesta ehdokasongelmasta kaksi asiaa:
   (a) *Mitä tyyppiä ongelma on?* — ennustamis-, luokittelu- vai
   generointiongelma (tai näiden yhdistelmä)? Ongelmatyyppi ohjaa suoraan sitä,
   millaista mallia/ratkaisua tarvitaan ja mikä on realistinen aikataulu. (b)
   *Onko meillä tarvittava data ongelman ratkaisemiseksi* — vai pitäisikö data
   ensin hankkia/rakentaa? Ongelmat, joihin ei ole dataa eikä realistista
   dataa hankkimaan, eivät ole vielä AI-kelpoisia mahdollisuuksia.
3. **Datan data flywheel -potentiaali.** Arvioi tuottaako ratkaisu käytössä
   uniikkia dataa, joka parantaa mallia ajan myötä ja vahvistaa kilpailuetua
   (data flywheel -efekti) — vai onko kyse kertaluonteisesta datasta ilman
   itseään vahvistavaa silmukkaa.
4. **Agenttisuuden aste.** Erottele, riittääkö perinteinen automaatio
   (sääntöpohjainen/ennalta määrätty prosessi) vai vaatiiko mahdollisuus
   agenttista tekoälyä (itsenäistä päätöksentekoa monimutkaisissa,
   ennalta-arvaamattomissa tilanteissa) — agenttinen ratkaisu on kalliimpi
   rakentaa ja hallita, joten sen valinta pitää perustella.
5. Tuota jäsennelty tulos: priorisoitu lista mahdollisuuksia, joissa jokaiselle
   on merkitty ongelmatyyppi, datan saatavuus, flywheel-potentiaali ja
   automaatio- vs. agenttisuustarve (ks. `../../references/` kun lisätty).
6. Validoi tulos sidosryhmillä tai omalla kokemuspohjaisella tarkistuslistalla.
   Varmista erityisesti, että mahdollisuuksia ei arvioida erillisenä siilona
   vaan suhteessa organisaation olemassa oleviin strategisiin tavoitteisiin.

## Mitä tämä skilli EI tee

- Ei tee lopullista päätöstä puolestasi — tuottaa jäsennellyn luonnoksen ihmisen
  päätöksenteon tueksi.
- Ei vahvista lukuja, markkinatietoa tai kilpailijadataa muistista — käyttää käyttäjän
  antamia lähtöarvoja tai merkitsee oletuksen selvästi (`[oletus — tarkista]`).
- Ei arvioi teknistä toteutettavuutta syvällisesti — se on ai-use-case-feasibility-skillin tehtävä.

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

- Samassa pakissa seuraavaksi (liiketoimintamallin suunnittelu): `../ai-native-business-model-canvas/SKILL.md` — Suunnittelee siirtymän AI-enhanced-liiketoiminnasta AI-native-liiketoimintamalliin laajennetulla Business Model Canvasilla.
- Samassa pakissa seuraavaksi (tekninen validointi): `../ai-use-case-feasibility-and-poc-scoping/SKILL.md` — Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
