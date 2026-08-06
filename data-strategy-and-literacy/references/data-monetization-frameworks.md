# Datan monetisoinnin viitekehykset — laajempi vertailu

Taustamateriaali skillille `../skills/data-monetization-model-selection/SKILL.md`.

## Suora monetisointi (Direct Monetization)

Data tai siitä suoraan johdetut tuotteet ovat itsessään myytävä hyödyke.
Vaatii vahvan data governancen, jotta toimitettava data on laadukasta,
tietoturvallista ja lisensoitavissa.

| Malli | Kuvaus | Esimerkki |
|---|---|---|
| Data-as-a-Service (DaaS) / raakadatan myynti | Puhdistetun, anonymisoidun datan myynti rajapintojen tai datakauppapaikkojen kautta | B2B-toimija lisensoi laitteistonsa tuottamaa prosessidataa teollisille asiakkaille T&K-käyttöön |
| Insight-as-a-Service | Datasta johdetun ymmärryksen (analyysit, trendiraportit, ennustemallit) myynti raakadatan sijaan | Toimialakohtainen benchmark-raportti, jossa asiakas voi verrata omaa suoritustaan aggregoituun markkinadataan |
| Datavaihdanta / IP-lisensointi | Dataa vaihdetaan toisen osapuolen dataan, teknologiaan tai markkinapääsyyn — ei suoraan rahaan | Uniikki data-assetti lisensoidaan startupin käyttöön osana perustajan pääomapanosta innovaatioekosysteemissä |

## Epäsuora monetisointi (Indirect Monetization)

Dataa ei myydä ulos, vaan sitä käytetään omien tuotteiden, palveluiden tai
prosessien optimointiin. Usein tuottoisampaa ja vähäriskisempää
(esim. tietosuojan kannalta) kuin suora myynti.

| Malli | Kuvaus | Esimerkki |
|---|---|---|
| Tuotteen/palvelun rikastaminen | Datan avulla rakennetaan uusia, maksullisia ominaisuuksia olemassa olevaan tuotteeseen | Oppimisalusta kerää dataa käyttäjän kysymyksistä ja oppimistyylistä, mahdollistaen hyperpersonoidun ohjauksen korkeammalla hinnalla |
| Käyttöasteen/resurssien optimointi | Data paljastaa pullonkaulat ja tehottomuudet, mahdollistaa dynaamisen hinnoittelun | Jaettujen resurssien alusta käyttää käyttödataa ruuhkahuippujen dynaamiseen hinnoitteluun ja tyhjäkäynnin minimointiin |
| Liiketoimintariskien minimointi | Data mahdollistaa ennakoivan havaitsemisen ennen tapahtumaa | Ennakoiva huolto, asiakaspoistuman tunnistus ennen sen tapahtumista, petosten esto |

## Suora vs. epäsuora — yhteenveto

| Ominaisuus | Suora monetisointi | Epäsuora monetisointi |
|---|---|---|
| Pääasiallinen tulonlähde | Datan/lisenssien myynti kolmansille osapuolille | Parempi tuote, uudet ominaisuudet, halvemmat operaatiot |
| Asiakkaan ostama arvo | Pääsy informaatioon | Parempi käyttäjäkokemus, säästetty aika, tarkemmat tulokset |
| Toteutuksen nopeus | Hitaampi — vaatii juridisia sopimuksia (IP, tietosuoja) ja rajapintojen rakentamista | Ketterämpi — data pysyy sisällä, iteroidaan suoraan tuotteeseen |
| Kilpailuetu | Perustuu datan ainutlaatuisuuteen | Perustuu datan ja algoritmien luomaan vauhtipyörään (flywheel) |

## Data Flywheel — mekanismi

1. **Uniikki data:** kerätään alkuvaiheen dataa käyttäjiltä.
2. **Mallin koulutus:** data syötetään koneoppimismalliin, joka tekee
   tuotteesta älykkäämmän.
3. **Parempi tuote:** älykkäämpi tuote houkuttelee lisää käyttäjiä.
4. **Lisää dataa:** uudet käyttäjät generoivat lisää dataa, sykli jatkuu.

Flywheel on strateginen assetti, jota kilpailijoiden on vaikea kopioida
pelkällä pääomalla — mutta väitetty flywheel pitää validoida neljällä
kohdalla ennen kuin siihen nojataan strategisesti, ks.
`../skills/data-monetization-model-selection/SKILL.md`:n tarkistuslista.

## Ks. myös

- `../skills/data-monetization-model-selection/SKILL.md` — pääskilli
- `../skills/data-role-diagnosis/SKILL.md` — edeltävä diagnoosi
