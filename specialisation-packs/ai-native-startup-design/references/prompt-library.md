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

## Promptti 6 — Need Themes, NMB-pisteytys ja AI wedge (`customer-vision-to-jtbd`)

```
Muunna yllä oleva Jobs To Be Done -analyysi tarveteemoiksi (Need Themes)
— anna 5 funktionaalista ja 2 psykologista teemaa. Palauta taulukkona
sarakkein: Tarveteema / Tyyppi / Taustalla oleva "miksi" / Liittyvä JTBD.
Jokaisen teeman tulee olla yhden tai kahden sanan substantiivilause, joka
kiteyttää tarpeen ytimen, esim. edullisuus, relevanssi, luottamus.
```

```
Pisteytä jokainen tarveteema viidellä kriteerillä, kukin 1-5: Need Depth
(tarpeen syvyys/kipeys), Frequency (kuinka usein tarve aktivoituu),
Market Coverage (kuinka laajasti tarve koskettaa kohdemarkkinaa),
Business Strength (oma lähtökohtani tämän tarpeen palvelemiseen),
AI Advantage (kuinka paljon kilpailuetua tekoäly tuo juuri tähän
tarpeeseen). Laske kokonaispistemäärä (max 25) ja luokittele jokainen
Differentiator- tai Table Stake -tason tarpeeksi. Palauta taulukkona ja
selitä korkeimmat pisteet.
```

```
Valitse yksi (tai kaksi) tarveteema AI-differentiaattoritarpeeksi (AI
wedge): tarve jolla on samanaikaisesti korkea syvyys, korkea toistuvuus,
heikko kilpailijakattavuus, vahva oma lähtökohtani, JA korkea
tekoälyetu. Perustele valinta ja selitä miksi muut korkean pistemäärän
tarpeet eivät täytä kaikkia kriteereitä yhtä hyvin.
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

---

**Huom promptit 8–10:** nämä on lisätty [redacted]n "AI-first SaaS
Product" -työpajasta (ks. `[redacted]-workshop-source.md`) ja ne sijaitsevat
työnkulussa promptin 6 (Need Themes / AI wedge) ja promptin 7 (PRD) välissä
— käytä niitä kun ratkaisusuunta ei ole vielä selvä valitulle AI wedgelle.

## Promptti 8 — Kolme ratkaisusuuntaa (`ai-differentiator-solution-ideation`)

```
Otetaan lähtökohdaksi valittu AI-differentiaattoritarpeeni (AI wedge):
[liitä tarveteema + NMB-pisteytys tähän].

Ideoi 3 täysin erilaista AI-natiivia ratkaisusuuntaa tälle tarpeelle,
kolmella eri linssillä:

1. Kilpailijalinssi: miten olemassa olevat toimijat ratkaisevat tätä
   tänään, ja mitä tekoäly mahdollistaisi joka niille ei ole mahdollista?
2. Tulevaisuuslinssi: miten tämä tarve ratkaistiin ennen (raskaasti,
   manuaalisesti, kontekstiin aina uudelleen sovittaen), ja miten se
   ratkaistaan tulevaisuudessa kun tekoäly rakentaa ja opettaa kontekstia
   jatkuvasti vuoropuhelussa käyttäjän kanssa?
3. Yhdistä-pisteet-linssi: mitkä muut erilliset tehtävät käyttäjä tekee
   tämän tarpeen ympärillä, jotka voitaisiin yhdistää yhdeksi tekoäly-
   natiiviksi kokemukseksi?

Anna jokaiselle suunnalle: nimi, konsepti (2-3 lausetta), pääasiallinen
output käyttäjälle, ja miksi se on erottuva kilpailijoihin/nykytilaan
nähden. Älä valitse puolestani — esitä kaikki kolme rinnakkain.
```

## Promptti 9 — RICE-pisteytys ja MVP-synteesi (`rice-scoring-and-mvp-synthesis`)

```
Pisteytä yllä olevat 3 ratkaisusuuntaa RICE-mallilla: Reach, Impact,
Confidence (kaikki 1-5), ja Effort käänteisesti (5 = helpoin/matalin
rakennuskustannus, 1 = vaikein). Perustele jokainen piste lyhyesti,
erityisesti Effort suhteessa nykyiseen tekniseen pinooni ja olemassa
oleviin työkaluihini/dataani. Suosittele mitä pitäisi rakentaa MVP:nä
ja miksi.
```

```
Kirjoita valitulle MVP:lle: a) MVP-määritelmä (2-3 lausetta), b) yhden
lauseen positiointilause muodossa "[Tuote] antaa [kohdeasiakkaalle]
[ydinhyödyn] [erottuvalla mekanismilla]", c) 3 "miksi voitamme"
-väittämää, jotka sitovat vahvuuteni konkreettiseen kilpailuetuun.
```

## Promptti 10 — Keskusteleva OS-flow (`ai-native-conversational-os-design`)

```
Suunnittele valitulle MVP:lle keskusteleva käyttöliittymäarkkitehtuuri
kuudella vaiheella:

1. Intent — mitkä ovat 3-6 pääasiallista syytä miksi käyttäjä tulee
   tähän tuotteeseen?
2. Strategy Cards — mitkä sisäiset "pelikirjat" (päättelymoduulit)
   tekoäly voi valita kunkin intentin mukaan? Sido jokainen korttini
   yhteen aiemmin tunnistettuun differentiaattori- tai table-stake-
   tarpeeseen.
3. Clarification — mitkä korkeintaan 2-4 täsmentävää kysymystä
   tarvitaan, ja milloin niitä kysytään?
4. Output Cards — mitkä strukturoidut tulokset käyttäjä saa kustakin
   strategiakortista?
5. Mission — mikä yhden lauseen missio kehystää seuraavat askeleet
   luottamuksen rakentamisen ympärille?
6. Agent Execution — mitä tekoäly voi tehdä itsenäisesti mission jälkeen
   luodakseen eteenpäin vievää liikevoimaa?

Kirjoita jokainen vaihe konkreettisesti tähän MVP:hen sovellettuna, älä
geneerisesti.
```
