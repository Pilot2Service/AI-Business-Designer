---
name: data-ai-strategy-design-and-prioritization
description: "Muotoilee Data & AI -strategian holistisesti (ei siiloissa) Driver Tree -työkalulla liiketoimintatavoitteiden pilkkomiseen datapisteiksi, ja priorisoi mitä dataa kerätä/käyttää nyt vs. tulevaisuutta varten Data Readiness x Strategic Value -nelikentällä. Käytä kun organisaatio suunnittelee mihin dataan ja AI-kyvykkyyksiin investoida seuraavaksi."
---

# Data & AI Strategy Design and Prioritization

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää kaksi yleistä datastrategiavirhettä: (1) AI/data-investoinnit
tehdään siiloissa ilman että kukaan on pilkkonut liiketoimintatavoitetta
konkreettisiksi datapisteiksi, jolloin lopputulos on teknisesti
vaikuttava mutta strategisesti irrallinen; ja (2) organisaatio yrittää
rakentaa tulevaisuuden malleja tämän päivän datalla huomaamatta, että
oikea data pitäisi alkaa kerätä jo nyt. Tämä skilli tuottaa jäsennellyn
sillan liiketoimintatavoitteen ja konkreettisen data-/AI-investoinnin
välille, ja priorisoi investoinnit sen mukaan mikä on strategisesti
arvokasta JA datavalmiudeltaan toteutettavissa.

## Ankkurointi tutkimukseen

- Data & AI Design Thinking -perinne (toimialan konsultointikäytäntö,
  usean lähteen synteesi): tekoälystrategiaa ei rakenneta siiloissa —
  moniammatillinen fasilitointi varmistaa, että strategia ratkaisee
  oikeita käyttäjä- ja sidosryhmätarpeita ("Systems over Objects").
- Driver Tree -työkalu (liiketoiminta-analytiikan vakiintunut menetelmä):
  liiketoimintatavoite pilkotaan hierarkkisesti komponenteiksi kunnes
  päästään konkreettisiin, mitattaviin ajureihin — sama looginen periaate
  kuin McKinsey-perinteen issue tree (ks.
  `../../../strategic-thinking/skills/hypothesis-driven-strategy/SKILL.md`),
  sovellettuna tässä datapisteiden ja AI-ratkaisujen tunnistamiseen.
- "Tulevaisuuden mallit vaativat nykypäivän dataa" -heuristiikka
  (data-monetisaatioputken suunnitteluperiaate): jos tietty AI-malli
  halutaan mahdolliseksi 12-24 kuukauden päästä, sen vaatima uniikki data
  pitää alkaa kerätä tänään — data-investoinnin aikaviive on tyypillisesti
  pidempi kuin mallin rakentamisen aikaviive.

## Rakenne (luonnos — täydennettävä)

1. **Rakenna Driver Tree liiketoimintatavoitteesta datapisteisiin.**
   Aloita ylimmän tason liiketoimintatavoitteesta (esim. "kasvata
   asiakaspysyvyyttä") ja pilko se peräkkäisiin kysymyksiin: mitkä
   osatekijät ajavat tätä tavoitetta? Mitä dataa tarvitaan kunkin
   osatekijän mittaamiseen? Mikä AI/analytiikkaratkaisu voisi vaikuttaa
   kuhunkin osatekijään? Jatka pilkkomista kunnes päädyt konkreettisiin,
   mitattaviin datapisteisiin — älä pysähdy abstraktille tasolle
   ("parempi asiakasymmärrys" ei ole datapiste, "asiakkaan käyttöaste
   ominaisuudesta X viimeisen 30 päivän aikana" on).
2. **Arvioi jokainen puun haara: tuoko AI/data tähän oikeasti
   lisäarvoa, vai onko se turhaa?** Ei jokainen liiketoimintatavoitteen
   osatekijä hyödy datasta tai AI:sta — osa ratkeaa paremmin
   prosessimuutoksella tai ihmisen päätöksellä. Merkitse jokainen haara
   joko "data/AI-relevantti" tai "ei data/AI-relevantti, ratkaistaan
   muuten" ennen kuin jatkat vain relevantteihin haaroihin.
3. **Erottele "mitä voimme tehdä nyt" vs. "mitä meidän pitää rakentaa
   tulevaisuutta varten" (Agile Value Assessment).** Jokaiselle
   tunnistetulle datapisteelle:
   - **Käytettävissä nyt:** data on jo olemassa riittävässä laadussa —
     voidaan aloittaa analyysi/malli välittömästi.
   - **Rakennettava:** dataa ei vielä ole tai sen laatu ei riitä —
     vaatii keräyspisteen suunnittelua ennen kuin malli on mahdollinen.
     Sovella "tulevaisuuden mallit vaativat nykypäivän dataa"
     -heuristiikkaa: jos tämä data halutaan käyttöön 12-24 kk päästä,
     keräys pitää aloittaa nyt, ei silloin kun malli halutaan rakentaa.
4. **Sijoita jokainen tunnistettu data/AI-mahdollisuus Data Readiness ×
   Strategic Value -nelikenttään:**
   - **Nyt toteutettavissa, korkea arvo:** aloita ensin — nopein reitti
     todistettuun arvoon.
   - **Rakennettava, korkea arvo:** käynnistä data-keräysinvestointi nyt,
     vaikka malli ei valmistu heti — tämä on strategisin nelikentän
     kohta, koska se rakentaa tulevaa defensoitavaa etua (ks.
     `../data-role-diagnosis/SKILL.md`:n flywheel-testi).
   - **Nyt toteutettavissa, matala arvo:** älä priorisoi, vaikka
     houkuttelisi helppouden vuoksi — matala strateginen arvo ei muutu
     helppoudella.
   - **Rakennettava, matala arvo:** hylkää tai laita jäähylle — kallein
     yhdistelmä (pitkä aikaviive, pieni hyöty).
   Tämä nelikenttä on rakenteeltaan sama logiikka kuin
   `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`:n
   2x2-priorisointimatriisi, mutta akselit ovat data-spesifit
   (Data Readiness, ei Technical Feasibility yleisesti) — käytä tätä
   ENNEN yleistä AI-mahdollisuuksien pisteytystä, kun kysymys on
   nimenomaan datan valmiudesta.
5. **Fasilitoi puun rakentaminen moniammatillisesti**, älä yksin tai
   pelkän data-tiimin kanssa. Liiketoiminnan omistaja tietää mikä ajuri
   on oikeasti tärkeä; data-/tekninen asiantuntija tietää mikä on
   toteutettavissa; loppukäyttäjä tietää mikä ratkaisu oikeasti
   auttaisi arjessa. Puu joka on rakennettu yhdessä näiden kolmen
   näkökulman kanssa on huomattavasti todennäköisemmin oikea kuin
   yhden funktion sisäisesti rakentama.
6. **Tuota priorisoitu tiekartta**, joka erottelee "aloita nyt" (korkea
   arvo, valmis data) ja "aloita datankeräys nyt, malli myöhemmin"
   (korkea arvo, rakennettava data) omiksi rinnakkaisiksi raiteikseen —
   älä sekoita niitä yhdeksi aikajanaksi, koska niillä on eri
   aikahorisontti ja eri onnistumiskriteerit.

## Mitä tämä skilli EI tee

- Ei tee lopullista päätöstä investoinnista puolestasi — tuottaa
  jäsennellyn priorisoinnin ihmisen päätöksenteon tueksi.
- Ei korvaa `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
  -skillin laajempaa 5-ulotteista pisteytystä — tämä skilli tuottaa
  syötteen sinne (erityisesti Data Readiness -ulottuvuuteen) eikä
  itsessään pisteytä koko liiketoimintavaikutusta.
- Ei rakenna teknistä data-arkkitehtuuria tai keräysjärjestelmää —
  tunnistaa MITÄ dataa tarvitaan, ei MITEN se teknisesti kerätään.
- Ei vahvista lukuja, markkinatietoa tai datan laatuarvioita muistista —
  käyttää käyttäjän antamia lähtöarvoja tai merkitsee oletuksen selvästi
  (`[oletus — tarkista]`).

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia Driver Tree -esimerkkejä eri toimialoilta
- konkreettinen fasilitointipohja Driver Tree -työpajalle
  (`../../references/`-kansioon)
- nyrkkisääntöjä siitä, kuinka syvälle puuta kannattaa tyypillisesti
  pilkkoa ennen kuin saavutetaan hyödyllinen datapiste-taso

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä: `../data-role-diagnosis/SKILL.md`
  — selvitä ensin toimiiko data mahdollistajana vai tavoitellaanko
  assetti-roolia, ennen kuin priorisoit investointeja.
- Samassa pakissa seuraavaksi (jos tavoite on monetisaatio):
  `../data-monetization-model-selection/SKILL.md`
- Liittyvä skilli toisessa pakissa: `../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
  — vastaanottaa tämän skillin tuottamat priorisoidut data/AI-
  mahdollisuudet laajempaan 5-ulotteiseen pisteytykseen.
- Liittyvä skilli toisessa pakissa: `../../../strategic-thinking/skills/hypothesis-driven-strategy/SKILL.md`
  — sama issue tree -logiikka sovellettuna yleisemmin strategisiin
  kysymyksiin, ei vain datapisteisiin.
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
