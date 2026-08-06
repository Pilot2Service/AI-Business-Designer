---
name: ai-capability-roadmap
description: "Rakentaa organisaation AI-kyvykkyyskartan ja roadmapin nykytilasta tavoitetilaan kolmella horisontilla (0-6kk tehostus, 6-18kk muutos, 18-36kk uusi liiketoiminta) sekä AI Target Operating Model (ATOM) / Readiness Scorecard -kuvauksen ihmisen ja tekoälyn työnjaosta."
---

# AI Capability Roadmap

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Rakentaa organisaation AI-kyvykkyyskartan ja ajoitetun roadmapin
nykytilasta tavoitetilaan. Vastaa kysymykseen "MILLOIN mikäkin
priorisoitu AI-mahdollisuus toteutetaan", täydentäen
`../ai-opportunity-portfolio/SKILL.md`-skilliä, joka vastaa kysymykseen
"MITÄ kannattaa tehdä ja MINKÄ TYYPPINEN muutos se on".

## Ankkurointi tutkimukseen

- Perplexity-tutkimus — roadmapit ja liiketoimintakyvykkyyskartat
- Käyttäjän toimittama tutkimusraportti "Tekoälymahdollisuuksien ja
  -kapasiteetin tunnistamismenetelmät, viitekehykset ja osaamiset
  liiketoiminnassa" (2026) — kolmihorisonttinen Strategic AI Roadmap
  ja AI Target Operating Model (ATOM) / Readiness Scorecard -konsepti,
  osana asiantuntijapalvelutalojen (McKinsey [redacted], BCG,
  Accenture, [redacted]) discovery-toimeksiantojen luovutettavaa
  aineistoa.

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. **Ota syötteeksi priorisoitu portfolio** `../ai-opportunity-portfolio/SKILL.md`
   -skilliltä: valitut kohteet pisteineen, Value Play -luokituksineen
   (jos transformatiivinen) ja Deploy/Reshape/Invent-luokkineen.
2. **Sijoita jokainen kohde yhteen kolmesta horisontista:**
   - **Horisontti 1 — Tehostus (0–6 kk).** Nopeat, matalan riskin
     kohteet. Vastaa tyypillisesti "Quick Wins"-luokkaa
     `ai-opportunity-portfolio`-skillin 2x2-matriisissa ja usein
     "Deploy"-luokkaa Deploy-Reshape-Invent-taksonomiassa (valmiiden
     työkalujen käyttöönotto).
   - **Horisontti 2 — Muutos (6–18 kk).** Ydinprosessien
     uudelleensuunnittelu. Vastaa usein "Reshape"-luokkaa — vaatii
     organisaatiomuutosta, ei vain työkalun käyttöönottoa.
   - **Horisontti 3 — Uusi liiketoiminta (18–36 kk).** Transformatiiviset,
     uutta liikevaihtoa luovat kohteet. Vastaa usein "Invent"-luokkaa ja
     "Strategic Bets" -sijaintia 2x2-matriisissa.
   **Huomio:** horisontti ja Deploy/Reshape/Invent-luokka KORRELOIVAT
   mutta eivät ole sama asia — sama Reshape-tason mahdollisuus voi
   sijoittua Horisonttiin 1 TAI 2 riippuen resursseista ja
   riippuvuuksista. Älä automaattisesti kopioi luokkaa horisontiksi,
   arvioi ajoitus erikseen (riippuvuudet, resurssit, organisaation
   muutoskyky samanaikaisesti käynnissä oleviin hankkeisiin nähden).
3. **Rakenna AI Target Operating Model (ATOM) / Readiness Scorecard.**
   Kuvaa jokaiselle horisontille tai keskeiselle kyvykkyysalueelle:
   - **Ihmisen ja tekoälyn työnjako** — mitkä roolit/tehtävät ovat
     Automate/Augment/Human-Only (ks.
     `../task-level-decomposition-and-automation-fit/SKILL.md`) TÄSSÄ
     vaiheessa roadmapia, ja miten työnjako muuttuu horisontista toiseen
     siirryttäessä.
   - **Organisaation valmiustaso** kyvykkyysalueittain (esim. data-
     arkkitehtuuri, hallintomalli/governance, henkilöstön AI-lukutaito,
     muutosjohtamiskapasiteetti) — karkea asteikko (matala/keskitaso/
     korkea) riittää tässä vaiheessa, ei tarvitse tarkkaa kypsyysmallia.
   - **Kriittiset puuttuvat kyvykkyydet** jotka pitää rakentaa ENNEN
     kuin seuraavan horisontin kohteita voi aloittaa (esim. Horisontti
     2 vaatii usein dataputken, jota Horisontti 1 ei vielä tarvinnut).
4. **Tunnista horisonttien väliset riippuvuudet eksplisiittisesti.**
   Horisontti 2 ja 3 -kohteet nojaavat usein Horisontti 1:ssä
   rakennettuun infrastruktuuriin tai organisaation oppimiseen — merkitse
   nämä riippuvuudet roadmapiin, älä käsittele horisontteja toisistaan
   irrallisina.
5. Tuota jäsennelty tulos: horisontoitu roadmap (kohde → horisontti →
   riippuvuudet → ATOM-työnjakokuvaus) (ks. `../../references/` kun
   lisätty).
6. Validoi tulos sidosryhmillä tai omalla kokemuspohjaisella
   tarkistuslistalla. Varmista erityisesti että Horisontti 1
   -toteutukset eivät vaadi enemmän resursseja kuin organisaatio pystyy
   antamaan Horisontti 2:n suunnittelun rinnalla.

## Mitä tämä skilli EI tee

- Ei tee lopullista päätöstä puolestasi — tuottaa jäsennellyn luonnoksen ihmisen
  päätöksenteon tueksi.
- Ei vahvista lukuja, markkinatietoa tai kilpailijadataa muistista — käyttää käyttäjän
  antamia lähtöarvoja tai merkitsee oletuksen selvästi (`[oletus — tarkista]`).
- Ei sitouta budjettia tai resursseja — tuottaa roadmap-luonnoksen hyväksyttäväksi.
- Ei tee itse priorisointia — käyttää `../ai-opportunity-portfolio/SKILL.md`
  -skillin tuottamaa jo priorisoitua listaa syötteenä, ei arvioi
  mahdollisuuksien arvoa uudelleen.
- Ei rakenna täyttä organisaation AI-kypsyysmallia — ATOM/Readiness
  Scorecard tässä on karkea, roadmapia tukeva kuvaus, ei erillinen
  kypsyysauditointi.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt ja heuristiikat tässä tekniikassa — esim. kuinka
  monta Horisontti 1 -kohdetta organisaatio tyypillisesti pystyy
  ajamaan rinnakkain
- konkreettiset mallipohjat (`../../references/`-kansioon, esim.
  ATOM/Readiness Scorecard -template)
- referenssitapaukset / omat caset
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../ai-opportunity-portfolio/SKILL.md`
  — tuottaa priorisoidun listan, jonka tämä skilli aikatauluttaa.
- Kun tämä vaihe on valmis, siirry pakkiin `../../../change-and-communication/skills/stakeholder-communication-plan/SKILL.md`
- Liittyvä skilli samassa pakissa: `../ai-discovery-engagement-design/SKILL.md`
  — jos roadmap tuotetaan osana laajempaa discovery-toimeksiantoa,
  tämä skilli vastaa toimeksiannon Vaihe 4:ää.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
