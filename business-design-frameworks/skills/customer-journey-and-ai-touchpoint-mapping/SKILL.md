---
name: customer-journey-and-ai-touchpoint-mapping
description: "Kartoittaa asiakkaan palvelupolun vaiheet ja kitkakohdat, ja sijoittaa AI:n palvelupolulle vain niihin kohtiin, joissa se tuottaa aidosti arvoa asiakkaalle — ei teknologia edellä."
---

# Customer Journey & AI Touchpoint Mapping

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Kartoittaa asiakkaan palvelupolku vaihe vaiheelta asiakkaan näkökulmasta,
tunnistaa kitkakohdat, ja päättää tietoisesti mihin kohtiin polkua AI
kannattaa sijoittaa — vain sinne missä se poistaa aidon kitkan tai luo
uutta arvoa, ei kaikkialle missä se on teknisesti mahdollista.

## Ankkurointi tutkimukseen

- Service design / customer journey mapping -perinne (yleisesti tunnettu
  palvelumuotoilun tekniikka, esim. Stickdorn & Schneider, *This Is
  Service Design Thinking*).
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — konseptoinnin ja mallintamisen osio: strategiset
  tavoitteet käännetään palvelupoluiksi ja prototyypeiksi, ja AI
  sijoitetaan polulle arvoa tuovalla tavalla.

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. Valitse tarkasteltava asiakaspolku (esim. ostoprosessi, onboarding,
   tukiprosessi) ja rajaa sen alku- ja loppupiste.
2. Kartoita palvelupolun vaiheet asiakkaan näkökulmasta kronologisesti —
   mitä asiakas tekee, ajattelee ja tuntee kussakin vaiheessa.
3. Tunnista kitkakohdat (pain points): missä vaiheissa asiakas kokee
   turhautumista, epävarmuutta, hidastumista tai tarpeetonta vaivaa?
4. Kussakin kitkakohdassa kysy: onko tämä ongelma, jossa tekoäly voisi
   tuoda aidosti arvoa asiakkaalle — ei vain sisäistä tehokkuutta? Käytä
   `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`:n
   triagia (ennustus/luokittelu/generointi + datan saatavuus) tähän
   arviointiin.
5. Sijoita AI-kosketuspisteet (AI touchpoints) palvelupolulle vain niihin
   kohtiin, joissa ne poistavat aidon kitkan tai luovat uutta arvoa —
   vältä AI:n lisäämistä pelkästään koska se on mahdollista.
6. Tarkista kokonaiskuva: tuottaako AI-kosketuspisteiden summa
   yhtenäisen, johdonmukaisen kokemuksen vai hajanaisen kokoelman
   pistemäisiä tekoälyominaisuuksia?
7. Tuota jäsennelty palvelupolkukartta (vaihe, kitkakohta, AI-kosketuspiste
   tai ei, perustelu) ja validoi se asiakasdatalla tai -haastatteluilla,
   ei vain sisäisellä oletuksella.

## Mitä tämä skilli EI tee

- Ei korvaa oikeaa asiakastutkimusta — kitkakohtien tunnistus perustuu
  parhaimmillaan oikeaan asiakasdataan, ei pelkkään sisäiseen oletukseen.
- Ei tee AI-toteutuspäätöstä puolestasi — ks.
  `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
  ja `ai-use-case-feasibility-and-poc-scoping` tekniseen/liiketoiminnalliseen
  arviointiin.
- Ei ole sama asia kuin `../value-chain-mapping/SKILL.md` — arvoketju
  katsoo yrityksen sisäisiä toimintoja, tämä skilli katsoo asiakkaan
  kokemusta ulkoa käsin.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt siitä, milloin AI-kosketuspiste kannattaa lisätä
  palvelupolulle vs. milloin ei
- konkreettiset mallipohjat (`../../references/`-kansioon, esim.
  journey map -template)
- referenssitapaukset / omat caset onnistuneesta tai epäonnistuneesta
  AI-kosketuspisteen sijoittelusta
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Liittyvä skilli samassa pakissa: `../value-chain-mapping/SKILL.md`
  (täydentävä sisäinen näkökulma), `../strategy-canvas-and-value-curve/SKILL.md`
  (kitkakohdat voivat olla erottautumistekijöitä kilpailijoihin nähden).
- Liittyvä skilli toisessa pakissa:
  `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`,
  `../../../specialisation-packs/ai-native-startup-design/skills/customer-vision-to-jtbd/SKILL.md`
  (JTBD-pohjainen asiakasymmärrys tukee palvelupolun rakentamista).
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
