# AI Capability Pattern Library

Tämä on `../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`
-skillin **Capability Pattern Mapping** -menetelmän konkreettinen sovellus AI-
ratkaisuihin. Sen sijaan että etsittäisiin "onko meidän toimialaltamme AI-esimerkkiä",
tämä kirjasto tarjoaa **13 nimettyä, toimialariippumatonta AI-kyvykkyyspatternia**,
joista jokainen toimii diagnostisena kysymyksenä missä tahansa uudessa asiakas-
tilanteessa. Käyttöohje ja työnkulku: ks.
`../skills/ai-capability-pattern-matching/SKILL.md`.

## Miten tämä kirjasto on rakennettu — läpinäkyvyys lähteistä

Patternit on abstrahoitu kahdesta riippumattomasta, laajasta toimialan
AI-käyttötapausraportista. Tämä ei ole tyhjentävä listaus kaikista lähteiden
caseista, vaan **kuratoitu abstraktio** edustavasta otoksesta — ks. perustelu
miksi kuratointi on parempi lähestymistapa kuin raaka case-lista,
`../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`:n
Tarkoitus-osiosta.

1. **Ensisijainen lähde** — laaja toimialaraportti (2026-painos), 130
   käyttötapausta kuudella toimialalla (Consumer; Energy, Resources &
   Industrials; Financial Services; Government & Public Services; Life
   Sciences & Health Care; Technology, Media & Telecommunications). Raportti
   käyttää kuusiulotteista vastuullisen AI:n riskikehystä (fair and
   impartial, robust and reliable, transparent and explainable, safe and
   secure, responsible and accountable, private) jokaisen casen
   riskiarvioinnissa. Tästä raportista on tekstipohjaisesti poimittu ja
   tarkistettu **81 casea** viideltä kuudesta toimialasta (otsikko, toimiala,
   ensisijainen liiketoimintafunktio, Agentic AI / Physical AI -merkintä) —
   kuudes toimiala (Technology, Media & Telecommunications) on mukana vain
   teematasolla poiminnan teknisten rajoitteiden vuoksi, ei yksittäisin
   casein. Jokainen tässä kirjastossa mainittu esimerkki on suoraan tästä
   poiminnasta, ei muistista tuotettu.
2. **Toinen, riippumaton lähde** — toimialan AI-käyttötapauskooste, 63
   käyttötapausta 16 liiketoimintafunktiossa; sen oma analyysi osoittaa
   n. 75 %:n arvioidusta arvosta keskittyvän neljään funktioon:
   **asiakasoperaatiot (customer operations), markkinointi & myynti,
   ohjelmistokehitys ja T&K**. Tätä käytetään tässä kirjastossa
   **ristiintarkistuksena** patternien painotukselle — ei yksittäisten
   casejen lähteenä, koska yksittäisten casejen tarkka sisältö ei ollut
   luotettavasti saatavilla poiminnan aikana.

**Mitä tämä tarkoittaa käytännössä:** jokainen "Esimerkkejä toimialalta"
-kohdan viite alla on todellinen, oikein otsikoitu käyttötapaus
ensisijaisesta lähteestä. **Älä laajenna näitä esimerkkejä yksityiskohdilla,
joita ei ole tässä listattu** — jos tarvitset lisää yksityiskohtia, palaa
alkuperäiseen lähteeseen äläkä täydennä muistista.

## Toimialojen ja funktioiden peittävyys poiminnassa (81 casea)

| Toimiala | Caseja poiminnassa |
|---|---|
| Energy, Resources & Industrials | 28 |
| Consumer | 26 |
| Financial Services | 17 |
| Government & Public Services | 8 |
| Life Sciences & Health Care | 2 |
| Technology, Media & Telecommunications | 0 (vain teema-taso) |

Lähteen omat funktioluokat (esiintyvät "Tags"-merkintöinä): Sales, Marketing,
Operations, R&D/Product Development, Customer Service, Customer Experience,
Compliance & Risk, Procurement/Sourcing & Supply Chain, Manufacturing & Quality,
Field Services, Information Technology, Learning & Development, Cross-functional,
Distribution & Logistics. AI-tyyppimerkinnät: **Agentic AI** (moniagenttinen,
autonominen päätöksenteko), **Physical AI** (robotiikka/fyysinen toimeenpano),
ja merkitsemätön (perinteisempi ennustava/generatiivinen AI ilman agenttista tai
fyysistä komponenttia).

---

## Patternit

### 1. Moniagenttinen reaaliaikainen kompromissioptimointi

**Määritelmä:** Kaksi tai useampi keskenään riippuvainen päätös (hinta+varasto,
kassa+riski, reitti+kysyntä) tehdään tänään erillisissä tiimeissä/järjestelmissä
eri syklillä. Erikoistuneet agentit koordinoivat päätöksiä reaaliajassa yhteisen
tilannekuvan pohjalta.

**Diagnostinen kysymys:** *"Missä teillä on kaksi tai useampi toisiinsa vaikuttava
päätös, joita tehdään tänään erillään ja eri aikataululla?"*

**AI-tyyppi:** Agentic AI

**Esimerkkejä toimialalta:**
- [Consumer] *Dynamic pricing and inventory optimization* — hinnoittelu-,
  promootio- ja varastoagentit koordinoivat reaaliaikaisesti.
- [Consumer] *Autonomous supply chain operations* — kysynnän ennustus,
  suunnittelu ja häiriöiden havaitseminen yhtenä agenttiverkkona.
- [Consumer] *Integrated business planning* — myynti-, kysyntä- ja
  toimitusketjudatan yhdistäminen yhdeksi päätöksentekopohjaksi.
- [Energy, Resources & Industrials] *Intelligent commercial operations* —
  tarjoushinnoittelu, tarjousvalmistelu ja asiakasvuorovaikutus samalla
  agenttiverkolla.
- [Financial Services] *AI agents for algorithmic trading and market
  simulation* — kaupankäyntistrategiat ja markkinasimulaatio moniagenttisesti.
- [Financial Services] *Intraday liquidity optimization* — kassan ja riskin
  reaaliaikainen tasapainotus.

**Riskilinssi (vastuullisen AI:n ulottuvuudet):** *Fair and impartial* ja *Responsible
and accountable* korostuvat — nopeat, koordinoidut päätökset (esim. hinnoittelu)
voivat näyttää mielivaltaisilta asiakkaalle, jos päätöslogiikka ei ole selkeästi
rajattu ja loppuvastuu ihmisellä.

---

### 2. Rakenteettoman dokumentin validointi ja poikkeaman tunnistus

**Määritelmä:** Korkeasti palkattu asiantuntija selaa vapaamuotoista tekstiä tai
PDF-dokumentteja etsien poikkeamia, puutteita tai petosmerkkejä ennen
hyväksy/hylkää/eskaloi-päätöstä. (Tämä on käyttäjän oma esimerkkipatterni —
ks. `../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`.)

**Diagnostinen kysymys:** *"Missä kohtaa prosessianne korkeasti palkattu
asiantuntija joutuu etsimään poikkeamia vapaamuotoisesta tekstistä tai
PDF-dokumentista ennen päätöstä?"*

**AI-tyyppi:** Agentic AI / merkitsemätön (dokumenttianalyysi)

**Esimerkkejä toimialalta:**
- [Consumer] *Autonomous warranty adjudication* — takuuvaatimusten
  poikkeamien lippuutus ja dokumentaation tuki ihmisasiantuntijalle.
- [Financial Services] *AI agents for credit underwriting* — hakijadatan
  analyysi, markkinakontekstin seuranta ja compliance-tarkistus yhdessä.
- [Financial Services] *Research-based report generation* ("Getting to know
  your customer") — uusasiakasraporttien koostaminen onboarding-päätöksen
  tueksi.
- [Government & Public Services] *AI-supported regulatory examinations and
  inspections* — suurten dokumenttimäärien läpikäynti tarkastuksissa.
- [Government & Public Services] *AI-driven permitting* — hakemusten
  skannaus, tiedon poiminta, compliance-tarkistus, reaaliaikainen palaute.
- [Government & Public Services] *AI-enhanced benefits eligibility* —
  etuushakemusten käsittely- ja päätösprosessin virtaviivaistus.

**Riskilinssi:** *Robust and reliable* on kriittisin — huono data johtaa
huonoihin päätöksiin (esim. väärin tulkitut signaalit). Vahva datavalidointi
ja suodatus tarvitaan ennen kuin poikkeamalippuja käytetään päätöksenteossa.

---

### 3. Pysyvä henkilökohtainen neuvoja/konsierki-agentti

**Määritelmä:** Asiakas kohtaa monimutkaisen, korkean panoksen, toistuvan
päätöksen (mitä ostaa, miten sijoittaa, miten hoitaa terveyttä), johon hän saa
tänään geneeristä, kertaluontoista neuvontaa. Pysyvä agentti seuraa asiakkaan
tilannetta jatkuvasti ja päivittää suositusta ajan myötä.

**Diagnostinen kysymys:** *"Missä asiakkaanne kohtaa toistuvan, monimutkaisen
päätöksen, johon he saavat tänään vain kertaluontoisen, geneerisen neuvon?"*

**AI-tyyppi:** Agentic AI

**Esimerkkejä toimialalta:**
- [Consumer] *AI assistant for vehicle buying and leasing* — hyper-
  personoidut suositukset ostopäätöksen tueksi.
- [Financial Services] *Ultra-personalized financial advice and wealth
  management* — automatisoitu, jatkuvasti mukautuva varainhoitoneuvonta.
- [Financial Services] *Enhanced AI support for customers* ("Financial
  guardian") — henkilökohtainen virtuaaliavustaja päivittäisiin tarpeisiin.
- [Life Sciences & Health Care] *Hyper-personalized health care* — 24/7
  virtuaalinen hoitotiimi, joka seuraa potilasdataa ja koordinoi hoitoa.
- [Consumer] *Product recommendations* ("A virtual shopping assistant") —
  personoidut tuotesuositukset käyttäytymisdatan pohjalta.

**Riskilinssi:** *Private* ja *Transparent and explainable* — jatkuva,
henkilökohtainen seuranta vaatii selkeän tietosuojaperustan ja kyvyn
selittää, miksi suositus muuttui.

---

### 4. Ennakoiva laitehälytys ja autonominen interventio

**Määritelmä:** Laitteiden/infrastruktuurin kuntoa valvotaan jatkuvasti
sensoridatalla ajoitetun/manuaalisen tarkastuksen sijaan; vikaantuminen
ennustetaan ja siihen puututaan ennen katkosta.

**Diagnostinen kysymys:** *"Missä nojaatte ajoitettuun tai manuaaliseen
tarkastukseen jatkuvan mittauksen sijaan, ja mitä suunnittelematon katkos
siellä maksaisi?"*

**AI-tyyppi:** Agentic AI / Physical AI

**Esimerkkejä toimialalta:**
- [Energy, Resources & Industrials] *AI-driven predictive maintenance* —
  laitteiston kunnon valvonta, juurisyyn diagnoosi, ennakoiva huolto.
- [Energy, Resources & Industrials] *Autonomous drone-based infrastructure
  inspection* — miehittämättömät, AI-ohjatut tarkastukset voimalinjoilla,
  putkistoilla, siirtotorneissa.
- [Energy, Resources & Industrials] *Predictive monitoring for environment
  health & safety* — näkövalvonta droneilla, roboteilla ja kiinteällä
  infralla riskien varhaiseen tunnistamiseen.
- [Energy, Resources & Industrials] *Inspection of network and utility
  infrastructure* — satelliitti-, LiDAR- ja dronedatan käyttö
  rappeutumisen tunnistamiseen.
- [Financial Services] *Predictive maintenance and autonomous operations
  for IT infrastructure & ATMs* — reunalaskennan hyödyntäminen käyttöajan
  varmistamiseksi.

**Riskilinssi:** *Safe and secure* — fyysiseen infraan puuttuvan
automatisoidun toiminnon pitää olla varmistettu virhetilanteita vastaan
(esim. ihmisen vahvistus ennen fyysistä interventiota).

---

### 5. Etulinjan tehtävien ja työnjaon orkestrointi

**Määritelmä:** Etulinjan työntekijät (kauppa, huoltoteknikot, kaupunki-
infrastruktuuri) saavat päivän prioriteettinsa staattisesta aikataulusta tai
esihenkilön arviosta reaaliaikaisen, signaalipohjaisen uudelleenpriorisoinnin
sijaan.

**Diagnostinen kysymys:** *"Missä etulinjan työntekijät saavat päivän
prioriteettinsa staattisesta aikataulusta sen sijaan, että ne mukautuisivat
reaaliaikaisiin signaaleihin?"*

**AI-tyyppi:** Agentic AI

**Esimerkkejä toimialalta:**
- [Consumer] *Next-generation store operations* — autonominen kaupan sisäisten
  toimintojen koordinointi reaaliaikaisen tilanteen mukaan.
- [Energy, Resources & Industrials] *Autonomous field operations management* —
  tehtävien koordinointi ja etulinjan päätöksenteon automatisointi.
- [Energy, Resources & Industrials] *Workforce scheduling and dispatch* —
  huoltohenkilöstön aikataulutus vikaennusteiden perusteella.
- [Government & Public Services] *Smart city operations and urban
  infrastructure modernization* — kaupunki-infran valvonta ja tehtävien
  ohjaus reaaliaikaisesti.

**Riskilinssi:** *Responsible and accountable* — kun järjestelmä ohjaa
ihmisten päivittäistä työtä, pitää olla selvä, kuka kantaa vastuun jos
priorisointi menee pieleen.

---

### 6. Näköohjattu fyysinen käsittely ja laadunvalvonta

**Määritelmä:** Ihminen tarkastaa tai käsittelee fyysisiä kohteita visuaalisesti
toistuvassa, suurivolyymisessa, määritellyn toleranssin tehtävässä — kone-
näkö + robotiikka tekee saman.

**Diagnostinen kysymys:** *"Missä ihminen tarkastaa tai käsittelee fyysisiä
kohteita visuaalisesti toistuvassa, suurivolyymisessa tehtävässä, jolla on
selkeät toleranssirajat?"*

**AI-tyyppi:** Physical AI

**Esimerkkejä toimialalta:**
- [Consumer] *Vision-enabled store operations* — hyllyjen toteutuksen ja
  planogrammin noudattamisen seuranta konenäöllä.
- [Consumer] *Robotic stowing and picking system* — robottikäsittely
  varastohyllyillä konenäön avulla.
- [Consumer] *Vision-enabled robotic induction* — SKU-vaihtelun käsittely
  teollisella läpivirtausnopeudella.
- [Energy, Resources & Industrials] *Autonomous self-calibrating quality and
  process control* — vikojen tunnistus ja itsekalibroituva prosessinohjaus.
- [Energy, Resources & Industrials] *Defect detection for industrial
  machinery* — konenäköavusteinen tarkastus ihmisvahvistuksella.
- [Energy, Resources & Industrials] *Precision-critical high-value
  manufacturing* — tarkkuuskriittinen kokoonpano ihmisvalvonnassa.

**Riskilinssi:** *Robust and reliable* ja *Safe and secure* — konenäön
virhetunnistus fyysisessä ympäristössä voi aiheuttaa turvallisuusriskin,
ei vain laatuvirheen.

---

### 7. Autonominen liikkuva fyysinen operointi (logistiikka/kuljetus)

**Määritelmä:** Materiaalia tai ihmisiä siirretään fyysisesti ennalta
kiinteän reitin/aikataulun mukaan; autonomiset ajoneuvot/robotit havaitsevat
olosuhteet reaaliajassa ja mukauttavat reittiä, nopeutta ja toteutusta
liikkeessä.

**Diagnostinen kysymys:** *"Missä materiaali tai ihmiset liikkuvat kiinteän
reitin/aikataulun mukaan sen sijaan että reitti mukautuisi reaaliaikaisiin
olosuhteisiin?"*

**AI-tyyppi:** Physical AI

**Esimerkkejä toimialalta:**
- [Consumer] *Autonomous transport for urban mobility services* — kuljettaja-
  vapaat ajoneuvot henkilö- ja tavarakuljetuksiin.
- [Consumer] *Fleet telemetry and route optimization* — reunälaskenta
  ajoneuvoissa reitityksen mukauttamiseksi liikkeessä.
- [Consumer] *Autonomous material movement in consumer fulfillment
  environments* — AMR-robotit, jotka jakavat tilaa ihmistyöntekijöiden
  kanssa.
- [Energy, Resources & Industrials] *Autonomous haulage systems for safe &
  intelligent mining operations* — autonomiset kaivosrekat ja niiden
  turvallinen sensoripohjainen koordinointi.
- [Energy, Resources & Industrials] *Autonomous agriculture and precision
  farming* — drone- ja maarobottiverkosto peltotoimenpiteisiin.

**Riskilinssi:** *Safe and secure* on hallitseva — ihmisten ja koneiden
jaettu fyysinen tila vaatii todennettua turvallisuusarkkitehtuuria ennen
käyttöönottoa.

---

### 8. Jatkuva monimuotoinen sisällöntuotanto

**Määritelmä:** Sisällöntuotanto (teksti, kuva, video) on pullonkaulautunut
pieneen luovaan tiimiin; brändinmukaista luonnosta voitaisiin tuottaa
jatkuvasti ja trenditietoisesti sen sijaan.

**Diagnostinen kysymys:** *"Missä sisällöntuotanto pullonkaulautuu pieneen
tiimiin, ja voisiko brändinmukaisia luonnoksia tuottaa jatkuvasti?"*

**AI-tyyppi:** merkitsemätön (generatiivinen AI)

**Esimerkkejä toimialalta:**
- [Consumer] *Marketing content assistant* — tehokas, yhdenmukainen,
  personoitu sisällöntuotanto eri modaliteeteissa.
- [Consumer] *Social media content generation* — autonominen, trenditietoinen
  monimuotoinen sisällöntuotanto.
- [Consumer] *Planning for promotions* — promootiosuunnitelmien, neuvottelu-
  materiaalien ja pitch-deckien valmistelu.
- Teematasolla myös Technology, Media & Telecommunications -toimialalla:
  mediaorganisaatiot käyttävät generatiivista AI:ta hyperpersonoituun
  sisältöön ja editorial-työnkulkujen automatisointiin (raportin teema,
  ei yksittäinen poimittu case).

**Riskilinssi:** *Transparent and explainable* — automaattisesti tuotetun
sisällön alkuperä ja tekijänoikeusstatus pitää pystyä jäljittämään.

---

### 9. Luonnollisen kielen pääsy yrityksen tietoon

**Määritelmä:** Päätöksentekijä odottaa analyytikkoa tai erikoisosaajaa
kääntämään kysymyksen raportiksi, vaikka data on jo olemassa. Luonnollisen
kielen käyttöliittymä avaa pääsyn suoraan.

**Diagnostinen kysymys:** *"Missä päätöksentekijä odottaa analyytikkoa
kääntämään kysymyksen raportiksi, vaikka data on jo olemassa?"*

**AI-tyyppi:** merkitsemätön

**Esimerkkejä toimialalta:**
- [Consumer] *Data access for all* — liiketoimintakäyttäjien ohjaus
  kuluttajadatan oivalluksiin luonnollisen kielen kyselyillä.
- [Financial Services] *Business intelligence at your fingertips* —
  yrityslaajuinen data-haku luonnollisen kielen rajapinnalla.
- [Government & Public Services] *Digitizing policymaking* — politiikka-
  dokumenttien haku ja luonnollisen kielen vastaukset monimutkaisissa
  politiikkaympäristöissä.
- [Government & Public Services] *Global policy tracking* — julkisen
  politiikan kehityksen seuranta ja analyysi reaaliajassa satojen maiden
  yli.
- [Consumer] *Next-level market intelligence* ("Market research") —
  markkinatutkimuksen nopeuttaminen suurten materiaalimäärien tiivistyksellä.

**Riskilinssi:** *Robust and reliable* — luonnollisen kielen vastaus voi
näyttää varmalta vaikka data taustalla olisi puutteellista; lähteen
jäljitettävyys vastauksesta on tärkeä.

---

### 10. Jatkuva compliance- ja riskivalvonta

**Määritelmä:** Compliance/riski/petos tarkistetaan tänään jaksottaisella
syklillä (neljännesvuosittainen audit, pistokoe); jatkuva, monisignaalinen
valvonta korvaa jaksottaisen tarkistuksen.

**Diagnostinen kysymys:** *"Missä tarkistatte compliancea, riskiä tai
petosta jaksottaisella syklillä sen sijaan että valvonta olisi jatkuvaa?"*

**AI-tyyppi:** Agentic AI / merkitsemätön

**Esimerkkejä toimialalta:**
- [Financial Services] *AI-powered risk management and regulatory
  compliance* — aina-päällä-compliance-tiimi erikoistuneilla agenteilla.
- [Financial Services] *Focused cyber* — turva-hälytysten suodatus,
  analyysi ja priorisointi todellisten uhkien mukaan.
- [Government & Public Services] *Global policy tracking* — (ks. myös
  patterni 9 — tämä case istuu kahteen patterniin: tiedonhakuun JA
  jatkuvaan valvontaan riippuen käyttötarkoituksesta).

**Riskilinssi:** *Responsible and accountable* — jatkuva automaattinen
valvonta ei saa hämärtää sitä, kuka tekee lopullisen eskalointipäätöksen.

---

### 11. AI-nopeutettu suunnittelu- ja tutkimussilmukka

**Määritelmä:** T&K/suunnitteluprosessi etenee hitaana, porttivaiheistettuna
syklinä, jossa vain harvat mahdollisista vaihtoehdoista koskaan tutkitaan.
Simulaatio/generointi mahdollistaa nopeamman iteroinnin laajemmalla
vaihtoehtoavaruudella.

**Diagnostinen kysymys:** *"Missä T&K/suunnitteluprosessinne etenee hitaana,
porttivaiheistettuna syklinä, jossa vain harvat mahdollisista vaihtoehdoista
koskaan tutkitaan?"*

**AI-tyyppi:** Agentic AI / Physical AI (simulaatio)

**Esimerkkejä toimialalta:**
- [Consumer] *AI-orchestrated product design* — koko tuotesuunnittelun
  elinkaaren orkestrointi markkinasensoroinnista iterointiin.
- [Energy, Resources & Industrials] *Materials design* — laajempi
  materiaalien design-avaruus ja nopeutettu ominaisuusoptimointi.
- [Energy, Resources & Industrials] *Site design generation* — site-
  suunnittelun automatisointi ja ajan/kustannusten pienentäminen.
- [Energy, Resources & Industrials] *Hydrocarbon reservoir exploration* —
  löydösasteen optimointi ja riskien vähentäminen sijainnin
  karakterisoinnissa.
- [Energy, Resources & Industrials] *Simulation-first development & digital
  twins* — fyysisten järjestelmien validointi virtuaalisesti ennen
  käyttöönottoa.

**Riskilinssi:** *Robust and reliable* — simulaatiopohjaisen mallin
tarkkuus pitää validoida oikeaa maailmaa vasten ennen kuin sen tuottamiin
suunnitelmiin nojataan täysin.

---

### 12. Simulaatiopohjainen asiantuntemuksen skaalaus

**Määritelmä:** Asiantuntijaosaaminen on pullonkaulautunut harvoihin
ihmisiin, jotka eivät voi olla kaikkialla; digitaalinen kaksonen tai
simulaatio antaa useammalle mahdollisuuden harjoitella turvallisesti tai
saada etäasiantuntijatukea.

**Diagnostinen kysymys:** *"Missä asiantuntijaosaaminen on pullonkaulautunut
harvoihin ihmisiin, jotka eivät voi olla kaikkialla?"*

**AI-tyyppi:** Physical AI (simulaatio/AR-VR)

**Esimerkkejä toimialalta:**
- [Energy, Resources & Industrials] *Personalized OHS training* —
  personoitu, immersiivinen työturvallisuuskoulutus realistisilla
  skenaarioilla.
- [Energy, Resources & Industrials] *Simulation-driven remote operations
  and training* — AR/VR-digitaaliset kaksoset offshore-laitoksista
  etäasiantuntijatukea varten.

**Riskilinssi:** *Safe and secure* — simulaatiokoulutuksen pitää vastata
riittävän tarkasti oikeaa ympäristöä, jotta opittu käyttäytyminen siirtyy
turvallisesti oikeaan tilanteeseen.

---

### 13. AI-avusteinen ohjelmistokehitys

**Määritelmä:** Kehittäjät kirjoittavat, testaavat, dokumentoivat ja
debuggaavat koodia manuaalisesti; AI-avusteiset työkalut nopeuttavat samaa
työtä ilman että kehittäjän rooli katoaa.

**Diagnostinen kysymys:** *"Missä kehitystiiminne käyttää suurimman osan
ajastaan rutiininomaiseen koodin kirjoittamiseen, testaamiseen tai
dokumentointiin, joka voisi olla AI-avusteista?"*

**AI-tyyppi:** merkitsemätön / Agentic AI

**Esimerkkejä toimialalta:**
- [Consumer] *Code assist for developers* ("Augmented developer") —
  sovellusten ja alustojen kehityksen ja ylläpidon tuki.
- [Financial Services] *Transformation with speed and confidence* ("Code
  assistant for digital transformation") — pankkien digitalisaation
  nopeuttaminen koodiavustimilla.
- Teematasolla myös Technology, Media & Telecommunications -toimialalla:
  kehittäjät käyttävät AI-työkaluja koodin kirjoittamiseen, testaamiseen,
  dokumentointiin ja debuggaamiseen nopeammin, ja IT-operaatiotiimit
  ottavat käyttöön agentteja järjestelmien valvontaan, katkosennustukseen
  ja automaattiseen ratkaisuun (raportin teema, ei yksittäinen poimittu
  case).

**Riskilinssi:** *Robust and reliable* — AI-generoitu koodi tarvitsee saman
tai tiukemman testauskurin kuin ihmisen kirjoittama, ei löysempää.

---

## Ristiintarkistus toisella lähteellä

Toinen, riippumaton toimialan AI-käyttötapauskooste (63 käyttötapausta, 16
funktiota) osoittaa n. 75 %:n arvioidusta arvosta keskittyvän neljään
funktioon: **asiakasoperaatiot, markkinointi & myynti, ohjelmistokehitys,
T&K.** Yllä oleva 13 patternin kirjasto peittää kaikki neljä: patternit 3 ja 2
(asiakasoperaatiot/dokumenttivalidointi), patternit 8 ja 1 (markkinointi &
myynti), patterni 13 (ohjelmistokehitys), patternit 11–12 (T&K). Tämä ei ole
sattumaa — se on kohtuullinen ristiintarkistus siitä, että kuratointi ei ole
jättänyt suurinta arvoa tuottavia alueita ulkopuolelle.

## Miten kirjastoa käytetään ja miten sitä laajennetaan

Ks. `../skills/ai-capability-pattern-matching/SKILL.md` käyttöohjeelle.
Uusia patterneja lisätessä: seuraa samaa nelikysymysabstraktiota kuin
`../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`
kuvaa, vaadi vähintään kolme aidosti erilaista esimerkkiä ennen kuin nimeät
uuden patternin, ja merkitse lähde aina selvästi (mistä raportista/casesta
esimerkki on poimittu) — älä koskaan lisää esimerkkiä muistista.
