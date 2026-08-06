# Business Design Frameworks

Kasvava kokoelma tapoja jäsentää ja mallintaa liiketoimintaa, arvonluontia,
arvoketjuja ja asemointia. Toisin kuin muut ydinpakit, tämä pakki on
tarkoituksella avoin — uusia jäsentämis- ja mallinnustapoja lisätään ajan myötä
sitä mukaa kun niitä tunnistetaan ja jalostetaan.

## Skillit tässä pakissa

| Skilli | Kuvaus |
|---|---|
| `layer-based-business-structuring` | Jäsentää liiketoiminnan kerroksiin (OSI-mallin kaltaisesti) infrastruktuurista brändiin — päättää mitkä kerrokset toteutetaan itse ja mitkä kumppanien kautta. |
| `value-chain-mapping` | Jäsentää liiketoiminnan Porterin arvoketjumallin mukaisesti ydin- ja tukitoimintoihin — näkee mistä arvo ja marginaali syntyvät. |
| `category-definition-and-modeling` | Mallintaa tuotteen tai liiketoiminnan suhteessa markkinakategorioihin: assosioituminen, laajentaminen vai kokonaan uuden kategorian luominen. |
| `strategy-canvas-and-value-curve` | Jäsentää kilpailijat/vaihtoehdot yhteisillä kilpailutekijöillä (Blue Ocean Strategy Canvas), tunnistaa toimialan "peruskäyrän" ja etsii tapoja erottautua siitä ERRC-ruudukolla. |
| `customer-journey-and-ai-touchpoint-mapping` | Kartoittaa asiakkaan palvelupolun ja kitkakohdat, ja sijoittaa AI:n polulle vain sinne missä se tuottaa aidosti arvoa. |

`layer-based-business-structuring`, `value-chain-mapping`,
`category-definition-and-modeling` ja
`customer-journey-and-ai-touchpoint-mapping` ovat `maturity: scaffold`;
`strategy-canvas-and-value-curve` on `maturity: validated`,
`source_layer: owner` (ankkuroitu omistajan 360 Comparison Factors
-työkaluun) — ks. `../skills_index.json` kypsyystilalle (frontmatterissa ei
seurata kypsyyttä, ks. `../meta/frontmatter_schema.md`).

## Skillien looginen kulku

```
layer-based-business-structuring ──┐
                                    ├──► category-definition-and-modeling
value-chain-mapping ────────────────┘              ▲
                                                     │
strategy-canvas-and-value-curve ────────────────────┘
   (erottautuminen syötteenä kategoriapäätökselle)

customer-journey-and-ai-touchpoint-mapping
   (täydentävä, asiakkaan ulkoa päin katsottu näkökulma —
    voidaan käyttää yhdessä minkä tahansa yllä olevan kanssa)
```

Kaikki kolme voidaan käyttää myös itsenäisesti (ks.
`../meta/skill_design_principles.md` — independence-testi) — ne ovat
vaihtoehtoisia, osin täydentäviä linssejä samaan liiketoimintaan.

## Ankkurointi

- OSI-malli (tietoliikenne) — kerrosperiaatteen esikuva
- Hagel & Singer (1999) — "Unbundling the Corporation" (HBR)
- Baldwin & Clark (2000) — *Design Rules: The Power of Modularity*
- Porter, M. (1985) — *Competitive Advantage*, arvoketjumalli
- Ramadan, Peterson, Lochhead & Maney (2016) — *Play Bigger*, category design
- Kim & Mauborgne (2005) — *Blue Ocean Strategy* (Strategy Canvas, Value
  Curve, Four Actions Framework/ERRC, Six Paths Framework)
- Ries & Trout — positiointiteoria
- Omistajan 360 Comparison Factors -vertailutyökalu (omistajan oma tuote)

## Rakenne

```
CLAUDE.md                    pakin jaetut suojaukset (lue aina ensin)
skills/<skill-id>/SKILL.md   yksittäinen skilli (name + description -frontmatter)
references/                  taustamateriaali, lähteet, omat mallit (täydennettävä)
```

## Näin lisäät uuden jäsentämistavan tähän pakkiin

1. Luo `skills/<uusi-skill-id>/SKILL.md` samalla rakenteella kuin nykyiset
   skillit (ks. `../templates/skill-template/SKILL.md`).
2. Ankkuroi se tunnettuun viitekehykseen tai omaan validoituun kokemukseen —
   merkitse `source_layer` ja `maturity` rehellisesti `skills_index.json`:iin
   (`python3 ../scripts/generate_index.py` generoi rungon, päivitä kypsyys
   käsin tarpeen mukaan).
3. Lisää rivi tämän README:n skillitaulukkoon ja ristiinlinkitä
   "Jatka tästä" -osiossa lähimpiin sukulaisskilleihin tässä ja muissa
   pakeissa.
4. Aja `python3 ../scripts/validate.py` ennen committia.

Katso `../meta/maturity_levels.md` kypsyystasojen selityksille ja
`../AGENT_GUIDE.md` sille, miten agentin tulee lukea ja painottaa tämän pakin sisältöä.
