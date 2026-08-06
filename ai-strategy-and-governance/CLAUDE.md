# AI Strategy & Governance — jaetut suojaukset

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

Ei korvaa juridista EU AI Act -compliance-arviota — syvempään analyysiin käytä tämän workspacen tekoalysaantely-plugineja.

Tässä pakissa on useita samankaltaisia kolmi-/nelijaotteluja, jotka
vastaavat ERI kysymyksiin — älä sekoita niitä keskenään:

- **Automate/Augment/Human-Only** (`task-level-decomposition-and-
  automation-fit`) — vastaa "sopiiko TÄMÄ TEHTÄVÄ AI:lle ja millä
  tasolla".
- **Quick Wins/Strategic Bets/Hard-Low Value/Deprioritize**
  (`ai-opportunity-portfolio`) — vastaa "kannattaako TÄMÄ MAHDOLLISUUS
  ja onko se helppo toteuttaa".
- **Deploy/Reshape/Invent** (`ai-opportunity-portfolio`) — vastaa
  "kuinka SYVÄLLE organisaatiota tämän toteutus koskettaa".
- **Horisontti 1/2/3** (`ai-capability-roadmap`) — vastaa "MILLOIN tämä
  toteutetaan".
Kun viittaat johonkin näistä, käytä oikeaa termiä äläkä käytä niitä
toistensa synonyymeinä — ne korreloivat mutta eivät ole sama luokitus.

Raakalistan kokoamiseen on kaksi täydentävää, EI kilpailevaa, lähestymistapaa
— älä esitä toista "parempana" ilman kontekstia:

- **Bottom-up** (`task-level-decomposition-and-automation-fit`) — käydään
  olemassa oleva prosessi läpi tehtävä kerrallaan. Vahva kun prosessi on jo
  tarkasti kuvattu.
- **Top-down** (`ai-capability-pattern-matching`) — esitetään valmiin
  kyvykkyyspatternikirjaston (`references/ai-capability-pattern-library.md`)
  diagnostiset kysymykset ennen tarkkaa prosessikuvausta. Nopeampi
  ensimmäinen kartoitus, vaatii validoinnin ennen pisteytystä.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
