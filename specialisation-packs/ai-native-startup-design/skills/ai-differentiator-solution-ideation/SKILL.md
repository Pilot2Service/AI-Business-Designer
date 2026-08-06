---
name: ai-differentiator-solution-ideation
description: "Ideoi 3 keskenään erilaista AI-natiivia ratkaisusuuntaa valitulle AI-differentiaattoritarpeelle (AI wedge) kolmella linssillä — kilpailija-, tulevaisuus- ja yhdistä-pisteet-linssi — jotta tiimi ei rakastu ensimmäiseen ideaan."
---

# AI Differentiator Solution Ideation

*Tila: `draft`, `source_layer: owner` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin ideointivirhe: tartutaan ensimmäiseen ratkaisuideaan joka
tulee mieleen, eikä koskaan verrata sitä vaihtoehtoihin. Skilli pakottaa
kolmen aidosti erilaisen AI-natiivin ratkaisusuunnan ideoinnin yhdelle
valitulle AI-differentiaattoritarpeelle (AI wedge), käyttäen kolmea eri
näkökulmaa (linssiä) jotta suunnat eivät ole vain sama idea eri sanoin.

## Perustuu

- Ulkopuolisen "AI-first SaaS Product" -työpajan menetelmä, sovellettu
  omistajan toimesta omaan caseen — ks.
  `../../references/ai-first-saas-workshop-source.md` ja worked example
  `../../cases/ai-decision-coach-mvp-case.md` kohta 5. **Huom:** sovellettu
  toistaiseksi vain kerran (omistajan oma case) — ei laajasti validoitu.
- Sähköpostimarkkinoinnin personointiesimerkki työpajasta havainnollistaa
  "aidosti erilainen" -vaatimuksen: 1:1-historiapohjainen personointi vs.
  1:1-kontekstuaalinen sosiaalinen personointi vs. 1:ryhmä-klusteripohjainen
  personointi — kolme AI-natiivia lähestymistapaa samaan tarpeeseen
  (relevanssi), ei kolme muunnelmaa samasta ideasta.

## Rakenne (luonnos — täydennettävä)

1. **Ota lähtökohdaksi yksi valittu AI wedge**
   (`../customer-vision-to-jtbd/SKILL.md`-skillistä) — älä ideoi
   useammalle tarpeelle kerralla, se hajottaa vertailun.
2. **Ideoi ratkaisusuunta 1: kilpailijalinssi.** Kysy: miten olemassa
   olevat toimijat (TTOt, inkubaattorit, geneeriset AI-työkalut,
   konsultit) ratkaisevat tätä tarvetta tänään, ja mitä AI mahdollistaisi
   joka NIILLE ei ole mahdollista (skaala, jatkuvuus, personointi,
   nopeus)? Tavoite: erottuminen olemassa olevasta kilpailusta.
3. **Ideoi ratkaisusuunta 2: tulevaisuuslinssi.** Kysy: miten tämä
   tarve ratkaistiin ENNEN (työpajoissa, malleilla, post-it-lapuilla,
   yksin sovellettuina kehyksinä — raskas, energiaa kuluttava, aina
   kontekstiin sovitettava prosessi), ja miten se ratkaistaan
   TULEVAISUUDESSA kun konteksti rakentuu ja opetetaan jatkuvasti AI:lle,
   AI-mentori kysyy oikeat kysymykset yhteisen ymmärryksen
   saavuttamiseksi, ja käyttäjä on jatkuvassa vuorovaikutuksessa AI:n
   kanssa joka tuottaa jatkuvasti pieniä rakennuspalikoita (esim. ICP-
   määrittely, arvolupaus, tulomallihypoteesi)? Tavoite: kuvitella
   ratkaisu, joka ei vain digitoi vanhaa prosessia vaan muuttaa itse
   prosessin muotoa.
4. **Ideoi ratkaisusuunta 3: yhdistä-pisteet-linssi.** Kysy: mitkä muut
   erilliset tehtävät/aktiviteetit (a+b+c+d) tämä käyttäjä tekee tämän
   tarpeen ympärillä, jotka voitaisiin YHDISTÄÄ yhdeksi AI-natiiviksi
   kokemukseksi? Tavoite: ratkaisu joka syntyy usean erillisen askeleen
   yhdistämisestä, ei yhden askeleen tehostamisesta.
5. **Kirjaa jokaiselle kolmelle suunnalle:** nimi, AI-natiivi konsepti
   (2-3 lausetta — miten se toimii), pääasiallinen output käyttäjälle, ja
   miksi se on erottuva juuri kilpailijoihin/nykytilaan nähden (ei
   kopioitavissa staattisella tarkistuslistalla tai geneerisellä
   LLM-promptilla).
6. **Vertaile kolmea suuntaa rinnakkain** taulukossa: ydinarvo / miksi
   sopii valittuun AI wedgeen. Vastusta houkutusta valita heti — vie
   kaikki kolme `../rice-scoring-and-mvp-synthesis/SKILL.md`-skilliin
   objektiiviseen pisteytykseen ennen valintaa.

## Mitä tämä skilli EI tee

- Ei valitse MVP:tä puolestasi — tuottaa kolme vertailukelpoista
  vaihtoehtoa, valinta tehdään seuraavassa skillissä RICE-pisteytyksellä.
- Ei arvioi teknistä toteutettavuutta tai rakennuskustannusta — vain
  konseptin erottuvuutta. Toteutettavuus/effort arvioidaan
  `../rice-scoring-and-mvp-synthesis/SKILL.md`-skillissä.
- Ei takaa että kaikki kolme suuntaa ovat yhtä hyviä — tarkoituksella
  tuottaa myös heikompia/riskialttiimpia vaihtoehtoja, jotta vertailu on
  aito eikä keinotekoinen.

## [OWNER INPUT — täydennettävä]

Tämä skilli on sovellettu toistaiseksi yhteen caseen (omistajan oma case). Kun sovellat
sitä useampaan eri liiketoimintaan, täydennä:

- omia lisälinssejä tai muunnelmia kolmesta linssistä, jotka ovat
  osoittautuneet hyödyllisiksi
- tyypillisiä sudenkuoppia (esim. milloin kolme suuntaa päätyvät liian
  samankaltaisiksi ja miten sen huomaa)
- konkreettisia esimerkkejä muista caseista `../../cases/`-kansioon

Kun tämä osio on täytetty useammalla caseella, nosta
`skills_index.json`:n `maturity`-kenttä arvoon `validated`
(ks. `../../../../meta/maturity_levels.md`).

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../customer-vision-to-jtbd/SKILL.md`
  — tuottaa AI wedgen, jolle tässä ideoidaan.
- Seuraava skilli samassa pakissa:
  `../rice-scoring-and-mvp-synthesis/SKILL.md` — pisteyttää kolme suuntaa
  ja valitsee MVP:n.
- Worked example: `../../cases/ai-decision-coach-mvp-case.md` kohta 5.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/ai-first-saas-workshop-source.md` — lähdetiedot
- `../../cases/ai-decision-coach-mvp-case.md` — worked example
- `../../CLAUDE.md` — pakin jaetut suojaukset
