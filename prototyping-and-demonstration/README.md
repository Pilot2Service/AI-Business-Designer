# Prototyping & Demonstration

Miten AI-konsultti rakentaa nopeasti toimivan konseptin, kehystää sen
asiakkaalle oikein, esittää sen vakuuttavasti ja sitoo tuloksen business
caseen ja ROI-laskelmaan. Vastaa kysymykseen "miten mahdollisuus tehdään
konkreettiseksi ja uskottavaksi" — täydentää `opportunity-recognition`-
ja `ai-strategy-and-governance`-pakkien "mikä mahdollisuus tämä on"
-kysymystä ja `business-case-and-analysis`-pakin "kannattaako tämä
taloudellisesti" -kysymystä.

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `opportunity-visioning-with-pr-faq` | Kommunikoi ja näyttää AI-mahdollisuuden Amazonin Working Backwards / PR-FAQ-menetelmällä ennen kuin mitään on rakennettu. |
| `rapid-prototype-and-vibe-coding-craft` | Rakentaa nopeasti toimivan, riittävän uskottavan prototyypin AI-avusteisella koodauksella ("vibe coding") — oikea fideliteettitaso, tiukka iteraatiosykli, tunnetut riskit. |
| `demo-framing-and-expectation-setting` | Kehystää demon/PoC:n oikealla termillä (PoC vs. Pilotti vs. MVP) ja "todistaa/ei todista" -parilla ennen esittämistä — estää ylitulkinnan ja "pilot purgatoryn". |
| `demo-delivery-and-storytelling` | Rakentaa ja pitää demon Great Demo! -metodologialla (Situation Slide, kriittinen liiketoimintaongelma, "tee viimeinen asia ensin"). |
| `demo-to-business-case-bridge` | Kääntää demon/PoC:n tulokset business case -kelpoisiksi ROI-syötteiksi — tekninen suorituskyky vs. liiketoimintavaikutus, oletusketjun näkyväksi tekeminen, ROI-mekanismin yhteensopivuus asiakkaan organisaatioon. |

Kaikki `maturity: scaffold` — ks. `../skills_index.json` kypsyystilalle (frontmatterissa
ei seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Skillien looginen kulku

```
opportunity-visioning-with-pr-faq   (valinnainen: visio sanoiksi ennen koodia)
              │
              ▼
rapid-prototype-and-vibe-coding-craft   (rakenna kapea, hypoteesin todistava proto)
              │
              ▼
demo-framing-and-expectation-setting    (nimeä PoC/Pilotti/MVP, "todistaa/ei todista")
              │
              ▼
demo-delivery-and-storytelling          (Great Demo! -esitys)
              │
              ▼
demo-to-business-case-bridge            (oletusketju näkyväksi → ROI-syötteet)
              │
              ▼
   business-case-and-analysis/business-case-builder, roi-npv-sensitivity-model
```

`opportunity-visioning-with-pr-faq` on valinnainen ensimmäinen askel — käytä
sitä kun visio ei vielä ole selkeä tai kun protoilu ei vielä ole
kannattavaa. `demo-framing-and-expectation-setting` kannattaa aina tehdä
ENNEN demoa, ei jälkikäteen.

## Suhde muihin pakkeihin

- **`ai-strategy-and-governance/ai-use-case-feasibility-and-poc-scoping`** —
  määrittää PoC:n TEKNISET reunaehdot ennen protoilua. Tämän pakin
  `demo-framing-and-expectation-setting` kehystää saman rajauksen
  ASIAKASVIESTINTÄÄN — eri kysymys, käytä molempia yhdessä.
- **`change-and-communication/executive-narrative-and-storyline`** —
  kääntää analyysin johdon tarinaksi yleisemmin. Tämän pakin
  `demo-delivery-and-storytelling` ja `opportunity-visioning-with-pr-faq`
  ovat sen erikoistuneempia sovelluksia demo-/visiointitilanteeseen.
- **`business-case-and-analysis/business-case-builder` ja
  `roi-npv-sensitivity-model`** — vastaanottavat tämän pakin
  `demo-to-business-case-bridge`-skillin tuottamat validoidut syötteet.
- **`opportunity-recognition/pattern-and-analogy-connector` ja
  `ai-strategy-and-governance/ai-capability-pattern-matching`** —
  tuottavat raakalistan mahdollisuuksista, joita tämä pakki tekee
  konkreettisiksi ja uskottaviksi.

## Ankkurointi

- Cohan, Peter E. — *Great Demo! How To Create And Execute Stunning
  Software Demonstrations* ja Paul Pearcen "Great Demo! Five Imperatives"
  -sovellus (Discovery, Demo Prep, Demo Delivery, Documentation, Debrief;
  Situation Slide, Critical Business Issue, "tee viimeinen asia ensin")
- Bryar, Colin & Carr, Bill — *Working Backwards: Insights, Stories, and
  Secrets from Inside Amazon* (2021) — Working Backwards -menetelmä ja
  PR-FAQ-dokumentti
- Vibe coding -parhaat käytännöt 2026 (usean lähteen synteesi) —
  työkaluvalinta, iteraatiosykli, PRD-ensin-periaate, tunnetut riskit
- Prototyyppifideliteetti-tutkimus (UX-tutkimusperinne) — matalan vs.
  korkean fideliteetin prototyyppien käyttötilanteet
- PoC vs. Pilotti vs. MVP -erottelu (usean 2026-lähteen synteesi)
- "Pilot purgatory" -tutkimus (McKinsey/BCG/IDC/MIT-synteesejä) —
  miksi suuri osa yrityssektorin AI-piloteista ei etene tuotantoon
- Tutkimussynteesi (2026) demon/PoC:n ROI-kääntämisestä liiketoiminta-
  kieleksi

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
