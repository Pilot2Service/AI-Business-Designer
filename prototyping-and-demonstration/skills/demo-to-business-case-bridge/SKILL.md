---
name: demo-to-business-case-bridge
description: "Kääntää demon/PoC:n tulokset business case -kelpoisiksi ROI-syötteiksi: erottelee teknisen suorituskyvyn ja liiketoimintavaikutuksen mittarit, testaa skaalautuuko PoC-mittakaavan tulos vastuullisesti tuotantomittakaavaan, ja tarkistaa vastaako oletettu ROI-mekanismi asiakkaan todellista organisaatiorakennetta. Käytä heti onnistuneen demon/PoC:n jälkeen ennen kuin sen tuloksia syötetään business case- tai ROI-laskelmaan."
---

# Demo-to-Business-Case Bridge

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin virhe demon jälkeen: **PoC-mittakaavan tuloksen suoraviivainen
ekstrapolointi** tuotantomittakaavan ROI-luvuksi ilman että kukaan
tarkistaa, pitääkö oletus paikkansa. "Säästi 2 tuntia 10 testitapauksessa"
ei automaattisesti tarkoita "säästää 200 tuntia kuukaudessa tuotannossa" —
väliin tarvitaan eksplisiittinen, tarkistettu oletusketju. Tämä skilli on
silta `../rapid-prototype-and-vibe-coding-craft/SKILL.md`- ja
`../demo-delivery-and-storytelling/SKILL.md`-skillien tuottaman demo-
näytön ja `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`-
sekä `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`-
skillien vaatiman jäsennellyn talousperustelun välillä.

## Ankkurointi tutkimukseen

- Tutkimussynteesi (2026) demon/PoC:n tulosten kääntämisestä liiketoiminta-
  kieleksi: kaksi erillistä mittariluokkaa (tekninen suorituskyky ja
  liiketoimintavaikutus), paluu alkuperäiseen hypoteesiin ja
  lähtötasoon/onnistumiskriteereihin, talousosaston ottaminen mukaan
  varhain mittaustavan validoimiseksi, ja varoitus siitä että ROI-
  mekanismin (esim. "säästää henkilötyötä") pitää vastata asiakkaan
  todellista organisaatiorakennetta — jos organisaatio ei pysty tai halua
  vähentää henkilöstöä, henkilötyösäästöön perustuva ROI ei realisoidu
  vaikka tekninen suorituskyky olisi todistettu.

## Rakenne (luonnos — täydennettävä)

1. **Palaa alkuperäiseen hypoteesiin ja onnistumiskriteereihin** (ks.
   `../rapid-prototype-and-vibe-coding-craft/SKILL.md` kohta 1 ja
   `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`).
   Vertaa demon oikeaa tulosta alkuperäiseen kriteeriin sellaisenaan —
   älä anna demon aikana syntyneen innostuksen (tai pettymyksen) vääristää
   arviota siitä, täyttyikö alkuperäinen kriteeri.
2. **Erottele kaksi mittariluokkaa selvästi:**
   - **Tekninen suorituskyky** — tarkkuus, kattavuus, virhetaajuus,
     nopeus, mitattuna demo-/PoC-olosuhteissa. Nämä ovat *johtavia
     indikaattoreita*, eivät vielä liiketoiminta-arvoa.
   - **Liiketoimintavaikutus** — aikasäästö, kustannussäästö, uusi
     liikevaihto, riskin pieneneminen, parempi päätöksenteko. Näiden
     PITÄÄ olla johdettu teknisistä tuloksista eksplisiittisellä
     oletusketjulla, ei suoraan väitettynä.
3. **Kirjoita oletusketju näkyväksi jokaiselle liiketoimintavaikutus-
   luvulle:** "PoC:ssa X tapahtui otoksella N → oletamme että sama
   pätee tuotantomittakaavassa, koska [perustelu] → tämä tarkoittaa
   Y liiketoiminta-arvoa, olettaen Z [esim. käyttöaste, adoptioaste]."
   Jos et pysty täyttämään perustelu-kohtaa uskottavasti, älä esitä
   liiketoimintalukua vahvistettuna — merkitse se `[oletus — tarkista]`
   (ks. pakin `../../CLAUDE.md`).
4. **Tarkista, että oletettu ROI-mekanismi vastaa asiakkaan todellista
   organisaatiorakennetta ja -kulttuuria.** Yleisin sudenkuoppa: ROI
   perustuu oletettuun henkilötyön vähenemiseen, mutta asiakkaan
   organisaatio ei aio tai pysty vähentämään henkilöstöä (ay-sopimukset,
   strateginen päätös pitää henkilöstö ja suunnata heidät muihin
   tehtäviin, jne.) — tällöin ROI pitää laskea uudelleen kapasiteetin
   vapautumisena/laadun paranemisena, ei suorana kustannussäästönä.
   Kysy tämä eksplisiittisesti asiakkaalta ennen kuin lukitset ROI-
   mekanismin.
5. **Ota talousosasto tai vastaava mukaan mahdollisimman varhain**
   validoimaan mittaustapa ja lähtötaso (baseline) — ROI-luku jonka
   asiakkaan oma talousosasto on hyväksynyt on huomattavasti
   vakuuttavampi kuin konsultin oma laskelma.
6. **Vie validoidut oletukset ja liiketoimintavaikutusluvut**
   `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
   -skilliin täydeksi business caseksi (ongelma, ratkaisu, talous, riskit,
   aikataulu, suositus) ja
   `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`
   -skilliin ROI/NPV/IRR-laskentaan ja herkkyysanalyysiin — tee
   herkkyysanalyysi erityisesti niille oletuksille jotka merkitsit
   kohdassa 3 heikoimmiksi.
7. **Kirjaa myös se, mitä demo/PoC EI todistanut** liiketoimintavaikutuksen
   osalta (esim. adoptioaste, muutosjohtamisen kustannus, integraatiotyö)
   business casen riskiosioon — nämä ovat tyypillisesti juuri ne asiat
   jotka johtavat "pilot purgatoryyn" jos niitä ei huomioida etukäteen.

## Mitä tämä skilli EI tee

- Ei laske ROI:ta, NPV:tä tai IRR:ää itse — tuottaa validoidut,
  läpinäkyvät syötteet
  `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`
  -skillille.
- Ei kirjoita täyttä business casea — se on
  `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
  -skillin tehtävä.
- Ei takaa että PoC-mittakaavan tulos skaalautuu tuotantoon — päinvastoin,
  sen ydintehtävä on pakottaa näkyväksi ne oletukset joiden varassa
  skaalautumisväite lepää.
- Ei arvioi teknistä toteutettavuutta tuotantomittakaavassa — ks.
  `../../../ai-strategy-and-governance/skills/ai-use-case-feasibility-and-poc-scoping/SKILL.md`
  ja `../../../ai-strategy-and-governance/skills/build-vs-buy-vs-partner-ai/SKILL.md`.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia esimerkkejä oletusketjuista, jotka osoittautuivat vääriksi
  skaalautuessa PoC:sta tuotantoon — ja mitä opit siitä
- oma mallipohja oletusketjun dokumentointiin (`../../references/`-kansioon)
- nyrkkisääntöjä siitä, minkä tyyppiset ROI-mekanismit yleisimmin
  törmäävät asiakkaan organisaatiorakenteeseen

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä: `../demo-delivery-and-storytelling/SKILL.md`
- Samassa pakissa (jos kehys tehtiin ennen demoa, palaa tarkistamaan
  onnistumiskriteerit): `../demo-framing-and-expectation-setting/SKILL.md`
- Seuraavaksi: `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
  ja `../../../business-case-and-analysis/skills/roi-npv-sensitivity-model/SKILL.md`
- Oletusten testaus ennen lukitsemista: `../../../business-case-and-analysis/skills/assumption-and-evidence-audit/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- Tutkimussynteesi (2026) demon/PoC:n ROI-kääntämisestä — kaksi
  mittariluokkaa, baseline/hypoteesi-vertailu, talousosaston varhainen
  osallistaminen, ROI-mekanismin ja organisaatiorakenteen yhteensopivuus
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
