---
name: task-level-decomposition-and-automation-fit
description: "Pilkkoo roolit ja prosessit tehtävätasolle (People Path + Process Path) ja luokittelee jokaisen tehtävän Automate/Augment/Human-Only -kategoriaan SML-kriteereillä (syöte/tuotos-selkeys, kognitiivinen luonne, virhesietoisuus, aika-asteikko) ennen AI-mahdollisuuksien priorisointia."
---

# Task-Level Decomposition & Automation Fit

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Estää yleisin AI-mahdollisuuksien tunnistamisen virhe: arvioidaan koko
roolia tai prosessia kerralla ("voisiko tekoäly hoitaa asiakaspalvelun?")
sen sijaan että pilkotaan se yksittäisiin tehtäviin, joista jokainen
arvioidaan erikseen. Tekoäly ei yleensä korvaa kokonaisia ammattinimikkeitä
tai monimutkaisia prosesseja — se korvaa tai avustaa tiettyjä kognitiivisia
ja rutiininomaisia TEHTÄVIÄ prosessin sisällä. Tämä skilli on
`ai-opportunity-portfolio`-skillin syötepohja: se tuottaa priorisoitavan
raakalistan luokitelluista tehtävistä, joista portfolio sitten valitsee ja
pisteyttää parhaat.

## Ankkurointi tutkimukseen

- Käyttäjän toimittama tutkimusraportti "Tekoälymahdollisuuksien ja
  -kapasiteetin tunnistamismenetelmät, viitekehykset ja osaamiset
  liiketoiminnassa" (2026) — task-level-atomisointi, Dual Decomposition
  -malli, prosessi-/tehtäväanalyysin datalähtöiset tekniikat.
- Brynjolfsson, E. & Mitchell, T. (2017/2019) — *Suitable for Machine
  Learning* (SML) -indeksi. Alkuperäinen malli arvioi tehtäviä yhdeksällä
  kriteerillä; tämä raportti nimeää niistä eksplisiittisesti neljä (ks.
  Rakenne kohta 2) — **loput viisi eivät ole tämän raportin lähteessä
  eriteltyinä**, älä keksi niitä, käytä vain näitä neljää kunnes
  omistaja tai tarkempi lähde täydentää loput.
- Nuvepro (2026) — *The Dual Decomposition Framework: People Path +
  Process Path*.

## Rakenne (luonnos — täydennettävä)

1. **Valitse tarkastelun laajuus.** Yksi rooli/tiimi (People Path) tai
   yksi arvoketjun/prosessin vaihe (Process Path) — älä yritä molempia
   kerralla ensimmäisellä kierroksella. Jos Process Path -tarkastelu
   puuttuu vielä kokonaan, tee ensin karkea arvoketjukartoitus (ks.
   `../../../business-design-frameworks/skills/value-chain-mapping/SKILL.md`)
   ennen tätä syvempää tehtävätason pilkkomista.
2. **Pilkkoutuslinja People Path -tarkastelussa:** Organisaatio →
   Osasto → Rooli → Tehtävät. **Pilkkoutuslinja Process Path
   -tarkastelussa:** Arvoketju → Työnkulku → Tehtävät. Molemmat linjat
   kohtaavat tehtävätasolla — tämä on tarkoituksellista: sama tehtävä
   näkyy usein kummastakin näkökulmasta ja kannattaa ristiin tarkistaa.
3. **Kerää tehtävälista datalähtöisesti, ei pelkillä haastatteluilla.**
   Haastattelut aliarvioivat systemaattisesti rutiinityön määrän
   (ihmiset unohtavat/vähättelevät toistuvia pieniä tehtäviä). Käytä
   soveltuvin osin:
   - **Process Mining** (esim. Celonis, UiPath Process Mining) —
     järjestelmälokeista (ERP, CRM) uutetaan prosessin todelliset
     toteutumat: pitkät läpimenoajat, kääntöpaikat (*re-work loops*),
     manuaaliset tiedonsiirtovaiheet järjestelmien välillä.
   - **Task Mining** — käyttäjänäyttöjen/-toimintojen tason seuranta:
     kohdat joissa asiantuntija kopioi tietoa järjestelmästä toiseen tai
     hakee tietoa useasta dokumentista samanaikaisesti.
   - **Kognitiivisen kitkan analyysi** — missä kohdissa työntekijän
     mentaalinen kuormitus on suurin (esim. pitkän dokumentin
     analysointi vs. lopullinen päätös sen pohjalta) — näissä kohdissa
     Augment-tyyppinen tuki on usein arvokkaampaa kuin Automate.
   Jos mitään näistä työkaluista ei ole käytössä, tee sama analyysi
   kevyemmin: pyydä työntekijää pitämään yhden päivän ajan lokia
   jokaisesta järjestelmästä toiseen siirtymisestä ja jokaisesta
   kohdasta jossa hän kokee epävarmuutta tai kuormitusta.
4. **Luokittele jokainen tehtävä neljällä SML-kriteerillä (1–5 tai
   kyllä/ei):**
   - **Syötteen ja tuotoksen selkeys** — onko tehtävässä selkeästi
     määriteltävissä oleva digitaalinen syöte ja tuotos?
   - **Kognitiivinen luonne** — perustuuko tehtävä kuvioiden
     tunnistamiseen, kielen kääntämiseen, tiivistämiseen tai datan
     luokitteluun (AI:lle luontaista) vai fyysiseen läsnäoloon,
     neuvotteluun tai eettiseen harkintaan (ei)?
   - **Virhesietoisuus** — sietääkö prosessi ei-deterministisen,
     todennäköisyyspohjaisen tuloksen (esim. luonnos, ehdotus) vai
     vaatiiko se 100 %:n deterministisen tarkkuuden (esim.
     lääkeannostus, lakisääteinen raportointi)?
   - **Aika-asteikko ja vasteaika** — vaatiiko tehtävä sekunnin
     murto-osan reaktion (reaaliaikainen) vai syvällisen, pitkän
     aikavälin harkinnan?
5. **Luokittele jokainen tehtävä yhteen kolmesta kategoriasta:**
   - **Automate** — tekoäly/agentti suorittaa itsenäisesti ilman
     ihmisen väliintuloa. Tyypillisesti: rutiininomainen, korkea
     volyymi, deterministisesti tarkistettavissa.
   - **Augment** — tekoäly toimii ihmisen avustajana/rinnakkaisagenttina
     (human-in-the-loop). Tyypillisesti: kompleksinen päätöksenteko,
     luova luonnostelu, asiantuntijan taustoitus, kontekstinhaku.
   - **Human-Only** — säilyy täysin ihmisen vastuulla. Tyypillisesti:
     strateginen harkinta, korkean vastuun neuvottelu, fyysinen
     läsnäolo, eettinen päätöksenteko.
6. **Tuota jäsennelty tehtävälista** kolmella sarakkeella: tehtävä /
   SML-arvio lyhyesti / luokitus (Automate/Augment/Human-Only) +
   perustelu. Tämä on syöte `../ai-opportunity-portfolio/SKILL.md`
   -skilliin, jossa Automate- ja Augment-tehtävät ryhmitellään
   suuremmiksi mahdollisuuksiksi ja pisteytetään.
7. **Varo kahta systemaattista virhettä:** (a) älä luokittele koko
   roolia yhdellä kertaa "Automate"-kategoriaan vain siksi että osa sen
   tehtävistä on sitä — useimmat roolit ovat tehtäväsekoitus; (b) älä
   luokittele tehtävää Human-Only-kategoriaan vain koska se on
   monimutkainen — monimutkaisuus itsessään ei estä Augment-tason
   AI-tukea, se vain nostaa virhesietoisuusvaatimusta.

## Mitä tämä skilli EI tee

- Ei arvioi tehtävän/mahdollisuuden liiketoiminta-arvoa tai
  toteutettavuutta laajemmin — se on `../ai-opportunity-portfolio/SKILL.md`
  -skillin tehtävä. Tämä skilli vastaa vain kysymykseen "sopiiko tämä
  tehtävä ylipäätään AI:lle ja millä tasolla", ei "kannattaako tämä
  tehdä".
- Ei korvaa `../../../business-design-frameworks/skills/value-chain-mapping/SKILL.md`
  -skilliä toiminto-/prosessitason kartoituksessa — tämä skilli menee
  yhtä tasoa syvemmälle, yksittäisiin tehtäviin toimintojen sisällä.
- Ei tee teknistä toteutettavuusarviota (mallin valinta, arkkitehtuuri)
  — se on `../ai-use-case-feasibility-and-poc-scoping/SKILL.md`-skillin
  tehtävä myöhemmässä vaiheessa.
- Ei sisällä koko yhdeksänkriteeristä SML-mallia — vain neljä kriteeriä,
  jotka lähdemateriaali eritteli. Älä esitä muita viittä kriteeriä
  tunnettuina ilman tarkempaa lähdettä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä
sisällä omaa kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä
tähän:

- omia nyrkkisääntöjä siitä, mitkä tehtävätyypit yllättävät useimmin
  (luultu Human-Only mutta osoittautuu Augment-kelpoiseksi, tai
  päinvastoin)
- konkreettisia esimerkkejä process mining- / task mining -työkalujen
  käytöstä omissa toimeksiannoissa (`../../references/`-kansioon)
- SML-mallin loput viisi kriteeriä, jos löydät ne tarkemmasta
  alkuperäislähteestä (Brynjolfsson & Mitchell 2017/2019)

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä
`skills_index.json`:n `maturity`-kenttä arvoon `draft`, `validated` tai
`canonical` (ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei
lisätä uusia kenttiä** — `name` ja `description` ovat ainoat sallitut
(ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (jos arvoketjua ei ole vielä kartoitettu):
  `../../../business-design-frameworks/skills/value-chain-mapping/SKILL.md`
- Samassa pakissa seuraavaksi: `../ai-opportunity-portfolio/SKILL.md` —
  ryhmittelee ja pisteyttää tämän skillin tuottamat Automate/Augment-
  tehtävät mahdollisuuksiksi.
- Rinnakkainen, top-down-lähestymistapa (nopea ensimmäinen kartoitus ennen
  tarkkaa prosessikuvausta): `../ai-capability-pattern-matching/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
