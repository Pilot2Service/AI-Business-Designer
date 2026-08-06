---
name: ai-capability-pattern-matching
description: "Käyttää valmista, tutkimuspohjaista 13 AI-kyvykkyyspatternin kirjastoa (ks. ../../references/ai-capability-pattern-library.md) diagnostisten kysymysten esittämiseen uudelle asiakkaalle/toimialalle raakalistan AI-mahdollisuusehdokkaista kokoamiseksi — vaihtoehto tai täydennys tehtävätason pilkkomiselle."
---

# AI Capability Pattern Matching

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Tuottaa raakalista AI-mahdollisuusehdokkaista **top-down, hypoteesivetoisesti**
käyttäen valmista kyvykkyyspatternikirjastoa — vastapainoksi
`../task-level-decomposition-and-automation-fit/SKILL.md`-skillin **bottom-up,
data-vetoiselle** lähestymiselle (prosessi-/task mining tehtävä kerrallaan).
Nämä kaksi täydentävät toisiaan:

- **Bottom-up** (task-level-decomposition): käydään läpi olemassa oleva
  prosessi/rooli tehtävä kerrallaan ja luokitellaan jokainen. Vahva kun
  prosessi on jo tarkasti kuvattu, mutta ei löydä mahdollisuuksia jotka
  syntyisivät prosessin *uudelleensuunnittelusta*.
- **Top-down** (tämä skilli): esitetään asiakkaalle 13 patternin diagnostiset
  kysymykset ilman että prosessia on vielä kuvattu tarkasti. Nopeampi
  ensimmäinen kartoitus, tuo esiin mahdollisuuksia joita asiakas ei itse
  olisi osannut nimetä ("emme olleet ajatelleet sitä noin"), mutta vaatii
  validoinnin (kohta 4) ennen kuin ehdokas viedään pisteytykseen.

Käytä tätä skilliä erityisesti discovery-työpajan/haastattelun **alussa**,
ennen kuin syvä prosessikuvaus on tehty — ja `task-level-decomposition-and-
automation-fit`-skilliä sen jälkeen kun jokin tietty prosessi on valittu
tarkempaan tarkasteluun.

## Ankkurointi tutkimukseen

- `../../references/ai-capability-pattern-library.md` — 13 patternia,
  abstrahoitu laajan toimialaraportin (2026) 81 tarkistetusta
  käyttötapauksesta ja ristiintarkistettu toisella, riippumattomalla
  AI-käyttötapauskoosteella (63 casea, 16 funktiota).
- `../../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`
  — yleinen Capability Pattern Mapping -abstraktiomenetelmä, jonka
  konkreettinen AI-sovellus patternikirjasto on.

## Rakenne (luonnos — täydennettävä)

1. **Ennen tapaamista: valitse 4–6 relevanteinta patternia** patternikirjastosta
   asiakkaan toimialan/tilanteen perusteella (ei kaikkia 13 kerralla — liikaa
   kysymyksiä yhdellä kertaa hukuttaa keskustelun). Käytä lähdemateriaalin
   toimialakohtaista funktiopainotusta karkeana ohjeena (esim. valmistava
   teollisuus → patternit 4, 5, 6, 11; asiantuntijapalvelu → patternit 2, 3, 9).
2. **Esitä jokaisen valitun patternin diagnostinen kysymys asiakkaalle
   sellaisenaan**, älä muunna sitä teknisemmäksi tai AI-sanastoa käyttäväksi.
   Kysymykset on tarkoituksella muotoiltu liiketoiminnan, ei teknologian,
   kielellä (esim. "missä korkeasti palkattu asiantuntija joutuu etsimään
   poikkeamia..." ei "voisiko LLM lukea dokumentteja...").
3. **Kirjaa jokainen "kyllä, meillä on tällainen tilanne" -vastaus
   rakenteisena ehdokkaana:** patternin nimi, asiakkaan oma kuvaus
   tilanteesta, kuka tekee työn tänään, arvioitu volyymi/toistuvuus (jos
   tiedossa). Älä vielä pisteytä tässä vaiheessa — se tehdään kohdassa 5.
4. **Validoi jokainen ehdokas ennen jatkokäsittelyä kolmella tarkistuksella:**
   - Onko tilanne aidosti toistuva/riittävän suurivolyyminen ollakseen
     mahdollisuus, vai kertaluontoinen poikkeustapaus?
   - Vastaako patternin oletettu AI-tyyppi (Agentic/Physical/muu) organisaation
     nykyistä kypsyystasoa, vai onko kuiluvaaraa (esim. Physical AI -patterni
     organisaatiossa jolla ei ole mitään sensoridataa)?
   - Onko olemassa ilmeinen syy miksi tämä TEI toimisi juuri tässä
     kontekstissa (sääntely, ay-sopimus, turvallisuuskriittisyys)? Jos on,
     merkitse se näkyviin äläkä piilota sitä.
5. **Vie validoidut ehdokkaat `../ai-opportunity-portfolio/SKILL.md`
   -skilliin** 5D-pisteytystä ja 2x2-priorisointia varten — tämä skilli
   tuottaa vain raakalistan, ei priorisoi.
6. **Jos asiakas ei tunnista mitään patternia omakseen**, se on itsessään
   tieto: joko organisaatio on jo pitkälle automatisoitu näillä alueilla,
   tai keskustelu ei ole tavoittanut oikeaa tasoa organisaatiossa (kokeile
   toista roolia/tiimiä) — älä pakota sovitusta.

## Mitä tämä skilli EI tee

- Ei korvaa `../task-level-decomposition-and-automation-fit/SKILL.md`-skilliä
  — tuottaa nopean, hypoteesivetoisen raakalistan, ei tarkkaa tehtävätason
  luokittelua. Molempia kannattaa käyttää samassa toimeksiannossa eri
  vaiheissa.
- Ei pisteytä tai priorisoi ehdokkaita — se on
  `../ai-opportunity-portfolio/SKILL.md`-skillin tehtävä.
- Ei väitä että jokainen 13 patternista sopii jokaiseen asiakkaaseen — osa
  patterneista on selvästi toimialasidonnaisempia (esim. Physical AI
  -patternit) kuin toiset.
- Ei laajenna patternikirjaston esimerkkejä yksityiskohdilla, joita
  `../../references/ai-capability-pattern-library.md`:ssä ei ole — jos
  tarvitset syvempää esimerkkiä, viittaa alkuperäisiin lähteisiin äläkä
  täydennä muistista.
- Ei ole tyhjentävä listaus kaikista mahdollisista AI-mahdollisuuksista —
  13 patternia on kuratoitu otos, ei kattava taksonomia. Uusia patterneja
  löytyy ajan myötä; lisää ne kirjastoon samalla menetelmällä (ks.
  `../../references/ai-capability-pattern-library.md`:n viimeinen osio).

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Patternikirjasto
on rakennettu tutkimuspohjaisesti (kahdesta riippumattomasta toimialan
AI-käyttötapausraportista), mutta omaa käytännön kokemusta siitä, mitkä
patternit toimivat parhaiten missäkin asiakastilanteessa, ei vielä ole
liitetty. Täydennä tähän:

- omia havaintoja siitä, mitkä patternit resonoivat useimmin minkäkin
  tyyppisten asiakkaiden kanssa
- uusia patterneja, jotka olet itse tunnistanut mutta joita ei ole
  lähteissä — lisää ne
  `../../references/ai-capability-pattern-library.md`-kirjastoon samalla
  formaatilla
- konkreettinen työpajapohja/kysymyslomake (`../../references/`-kansioon)

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä
`skills_index.json`:n `maturity`-kenttä arvoon `draft`, `validated` tai
`canonical` (ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei
lisätä uusia kenttiä** — `name` ja `description` ovat ainoat sallitut
(ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (yleinen menetelmä): `../../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`
- Rinnakkainen, bottom-up-lähestymistapa: `../task-level-decomposition-and-automation-fit/SKILL.md`
- Samassa pakissa seuraavaksi: `../ai-opportunity-portfolio/SKILL.md` —
  pisteyttää ja priorisoi tämän skillin tuottamat validoidut ehdokkaat.
- Jos koko prosessi tehdään maksullisena toimeksiantona:
  `../ai-discovery-engagement-design/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/ai-capability-pattern-library.md` — 13 patternin
  kirjasto esimerkkeineen
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
