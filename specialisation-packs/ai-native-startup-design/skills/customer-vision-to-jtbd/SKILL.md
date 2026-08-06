---
name: customer-vision-to-jtbd
description: "Jäsentää alustavan, vapaamuotoisen liiketoimintavision asiakasprofiiliksi (ICP), Jobs-To-Be-Done-analyysiksi ja 5+2 tarveteemaksi, pisteyttää ne 5-kriteerisellä NMB+AI-advantage-mallilla, ja valitsee AI-differentiaattoritarpeen (AI wedge) jatkokehitykseen."
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
- [redacted]n "AI-first SaaS Product" -työpajan menetelmä (omistajan
  itse soveltama [redacted]-caseen, ks. `../../references/[redacted]-workshop-
  source.md` ja `../../cases/[redacted]-decision-coach-mvp.md`) — syventää
  tämän skillin vaiheita 5–7: verbivetoinen JTBD-muotoilu, tarkempi
  5-kriteerinen NMB+AI-advantage-pisteytys (korvaa aiemman yksittäisen
  AI-advantage-pisteen), ja eksplisiittinen AI wedge -valintakriteeristö.
  **Huom:** tämä syventävä osa on toistaiseksi sovellettu vain kerran
  ([redacted]) — ei yhtä laajasti validoitu kuin skillin ICP/JTBD-runko, joka
  perustuu useamman osallistujan työpajaan.
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
4. **Jobs To Be Done (JTBD) — verbivetoisesti.** Syvenny asiakkaan
   todelliseen käyttäytymiseen ja tilanteeseen, jossa ongelma pitää
   ratkaista, ja siihen mitä hän todella yrittää saavuttaa — katso
   tuotteen ohi asiakkaan aitoon tavoitteeseen. Muotoile jokainen JTBD
   verbillä alkavaksi, ongelma-/ratkaisuriippumattomaksi *edistymiseksi*
   ("selvittää", "arvioida", "kääntää" — ei "saa dashboardin" tai "käyttää
   ominaisuutta X"). Tuota tyypillisesti 5-8 JTBD:tä. Testi: JTBD:n pitäisi
   pysyä totena vaikka koko tuote vaihtuisi täysin erilaiseksi ratkaisuksi.
5. **Tiivistä Need Themes -tarveteemoiksi (5+2).** Muunna JTBD-analyysi 5
   funktionaaliseksi ja 2 psykologiseksi teemaksi taulukkomuodossa. Jokainen
   teema on yhden tai kahden sanan substantiivilause, joka kiteyttää tarpeen
   ytimen (esim. *edullisuus*, *luotettavuus*, *itsevarmuus*). Käytä
   nelisarakkeista taulukkoa: Tarveteema / Tyyppi (Funktionaalinen: Understand,
   Diagnose/Evaluate, Plan/Structure, Communicate, Decide/Act — tai
   Psykologinen: Confidence, Uncertainty Reduction) / Taustalla oleva "miksi"
   / Liittyvä(t) JTBD(t). Ks. worked example
   `../../cases/[redacted]-decision-coach-mvp.md` kohta 2.
6. **NMB + AI-advantage-pisteytys — 5 kriteeriä, ei yksi.** Pisteytä
   jokainen tarveteema viidellä kriteerillä, kukin 1–5:
   - **Need Depth** — kuinka syvä/kipeä tarve on, kun se aktivoituu.
   - **Frequency** — kuinka usein asiakas kohtaa tämän tarpeen.
   - **Market Coverage** — kuinka laajasti tarve koskettaa kohdemarkkinaa.
   - **Business Strength** — kuinka vahva OMA lähtökohtasi on tämän
     tarpeen palvelemiseen (data, kokemus, olemassa olevat työkalut).
   - **AI Advantage** — kuinka paljon kilpailuetua AI tuo juuri tämän
     tarpeen palvelemiseen (aito erottautumistekijä, ei nice-to-have).
   Laske kokonaispistemäärä (max 25) ja luokittele jokainen tarveteema:
   **Differentiator** (korkea kokonaispiste, kilpailijat eivät kata hyvin)
   vs. **Table Stake** (tarpeellinen mutta geneerisiä kilpailijoita/muita
   AI-työkaluja saatavilla). Ks. worked example
   `../../cases/[redacted]-decision-coach-mvp.md` kohta 3.
7. **Valitse AI-differentiaattoritarve ("AI wedge").** AI wedge on
   tarveteema, joka täyttää SAMANAIKAISESTI: korkea Need Depth, korkea
   Frequency, heikko Market Coverage kilpailijoilla, korkea oma Business
   Strength, JA korkea AI Advantage. Tämä on se yksi (tai kaksi) tarve,
   jonka ympärille ratkaisuideointi (ks.
   `../ai-differentiator-solution-ideation/SKILL.md`) rakennetaan — älä
   yritä palvella kaikkia Differentiator-tason tarpeita kerralla.
8. **(Syventävä, valinnainen) Deep research.** Käytä AI-työkalun deep
   research -tilaa asiakkaan/ongelman, kilpailevien ratkaisujen ja
   markkina-/tutkimusdatan syventämiseen ennen ratkaisuideointia. Tulos
   on tutkimusluonnos raportteineen ja viitteineen — ei lopullinen totuus.
9. Vie tulos (ICP + JTBD + Need Themes + NMB-pisteytys + valittu AI wedge)
   `../ai-differentiator-solution-ideation/SKILL.md`-skilliin ratkaisu-
   suuntien ideoinnin pohjaksi — tai suoraan
   `../ai-buildable-prd-writing/SKILL.md`-skilliin, jos ratkaisusuunta on
   jo selvä eikä ideointivaihetta tarvita.

## Mitä tämä skilli EI tee

- Ei korvaa oikeaa asiakastutkimusta tai -haastatteluja — AI jäsentää
  ajattelua ja olemassa olevaa tietoa, se ei tuota uutta empiiristä
  asiakastietoa.
- Ei tee lopullista ICP- tai prioriteettivalintaa puolestasi.
- Deep research -tulokset ovat tutkimusluonnos — tarkista primäärilähteet
  ennen kuin viet ne PRD:hen tai päätöksentekoon.

## Jatka tästä

- Edeltävä skilli samassa pakissa: `../ai-native-opportunity-scan/SKILL.md`
- Seuraava skilli samassa pakissa:
  `../ai-differentiator-solution-ideation/SKILL.md` — 3 ratkaisusuunnan
  ideointi valitulle AI wedgelle. (Jos ratkaisusuunta on jo selvä,
  voit siirtyä suoraan `../ai-buildable-prd-writing/SKILL.md`-skilliin.)
- Liittyvä skilli toisessa pakissa:
  `../../../opportunity-recognition/skills/opportunity-value-assessment/SKILL.md`
- Worked example: `../../cases/[redacted]-decision-coach-mvp.md` — täysi [redacted]-case
  vaiheista 4–7.
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/prompt-library.md` — promptit 3–6
- `../../references/workshop-source.md` — lähdetiedot (AI-training-P6)
- `../../references/[redacted]-workshop-source.md` — lähdetiedot
  ([redacted], NMB-pisteytys ja AI wedge -syvennys)
- `../../cases/[redacted]-decision-coach-mvp.md` — worked example
- `../../CLAUDE.md` — pakin jaetut suojaukset
