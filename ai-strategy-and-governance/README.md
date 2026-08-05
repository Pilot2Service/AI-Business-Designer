# AI Strategy & Governance

AI-mahdollisuuksien tunnistaminen, priorisointi ja vastuullinen käyttöönotto liiketoiminnassa.

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `ai-opportunity-portfolio` | Tunnistaa ja priorisoi AI-käyttötapaukset liiketoiminta-arvon ja toteutettavuuden mukaan. |
| `ai-native-business-model-canvas` | Suunnittelee siirtymän AI-enhanced-liiketoiminnasta AI-native-liiketoimintamalliin laajennetulla Business Model Canvasilla. |
| `ai-use-case-feasibility-and-poc-scoping` | Määrittää AI-käyttötapauksen tekniset reunaehdot ja PoC-vaiheen rajauksen. |
| `responsible-ai-and-governance-check` | Tarkistaa AI-aloitteen sääntely-, riski- ja eettisyysnäkökulmat. Syvempään EU AI Act -compliance-analyysiin käytä tämän workspacen tekoalysaantely-plugineja (tekoaly-luokittelu, tekoaly-velvoitteet, tekoaly-vaatimustenmukaisuus). |
| `build-vs-buy-vs-partner-ai` | Jäsentää päätöksen rakentaa itse, ostaa alustalta vai kumppanoitua AI-ratkaisussa. |
| `ai-capability-roadmap` | Rakentaa organisaation AI-kyvykkyyskartan ja roadmapin nykytilasta tavoitetilaan. |
| `shadow-ai-response-and-safe-adoption` | Tunnistaa luvattoman AI-työkalujen käytön (Shadow AI) ja korvaa sen turvallisella, ROI-perustellulla virallisella ratkaisulla. |
| `ai-output-curation-and-quality-control` | Suunnittelee laadunvalvonta- ja kuratointiprosessin AI:n tuotoksille — siirtymä tekijästä kuraattoriksi. |

Kaikki `maturity: scaffold` — ks. `../skills_index.json` kypsyystilalle (frontmatterissa
ei seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Ankkurointi

- EU AI Act (asetus (EU) 2024/1689)
- LinkedIn 2026 — Risk & Compliance Management
- LinkedIn Skills on the Rise 2026 — AI Business Strategy
- Perplexity-tutkimus — PoC-määrittely tuotannollistamiseen asti
- Perplexity-tutkimus — roadmapit ja liiketoimintakyvykkyyskartat
- Perplexity-tutkimus: Senior AI Business Designer (Solita/HP)
- strategic-options-evaluation -logiikka sovellettuna AI-päätöksiin
- Käyttäjän toimittama tutkimusraportti "AI Business Designer tekoälyn
  aikakaudella" (2026) — AI-soveltuvuuden triagi, data flywheel, AI-native
  Business Model Canvas, Shadow AI, AI-tuotosten kuratointi ja
  laadunvalvonta
- Yleinen "Shadow IT" -kirjallisuus ja -käytäntö, laajennettuna
  AI-työkalujen kontekstiin

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
