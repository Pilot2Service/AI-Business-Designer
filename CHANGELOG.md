# Changelog

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
