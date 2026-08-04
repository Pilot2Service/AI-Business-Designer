# Contributing — AI Business Designer Skills

## Suunnitteluperiaate

SKILL.md koodaa oikean toiminnan; pakin CLAUDE.md on varaverkko. Jos skillin oikea
lopputulos riippuu siitä, että CLAUDE.md pelastaa virheen, se on suunnitteluvirhe — vie
tieto SKILL.md:hen. (Periaate: `[redacted]/claude-for-legal-finland`.)

## Uuden skillin lisääminen

1. Kopioi `templates/skill-template/SKILL.md` oikeaan pakkiin
   (`<pack>/skills/<uusi-skilli-id>/SKILL.md`).
2. Frontmatterissa **vain** `name` ja `description` — ei muita kenttiä. `name` on
   kebab-case ja sama kuin kansion nimi. `description` kertoo mitä skilli tekee ja
   milloin se triggeröityy.
3. Kirjoita `Tarkoitus`, `Ankkurointi tutkimukseen` ja `Rakenne` -osiot ensin — nämä
   voivat pohjautua julkiseen tutkimukseen/kehykseen.
4. Kirjoita `Mitä tämä skilli EI tee` -osio — vähintään yksi skillikohtainen rajaus
   yleisten lisäksi.
5. Lisää `Jatka tästä` -linkit: mihin skilliin tästä luontevasti siirrytään (saman pakin
   sisällä ja tarvittaessa toiseen pakkiin).
6. Jätä `[OWNER INPUT — täydennettävä]`-osio auki kunnes sinulla on oikeasti oma,
   validoitu sisältö sille. Älä täytä sitä geneerisellä tekstillä.
7. **Aja `python3 scripts/generate_index.py`** — päivittää `skills_index.json` levyltä ja
   frontmattereista. Älä muokkaa `skills_index.json`:ia käsin.
8. **Aja `python3 scripts/validate.py` ennen commitia.** Sen pitää olla vihreä.

## Uuden erikoistumispakin lisääminen

Käytä `templates/specialisation-pack-template/README.md`-pohjaa ja lisää se
`specialisation-packs/`-kansioon. Noudata samaa `skills/` + `references/` + `cases/`
-rakennetta kuin ydinpakeissa. Lisää tarvittaessa oma `CLAUDE.md`.

## Kypsyystason nostaminen

Kun `[OWNER INPUT]`-osio on täytetty ja käytetty vähintään kerran oikeassa tilanteessa:
päivitä `skills_index.json`:n `maturity: scaffold` → `draft` (aja generate_index.py
uudelleen dokumentoinnin jälkeen, tai päivitä käsin ja validoi). Kun sisältö on
validoitu useammassa tilanteessa: → `validated`. `canonical` on varattu vakiintuneille,
organisaation viralliseksi standardiksi nostetuille skilleille.

## Nimeämiskonventiot

- Skilli-id: `kebab-case`, verbitön substantiivimuoto (esim. `business-case-builder`)
- Pakin kansio: pelkkä domain-nimi, **ei numeroprefiksiä** (`strategic-thinking`, ei
  `01-strategic-thinking`) — plugin-lähteet viitataan nimellä `marketplace.json`:ssa,
  ei järjestyksellä.
- Ei erikoismerkkejä, ei isoja kirjaimia kansio-/tiedostonimissä
