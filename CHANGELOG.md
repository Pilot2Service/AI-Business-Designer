# Changelog

## 0.13.0 — 2026-08-06

AI use case -patteristo: käyttäjän pyynnöstä koottu skills packiin oma
osio AI-käyttötapausten systemaattiseen tunnistamiseen. Lähtökohtana
käyttäjän kuvaama **Capability Pattern Mapping** -abstraktiomenetelmä
(pintapuolisesti erilaiset casejoukot → yksi nimetty, toimialariippumaton
patterni → diagnostinen kysymys uudessa kontekstissa) sekä kaksi
käyttäjän toimittamaa/osoittamaa primäärilähdettä: [redacted], "The AI
Dossier" (2026-painos, PDF, 130 käyttötapausta 6 toimialalla,
Trustworthy AI™ -riskikehys) ja McKinsey, "Generative AI Use Case
Catalog" (63 käyttötapausta, 16 funktiota). [redacted]-raportista
tekstipohjaisesti poimittu ja tarkistettu 81 casea (5/6 toimialaa) —
jokainen tämän version esimerkkiviittaus on suoraan tästä poiminnasta,
ei muistista tuotettu.

**Rikastettu** `opportunity-recognition/pattern-and-analogy-connector`
(pysyy `scaffold`): täytetty yleinen, toimialariippumaton Capability
Pattern Mapping -menetelmä 7-vaiheisena rakenteena (kerää 3+ erilaista
havaintoa → nelikysymysabstraktio syöte/toimija/kognitiivinen ydin/
lopputulos → yhden lauseen patternimääritelmä → diagnostinen kysymys →
kattavuus-/terävyystestaus → käyttö uudessa kontekstissa → validointi),
havainnollistettu käyttäjän omalla lasku-/tulli-/CV-dokumentti-
esimerkillä.

**1 uusi referenssitiedosto**, `ai-strategy-and-governance/references/ai-capability-pattern-library.md`:
13 nimettyä AI-kyvykkyyspatternia (mm. Moniagenttinen reaaliaikainen
kompromissioptimointi, Rakenteettoman dokumentin validointi ja
poikkeaman tunnistus, Pysyvä henkilökohtainen neuvoja/konsierki-agentti,
Ennakoiva laitehälytys ja autonominen interventio, Näköohjattu fyysinen
käsittely ja laadunvalvonta, Autonominen liikkuva fyysinen operointi,
AI-avusteinen ohjelmistokehitys, ym.) — kukin: määritelmä, diagnostinen
signaalikysymys, AI-tyyppi (Agentic/Physical/muu), 3-6 oikeaa
esimerkkicasea [redacted]n poiminnasta ja [redacted]n Trustworthy AI
-riskilinssi. Sisältää läpinäkyvän lähdeselvityksen ja
McKinsey-ristiintarkistuksen (4 funktiota joissa ~75% arvosta:
asiakasoperaatiot, markkinointi & myynti, ohjelmistokehitys, T&K —
kaikki 4 katettu patterneissa).

**1 uusi skilli**, `ai-strategy-and-governance/ai-capability-pattern-matching`,
`maturity: scaffold`, `source_layer: research`: opettaa patternikirjaston
käytön top-down-vaihtoehtona `task-level-decomposition-and-automation-fit`
-skillin bottom-up-lähestymiselle raakalistan kokoamisessa ennen
`ai-opportunity-portfolio`-pisteytystä. Ristiinlinkitetty molempiin
pakkeihin (`ai-opportunity-portfolio`, `task-level-decomposition-and-
automation-fit`, `pattern-and-analogy-connector`).

## 0.12.0 — 2026-08-06

Analysoitu käyttäjän toimittama tutkimusraportti "Tekoälymahdollisuuksien
ja -kapasiteetin tunnistamismenetelmät, viitekehykset ja osaamiset
liiketoiminnassa" (2026, synteesi mm. [redacted]/[redacted]/McKinsey
[redacted]/BCG/Brynjolfsson & Mitchell -lähteistä). Käytetty
`ai-strategy-and-governance`-pakin rikastamiseen ja laajentamiseen.

**2 uutta skilliä**, `maturity: scaffold`, `source_layer: research`:

- `task-level-decomposition-and-automation-fit` — pilkkoo roolit/
  prosessit tehtävätasolle (People Path + Process Path -Dual
  Decomposition) ja luokittelee jokaisen tehtävän Automate/Augment/
  Human-Only SML-kriteereillä (Brynjolfsson & Mitchell); sisältää myös
  process mining-, task mining- ja kognitiivisen kitkan analyysin
  datalähtöisenä vaihtoehtona haastatteluille
- `ai-discovery-engagement-design` — tuotteistaa koko tunnistamis-
  prosessin maksulliseksi/sisäiseksi discovery-toimeksiannoksi:
  4-vaiheinen rakenne, kaksi palvelutuotetta (AI Opportunity Sprint,
  AI Maturity & Opportunity Audit), standardoitu luovutettava aineisto

**Täysin uudelleenkirjoitettu** `ai-opportunity-portfolio` (pysyy
`scaffold`): aiempi kevyt kolmi-kriteerinen triagi korvattu formaalilla
5-ulotteisella pisteytysmallilla (Business Impact, Technical
Feasibility & AI Fit, Data Readiness, Strategic Alignment, Speed to
Value & Governance/Risk), 2x2-priorisointimatriisilla (Quick Wins/
Strategic Bets/Hard-Low Value/Deprioritize), Value-Play-taksonomialla
transformatiivisille mahdollisuuksille (Zero-Marginal-Cost Expertise,
Hyper-Personalization at Scale, Outcome-Based/Agentic Business) ja
BCG:n Deploy-Reshape-Invent-luokittelulla — eksplisiittisesti erotettuna
`ai-capability-roadmap`-skillin Horisontti-jaosta sekaannuksen
välttämiseksi.

**Rikastettu** `ai-capability-roadmap`: kolmihorisonttinen rakenne
(0-6kk tehostus / 6-18kk muutos / 18-36kk uusi liiketoiminta) ja
AI Target Operating Model (ATOM) / Readiness Scorecard -konsepti
(ihmisen ja tekoälyn työnjaon + organisaation valmiustason kuvaus).

**Kevyesti rikastettu** `ai-native-business-model-canvas`: uusi
eksplisiittinen "Human-AI Interaction Model" -kohta (Copilot/
Autonomous Agent/Generative Interface), ristiinlinkitetty
`closed-loop-process-and-human-oversight-design`- ja
`ai-native-conversational-os-design`-skilleihin (specialisation-packs/
ai-native-startup-design) täsmentäen että vuorovaikutusmuoto ja
valvontataso ovat kaksi eri kysymystä.

Lisäksi: pakin `CLAUDE.md`:hen lisätty selkeä erottelu neljästä
samankaltaisesta kolmi-/nelijaottelusta (Automate/Augment/Human-Only,
Quick Wins/Strategic Bets/Hard-Low Value/Deprioritize, Deploy/Reshape/
Invent, Horisontti 1/2/3) sekaantumisen estämiseksi. Pack-README
päivitetty skillien loogisella kulkukaaviolla. Pakki kasvoi 8 → 10
skilliin. Yhteensä nyt 66 skilliä.

## 0.11.0 — 2026-08-06

Analysoitu omistajan (Tommi Järvinen) uploadaama [redacted]n "AI-first
SaaS Product workshop" -muistiinpano ja käytetty sitä
`specialisation-packs/ai-native-startup-design/`-pakin rikastamiseen ja
laajentamiseen. Muistiinpano sisältää sekä yleisen menetelmän että
omistajan itsensä läpikäymän täyden sovellusesimerkin
[redacted]-tuotteeseen ("Decision Coach" MVP).

**Rikastettu** `customer-vision-to-jtbd` (`validated`/`owner` säilyy):
verbivetoinen JTBD-muotoilu, Need Themes -taulukko laajennettu
("Tyyppi"/"miksi"/"liittyvä JTBD" -sarakkeilla), aiempi yksittäinen
AI-advantage-piste korvattu 5-kriteerisellä NMB-pisteytyksellä (Need
Depth, Frequency, Market Coverage, Business Strength, AI Advantage →
Differentiator vs. Table Stake), uusi vaihe: AI-differentiaattoritarpeen
("AI wedge") eksplisiittinen valintakriteeristö.

**3 uutta skilliä**, `maturity: draft` (sovellettu toistaiseksi kerran,
[redacted]-caseen — ei vielä yhtä laajasti validoitu kuin pakin muut skillit),
`source_layer: owner`:

- `ai-differentiator-solution-ideation` — 3 keskenään erilaisen AI-
  natiivin ratkaisusuunnan ideointi valitulle AI wedgelle kolmella
  linssillä (kilpailija-, tulevaisuus-, yhdistä-pisteet-linssi)
- `rice-scoring-and-mvp-synthesis` — RICE-pisteytys (Reach, Impact,
  Confidence, Effort) MVP:n valitsemiseksi + MVP-määritelmä +
  positiointilause + "miksi voitamme" -väittämät
- `ai-native-conversational-os-design` — keskustelevan käyttöliittymä-
  arkkitehtuurin suunnittelu (Intent → Strategy Cards → Clarification →
  Output Cards → Mission → Agent Execution) + 5 AI-first-tuoteperiaatetta
  ("5 shifts": klikkaus>kysymys, valikot>promptit, dashboardit>dialogi,
  manuaaliset toiminnot>agentit, ruudut>chat+kortit)

Lisäksi: `references/[redacted]-workshop-source.md` (uusi lähde,
selittää miksi `draft` eikä `validated`), `cases/[redacted]-decision-coach-mvp.md`
(täysi worked example — ensimmäinen tiedosto pakin `cases/`-kansiossa),
`references/prompt-library.md` laajennettu (promptit 6 päivitetty +
uudet promptit 8–10), pakin `README.md`/`CLAUDE.md` päivitetty
kaksitasoisen kypsyyden näkyväksi tekemiseksi, ristiinlinkitys
`ai-native-opportunity-scan`- ja `ai-buildable-prd-writing`-skilleihin.
Pakki kasvoi 5 → 8 skilliin. Yhteensä nyt 64 skilliä.

## 0.10.0 — 2026-08-05

Uusi erikoistumispakki `specialisation-packs/business-model-canvas/` (7 skilliä),
rakennettu kahdesta omistajan (Tommi Järvinen) toimittamasta lähteestä:

- [redacted]-alustan (firstkiss.co) 159 patternin koneluettava innovaatio-
  kirjasto (`business-model-patterns.json`, ladattu 5.8.2026) — konvertoitu
  täydeksi markdown-referenssiksi `references/bmc-innovation-pattern-library.md`
- `[redacted]`-repo, omistajan oma kesken oleva "semanttinen kerros"
  -projekti BMC-konsultointiasiantuntijuuden kaappaamiseksi. Repo jakautuu
  asiantuntijakerrokseen (huhtikuun 2026 konsulttihaastattelu, `status:
  accepted`) ja tutkimuskerrokseen (Jeffries/Williams/van der
  Linden/Blank/Ash Maurya -synteesi, `status: template`)

3 skilliä `maturity: validated`, `source_layer: owner` (asiantuntijakerroksesta):

- `bmc-innovation-pattern-matching` — 3-5 yhteensopivan innovaatiopatternin
  tunnistus 159 patternin kirjastosta asiantuntijan neliosaisella taksonomialla
  (Financial/Operative/Value-based/Experience Model Innovations)
- `bmc-canvas-clarity-and-iteration` — variointilogiikka, jumissa-olon
  tunnistus, "selkeys > syvyys" -valmiuskriteeri
- `bmc-antipattern-and-misunderstanding-correction` — 5 työtavan
  antipatternia + 4 asiakkaan väärinkäsitystä BMC:n roolista

4 skilliä `maturity: scaffold`, `source_layer: research` (tutkimuskerroksesta):

- `bmc-session-facilitation-design` — session rakenne, aloituskohta,
  täyttöjärjestys, evidenssin värikoodaus
- `bmc-canvas-diagnostic-reading` — 6 diagnostista sääntöä (Hook Rule ym.)
  + nelidimensioinen laaturubriikki
- `bmc-tool-switching-decisions` — milloin siirtyä VPC:hen, Lean Canvasiin,
  Mission Model Canvasiin tai taloudelliseen mallinnukseen
- `bmc-client-language-translation` — asiakaslauseiden tulkinta + 3
  käsiteväärinkäsitystä

Lisäksi: `references/bmc-source-material-notes.md` (lähdeaineiston
kaksikerroksinen tausta), pakkikohtainen `CLAUDE.md` (mixed-maturity-
disclosure) ja `README.md`, `marketplace.json`-merkintä
`specialisation-business-model-canvas`. Yhteensä nyt 61 skilliä.

## 0.9.0 — 2026-08-05

Kattavuusaudit "AI Business Designer tekoälyn aikakaudella" -tutkimusraporttia
vasten (sama raportti kuin 0.5.0:ssa, nyt käyty läpi kokonaan grep+sisältö-
tarkistuksella koko repoa vasten). 4 aitoa aukkoa tunnistettu ja täytetty
(`maturity: scaffold`, `source_layer: research`):

- `business-design-frameworks/customer-journey-and-ai-touchpoint-mapping`
  — palvelupolkujen kartoitus ja AI:n sijoittelu kitkakohtiin arvoa
  tuovalla tavalla
- `strategic-thinking/second-and-third-order-effects-mapping` — päätöksen
  toisen/kolmannen kertaluvun vaikutusten ennakointi (asiakaskäyttäytyminen,
  kilpailijareaktiot)
- `ai-strategy-and-governance/shadow-ai-response-and-safe-adoption` —
  luvattoman AI-työkalujen käytön kartoitus ja turvallinen virallistaminen
- `ai-strategy-and-governance/ai-output-curation-and-quality-control` —
  AI-tuotosten laadunvalvonta, siirtymä tekijästä kuraattoriksi
- Muu osa raportista vahvistettiin jo katetuksi: AI-mahdollisuuksien
  tunnistus, AI-native Business Model Canvas, business case -rakennus,
  vastuullinen AI, hypoteesivetoinen ajattelu, skenaariosuunnittelu,
  fasilitointi, agenttinen tekoäly (ks. `ai-native-startup-design`-pakki)
- Yhteensä nyt 54 skilliä

## 0.8.0 — 2026-08-05

Toinen täysin täytetty erikoistumispakki — `specialisation-packs/ai-native-
startup-design/`, konvertoitu omistajan (Tommi Järvinen) fasilitoimasta
**AI-native Business Design** -työpajasta pre-startup-perustajille
([redacted]/firstkiss.co, pidetty 1.–2.6.2026, julkinen lähde
github.com/Pilot2Service/AI-training-P6):

- 5 uutta skilliä (`maturity: validated`, `source_layer: owner`):
  `ai-native-opportunity-scan` (agenttinen/closed-loop-mahdollisuuksien
  löytö ja priorisointi), `customer-vision-to-jtbd` (ICP/JTBD/Need
  Themes/AI-advantage-pisteytys), `ai-buildable-prd-writing`
  (rakennusagentille annettava PRD + tukidokumentit), `closed-loop-
  process-and-human-oversight-design` (open/closed loop -mentaalimalli +
  human-in/on/outside-the-loop), `ai-native-tool-stack-selection`
  (12 työkalukategorian valintaheuristiikka)
- `references/workshop-source.md`, `prompt-library.md` (työpajan
  promptit suomennettuina), `tool-category-map.md` (aikaleimattu
  työkalukategoriakartta, kesäkuu 2026)
- Ristiinlinkitys `ai-strategy-and-governance`-pakin
  `ai-opportunity-portfolio`- ja `responsible-ai-and-governance-check`
  -skilleihin, `business-design-frameworks`-pakin
  `value-chain-mapping`-skilliin, ja `opportunity-recognition`- sekä
  `business-case-and-analysis`-pakkien vastaaviin skilleihin
- Pakkikohtainen `CLAUDE.md` ja täysi `README.md` (placeholder poistettu)
- `marketplace.json`: `specialisation-ai-native-startup-design`-kuvaus
  päivitetty, scaffold-merkintä poistettu
- Yhteensä nyt 50 skilliä, 6 ydinpakkia + 2 täytettyä erikoistumispakkia

## 0.7.0 — 2026-08-05

Uusi skilli `business-design-frameworks/skills/strategy-canvas-and-value-curve`
— Blue Ocean Strategy -mallia mukaileva jäsentämistapa kilpailijoiden/
vaihtoehtoisten ratkaisujen vertailuun:

- Ankkuroitu Kim & Mauborgne (2005) *Blue Ocean Strategy* -teoriaan
  (Strategy Canvas, Value Curve, Four Actions Framework/ERRC-ruudukko,
  Six Paths Framework) sekä omistajan (Tommi Järvinen) tuotteistettuun
  **[redacted] 360 Comparison Factors** -vertailutyökaluun (käyttäjän lataama
  taulukko: 10 esimerkkitekijää, 0–2-asteikko, oma ratkaisu + 4
  kilpailijaa)
- `maturity: validated`, `source_layer: owner` — pakin ensimmäinen
  ei-scaffold-skilli
- Uusi `references/[redacted]-360-comparison-template.md` — mallipohja ja
  käyttöohje, sisältää alkuperäisen esimerkkitäytön
- Ristiinlinkitys pakin muihin skilleihin ja
  `opportunity-recognition/skills/competitive-and-five-forces-mapping`
  sekä `opportunity-value-assessment`
- README ja CLAUDE.md päivitetty kuvaamaan pakin sekoitettua kypsyystasoa
- Yhteensä nyt 45 skilliä

## 0.6.0 — 2026-08-05

Uusi ydinpakki `business-design-frameworks/` — tarkoituksella avoin ja kasvava
kokoelma liiketoiminnan jäsentämis- ja mallinnustapoja (kerrokset, arvoketjut,
kategoriamallinnus, ja lisää myöhemmin käyttäjän toimesta):

- `layer-based-business-structuring` — OSI-mallin analoginen kerrosjäsennys,
  ankkuroitu Hagel & Singer (1999) "Unbundling the Corporation" ja
  Baldwin & Clark modulaarisuusteoriaan
- `value-chain-mapping` — Porterin (1985) arvoketjumalli
- `category-definition-and-modeling` — category design (Play Bigger,
  Ramadan et al. 2016) ja Blue Ocean Strategy (Kim & Mauborgne 2005)
- Kaikki `maturity: scaffold`, `source_layer: research` — ei vielä omaa
  validoitua kokemusta, tarkoituksella rakennettu täydennettäväksi
- Pakki on suunniteltu kasvamaan: README sisältää ohjeen uuden
  jäsentämistavan lisäämiseksi
- Yhteensä nyt 44 skilliä, 6 ydinpakkia + 1 täytetty erikoistumispakki

## 0.5.0 — 2026-08-04

Käyttäjän toimittaman tutkimusraportin ("AI Business Designer tekoälyn
aikakaudella") pohjalta lisätty `ai-strategy-and-governance`-pakkiin:

- `ai-opportunity-portfolio` rikastettu konkreettisella AI-soveltuvuuden
  triagilla (ennustus/luokittelu/generointi + datan saatavuus), data
  flywheel -tarkistuksella ja automaatio-vs-agenttisuus-erottelulla
  (edelleen `maturity: scaffold`, `source_layer: research`)
- Uusi skilli `ai-native-business-model-canvas` (`maturity: scaffold`) —
  laajennettu, tekoälyspesifi Business Model Canvas (arvolupaus,
  avainresurssit, kustannusrakenne, ekosysteemi)
- Muu osa raportista (business case -rakennus, taitomatriisi) arvioitiin
  toistavan jo olemassa olevaa sisältöä (`ai-opportunity-portfolio`,
  `build-vs-buy-vs-partner-ai`, `ai-capability-roadmap`,
  `responsible-ai-and-governance-check`, `meta/competency_map.md`) — ei lisätty
  uudelleen
- Yhteensä nyt 41 skilliä

## 0.4.0 — 2026-08-04

Laajennus ydinpakkiin `opportunity-recognition/` omistajan (Tommi Järvinen)
[redacted]-palvelun Opportunity Value Assessment -tuotteesta (sales page,
input wizard, raporttipohja) ja sitä tukevasta S1-taustatutkimuksesta
(Mullins Seven Domains, Timmons, POEM, NABC, Opportunity Canvas):

- 3 uutta skilliä (`maturity: validated`, `source_layer: owner`):
  `opportunity-intake-elicitation`, `opportunity-value-assessment`,
  `opportunity-brief-writing` — pakin ensimmäiset ei-scaffold-skillit,
  rinnakkain 5 alkuperäisen scaffold-skillin kanssa
- `references/[redacted]-frameworks-review.md`, `intake-questions.md`,
  `opportunity-brief-template.md`
- Ristiinlinkitys: `opportunity-evaluation-and-judgment` (scaffold) →
  `opportunity-value-assessment` (validated); `research-opportunity-recognition`
  (research-commercialisation) ↔ `opportunity-value-assessment`
- `CLAUDE.md` ja `README.md` päivitetty kuvaamaan sekoitettua kypsyystasoa
  saman pakin sisällä
- Yhteensä nyt 40 skilliä

## 0.3.0 — 2026-08-04

Ensimmäinen täysin täytetty erikoistumispakki — `specialisation-packs/research-commercialisation/`,
konvertoitu omistajan (Tommi Järvinen) julkaisemasta *[redacted] Innovator's Guide to
Commercialisation* -käsikirjasta ja AFCA-itsearviointityökalusta:

- 12 uutta skilliä (`maturity: validated`, `source_layer: owner`) — ensimmäiset
  tässä repossa, jotka eivät ole `scaffold`-tasolla
- `references/afca-framework.md`, `case-studies.md`, `terminology.md`, `sources.md`
- Pakkikohtainen `CLAUDE.md` ja täysi `README.md` (placeholder poistettu)
- `scripts/generate_index.py` ja `scripts/validate.py` laajennettu indeksoimaan ja
  validoimaan myös `specialisation-packs/*/skills/`-sisältöä (ei vain top-level
  plugin.json-pakkeja)
- `marketplace.json`: `specialisation-research-commercialisation`-kuvaus päivitetty,
  scaffold-merkintä poistettu
- Yhteensä nyt 37 skilliä, 5 ydinpakkia + 1 täytetty erikoistumispakki

## 0.2.0 — 2026-08-04

Rakennekorjaus `[redacted]/claude-for-legal-finland`-repon (tuotantokäytössä oleva
suomalainen Claude-plugin-markkinapaikka) rakenneanalyysin pohjalta:

- SKILL.md-frontmatter siivottu minimiin (`name` + `description`) — kypsyys/lähdekerros
  siirretty yksinomaan `skills_index.json`:iin
- Pakkikansioista poistettu numeroprefiksit (`01-strategic-thinking` → `strategic-thinking`)
- Lisätty pakkitason `CLAUDE.md`-suojauskerros jokaiseen 5 ydinpakkiin
- Lisätty jokaiseen skilliin `Mitä tämä skilli EI tee` ja `Jatka tästä` -osiot
- Lisätty `scripts/generate_index.py` ja `scripts/validate.py`
- `marketplace.json`: lisätty `$schema` ja `displayName`-kentät

## 0.1.0 — 2026-08-04

- Ensimmäinen scaffold: 5 ydinpakkia, 25 skilliä (kaikki `maturity: scaffold`)
- 3 erikoistumispakin placeholder
- `skills_index.json` koneluettava indeksi
- `AGENT_GUIDE.md`, meta-hallintodokumentit Charlotte-semantic-layer-templaten
  arkkitehtuuriperiaatteita soveltaen
- 2 aloitusplaybookia
