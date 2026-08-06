---
name: data-bias-and-quality-critical-reading
description: "Lukee annetun datasetin tai raportin kriittisesti ennen kuin sen perusteella tehdään päätöksiä tai koulutetaan AI-malli: tunnistaa puuttuvat ryhmät, vinoumatyypit (valinta, selviytyjä, historiallinen, mittaus, aggregointi) ja erottaa turhamaisuusmetriikan päätöksiä ohjaavasta mittarista. Käytä aina ennen datapohjaisen väitteen, mallin tai suosituksen hyväksymistä sellaisenaan."
---

# Data Bias & Quality Critical Reading

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin ja kallein datavirhe: datan hyväksyminen kyseenalaistamattomana
totuutena. Data on aina jonkun valinnan, mittauksen ja historian tulos —
se on **edustus todellisuudesta, ei todellisuus itse** (ks. pakin
`../../CLAUDE.md`). Kun AI-malli koulutetaan vinoutuneella datalla tai
päätös tehdään puutteellisen raportoinnin perusteella, virhe ei näy datassa
itsessään — se näkyy vasta lopputuloksessa, usein liian myöhään. Tämä
skilli tuottaa systemaattisen tarkistuksen ennen sitä hetkeä.

## Ankkurointi tutkimukseen

- Datalukutaidon "Datan ymmärtäminen" -osa-alue (ks.
  `../data-literacy-competency-assessment/SKILL.md`): kriittinen ajattelu
  datan alkuperästä, omistajuudesta ja edustavuudesta on datalukutaidon
  perusta, ei erillinen erikoisosaaminen.
- Tilastotieteen ja koneoppimisen vakiintunut vinoumataksonomia (usean
  lähteen synteesi): selection bias, survivorship bias, historical/label
  bias, measurement bias, aggregation bias — yleisesti tunnetut,
  toistuvat vinoumatyypit joita ei ole sidottu yhteen tuotteeseen tai
  yritykseen.
- "Vanity metric vs. actionable metric" -erottelu (lean-analytiikka-
  perinne): mittari on hyödytön päätöksenteolle, jos se ei muuttaisi
  mitään päätöstä riippumatta siitä, mihin suuntaan se liikkuu.

## Rakenne (luonnos — täydennettävä)

1. **Kysy ensin alkuperäkysymykset** jokaisesta merkittävästä datasetistä:
   mistä tämä data tulee, kuka sen keräsi ja miksi, ja kuka omistaa sen
   tänään? Jos et pysty vastaamaan kaikkiin kolmeen, älä vielä tee
   päätöstä datan perusteella — selvitä alkuperä ensin.
2. **Käy läpi viisi vinoumatyyppiä eksplisiittisesti** jokaiselle
   päätöksiä ohjaavalle datasetille:
   - **Valintavinouma (selection bias):** ketkä/mitkä tapaukset päätyivät
     datasettiin ja ketkä/mitkä jäivät systemaattisesti ulos? (esim.
     vain asiakaspalveluun yhteyttä ottaneet asiakkaat, ei kaikki
     asiakkaat)
   - **Selviytyjävinouma (survivorship bias):** näkyykö datassa vain ne
     tapaukset jotka "selvisivät" prosessista (esim. vain hyväksytyt
     hakemukset, ei hylätyt), jolloin epäonnistumisen syyt jäävät
     näkymättömiin?
   - **Historiallinen/leimavinouma (historical/label bias):** heijastaako
     data menneisyyden epätasa-arvoa tai yksipuolista päätöksentekoa
     (esim. ketä on aiemmin ylennetty tai kenelle myönnetty luottoa) niin,
     että malli oppii toistamaan sen tulevaisuudessa uutena "totuutena"?
   - **Mittausvinouma (measurement bias):** onko käytetty muuttuja hyvä
     approksimaatio sille mitä oikeasti haluttiin mitata, vai mitataanko
     jotain mikä on vain helppo mitata (esim. klikit todellisen
     asiakastyytyväisyyden sijaan)?
   - **Aggregointivinouma (aggregation bias):** katoaako oleellinen
     vaihtelu, kun data yhdistetään keskiarvoiksi tai kokonaissummiksi
     (esim. keskimääräinen käyttöaste peittää sen, että kaksi
     asiakasryhmää käyttäytyvät täysin eri tavoin)?
   Merkitse jokaisesta löydetystä vinoumasta: mikä tyyppi, mikä on
   todennäköinen vaikutussuunta, ja onko se korjattavissa vai vain
   huomioitavissa.
3. **Kysy eksplisiittisesti mitä datasta puuttuu ja kenen näkökulma
   puuttuu.** Puuttuva data ei ole neutraali — se on yleensä
   systemaattisesti puuttuvaa jonkun ryhmän tai tilanteen osalta. Nimeä
   puuttuva ryhmä/tilanne, älä vain totea "dataa puuttuu".
4. **Erota turhamaisuusmetriikka toimintaan johtavasta mittarista.**
   Testaa jokainen esitetty mittari kysymyksellä: *"Jos tämä luku
   muuttuisi 20 % suuntaan tai toiseen, muuttaisiko se jotain päätöstä?"*
   Jos vastaus on ei, mittari on "nice-to-know" eikä ansaitse paikkaa
   päätöksenteon ytimessä — se voi silti olla hyödyllinen konteksti,
   mutta sitä ei pidä esittää keskeisenä perusteluna.
5. **Arvioi datan tuoreus ja edustavuus ajassa.** Onko data kerätty
   olosuhteissa, jotka vastaavat nykytilannetta (esim. ei kerätty
   poikkeuksellisen ajanjakson aikana), ja onko se riittävän tuore
   päätökseen jota sillä ollaan perustelemassa?
6. **Tuota lyhyt "luotettavuusmerkintä" jokaiselle keskeiselle
   datalöydökselle** ennen sen viemistä eteenpäin: mitä vinoumia
   tunnistettiin, kuinka vakavia ne ovat päätöksen kannalta, ja
   voidaanko löydöstä käyttää sellaisenaan vai vaatiiko se lisä-
   validointia.

## Mitä tämä skilli EI tee

- Ei korjaa dataa teknisesti (esim. uudelleenpainotusta, imputointia) —
  tunnistaa ja nimeää vinouman, korjaus on erillinen tekninen tehtävä.
- Ei väitä, että kaikki vinouma pitää poistaa ennen kuin dataa voi käyttää
  — moni päätös voidaan tehdä tunnetulla, dokumentoidulla vinoumalla,
  kunhan se on näkyvissä eikä piilossa.
- Ei korvaa tilastollista tai koneoppimisen teknistä auditointia
  (esim. mallin fairness-metriikkaa) — tuottaa liiketoiminnallisen,
  kriittisen ensiluvun ennen syvempää teknistä analyysiä.
- Ei vahvista lukuja tai vinoumaväitteitä muistista — perustaa arvion
  käyttäjän antamaan dataan tai merkitsee oletuksen selvästi
  (`[oletus — tarkista]`).

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia esimerkkejä vinoumista jotka olet löytänyt asiakasdatasta ja mitä
  ne olisivat aiheuttaneet jos niitä ei olisi huomattu
- konkreettinen tarkistuslistapohja viiden vinoumatyypin läpikäyntiin
  (`../../references/`-kansioon)
- nyrkkisääntöjä siitä, millä toimialoilla/datatyypeillä mikäkin
  vinoumatyyppi on yleisin

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (jos rooli on vielä epäselvä): `../data-role-diagnosis/SKILL.md`
- Samassa pakissa seuraavaksi: `../data-storytelling-and-business-translation/SKILL.md`
  — käytä tämän skillin luotettavuusmerkintöjä, kun käännät löydöksen
  tarinaksi äläkä piilota tunnettua vinoumaa kertomuksesta.
- Liittyvä skilli toisessa pakissa: `../../../business-case-and-analysis/skills/assumption-and-evidence-audit/SKILL.md`
  — laajempi oletusten ja evidenssin tarkistus koko business casen tasolla.
- Liittyvä skilli toisessa pakissa: `../../../ai-strategy-and-governance/skills/responsible-ai-and-governance-check/SKILL.md`
  — jos vinouma vaikuttaa AI-mallin koulutusdataan, tarkista myös
  vastuullisuus-/riskinäkökulma.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
