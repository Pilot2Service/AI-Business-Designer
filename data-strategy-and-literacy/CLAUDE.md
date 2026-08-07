# Data Strategy & Literacy — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

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

## Vastuuvapaus tässä pakissa — myös sääntelyvastuu

Yleisen vastuuvapauden (`shared-guardrails.md`) lisäksi: datan monetisointiin ja
käsittelyyn liittyvät yksityisyys- ja sääntelykysymykset (esim. GDPR) vaativat
erillisen tietosuoja-asiantuntemuksen — tämä pakki ei korvaa sitä.

## Kypsyystaso tässä pakissa

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia (datalukutaitokehykset, data-arvoketjun ja Data & AI -strategian
kirjallisuus, monetisointimallien synteesi), mutta omaa validoitua konsultointi-
kokemusta ei vielä ole liitetty.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
