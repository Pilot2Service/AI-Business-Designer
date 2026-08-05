---
name: category-definition-and-modeling
description: "Mallintaa tuotteen tai liiketoiminnan suhteessa markkinakategorioihin: assosioida olemassa olevaan kategoriaan, laajentaa/uudelleenmääritellä kategoriaa, tai arvioida kokonaan uuden kategorian luomista."
---

# Category Definition & Modeling

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Mallintaa tuote tai liiketoiminta suhteessa markkinakategorioihin: joko
assosioida se olemassa olevaan kategoriaan, laajentaa tai uudelleenmääritellä
olemassa olevaa kategoriaa, tai arvioida kokonaan uuden kategorian
luomista. Kategoriapäätös ei ole vain brändäystä — se muokkaa suoraan sitä,
mihin asiakas vertaa tuotetta, keitä kilpailijoiksi mielletään, ja kuinka
suuri osa markkinan arvosta kategoriajohtajalle voi kertyä.

## Ankkurointi tutkimukseen

- Ramadan, A., Peterson, D., Lochhead, C. & Maney, K. (2016), *Play Bigger:
  How Pirates, Dreamers, and Innovators Create and Dominate Markets* —
  Category Design -koulukunta: kategoriakuninkuus (Category King) — yritys,
  joka rakentaa ja omistaa uuden kategorian, saa suhteettoman osan
  kategorian arvosta; "Lightning Strike" -konsepti kategorian
  lanseeraukseen; flywheel-efekti kategoriajohtajuuden vahvistamiseen ajan
  myötä.
- Kim, W. C. & Mauborgne, R. (2005), *Blue Ocean Strategy* — kilpailemattoman
  markkinatilan luominen erottamalla arvoinnovaatio nykyisistä
  kategoriarajoista; nelikenttäkehys (poista/vähennä/nosta/luo).
- Ries, A. & Trout, J., positiointiteoria — miten kategoria muokkaa
  asiakkaan mielikuvaa ja vertailukehystä ennen kuin tuotteen ominaisuuksia
  edes arvioidaan.

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

1. Kartoita nykyiset kategoriat, joihin tuote tai liiketoiminta voitaisiin
   luontevasti assosioida — mihin asiakas jo intuitiivisesti vertaisi tätä?
2. Arvioi kolme vaihtoehtoista kategoriastrategiaa:
   - **(a) Assosioidu olemassa olevaan kategoriaan.** Hyödynnä valmista
     asiakasymmärrystä ja ostologiikkaa, mutta kilpaile suoraan kategorian
     ehdoilla vakiintuneita toimijoita vastaan. Nopein ja halvin reitti.
   - **(b) Laajenna tai uudelleenmäärittele olemassa olevaa kategoriaa.**
     Tuo uusi ulottuvuus tai ala-kategoria, joka muuttaa vertailukehystä
     osittain omaksi eduksi. Keskitason resurssivaatimus.
   - **(c) Luo kokonaan uusi kategoria.** Irrota tuote olemassa olevista
     vertailukehyksistä. Korkea riski ja pitkä sykli (vaatii merkittävää
     markkinaedukaatiota), mutta onnistuessaan "kategoriakuningas" saa
     suhteettoman osan kategorian arvosta (Play Bigger).
3. Jos harkitset uutta tai laajennettua kategoriaa: testaa Blue Ocean
   -nelikentällä — mitkä toimialan itsestäänselvyydet voidaan **poistaa**,
   mitä voidaan **vähentää** selvästi alle toimialan standardin, mitä
   voidaan **nostaa** selvästi yli standardin, ja mitä täysin **uutta**
   voidaan luoda?
4. Arvioi kategoriapäätöksen resurssivaatimus rehellisesti: olemassa
   olevaan kategoriaan assosioituminen on nopein ja halvin, laajentaminen
   keskitasoinen, uuden kategorian luominen vaatii pitkäjänteistä
   markkinaedukaatiota ja merkittävää viestintäpanostusta.
5. Määritä kategorianimi ja -kuvaus, joka kiteyttää valitun position
   asiakkaan mielessä — kategorianimi on osa strategiaa, ei vain brändäystä.
6. Tunnista kategorian "flywheel" — mikä mekanismi vahvistaa
   kategoriajohtajuutta ajan myötä (verkostovaikutukset, kertyvä data,
   brändin muistijälki, jakelun laajuus)?
7. Pidä kategoriapäätös elävänä hypoteesina — markkinan reaktio
   (kilpailijoiden asemointi, asiakaspuhe, analyytikkoluokittelu) validoi
   tai haastaa valitun kategoriastrategian ajan myötä; älä lukitse
   kategoriaa liian aikaisin ilman markkinasignaalia.

## Mitä tämä skilli EI tee

- Ei takaa uuden kategorian onnistumista — uuden kategorian luominen on
  korkean riskin strategia, jonka onnistuminen vaatii merkittäviä
  resursseja ja pitkäjänteisyyttä.
- Ei tee lopullista kategoriapäätöstä puolestasi — jäsentää vaihtoehdot ja
  niiden riski-/resurssiprofiilin ihmisen päätöksenteon tueksi.
- Ei korvaa markkinatutkimusta asiakkaan nykyisistä mielikuvista — päätös
  pitää validoida oikealla asiakasymmärryksellä, ei vain sisäisellä
  pohdinnalla.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt siitä, milloin uuden kategorian luominen kannattaa
  tutkimuspohjaisille/deep tech -mahdollisuuksille vs. milloin ei
- konkreettiset mallipohjat (`../../references/`-kansioon)
- referenssitapaukset / omat caset onnistuneesta tai epäonnistuneesta
  kategoriapäätöksestä
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Edeltävät skillit samassa pakissa: `../layer-based-business-structuring/SKILL.md`,
  `../value-chain-mapping/SKILL.md` — täydentäviä tapoja jäsentää samaa
  liiketoimintaa ennen kategoriapäätöstä.
- Liittyvä skilli toisessa pakissa (kilpailuedun vahvuus osana
  mahdollisuuden arviointia): `../../../opportunity-recognition/skills/opportunity-value-assessment/SKILL.md`
- Liittyvä skilli toisessa pakissa: `../../../strategic-thinking/skills/strategic-intent-framing/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
