---
name: ai-output-curation-and-quality-control
description: "Suunnittelee laadunvalvonta- ja kuratointiprosessin AI:n tuottamalle sisällölle tai päätöksille — siirtymä 'tekijästä' 'kuraattoriksi': mikä tarkistetaan, kuka tarkistaa, ja millä kriteereillä ennen julkaisua tai käyttöä."
---

# AI Output Curation & Quality Control

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Suunnitella prosessi, jolla AI:n tuottamaa sisältöä tai päätöksiä
arvioidaan, korjataan ja hyväksytään ennen käyttöä — rooli, jossa ihminen
ei enää tuota sisältöä alusta ("tekijä") vaan arvioi ja ohjaa AI:n
tuotosta kohti brändinmukaista, eheää ja luotettavaa lopputulosta
("kuraattori").

## Ankkurointi tutkimukseen

- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — "kuratointi ja laadunvalvonta: siirtymä tekijästä
  kuraattoriksi", osana mallintamisen ja muotoilun kompetenssialuetta.
- Human-in/on/outside-the-loop-malli, ks.
  `../../../specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design/SKILL.md`
  — tämä skilli soveltaa samaa mallia nimenomaan sisällön/tuotoksen
  laatuun yleisen prosessisuunnittelun sijaan.

## Rakenne (luonnos — täydennettävä)

1. Määritä mitä AI tuottaa (teksti, koodi, kuva, päätössuositus,
   luokittelu) ja mihin sitä käytetään — sisäiseen vai asiakkaalle
   näkyvään tarkoitukseen?
2. Määritä laatukriteerit ennen kuin AI alkaa tuottaa: mitä "hyvä"
   tarkoittaa tässä tuotoksessa (faktantarkkuus, brändinmukaisuus, sävy,
   oikeellisuus, eheys)?
3. Valitse tarkistuksen taso human-in/on/outside-the-loop-mallilla (ks.
   `../../../specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design/SKILL.md`):
   korkean panoksen/riskin tuotokset tarkistetaan aina ennen julkaisua,
   matalamman riskin tuotoksia voidaan valvoa pistokokein.
4. Nimeä kuraattori(t) — kuka omistaa laadun, ja mikä on heidän roolinsa:
   eivät enää tuota sisältöä alusta, vaan arvioivat, korjaavat ja
   hyväksyvät/hylkäävät AI:n tuotoksen.
5. Rakenna tarkistuslista tai rubriikki, jota kuraattori käyttää
   johdonmukaisesti — subjektiivinen "tuntuu hyvältä" ei skaalaudu.
6. Suunnittele palautesilmukka: miten kuraattorin korjaukset syötetään
   takaisin promptiin tai järjestelmään, jotta samat virheet eivät
   toistu (closed-loop-ajattelu).
7. Seuraa laatua ajan myötä: kuinka suuri osuus AI:n tuotoksista menee
   läpi ilman korjauksia — tämä kertoo, onko prosessi kypsymässä kohti
   vähemmän ihmisvalvontaa vai ei.

## Mitä tämä skilli EI tee

- Ei arvioi AI-mallin teknistä suorituskykyä (esim. tarkkuus-/recall-
  mittarit) — se on tekninen/data science -tehtävä, tämä skilli on
  liiketoiminnallinen laadunvarmistusprosessi.
- Ei poista tarvetta ihmisvalvonnalle korkean riskin tuotoksissa vain
  koska prosessi on olemassa — kuratointiprosessi täydentää, ei korvaa,
  vastuullisen AI:n periaatteita (ks.
  `../responsible-ai-and-governance-check/SKILL.md`).
- Ei tee lopullista hyväksymis-/hylkäämispäätöstä puolestasi yksittäisestä
  tuotoksesta.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt siitä, milloin pistokoevalvonta riittää vs. milloin
  tarvitaan 100 %:n tarkistus
- konkreettiset mallipohjat (`../../references/`-kansioon, esim.
  kuratointirubriikki)
- referenssitapaukset / omat caset AI-tuotosten laadunvalvonnasta
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa: `../responsible-ai-and-governance-check/SKILL.md`
- Liittyvä skilli toisessa pakissa:
  `../../../specialisation-packs/ai-native-startup-design/skills/closed-loop-process-and-human-oversight-design/SKILL.md`,
  `../../../change-and-communication/skills/workshop-and-facilitation-design/SKILL.md`
  (kuraattoritiimin kouluttaminen).
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
