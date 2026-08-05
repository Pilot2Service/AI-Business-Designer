# Lähdeaineiston muistiinpanot — Business Model Canvas -pakki

Tämä pakki on rakennettu kahdesta omistajan (Tommi Järvinen) toimittamasta
lähteestä, jotka täydentävät toisiaan:

## 1. [redacted]-pattern-kirjasto (koneluettava)

Käyttäjän lataamat tiedostot 5.8.2026:

- `business-model-patterns.json` — 159 patternia neljässä ryhmässä
  (Financial/Operating/Value/Experience Model), 13 ala-mallissa. Täysi
  kirjasto tässä pakissa: `bmc-innovation-pattern-library.md`.
- `Business-model-patterns-README.md` — [redacted]-alustan (AI-pohjainen
  liiketoiminnan prototyyppaus- ja simulaatiopalvelu) käyttöohje AI-
  agenteille: kontekstuaalinen relevanssi, JSON-polkujen tulostus,
  ristiriitaisten patternien välttäminen, eettinen vaatimustenmukaisuus,
  toteutettavuusarviointi, [redacted]-skeema (`pattern_id`, `pattern_name`,
  `sub_model`, `rationale`).
- `business_model_patterns_from_context.md` — tehtäväspesifikaatio
  ("TASK: Business Model Pattern Recommendation From Context"): kontekstista
  (ICP, ratkaisukategoria, markkinaominaisuudet, kustannusrakenne) 3–5
  koherentin patternin suositus, tulostusskeema
  `{recommendations, conflicts_avoided, assumptions}`.

Nämä kolme tiedostoa yhdessä muodostavat skillin
`bmc-innovation-pattern-matching` teknisen selkärangan.

## 2. Charlotte BMC Pilot -semanttikerros (asiantuntijasisältö)

Kansio `/Users/tommijarvinen/[redacted]/` — omistajan oma,
kesken oleva "semanttinen kerros" -projekti BMC-konsultointiasiantuntijuuden
kaappaamiseksi koneluettavaan muotoon (sama arkkitehtuuriperhe kuin
`charlotte-semantic-layer-template`, johon tämän koko skills-repon
alkuperäinen rakenne viittasi).

Repo jakaa sisällön kahteen selvästi merkittyyn kerrokseen (ks. jokaisen
tiedoston YAML-frontmatter):

- **Tutkimuskerros** (`status: template`, `source: research_layer`) —
  esitäytetty synteesi tunnetuista BMC-lähteistä (Jeffries, Williams,
  van der Linden, Blank/Strategyzer, Ash Maurya) sisältäen
  `[EXPERT INPUT]`-merkityt kohdat, joita omistaja ei ole vielä täyttänyt
  (asiantuntijasessiot merkitty "pending" `README.md`:ssä).
- **Asiantuntijakerros** (`status: accepted`, `authority: individual`,
  `confidence: high`, `source_refs: expert_interview 2026-04`) — aidosti
  täytetty, huhtikuussa 2026 tehdystä konsulttihaastattelusta poimittu
  omistajan oma metodologia. Nämä tiedostot:
  - `06_expertise_and_cognition/expert_profiles/bmc_expert_profile.md`
  - `06_expertise_and_cognition/cognitive_signatures/bmc_cognitive_signature.md`
  - `07_reasoning_model/reasoning_patterns/bmc_iteration_logic.md`
  - `12_quality_model/bmc_canvas_readiness.md`
  - `30_domain_packs/bmc/tools/bmc_innovation_patterns.md`
  - `30_domain_packs/bmc/antipatterns/bmc_antipatterns_expert.md`
  - `30_domain_packs/bmc/facilitation/bmc_client_misunderstandings.md`

Tämän skills-pakin skillien `maturity`/`source_layer` on määritetty
suoraan tämän jaon mukaan: asiantuntijakerroksesta rakennetut skillit ovat
`validated`/`owner`, tutkimuskerroksesta rakennetut ovat `scaffold`/`research`
— täsmälleen sama periaate jota koko tämä repo muutenkin noudattaa.

**Vielä täysin tyhjät tiedostot** (`status: draft`, `confidence: low`,
pelkkiä `[EXPERT INPUT]`-kysymyksiä, ei sisältöä): `intuition_signals.md`,
`red_flag_sensitivity.md`, `07_reasoning_model/heuristics/bmc_heuristics.md`,
`07_reasoning_model/situation_reading/diagnostic_question_patterns.md`,
`01_organisation_model/identity/organisation_identity.md`. Näitä EI ole
käytetty minkään skillin pohjana — ei ole vielä mitään konvertoitavaa.
Kun omistaja täyttää nämä myöhemmin (Session 1/2 SESSION_GUIDE.md:n
mukaan), tämän pakin skillejä kannattaa rikastaa uudelleen.

## 3. Miksi oma pakki eikä osa business-design-frameworks -pakkia

`business-design-frameworks`-pakki on tarkoituksella löyhä kokoelma
itsenäisiä, toisistaan riippumattomia jäsentämismalleja (kerrokset,
arvoketju, kategoria, strategiakartta, palvelupolku). BMC-konsultoinnin
asiantuntijuus on sen sijaan yksi yhtenäinen, sisäisesti riippuvainen
käytäntöalue — oma sanasto, diagnostiikka ja patternkirjasto — samaan
tapaan kuin `research-commercialisation` ja `ai-native-startup-design`.
Siksi tämä on oma erikoistumispakki, ei lisäys business-design-frameworksiin.
