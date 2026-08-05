# Promptikirjasto — AI-native Business Design -työpaja

Näihin viittaavat pakin skillit (`skills/*/SKILL.md`, "Rakenne"-osio).
Promptit on suomennettu ja kevyesti muotoiltu selkeyden vuoksi alkuperäisestä
`day1.md`:stä (ks. `workshop-source.md`) — merkitys ei ole muutettu. Aja
promptit AI-ajattelukumppanin (Claude/ChatGPT) projektissa, jolla on
käytössään oma liiketoimintakonteksti.

## Promptti 1 — AI-mahdollisuuksien löytö (`ai-native-opportunity-scan`)

```
Toimi startup-strategina, joka ymmärtää tekoälyä syvällisesti — myös
agenttisia ja closed-loop-lähestymistapoja, ei vain perustuottavuuskäyttöä.

Katso liiketoimintaani (käytä kaikkea mitä tiedät siitä tästä projektista).
Tunnista 5 aluetta, joissa tekoäly voisi luoda meille AIDOSTI UUSIA
liiketoimintamahdollisuuksia — ei vain nopeuttaa olemassa olevaa prosessia.

Haluan jokaiseen viiteen alueeseen kehittyneen tai agenttisen käytön:
closed-loop-prosesseja, autonomisia agentteja, uusia tekoälypohjaisia
ominaisuuksia, tuotteita tai liiketoimintamalleja, jotka olivat aiemmin
liian hitaita, kalliita tai mahdottomia.

Anna jokaisesta viidestä alueesta:
- lyhyt nimi mahdollisuudelle
- mikä se on, 2-3 lauseessa
- miksi se on uutena mahdollinen juuri tekoälyn ansiosta
- mitä pitäisi karkeasti olla totta, jotta voisimme tehdä tämän

Ole spesifinen minun liiketoimintaani nähden. Vältä geneerisiä "käytä
tekoälyä säästämään aikaa" tai "automatisoi asiakaspalvelu AI-agentilla"
-tyyppisiä ehdotuksia.
```

## Promptti 2 — Pressure-test ja priorisointi (`ai-native-opportunity-scan`)

Kirjoita ensin omat lyhyet kommenttisi ja arviosi viidestä löydöksestä, ja
liitä sitten seuraava:

```
Ota yllä olevat 5 mahdollisuutta. Arvioi jokainen:

- Liiketoimintapotentiaali: kuinka iso tämä voisi olla meille, ja miksi?
- Asiakasarvo: mitä todellista ongelmaa se ratkaisee, ja kenelle?
- Toteutettavuus pienelle tiimille nykyisillä tekoälytyökaluilla ja
  resursseilla (matala / keskitaso / korkea)
- Mikä olisi pienin ensimmäinen versio, jonka voisimme prototypoida tällä
  viikolla?

Järjestä sitten nämä 5 lupaavimmasta vähiten lupaavaan tämänhetkisenä
tekoälyyn liittyvänä liiketoimintamahdollisuutena meille, ja perustele
järjestys yhdellä lauseella per kohta. Suosittele yhtä, jonka
prototypoisit ensin, ja miksi.
```

## Promptti 3 — Vision terävöitys (`customer-vision-to-jtbd`)

```
Toimi kokeneena tuotestrategina, joka työskentelee varhaisen vaiheen
startupin kanssa.

Alla (ja tässä projektissa) on karkea tuotevisioni ja asiakastilanteeni.
Lue se ja auta terävöittämään sitä.

1. Kerro mikä on vielä epäselvää tai määrittelemättä ja vaatii päätöksen
   minulta.
2. Kysy enintään 7 tarkentavaa kysymystä tärkeysjärjestyksessä.
3. Nosta esiin oletukset, joita näytän tekevän ja jotka kannattaisi
   tarkistaa.

Älä vielä kirjoita suunnitelmaa — auta ensin ajattelemaan.
```

## Promptti 4 — Ideal Customer Profile

```
Tutki useampi asiakasprofiili, joilla on tämä ongelma, kuvaa kukin, ja
priorisoi ketä meidän pitäisi palvella ensin ja miksi.
```

## Promptti 5 — Jobs To Be Done

```
Käy kanssani läpi Jobs To Be Done -harjoitus. Mene syvemmälle asiakkaan
käyttäytymiseen ja siihen tilanteeseen, jossa ongelma pitää ratkaista, ja
mitä hän todella yrittää saavuttaa.
```

## Promptti 6 — Need Themes ja AI-advantage-pisteytys

```
Muunna yllä oleva Jobs To Be Done -analyysi tarveteemoiksi (Need Themes)
— anna 5 funktionaalista ja 2 psykologista teemaa. Palauta taulukkona.
Jokaisen teeman tulee olla yhden tai kahden sanan substantiivilause, joka
kiteyttää tarpeen ytimen, esim. edullisuus, relevanssi, luottamus.
```

```
Pisteytä jokainen tarveteema 1-5 sen mukaan, kuinka paljon kilpailuetua
tekoäly tuo sen palvelemiseen, ja selitä korkeimmat pisteet. Missä
tekoälyetumme on suurin?
```

## Promptti 7 — Mini-PRD (`ai-buildable-prd-writing`)

```
Toimi kokeneena tuotepäällikkönä, joka auttaa varhaisen vaiheen startupia
kirjoittamaan fokusoidun mini-PRD:n tekoälyllä rakennettavaa prototyyppiä
varten.

Käytä kaikkea mitä tiedät liiketoiminnastani tässä projektissa, sekä
mahdollisuutta ja muistiinpanoja aiemmasta työstämme tässä keskustelussa.

Kirjoita MINI-PRD seuraavilla osioilla:

1. Ongelma & asiakas — kenelle tämä on, ja mitä kipua se ratkaisee?
2. Tuotevisio — kuvaa kokemus asiakkaan omin sanoin.
3. Core-ominaisuudet — listaa vain ne ominaisuudet, joita ensimmäinen
   versio tarvitsee. Kuvaa jokainen lopputuloksena, jonka käyttäjä
   saavuttaa, ei teknisenä toteutuksena.
4. Rajaukset — mitä TIETOISESTI emme rakenna tässä versiossa.
5. Onnistumiskriteerit — miten tiedämme prototyypin toimivan.

Pidä se riittävän tiiviinä prototypoitavaksi tällä viikolla. Luonnoksen
jälkeen kysy minulta enintään 5 kysymystä, jotka terävöittäisivät PRD:tä,
ja anna sitten tarkistettu versio.
```

## PRD-tarkistuslista (`ai-buildable-prd-writing`, vaihe 4)

- [ ] Ongelma & asiakas on spesifinen — ei "kaikille jotka..."
- [ ] Tuotevisio on kirjoitettu asiakkaan sanoin, ei ominaisuuslistana
- [ ] Core-ominaisuudet on kuvattu lopputuloksina ("käyttäjä voi…"), ei
      teknisenä toteutuksena
- [ ] Rajaukset-osio on olemassa ja konkreettinen (ei tyhjä)
- [ ] Onnistumiskriteerit ovat mitattavissa tai havaittavissa
- [ ] PRD ei sisällä teknologiavalintoja tai arkkitehtuuripäätöksiä
- [ ] Laajuus on karsittu MVP-tasolle: yksi asiakas, yksi ydin-job
