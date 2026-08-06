---
name: data-monetization-model-selection
description: "Valitsee ja perustelee sopivan datan monetisointimallin (suora: DaaS/Insight-as-a-Service/datavaihdanta vs. epäsuora: tuotteen rikastaminen/resurssien optimointi/riskien minimointi/Data Flywheel) päätöspuulla ja tarkistaa Data Flywheel -väitteen toteutettavuuden nelikohtaisella listalla. Käytä kun data on validoitu strategiseksi assetiksi ja pitää päättää MITEN sitä monetisoidaan."
---

# Data Monetization Model Selection

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Kun data on diagnosoitu strategiseksi assetiksi (ks.
`../data-role-diagnosis/SKILL.md`), seuraava kysymys ei ole "kannattaako
monetisoida" vaan "millä mallilla". Suora ja epäsuora monetisointi
vaativat eri valmiudet, eri riskiprofiilin ja eri aikataulun — sekoitus
näiden välillä ilman tietoista valintaa johtaa tyypillisesti siihen, että
organisaatio yrittää myydä dataa ulos ennen kuin sisäinen tuotteistus on
edes kokeiltu, tai päinvastoin jättää selvän ulkoisen kysynnän
hyödyntämättä. Tämä skilli tuottaa perustellun mallivalinnan ja
tarkistaa erikseen, onko "data flywheel" -väite todellinen vai
toiveajattelua.

## Ankkurointi tutkimukseen

- Suoran ja epäsuoran datan monetisoinnin mallit (toimialan
  konsultointikäytäntö, usean lähteen synteesi 2026): Data-as-a-Service,
  Insight-as-a-Service, datavaihdanta/IP-lisensointi (suora); tuotteen
  rikastaminen, käyttöasteen/resurssien optimointi, liiketoimintariskien
  minimointi (epäsuora).
- Data Flywheel -mekanismi AI-liiketoiminnassa: uniikki data → mallin
  koulutus → parempi tuote → lisää käyttäjiä → lisää dataa. Käsitteenä
  laajennus Collinsin (2001) flywheel-mekanismista (ks.
  `../data-role-diagnosis/SKILL.md`:n ankkurointi) sovellettuna
  data-/AI-kontekstiin.
- `../../../business-design-frameworks` ja
  `../../../specialisation-packs/business-model-canvas` -pakkien
  liiketoimintamallin innovaatiopatternit (mm. `financial.rev.data_monetization`,
  `operating.resources.leverage_customer_data`) — tämä skilli syventää
  yhtä patterniperhettä data-spesifisti.

## Rakenne (luonnos — täydennettävä)

1. **Käy läpi suoran monetisoinnin päätöspuu ensin, koska se sulkee pois
   vaihtoehtoja nopeasti:**
   - Onko datan ulosmyynti juridisesti/sopimuksellisesti sallittua
     (asiakassopimukset, GDPR ja muu tietosuoja, kolmansien osapuolten
     IP-oikeudet)? Jos ei, suora malli on suljettu pois ilman erillistä
     juridista selvitystä — älä jatka suoraan malliin ennen tätä
     tarkistusta.
   - Onko olemassa tunnistettu ulkoinen ostaja tai markkina tälle
     datalle/oivallukselle TÄNÄÄN (resale-testi, ks.
     `../data-role-diagnosis/SKILL.md`)? Jos ei, suora malli vaatisi
     ensin markkinan validoinnin, ei vain tuotteistuksen.
   - Onko data riittävän uniikkia, ettei ostaja voisi hankkia samaa
     halvemmalla muualta (defensibility-testi)? Jos data on yleisesti
     saatavilla, hinnoitteluvoima suoramyynnissä on heikko.
   Jos kaikki kolme läpäistään, harkitse suoraa mallia: DaaS/raakadatan
   myynti (matalin jalostusaste, vaatii vahvimman data governancen),
   Insight-as-a-Service (analytiikka/ennusteet raakadatan sijaan,
   suojaa raakadatan paremmin) tai datavaihdanta/IP-lisensointi
   (data vaihdetaan toisen osapuolen dataan, teknologiaan tai
   markkinapääsyyn — yleinen malli innovaatioekosysteemeissä).
2. **Jos suora malli ei läpäissyt kohtaa 1, siirry epäsuoraan malliin**
   — tämä on useimmiten sekä tuottoisampi että riskittömämpi vaihtoehto:
   - **Tuotteen/palvelun rikastaminen:** data mahdollistaa uuden,
     maksullisen ominaisuuden tai paremman käyttäjäkokemuksen olemassa
     olevassa tuotteessa (esim. hyperpersonointi).
   - **Käyttöasteen/resurssien optimointi:** data paljastaa pullonkaulat
     ja mahdollistaa dynaamisen hinnoittelun tai resurssien
     tehokkaamman allokoinnin — näkyy suoraan kustannussäästönä tai
     lisätulona.
   - **Liiketoimintariskien minimointi:** data mahdollistaa ennakoivan
     havaitsemisen (esim. asiakaspoistuma, petos, laitevika) ennen
     tapahtumaa — "säästetty euro on ansaittu euro".
3. **Jos väitetään "data flywheel" -mallia, tarkista se erikseen
   nelikohtaisella listalla — älä hyväksy flywheel-väitettä ilman tätä:**
   - **Uniikki keräyskanava:** onko olemassa todellinen, jatkuva tapa
     kerätä dataa jota kilpailijalla ei ole samassa laajuudessa?
   - **Mitattava mallin paraneminen:** paraneeko malli/tuote todistetusti
     (ei oletetusti) kun dataa kertyy lisää — onko tästä jo havaintoa
     vai on tämä vielä olettamus?
   - **Havaittava käyttäjäkokemuksen paraneminen:** huomaako käyttäjä
     mallin paranemisen, vai onko parannus niin pieni ettei se vaikuta
     käyttäytymiseen?
   - **Silmukan sulkeutuminen kasvuna:** houkutteleeko havaittu
     parannus todistetusti lisää käyttäjiä, jotka tuottavat lisää dataa
     — vai katkeaako silmukka jossain (esim. parannus ei riitä uusien
     käyttäjien houkutteluun)?
   Jos yksikin neljästä kohdasta ei läpäise tarkistusta tai on vielä
   pelkkä oletus, nimeä se eksplisiittisesti riskiksi äläkä esitä
   flywheeliä valmiina, itsestään toimivana mekanismina.
4. **Vertaile mallia nopeuden, riskin ja kilpailuedun akselilla**, ei
   pelkän tulopotentiaalin: suora malli tuottaa usein nopeamman,
   mutta helpommin kopioitavan tulovirran (data itsessään ei enää ole
   yksinoikeutesi kun se on myyty); epäsuora malli rakentaa hitaammin
   mutta defensoitavampaa etua.
5. **Tuota perusteltu suositus yhdellä lauseella per vaihtoehto**, joka
   nimeää MIKSI malli sopii tai ei sovi tähän tilanteeseen — ei pelkkää
   mallin nimeä.

## Mitä tämä skilli EI tee

- Ei tee juridista arviota tietosuoja- tai sopimusoikeudellisista
  esteistä datan ulosmyynnille — tunnistaa että tarkistus tarvitaan,
  ei korvaa erillistä tietosuoja-/juridista asiantuntemusta.
- Ei laske tarkkaa hinnoittelua tai ROI:ta valitulle mallille — ks.
  `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`.
- Ei väitä, että epäsuora malli on aina parempi kuin suora — konteksti
  ratkaisee; skilli tuottaa jäsennellyn vertailun, ei valmista vastausta.
- Ei vahvista lukuja, markkinakysyntää tai kilpailijadataa muistista —
  käyttää käyttäjän antamia lähtöarvoja tai merkitsee oletuksen selvästi
  (`[oletus — tarkista]`).

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia esimerkkejä siitä, missä tilanteessa suora vs. epäsuora malli
  osoittautui oikeaksi valinnaksi (ja miksi väärä valinta olisi
  epäonnistunut)
- konkreettinen päätöspuupohja visuaalisena työkaluna
  (`../../references/`-kansioon)
- omia havaintoja siitä, mikä flywheel-tarkistuksen neljästä kohdasta
  pettää useimmin käytännössä

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä: `../data-role-diagnosis/SKILL.md`
  — vahvista ensin, että data läpäisee assetti-testit.
- Ennen tätä (priorisointi ennen mallivalintaa): `../data-ai-strategy-design-and-prioritization/SKILL.md`
- Liittyvä skilli toisessa pakissa: `../../../specialisation-packs/business-model-canvas/skills/bmc-innovation-pattern-matching/SKILL.md`
  — jos valittu monetisointimalli pitää vielä sovittaa laajempaan
  liiketoimintamalliin (Financial Model -patternit).
- Liittyvä skilli toisessa pakissa: `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`
  — kääntää valitun mallin taloudelliseksi laskelmaksi.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/data-monetization-frameworks.md` — laajempi
  vertailu suoran ja epäsuoran monetisoinnin malleista
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
