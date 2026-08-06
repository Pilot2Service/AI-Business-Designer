# Prototyping & Demonstration — jaetut suojaukset

Tämän tiedoston ohjeet koskevat **jokaista** tämän pakin skilliä. Yksittäinen skilli
(`skills/<nimi>/SKILL.md`) kertoo *mitä* tehdään; tämä tiedosto on **varaverkko**, joka
estää tyypilliset virheet riippumatta siitä, mikä skilli on käynnissä.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei tänne. Jos skillin
> oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa virheen,
> vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus, eivät
> ensisijainen mekanismi.

---

## Demo ei ole tuote — sano se ääneen aina

Tämän pakin ydinriski on **proto/demo-menestyksen sekoittaminen tuotantovalmiuteen.**
Nopeasti rakennettu, "vibe coodattu" proto todistaa idean toimivan periaatteessa —
se ei todista, että ratkaisu on turvallinen, skaalautuva, ylläpidettävä tai
tietoturvallinen tuotannossa. Jokaisessa tämän pakin tuotoksessa:

- Merkitse selvästi, mikä on demo-tason löydös ("toimi 3 testitapauksessa
  hallitussa ympäristössä") vastaan tuotantotason väite ("toimii luotettavasti
  kaikissa tapauksissa") — älä koskaan anna näiden sekoittua.
- Muistuta, että AI-avusteisesti ("vibe coodaten") tuotettu koodi sisältää
  tyypillisesti hallusinoituja rajapintoja, puutteellista virhekäsittelyä ja
  heikkoja autentikointi-/oikeustarkistuksia, kunnes ihminen on ne erikseen
  tarkistanut — tämä koskee erityisesti mitä tahansa demoa, jossa käsitellään
  oikeaa dataa tai esitetään live-ympäristössä.
- Älä koskaan esitä demoa asiakkaalle "melkein valmiina tuotteena" — kehystä se
  aina sen mukaan, mitä se todella on (konseptin todistus, ei tuotantosovellus).

## PoC / Pilotti / MVP — eri termit, eri kysymykset

Näitä käytetään usein virheellisesti synonyymeinä. Ne vastaavat eri
epävarmuuksiin, älä sekoita niitä:

- **PoC (Proof of Concept)** — vastaa "toimiiko tämä teknisesti ylipäätään
  edustavalla datalla?" Aikarajattu, matalariskinen, ei vielä tuotantodataa
  tai -kuormaa.
- **Pilotti** — vastaa "toimiiko tämä oikeiden ihmisten ja oikeiden
  operatiivisten olosuhteiden kanssa?" Olettaa, että tekninen toteutettavuus
  ja arvo on jo ennustettu — pilotti vahvistaa sen käytännössä.
- **MVP (Minimum Viable Product)** — vastaa "mitä pitäisi rakentaa seuraavaksi
  oikean käyttäjäpalautteen perusteella?" Tuotekehitysote, ei
  todistamisvaihe.

Käytä oikeaa termiä äläkä käytä niitä toistensa synonyymeinä asiakasviestinnässä
— väärä termi luo väärän odotuksen budjetista, aikataulusta ja siitä mitä
seuraavaksi tapahtuu.

## Pilot purgatory -riski on todellinen ja se torjutaan framingilla, ei koodilla

Tutkimus (mm. McKinsey, BCG, IDC, MIT) osoittaa toistuvasti, että suuri osa
(arviot vaihtelevat lähteittäin, karkeasti 80–95 %) yrityssektorin AI-piloteista
ei koskaan etene tuotantoon — pullonkaula on tyypillisesti operatiivinen
(työnkulun uudelleensuunnittelu, johdon sitoutuminen, mittakaavan investointi),
ei tekninen. Tämän pakin skillit eivät voi ratkaista tätä demo-vaiheessa, mutta
niiden PITÄÄ tehdä riski näkyväksi jo demo-/PoC-vaiheen kehystyksessä (ks.
`skills/demo-framing-and-expectation-setting/SKILL.md`) — älä anna asiakkaan
uskoa, että onnistunut demo tarkoittaa automaattista tuotantoon etenemistä.

## Vastuuvapaus — luonnos, ei päätös

**Jokainen tuotos on päätöksenteon tueksi tehty luonnos, ei itse päätös.** Analyysin,
kehystyksen tai suosituksen tekee tämä skilli; päätöksen ja sen seuraukset kantaa aina
ihminen, jolla on siihen valtuudet ja vastuu organisaatiossa.

- Älä esitä demon tulosta tai ROI-arviota lopullisena totuutena.
- Tunnista epävarmuus avoimesti — jos lähtötieto on ohut tai oletuksenvarainen, sano se.
- Ennen kuin demo-tulos tai sen pohjalta laskettu ROI-arvio viedään
  päätöksentekoon: **ihminen tarkistaa ja hyväksyy.**

## Ei keksitä lukuja tai faktoja

Älä tuota tarkkoja ROI-, aikasäästö- tai muita lukuja muistista tai arvauksena
esittäen niitä vahvistettuina. Kaksi hyväksyttyä tapaa:

1. **Käyttäjän antama lähtöarvo tai demossa mitattu havainto** — käytä sitä ja
   mainitse lähde ja mittausolosuhteet (esim. otoskoko, testiympäristö).
2. **Läpinäkyvä oletus** — merkitse selvästi `[oletus — tarkista]` luvun viereen,
   älä kappaleen loppuun yleisenä varauksena. Muista erityisesti: PoC-mittakaavan
   tulos (esim. "säästi 2 tuntia 10 tapauksessa") ei ekstrapoloidu suoraviivaisesti
   tuotantomittakaavaan ilman selkeää oletusta siitä, miksi skaalautuminen olisi
   lineaarista.

## Kypsyystaso näkyväksi

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia (Great Demo! -metodologia, vibe coding -käytännöt, PoC/Pilot/MVP-
kirjallisuus, Amazon Working Backwards, prototyyppifideliteetti-tutkimus), mutta omaa
validoitua konsultointikokemusta ei vielä ole liitetty. Kun käytät tämän pakin
skillejä, tee tämä näkyväksi äläkä esitä `[OWNER INPUT]`-osion puuttumista
täydellisenä osaamisena.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
