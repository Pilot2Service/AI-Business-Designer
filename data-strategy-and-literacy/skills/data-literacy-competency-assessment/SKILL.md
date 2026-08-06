---
name: data-literacy-competency-assessment
description: "Arvioi organisaation tai tiimin datalukutaidon nelikenttäkehyksellä (Datan ymmärtäminen, Datasta toimintaan, Datan kautta vaikuttaminen, Etiikka & yksityisyys) ja neliportaisella kypsyystikapuulla, roolikohtaisesti eriytettynä. Käytä ennen datastrategian tai AI-hankkeen käynnistämistä, kun pitää tunnistaa mistä osaamisvaje estää datan hyödyntämistä."
---

# Data Literacy Competency Assessment

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Datalukutaito ei tarkoita, että jokaisen pitää osata kirjoittaa SQL-
kyselyitä. Se tarkoittaa kykyä ymmärtää, arvioida ja soveltaa dataa
päätöksenteossa. Kun AI- tai datahanke epäonnistuu organisatorisista
syistä (ei teknisistä), syy on usein osaamisvajeessa jossain neljästä
osa-alueesta — ei työkalussa. Tämä skilli tuottaa rakenteisen arvion
siitä, missä osa-alueessa ja millä organisaatiotasolla vaje on, jotta
kehitystoimet kohdistetaan oikein sen sijaan että "koulutetaan kaikki
kaikkeen".

## Ankkurointi tutkimukseen

- DALI-tyyppinen datalukutaitokehys (usean lähteen synteesi, kansalais-
  ja ammattilaistason datalukutaitomääritelmistä): neljä pääelementtiä —
  Datan ymmärtäminen, Datasta toimintaan, Datan kautta vaikuttaminen ja
  osallistuminen, Etiikka & yksityisyys läpileikkaavana teemana.
- Ackoff, Russell L. — DIKW-hierarkia (*Data, Information, Knowledge,
  Wisdom*, 1989) kypsyystikapuun taustalla: data itsessään ei ole
  tietoa, tieto ei ole ymmärrystä, ymmärrys ei ole viisautta toimia
  oikein.
- DAMA International — DAMA-DMBOK (Data Management Body of Knowledge)
  ammattistandardina data governance -osaamisen määrittelyssä
  (ammattikuntastandardi samaan tapaan kuin BABOK/PMI/SFIA muualla
  tässä repossa).

## Rakenne (luonnos — täydennettävä)

1. **Arvioi neljä osa-aluetta erikseen** — älä anna yhtä kokonaispistettä,
   koska organisaatio on tyypillisesti epätasainen osa-alueiden välillä:
   - **A. Datan ymmärtäminen (Understanding):** ymmärretäänkö mitä data
     on, mistä se tulee, kuka sen omistaa, ja että "data on edustus
     todellisuudesta, ei todellisuus itse" (ks.
     `../data-bias-and-quality-critical-reading/SKILL.md`)?
   - **B. Datasta toimintaan (Acting):** osataanko arvioida datan laatua,
     tunnistaa harhaanjohtava raportointi, ja johtaako data oikeasti
     päätöksiin ja käyttäytymisen muutokseen — vai kerätäänkö "nice-to-
     know"-mittareita jotka eivät johda mihinkään?
   - **C. Datan kautta vaikuttaminen (Engaging):** osataanko syntetisoida,
     visualisoida ja kertoa data tarinana, joka saa päätöksentekijän
     toimimaan (ks.
     `../data-storytelling-and-business-translation/SKILL.md`)?
   - **D. Etiikka & yksityisyys:** ymmärretäänkö eettiset ja juridiset
     rajat datan keräämisessä ja käytössä (erityisesti AI-malleissa) —
     tämä on läpileikkaava teema kaikissa kolmessa muussa, ei erillinen
     vaihe.
2. **Käytä neliportaista kypsyystikapuuta jokaiselle osa-alueelle:**
   - **Taso 1 — Ei-tietoinen:** dataa käytetään ilman että sen alkuperää
     tai rajoituksia kyseenalaistetaan.
   - **Taso 2 — Tietoinen:** rajoitukset tunnistetaan, mutta niitä ei
     systemaattisesti huomioida päätöksenteossa.
   - **Taso 3 — Soveltava:** rajoitukset huomioidaan systemaattisesti,
     data johtaa toistuvasti oikeisiin päätöksiin.
   - **Taso 4 — Sulautunut:** datalukutaito on osa organisaation
     oletusarvoista toimintatapaa, ei erillinen taito jota pitää
     erikseen muistaa käyttää.
   Merkitse jokaiselle osa-alueelle (A-D) taso 1-4 erikseen — organisaatio
   voi olla tasolla 3 ymmärtämisessä mutta tasolla 1 vaikuttamisessa.
3. **Eriytä arvio roolin mukaan** — sama datalukutaitovaatimus ei koske
   kaikkia:
   - **Johto/päättäjät** tarvitsevat ennen kaikkea C (vaikuttaminen —
     osattava vaatia ja tulkita dataa tarinana) ja D (etiikka — vastuu
     päätöksistä).
   - **Analyytikot/data-ammattilaiset** tarvitsevat ennen kaikkea A
     (ymmärtäminen) ja B (toimintaan vieminen) syvällisesti.
   - **Linjaesihenkilöt/loppukäyttäjät** tarvitsevat riittävän tason A:ta
     (osata kyseenalaistaa) ja D:tä (osata tunnistaa eettiset riskit
     omassa työssään) — ei välttämättä syvää B/C-osaamista.
   Jos koko organisaatiota koulutetaan samalla ohjelmalla riippumatta
   roolista, se on tyypillisin datalukutaito-investoinnin hukka.
4. **Tunnista suurin pullonkaula, älä yritä korjata kaikkea kerralla.**
   Datalukutaitoketju on yhtä vahva kuin sen heikoin lenkki: jos johto on
   tasolla 1 vaikuttamisessa (C), paras analyysi (A/B tasolla 4) ei
   koskaan johda päätökseen, koska sitä ei osata tulkita tai siihen ei
   luoteta. Priorisoi kehitystoimet sen mukaan, missä osa-alueessa/
   roolissa heikoin lenkki on, ei sen mukaan missä on helpoin kouluttaa.
5. **Tuota arvio taulukkona:** rooli × osa-alue (A-D) × taso (1-4) ×
   suurin havaittu riski kyseisessä solussa. Tämä taulukko on skillin
   ensisijainen tuotos, ei pitkä sanallinen kuvaus.

## Mitä tämä skilli EI tee

- Ei suunnittele itse koulutusohjelmaa tai sen sisältöä — tuottaa
  diagnoosin, jonka pohjalta koulutus tai muu kehitystoimi suunnitellaan
  erikseen.
- Ei arvioi yksittäisten henkilöiden osaamista nimellä — arvioi rooleja
  ja organisaatiotasoja, ei yksilöitä.
- Ei korvaa teknistä data-arkkitehtuurin tai -infrastruktuurin arviointia
  — arvioi ihmisten kykyä käyttää ja tulkita dataa, ei järjestelmien
  teknistä kuntoa.
- Ei vahvista lukuja tai kypsyystasoja muistista — perustaa arvion
  käyttäjän antamiin havaintoihin (haastattelut, kysely, havainnointi)
  tai merkitsee oletuksen selvästi (`[oletus — tarkista]`).

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- konkreettinen haastattelu-/kyselypohja kunkin osa-alueen (A-D) tason
  arvioimiseksi (`../../references/`-kansioon)
- omia havaintoja siitä, mikä rooli/osa-alue-yhdistelmä on useimmin
  heikoin lenkki eri toimialoilla
- esimerkkejä siitä, miten epätasapainoinen datalukutaito (esim. vahva
  analytiikka, heikko johdon vaikuttaminen) on estänyt hankkeen etenemisen

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Samassa pakissa seuraavaksi (jos C-osa-alue on heikko):
  `../data-storytelling-and-business-translation/SKILL.md`
- Samassa pakissa seuraavaksi (jos A-osa-alue on heikko):
  `../data-bias-and-quality-critical-reading/SKILL.md`
- Liittyvä skilli toisessa pakissa: `../../../change-and-communication/skills/workshop-and-facilitation-design/SKILL.md`
  — jos diagnoosin pohjalta suunnitellaan koulutus-/fasilitointisessio.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
