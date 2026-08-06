---
name: second-and-third-order-effects-mapping
description: "Ennakoi strategisen päätöksen tai AI-ratkaisun toisen ja kolmannen kertaluvun vaikutuksia — miten se muuttaa asiakaskäyttäytymistä, kilpailukenttää ja omaa organisaatiota ajan myötä, suoran ensivaikutuksen lisäksi."
---

# Second- & Third-Order Effects Mapping

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Nostaa esiin päätöksen tai ratkaisun vaikutukset, jotka jäävät helposti
huomaamatta koska ne eivät ole välittömiä: mitä ensimmäinen vaikutus
laukaisee seuraavaksi (toinen kertaluku), ja mitä se puolestaan laukaisee
laajemmin markkinassa, kilpailussa tai sääntelyssä (kolmas kertaluku).
Useimmat päätökset arvioidaan vain ensimmäisen kertaluvun vaikutuksen
perusteella — tämä skilli pakottaa katsomaan pidemmälle.

## Ankkurointi tutkimukseen

- Systeemiajattelu ja "second-order thinking" -tekniikka strategisessa
  päätöksenteossa (yleisesti tunnettu, mm. konsultoinnin "consequence
  scanning" -käytäntö).
- Liedtka (1998) — systeeminäkökulma (systems perspective) ja thinking in
  time; samat juuret kuin `../scenario-and-foresight/SKILL.md`, mutta
  tämä skilli operationalisoi nimenomaan kertaluku-ajattelun yhden
  päätöksen ympärille sen sijaan että rakentaisi laajempia vaihtoehtoisia
  tulevaisuuksia.
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — nostaa tämän eksplisiittisesti esiin AI-ratkaisun
  business case -arvioinnin yhteydessä: miten ratkaisu muuttaa
  asiakaskäyttäytymistä pitkällä aikavälillä, ja millaisia uusia
  kilpailijoita se voi houkutella markkinalle.

## Rakenne (luonnos — täydennettävä)

1. Määritä tarkasteltava päätös tai ratkaisu (esim. uusi AI-ominaisuus,
   hinnoittelumuutos, automaatio, uusi liiketoimintamalli).
2. Kartoita **ensimmäisen kertaluvun vaikutus**: mikä on suora, välitön
   seuraus? Tämä on yleensä ainoa vaikutus, joka huomioidaan
   päätöksenteossa oletusarvoisesti.
3. Kartoita **toisen kertaluvun vaikutukset**: mitä ensimmäinen vaikutus
   laukaisee seuraavaksi? Esimerkiksi miten asiakas todella *muuttaa*
   käyttäytymistään kun ratkaisu on ollut käytössä pidempään — ei vain
   ensireaktio.
4. Kartoita **kolmannen kertaluvun vaikutukset**: mitä toisen kertaluvun
   muutokset laukaisevat laajemmin — kilpailijoiden reaktiot, uudet
   markkinatulokkaat, sääntelyn kiristyminen, sidosryhmien odotusten
   muutos?
5. Kunkin kertaluvun kohdalla kysy erikseen: keneen tämä vaikuttaa
   (asiakas, kilpailija, oma organisaatio, sääntelijä, laajempi
   ekosysteemi), ja onko vaikutus todennäköisesti positiivinen,
   negatiivinen vai ambivalentti?
6. Tunnista, mitkä toisen/kolmannen kertaluvun vaikutuksista ovat
   riittävän todennäköisiä ja merkittäviä muuttaakseen alkuperäistä
   päätöstä — palaa tarvittaessa päätökseen ja säädä sitä.
7. Tuota jäsennelty vaikutusketju (1. → 2. → 3. kertaluku)
   päätöksenteon tueksi; merkitse selvästi mikä on perusteltu päättely ja
   mikä spekulaatio (`[oletus — tarkista]`).

## Mitä tämä skilli EI tee

- Ei ennusta tulevaisuutta varmuudella — toisen/kolmannen kertaluvun
  vaikutukset ovat uskottavia hypoteeseja, ei todennäköisyyslaskelmia.
- Ei korvaa `../scenario-and-foresight/SKILL.md`-skilliä — tämä skilli
  seuraa yhden päätöksen vaikutusketjua eteenpäin, scenario-and-foresight
  rakentaa vaihtoehtoisia tulevaisuuksia laajemmasta epävarmuudesta.
- Ei tee päätöstä puolestasi — nostaa esiin vaikutuksia joita ei muuten
  huomioitaisi, itse päätös jää ihmiselle.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omat nyrkkisäännöt siitä, kuinka pitkälle vaikutusketjua kannattaa
  seurata ennen kuin se muuttuu liian spekulatiiviseksi
- konkreettiset mallipohjat (`../../references/`-kansioon)
- referenssitapaukset / omat caset, joissa 2./3. kertaluvun vaikutus
  muutti alkuperäistä päätöstä
- mitä tässä ei tehdä (guardrailsit, tyypilliset virheet) — täydennä yllä olevaa listaa

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa: `../scenario-and-foresight/SKILL.md` (täydentävä,
  laajempi epävarmuuden käsittely), `../strategic-options-evaluation/SKILL.md`
  (vie vaikutusketjun havainnot vaihtoehtojen vertailuun).
- Liittyvä skilli toisessa pakissa:
  `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`,
  `../../../business-case-and-analysis/skills/risk-matrix-and-mitigation/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
