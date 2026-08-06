# Datan roolin heuristiikat — laajempi kokoelma

Taustamateriaali skillille `../skills/data-role-diagnosis/SKILL.md`. Tämä
tiedosto kokoaa lisää diagnostisia kysymyksiä ja esimerkkejä kahden
päänäkökulman (mahdollistaja vs. strateginen assetti) tueksi.

## Mahdollistaja vs. strateginen assetti — vertailutaulukko

| Ulottuvuus | Data mahdollistajana | Data strategisena assettina |
|---|---|---|
| Perusluonne | Hyödyke, kustannus (välttämätön) | Omaisuus, jonka arvo kasvaa |
| Ydinkysymys | "Auttaako tämä meitä tekemään nykyisen asiamme nopeammin, halvemmin, laadukkaammin?" | "Voimmeko myydä tätä, tai kouluttaa sillä mallin jota kilpailija ei pysty kopioimaan?" |
| Fokus | Data governance, laatu, integraatiot, operatiivinen tehokkuus | Monetisaatio, data-verkostovaikutukset (flywheel), uudet liiketoimintamallit |
| Mittari | Kustannussäästö, virheiden vähentyminen, prosessin nopeus | ROI, uusi liikevaihto, defensoitava kilpailuetu |
| Tyypillinen esimerkki | Data governance -mallin pystyttäminen ei itsessään tuota rahaa, mutta mahdollistaa esim. asiakasraportoinnin automatisoinnin | Ostokäyttäytymisdata käytetään "Next Best Action" -suositusalgoritmin rakentamiseen, joka myydään palveluna |
| Riski jos roolia ei tunnisteta | Investoidaan monetisaatioon ilman toimivaa dataperustaa — epäonnistuu laadun/luotettavuuden takia | Datan arvo aliarvioidaan, sitä käsitellään pelkkänä IT-kuluna eikä kilpailuetuna |

## Diagnostisia lisäkysymyksiä

- Kuka organisaatiossa "omistaa" tämän datan tänään, ja onko omistajuus
  kytketty budjettiin (kustannuspaikka) vai tulokseen (P&L-vastuu)? Data
  joka on vain kustannuspaikan alla käsitellään lähes aina mahdollistajana
  riippumatta sen todellisesta potentiaalista.
- Onko organisaatiossa joskus kysytty "voisimmeko myydä tätä?" tästä
  datasta, ja mitä vastattiin? Jos kysymystä ei ole koskaan edes esitetty,
  se on merkki siitä että data on oletusarvoisesti kehystetty
  mahdollistajaksi ilman tietoista päätöstä.
- Onko dataa, joka näyttää mahdollistajalta yhdessä liiketoimintayksikössä
  mutta assetilta toisessa (esim. logistiikkadata joka on operatiivinen
  kulu logistiikkatiimille mutta arvokas ennustedata myynnille)? Rooli ei
  ole aina koko organisaation yhteinen totuus — se voi vaihdella
  näkökulman mukaan.

## Offense / Defense -kehys käytännössä

Datastrategian keskustelu menee usein sekaisin, koska samalla termillä
("datastrategia") tarkoitetaan kahta eri asiaa:

- **Defense (puolustus):** data governance, laatu, turvallisuus,
  vaatimustenmukaisuus. Tavoite: vähentää riskiä ja virheitä, mahdollistaa
  luotettava käyttö. Ei suoraan tuota uutta liikevaihtoa.
- **Offense (hyökkäys):** datan hyödyntäminen uuden liiketoiminnan,
  tuotteen tai kilpailuedun lähteenä. Tavoite: kasvu ja erottautuminen.
  Vaatii toimivan defense-perustan taustalle.

Tyypillinen sudenkuoppa: organisaatio haluaa "offense"-tason tuloksia
(uusia tulovirtoja, AI-tuotteita) mutta datansa on vasta "defense"-tason
kypsyydessä (siiloutunutta, epäjohdonmukaista, ei luotettavasti
saatavilla). Tällöin ensimmäinen oikea investointi ei ole offense vaan
defense — vasta sen jälkeen offense-investoinnit kannattavat.

## Ks. myös

- `../skills/data-role-diagnosis/SKILL.md` — pääskilli, joka käyttää
  tätä taustamateriaalia
- `../skills/data-monetization-model-selection/SKILL.md` — seuraava askel
  kun rooli on validoitu assetiksi
