# Lähdeaineiston muistiinpanot — Business Model Canvas -pakki

Tämä pakki on rakennettu kahdesta toisiaan täydentävästä lähteestä:

## 1. Innovaatiopattern-kirjasto (koneluettava)

- Julkinen liiketoimintamallin innovaatiopatternien kirjasto: 159 patternia
  neljässä ryhmässä (Financial/Operating/Value/Experience Model), 13
  ala-mallissa. Täysi kirjasto tässä pakissa: `bmc-innovation-pattern-library.md`.
- Käyttöohje AI-agenteille patternien soveltamiseen: kontekstuaalinen
  relevanssi, JSON-polkujen tulostus, ristiriitaisten patternien
  välttäminen, eettinen vaatimustenmukaisuus, toteutettavuusarviointi,
  tulostusskeema (`pattern_id`, `pattern_name`, `sub_model`, `rationale`).
- Tehtäväspesifikaatio kontekstipohjaiseen pattern-suositukseen: kontekstista
  (ICP, ratkaisukategoria, markkinaominaisuudet, kustannusrakenne) 3–5
  koherentin patternin suositus, tulostusskeema
  `{recommendations, conflicts_avoided, assumptions}`.

Nämä yhdessä muodostavat skillin `bmc-innovation-pattern-matching` teknisen
selkärangan.

## 2. Omistajan yksityinen asiantuntemuskerros

Omistajan oma, ei-julkinen tutkimustyö BMC-konsultointiasiantuntijuuden
kaappaamiseksi rakenteiseen, koneluettavaan muotoon. Sisältö on jaettu
kahteen selvästi merkittyyn kerrokseen:

- **Tutkimuskerros** — esitäytetty synteesi tunnetuista BMC-lähteistä
  (Jeffries, Williams, van der Linden, Blank/Strategyzer, Ash Maurya)
  sisältäen avoimia kohtia, joita omistaja ei ole vielä täyttänyt
  (asiantuntijasessiot merkitty odottaviksi).
- **Asiantuntijakerros** — aidosti täytetty, huhtikuussa 2026 tehdystä
  konsulttihaastattelusta poimittu omistajan oma metodologia: asiantuntija-
  profiili, kognitiiviset tunnusmerkit, iteraatiologiikka, canvas-valmiuden
  laatumalli, innovaatiopatternien soveltamisohjeet, antipatternit ja
  tyypilliset asiakasväärinkäsitykset.

Tämän skills-pakin skillien `maturity`/`source_layer` on määritetty
suoraan tämän jaon mukaan: asiantuntijakerroksesta rakennetut skillit ovat
`validated`/`owner`, tutkimuskerroksesta rakennetut ovat `scaffold`/`research`
— täsmälleen sama periaate jota koko tämä repo muutenkin noudattaa.

Osa asiantuntijakerroksen aihealueista (intuitiosignaalit, punaisen lipun
herkkyys, heuristiikat, tilanteenlukupatternit, organisaatioidentiteetti) on
vielä täysin tyhjiä eikä niitä ole käytetty minkään skillin pohjana. Kun
omistaja täyttää nämä myöhemmin, tämän pakin skillejä kannattaa rikastaa
uudelleen.

## 3. Miksi oma pakki eikä osa business-design-frameworks -pakkia

`business-design-frameworks`-pakki on tarkoituksella löyhä kokoelma
itsenäisiä, toisistaan riippumattomia jäsentämismalleja (kerrokset,
arvoketju, kategoria, strategiakartta, palvelupolku). BMC-konsultoinnin
asiantuntijuus on sen sijaan yksi yhtenäinen, sisäisesti riippuvainen
käytäntöalue — oma sanasto, diagnostiikka ja patternkirjasto — samaan
tapaan kuin `research-commercialisation` ja `ai-native-startup-design`.
Siksi tämä on oma erikoistumispakki, ei lisäys business-design-frameworksiin.
