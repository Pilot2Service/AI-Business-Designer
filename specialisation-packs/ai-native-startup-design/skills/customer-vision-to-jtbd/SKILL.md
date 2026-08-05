---
name: customer-vision-to-jtbd
description: "Jäsentää alustavan, vapaamuotoisen liiketoimintavision asiakasprofiiliksi (ICP), Jobs-To-Be-Done-analyysiksi ja tarveteemoiksi, ja pisteyttää missä AI tuo suurimman edun — strukturoitu promptiketju AI-ajattelukumppanin kanssa."
---

# Customer Vision to JTBD

*Tila: `validated`, `source_layer: owner` — ks. `../../../skills_index.json` ja
`../../../meta/maturity_levels.md`.*

## Tarkoitus

Muuttaa vapaamuotoinen, jopa jäsentymätön visio tuotteesta ja asiakkaasta
strukturoiduksi asiakasymmärrykseksi ennen PRD:n kirjoittamista: kuka
asiakas on (ICP), mitä hän todella yrittää saada aikaan (JTBD), mitkä
tarpeet tämän alla ovat (Need Themes), ja missä niistä AI tuo suurimman
kilpailuedun. Periaate on aloittaa asiakkaasta, ei teknologiasta — spec ei
koskaan lähde teknisestä kuvauksesta.

## Perustuu

- Omistajan (Tommi Järvinen) AI-native Business Design -työpaja
  ([redacted] / firstkiss.co), pidetty 1.–2.6.2026, Day 1 —
  Session 2 "Planning in the AI Era", vaiheet 1–3 (visio → suunnittelu-
  kumppani → ICP/JTBD/Need Themes/AI-advantage-pisteytys).
- Ideal Customer Profile (ICP) ja Jobs-To-Be-Done (JTBD) -tuotestrategia-
  kehykset (yleisesti tunnettuja, ei omistajan omia — työpaja soveltaa
  niitä AI-ajattelukumppanin kanssa käytävään promptiketjuun).
- Ks. `../../references/workshop-source.md` ja
  `../../references/prompt-library.md` (promptit 3–6).

## Rakenne

1. **Kirjoita vapaamuotoinen visio.** Avaa tyhjä dokumentti ja kirjoita
   vapaasti: mikä on asiakkaan tarve, miten palvelu toimii asiakkaan
   näkökulmasta, kuinka merkittävä ongelma on, miten asiakas käyttää
   palvelua, mitkä ovat omat arvot/periaatteet/fokus. Ei tarvitse olla
   looginen tai järjestyksessä — irralliset ajatukset ja kesken jääneet
   lauseet ovat hyväksyttäviä. Tavoite on saada oma ajattelu ulos siihen
   muotoon, jota AI voi käsitellä.
2. **Vie visio AI-ajattelukumppanille terävöitettäväksi**
   (`../../references/prompt-library.md` promptti 3): pyydä sitä
   kertomaan mikä on vielä epäselvää ja vaatii päätöksen, esittämään
   enintään 7 tarkentavaa kysymystä tärkeysjärjestyksessä, ja nostamaan
   esiin oletukset jotka kannattaa tarkistaa. Älä vielä pyydä suunnitelmaa
   — tässä vaiheessa tavoite on ajattelun terävöittäminen.
3. **Ideal Customer Profile (ICP).** Pyydä AI:ta hahmottamaan useampi
   asiakasprofiili, jolla on tämä ongelma voimakkaimmin, kuvaamaan kukin,
   ja priorisoimaan ketä palvellaan ensin ja miksi.
4. **Jobs To Be Done (JTBD).** Syvenny asiakkaan todelliseen
   käyttäytymiseen ja tilanteeseen, jossa ongelma pitää ratkaista, ja
   siihen mitä hän todella yrittää saavuttaa — katso tuotteen ohi
   asiakkaan aitoon tavoitteeseen.
5. **Tiivistä Need Themes -tarveteemoiksi.** Muunna JTBD-analyysi 5
   funktionaaliseksi ja 2 psykologiseksi teemaksi taulukkomuodossa. Jokainen
   teema on yhden tai kahden sanan substantiivilause, joka kiteyttää tarpeen
   ytimen (esim. *edullisuus*, *luotettavuus*, *itsevarmuus*).
6. **AI-advantage-pisteytys.** Pisteytä jokainen tarveteema 1–5 sen
   mukaan, kuinka paljon kilpailuetua AI tuo juuri sen tarpeen
   palvelemiseen — tunnista missä AI on aito erottautumistekijä eikä vain
   nice-to-have-lisä. Selitä korkeimmat pisteet.
7. **(Syventävä, valinnainen) Deep research.** Käytä AI-työkalun deep
   research -tilaa asiakkaan/ongelman, kilpailevien ratkaisujen ja
   markkina-/tutkimusdatan syventämiseen ennen PRD:n kirjoittamista. Tulos
   on tutkimusluonnos raportteineen ja viitteineen — ei lopullinen totuus.
8. Vie tulos (ICP + JTBD + Need Themes + AI-advantage-pisteytys)
   `../ai-buildable-prd-writing/SKILL.md`-skilliin ongelma&asiakas-osion
   pohjaksi.

## Mitä tämä skilli EI tee

- Ei korvaa oikeaa asiakastutkimusta tai -haastatteluja — AI jäsentää
  ajattelua ja olemassa olevaa tietoa, se ei tuota uutta empiiristä
  asiakastietoa.
- Ei tee lopullista ICP- tai prioriteettivalintaa puolestasi.
- Deep research -tulokset ovat tutkimusluonnos — tarkista primäärilähteet
  ennen kuin viet ne PRD:hen tai päätöksentekoon.

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../ai-native-opportunity-scan/SKILL.md`
- Seuraava skilli samassa pakissa: `../ai-buildable-prd-writing/SKILL.md`
- Liittyvä skilli toisessa pakissa:
  `../../../opportunity-recognition/skills/opportunity-value-assessment/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/prompt-library.md` — promptit 3–6
- `../../references/workshop-source.md` — lähdetiedot
- `../../CLAUDE.md` — pakin jaetut suojaukset
