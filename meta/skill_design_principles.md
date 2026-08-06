# Skill Design Principles

Jokaisen SKILL.md:n tulisi läpäistä nämä kuusi testiä:

1. **Riippumattomuustesti** — Toimisiko tämä sisältö vielä, jos vaihtaisimme Claude-mallin
   toiseen? Jos kyllä, se kuuluu tähän repoon rakenteena. Jos sisältö on omaa, validoitua
   kokemusta, se on vielä arvokkaampaa — sitä malli ei keksi itse.
2. **Konkreettisuustesti** — Onko skillissä käytettävä rakenne (vaiheet, kysymykset,
   taulukko), ei pelkkä otsikkolista tai buzzword-kuvaus.
3. **Ankkurointitesti** — Viittaako skilli tunnustettuun kehykseen (Liedtka, BABOK,
   Kirzner, McKinsey, SFIA) tai omaan validoituun kokemukseen — ei kumpaankaan.
4. **Rehellisyystesti kypsyystasosta** — Erottaako skilli selkeästi mikä on tutkimuspohjaista
   rakennetta ja mikä on vielä täyttämättä omalla kokemuksella (`[OWNER INPUT]`)?
5. **Rajaustesti** — Kertooko skilli myös mitä se EI tee? Skilli ilman rajausta houkuttaa
   käyttäjää luottamaan siihen laajemmin kuin pitäisi.
6. **Löydettävyystesti** — Onko skilli mukana `skills_index.json`:ssa oikealla
   metadatalla, jotta agentti löytää sen ilman koko repon lukemista?

## Frontmatterin minimalismi

SKILL.md-frontmatterissa on **vain** `name` ja `description`. Kaikki muu metadata
(kypsyys, lähdekerros, ankkurointi) elää `skills_index.json`:ssa tai itse tekstissä.
Tämä pitää skillit yhteensopivina kaikkien SKILL.md-formaattia tukevien agenttien kanssa
eikä sido niitä tämän repon omiin lisäkenttiin. (Periaate omaksuttu toisen
Claude-plugin-markkinapaikan rakenneanalyysistä — ks. CONTRIBUTING.md.)
