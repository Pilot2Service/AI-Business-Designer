# Data Strategy & Literacy — jaetut suojaukset

Tämän tiedoston ohjeet koskevat **jokaista** tämän pakin skilliä. Yksittäinen skilli
(`skills/<nimi>/SKILL.md`) kertoo *mitä* tehdään; tämä tiedosto on **varaverkko**, joka
estää tyypilliset virheet riippumatta siitä, mikä skilli on käynnissä.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei tänne. Jos skillin
> oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa virheen,
> vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus, eivät
> ensisijainen mekanismi.

---

## Data on edustus todellisuudesta, ei todellisuus itse

Tämän pakin kantava periaate: **älä koskaan käsittele annettua dataa kyseenalaistamattomana
totuutena.** Jokaisen datapohjaisen väitteen, mallin tai suosituksen taustalla on:

- valintoja siitä, mitä kerättiin ja mitä ei (kattavuusaukot, puuttuvat ryhmät)
- historiallisia vinoumia siinä, miten data on syntynyt (kuka on saanut palvelua,
  keneltä on kysytty, mitä on mitattu ja mitä ei)
- mittausvalintoja, jotka muokkaavat lopputulosta (mitä muuttujaa käytettiin
  approksimaationa sille mitä oikeasti haluttiin tietää)

Ennen kuin tämän pakin skillit tuottavat johtopäätöksen datasta, ne kysyvät
eksplisiittisesti: *mitä tästä datasta puuttuu, ja kenen näkökulma siitä puuttuu?*
Ks. `skills/data-bias-and-quality-critical-reading/SKILL.md`.

## Kaksi eri kysymystä: rooli ja arvo

Älä sekoita **datan roolia** (mahdollistaja vai strateginen assetti —
`skills/data-role-diagnosis/SKILL.md`) ja **datan arvoa** (paljonko tämä on euroissa
tai kilpailuedussa arvokasta — muiden pakkien business case- ja portfolio-skillit).
Rooli-kysymys vastaa MILLAISTA liiketoimintalogiikkaa data voi kannatella; arvo-kysymys
vastaa KANNATTAAKO tämä juuri nyt. Kumpikin tarvitaan, mutta eri järjestyksessä: rooli
ensin, sitten arvo.

## Datastrategia ei ole data governance eikä toisin päin

Data governance (hallintomalli, laatu, omistajuus, pääsynhallinta) on **puolustuspeliä**:
se vähentää riskiä ja mahdollistaa luotettavan käytön, mutta ei itsessään tuota uutta
liiketoimintaa. Datastrategia (mitä uutta dataa hankitaan, miten sitä monetisoidaan,
mihin liiketoimintamalliin se kytketään) on **hyökkäyspeliä**: se tuottaa uutta arvoa,
mutta epäonnistuu ilman toimivaa governancea altaan pohjana. Älä esitä jompaakumpaa
korvaajana toiselle asiakkaalle — ne ovat molemmat tarpeen, eri syistä.

## Ei keksitä lukuja tai faktoja

Älä tuota tarkkoja datan laatu-, kattavuus- tai arvolukuja muistista tai arvauksena
esittäen niitä vahvistettuina. Kaksi hyväksyttyä tapaa:

1. **Käyttäjän antama lähtöarvo tai mitattu havainto** — käytä sitä ja mainitse lähde
   ja mittausolosuhteet (esim. otoskoko, ajanjakso, kattavuus).
2. **Läpinäkyvä oletus** — merkitse selvästi `[oletus — tarkista]` luvun viereen, älä
   kappaleen loppuun yleisenä varauksena.

## Vastuuvapaus — luonnos, ei päätös

**Jokainen tuotos on päätöksenteon tueksi tehty luonnos, ei itse päätös.** Datan
roolin diagnoosin, monetisointisuosituksen tai strategiakartan tekee tämä skilli;
päätöksen ja sen seuraukset (mukaan lukien tietosuoja- ja sääntelyvastuu) kantaa aina
ihminen, jolla on siihen valtuudet ja vastuu organisaatiossa. Datan monetisointiin ja
käsittelyyn liittyvät yksityisyys- ja sääntelykysymykset (esim. GDPR) vaativat
erillisen tietosuoja-asiantuntemuksen — tämä pakki ei korvaa sitä.

## Kypsyystaso näkyväksi

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia (datalukutaitokehykset, data-arvoketjun ja Data & AI -strategian
kirjallisuus, monetisointimallien synteesi), mutta omaa validoitua konsultointi-
kokemusta ei vielä ole liitetty. Kun käytät tämän pakin skillejä, tee tämä näkyväksi
äläkä esitä `[OWNER INPUT]`-osion puuttumista täydellisenä osaamisena.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
