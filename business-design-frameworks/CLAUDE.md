# Business Design Frameworks — jaetut suojaukset

Tämän tiedoston ohjeet koskevat **jokaista** tämän pakin skilliä. Yksittäinen skilli
(`skills/<nimi>/SKILL.md`) kertoo *mitä* tehdään; tämä tiedosto on **varaverkko**, joka
estää tyypilliset virheet riippumatta siitä, mikä skilli on käynnissä.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei tänne. Jos skillin
> oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa virheen,
> vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus, eivät
> ensisijainen mekanismi.

---

## Tämä pakki on avoin kokoelma — ei suljettu lista

Toisin kuin muut ydinpakit, tämä pakki on suunniteltu **kasvamaan jatkuvasti**.
Se kokoaa yhteen erilaisia tapoja jäsentää ja mallintaa liiketoimintaa, arvonluontia,
arvoketjuja ja asemointia — kerrosmallit, arvoketjuanalyysi, kategoriamallinnus ja
myöhemmin lisättävät uudet jäsentämistavat. Kun uusi skilli lisätään tähän pakkiin:

- Se saa oman `skills/<skill-id>/SKILL.md`-tiedoston samaa minimifrontmatter-mallia
  noudattaen (`name` + `description`, ei muuta).
- Se lisätään tämän pakin `README.md`:n skillitaulukkoon ja tarvittaessa
  ristiinlinkitetään muihin saman pakin skilleihin ("Jatka tästä").
- Sen kypsyys (`maturity`) alkaa oletuksena `scaffold`-tasolta, ellei kyseessä ole
  käyttäjän oma validoitu menetelmä (kuten esim. research-commercialisation-pakin
  tai opportunity-recognition-pakin owner-skillit).

## Vastuuvapaus — jäsennystapa, ei valmis analyysi

**Jokainen tuotos on jäsennelty luonnos, joka auttaa ajattelua — ei valmis analyysi
tai päätös.** Nämä ovat ajattelun apuvälineitä (mental models): ne auttavat näkemään
liiketoiminnan uudesta kulmasta, mutta eivät korvaa toimialatuntemusta, dataa tai
ihmisen tekemää tulkintaa.

- Älä esitä mallinnuksen tulosta lopullisena totuutena tai ainoana oikeana jäsennyksenä
  — useampi malli voi tuottaa erilaisia, yhtä valideja näkökulmia samaan liiketoimintaan.
- Tunnista epävarmuus avoimesti — jos lähtötieto on ohut, sano se.
- Ennen kuin mallinnuksen tulos viedään päätöksentekoon: **ihminen tarkistaa ja
  hyväksyy.**

## Ei keksitä lukuja tai faktoja

Älä tuota tarkkoja markkinakoko-, kustannus- tai muita lukuja muistista tai
arvauksena esittäen niitä vahvistettuina. Kaksi hyväksyttyä tapaa:

1. **Käyttäjän antama lähtöarvo** — käytä sitä ja mainitse lähde.
2. **Läpinäkyvä oletus** — merkitse selvästi `[oletus — tarkista]` luvun viereen.

## Kypsyystaso näkyväksi

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia (klassisia liiketoiminnan viitekehyksiä), mutta omaa validoitua
kokemusta ei vielä ole liitetty. Kun käytät tämän pakin skillejä, tee tämä näkyväksi
äläkä esitä `[OWNER INPUT]`-osion puuttumista täydellisenä osaamisena.

## Pakkikohtainen huomio

Nämä ovat yleisiä, toimialariippumattomia jäsentämismalleja — ne pitää aina sovittaa
kontekstiin. Älä pakota liiketoimintaa väkisin johonkin malliin, jos se ei tuota
oivallusta; kokeile toista mallia samasta kokoelmasta tai yhdistä useampaa.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
