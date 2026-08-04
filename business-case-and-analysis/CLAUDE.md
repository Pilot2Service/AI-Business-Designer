# Business Case & Analysis — jaetut suojaukset

Tämän tiedoston ohjeet koskevat **jokaista** tämän pakin skilliä. Yksittäinen skilli
(`skills/<nimi>/SKILL.md`) kertoo *mitä* tehdään; tämä tiedosto on **varaverkko**, joka
estää tyypilliset virheet riippumatta siitä, mikä skilli on käynnissä.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei tänne. Jos skillin
> oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa virheen,
> vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus, eivät
> ensisijainen mekanismi. (Periaate lainattu ja sovellettu claude-for-legal-finland
> -repon CONTRIBUTING.md:stä.)

---

## Vastuuvapaus — luonnos, ei päätös

**Jokainen tuotos on päätöksenteon tueksi tehty luonnos, ei itse päätös.** Analyysin,
priorisoinnin tai suosituksen tekee tämä skilli; päätöksen ja sen seuraukset kantaa aina
ihminen, jolla on siihen valtuudet ja vastuu organisaatiossa.

- Älä esitä laskelmaa tai suositusta lopullisena totuutena.
- Tunnista epävarmuus avoimesti — jos lähtötieto on ohut tai oletuksenvarainen, sano se.
- Ennen kuin business case, roadmap tai suositus viedään päätöksentekoon: **ihminen
  tarkistaa ja hyväksyy.**

## Ei keksitä lukuja tai faktoja

Älä tuota tarkkoja markkinakoko-, ROI-, kilpailija- tai muita lukuja muistista tai
arvauksena esittäen niitä vahvistettuina. Kaksi hyväksyttyä tapaa:

1. **Käyttäjän antama lähtöarvo** — käytä sitä ja mainitse lähde.
2. **Läpinäkyvä oletus** — merkitse selvästi `[oletus — tarkista]` luvun viereen, älä
   kappaleen loppuun yleisenä varauksena.

## Premissien tarkistus

Jos käyttäjän esittämä liiketoimintafakta (markkinan koko, kilpailutilanne, sisäinen
prosessi) on olennainen lopputuloksen kannalta mutta epävarma, nosta se esiin ennen kuin
rakennat analyysin sen varaan. Älä jatka hiljaa väärän oletuksen pohjalta.

## Kypsyystaso näkyväksi

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia, mutta omaa validoitua kokemusta ei vielä ole liitetty. Kun käytät
tämän pakin skillejä, tee tämä näkyväksi äläkä esitä `[OWNER INPUT]`-osion puuttumista
täydellisenä osaamisena.

## Pakkikohtainen huomio

Ei korvaa talousosaston/controllerin virallista laskentaa — ROI/NPV-luvut ovat päätöksenteon tukena, viralliseen käyttöön tarvitaan vahvistus.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
