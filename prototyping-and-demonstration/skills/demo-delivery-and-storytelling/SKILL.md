---
name: demo-delivery-and-storytelling
description: "Rakentaa ja pitää demon Great Demo! -metodologian (Situation Slide, kriittinen liiketoimintaongelma/CBI, \"tee viimeinen asia ensin\"/käänteinen pyramidi) mukaisesti: Discovery → Demo Prep → Demo Delivery → Documentation → Debrief. Käytä kun protoitu ratkaisu pitää esittää asiakkaalle tai johdolle niin, että se todella vakuuttaa eikä vain esittele ominaisuuksia."
---

# Demo Delivery & Storytelling

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Muuttaa toimiva prototyyppi vakuuttavaksi demoksi. Toimiva proto ja hyvä demo
eivät ole sama asia — moni teknisesti pätevä prototyyppi epäonnistuu
demossa, koska se esitellään ominaisuuslistana ("katsotaan mitä kaikkea
tämä osaa") sen sijaan että se todistaisi asiakkaan omaa kriittistä
liiketoimintaongelmaa konkreettisesti. Tämä skilli soveltaa Peter Cohanin
Great Demo! -metodologiaa (myyntitekniikan sales engineering -kirjallisuuden
vakiintunut viitekehys) AI-konsultin demo-tilanteeseen.

## Ankkurointi tutkimukseen

- Cohan, Peter E. — *Great Demo! How To Create And Execute Stunning
  Software Demonstrations* (kolmoispainos) ja Paul Pearcen "Great Demo!
  Five Imperatives" -sovellus: Discovery, Demo Prep, Demo Delivery,
  Documentation, Debrief. Ydinkäsitteet: **Situation Slide** (ytimekäs
  yhteenveto asiakkaan tilanteesta ennen demoa), **kriittinen
  liiketoimintaongelma / Critical Business Issue (CBI)**, ja **"tee
  viimeinen asia ensin" / käänteinen pyramidi** (näytä ensin se, mikä
  tuottaa "wow"-vaikutuksen — älä rakenna demoa kronologisesti tuote-
  esittelynä).

Tausta-aineisto: `../../../../skills-tutkimus-analyysi.md` ja
`../../../../markkinan-taito-odotukset-analyysi.md` (AI-business-designer-projektin juuressa).

## Rakenne (luonnos — täydennettävä)

Sovellettu Great Demo! Five Imperatives -rakenne:

1. **Discovery — ennen kuin rakennat mitään demoa varten.** Selvitä
   asiakkaan **kriittinen liiketoimintaongelma (CBI)**: mikä konkreettinen
   kipu heillä on tänään, kuka sen omistaa, milloin se pitää ratkaista,
   ja kuinka paljon arvoa ratkaisu tuottaisi. Jos et pysty täyttämään
   näitä, et ole valmis rakentamaan demoa vielä — palaa
   `../../../opportunity-recognition/skills/pattern-and-analogy-connector/SKILL.md`
   tai `../../../ai-strategy-and-governance/skills/ai-capability-pattern-matching/SKILL.md`
   -skilliin tarkentamaan tilannetta.
2. **Demo Prep — kirjoita Situation Slide ennen demoa.** Yksi dia/kappale,
   joka tiivistää: asiakkaan tilanne, CBI, tarvittavat kyvykkyydet, haluttu
   arvo, aikataulu. Kokoa myös: demon runko ja agenda, mahdolliset
   sivupolut jos asiakas kysyy jotain odottamatonta, asiakkaan OMAA dataa
   muistuttava demodata (geneerinen esimerkkidata on selvästi heikompi),
   ja referenssitarinat samankaltaisista tilanteista.
3. **Demo Delivery — sovella "tee viimeinen asia ensin" -periaatetta.**
   Älä aloita yleiskatsauksesta tai teknisestä arkkitehtuurista — aloita
   siitä yhdestä asiasta, joka konkreettisesti ratkaisee CBI:n ja tuottaa
   "wow"-reaktion. Käänteinen pyramidi: tärkein ensin, tausta ja
   yksityiskohdat vasta jos kiinnostusta riittää. Kysy kysymyksiä demon
   aikana sen sijaan että pidät yksinpuhelua — tämä paljastaa reaaliajassa
   miten yleisö kokee arvon ja mitä he vielä tarvitsevat päättääkseen.
4. **Kytke demo aina takaisin kehykseen** joka on jo asetettu
   `../demo-framing-and-expectation-setting/SKILL.md`-skillillä: muistuta
   mitä tämä demo todistaa ja mitä ei, äläkä anna demon draaman viedä
   kehystä mukanaan (innostunut yleisö helposti ylitulkitsee).
5. **Documentation — jaa Situation Slide ja demo-kooste heti demon
   jälkeen.** Tutkimus (ks. Referenssit) osoittaa, että suurin osa demon
   sisällöstä unohtuu viikossa — kirjallinen kooste on se, mitä yleisö
   oikeasti vie mukanaan ja jakaa organisaationsa sisällä. Kirjaa CBI,
   demossa todistettu asia, ja sovitut seuraavat askeleet.
6. **Debrief — käy läpi mikä toimi ja mikä ei heti demon jälkeen**, kun
   se on vielä tuoreessa muistissa: mitkä kysymykset yllättivät, mikä osa
   demosta tuotti eniten reaktiota, mitä pitäisi tehdä toisin seuraavalla
   kerralla. Tämä on erityisen tärkeää AI-konsultille, joka pitää useita
   samantyyppisiä demoja peräkkäin eri asiakkaille — opit kumuloituvat
   nopeasti jos debrief tehdään systemaattisesti.
7. **Erityishuomio vibe coodatuille protoille:** älä koskaan improvisoi
   live-demossa polkuja, joita ei ole testattu etukäteen — AI-avusteisesti
   rakennetun prototyypin virhetilanteet voivat olla arvaamattomia. Pidä
   demo tiukasti niillä 2-3 testatulla polulla, jotka Demo Prep -vaiheessa
   varmistettiin toimiviksi (ks. `../rapid-prototype-and-vibe-coding-craft/SKILL.md`
   kohta 4).

## Mitä tämä skilli EI tee

- Ei rakenna itse prototyyppiä — ks. `../rapid-prototype-and-vibe-coding-craft/SKILL.md`.
- Ei aseta demon kehystä (PoC/Pilotti/MVP-termiä, todistaa/ei todista
  -paria) — se tehdään ennen tätä skilliä `../demo-framing-and-expectation-setting/SKILL.md`-skillissä.
- Ei korvaa myyntiprosessia kokonaisuudessaan — keskittyy yhteen demo-
  tapahtumaan Great Demo! -metodologian mukaisesti, ei koko myyntisykliin.
- Ei takaa, että hyvä demo johtaa kauppaan tai etenemiseen — hyvä demo
  poistaa esteitä, mutta päätös on aina asiakkaan.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- omia Situation Slide -mallipohjia (`../../references/`-kansioon)
- konkreettisia esimerkkejä demoista jotka toimivat erityisen hyvin —
  ja mikä niissä toimi
- nyrkkisääntöjä siitä, miten reagoida kun demo menee pieleen livenä
  (esim. AI antaa väärän vastauksen kesken demon)

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (protoilu): `../rapid-prototype-and-vibe-coding-craft/SKILL.md`
- Ennen tätä (kehystys): `../demo-framing-and-expectation-setting/SKILL.md`
- Johdon yleisölle syvempi tarina: `../../../change-and-communication/skills/executive-narrative-and-storyline/SKILL.md`
- Jos demo onnistuu: `../demo-to-business-case-bridge/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- Cohan, Peter E. — *Great Demo! How To Create And Execute Stunning
  Software Demonstrations*
- Pearce, Paul H. — "Great Demo! Five Imperatives" -sovellus (Discovery,
  Demo Prep, Demo Delivery, Documentation, Debrief)
- Tutkimus demon sisällön unohtumisesta ilman kirjallista dokumentaatiota
  (sales engineering -kirjallisuus)
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
