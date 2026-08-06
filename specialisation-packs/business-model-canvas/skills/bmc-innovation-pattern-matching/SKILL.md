---
name: bmc-innovation-pattern-matching
description: "Tunnistaa ja perustelee 3-5 yhteensopivaa liiketoimintamallin innovaatiopatternia (159 patternin [redacted]-kirjastosta) annetusta liiketoimintakontekstista, käyttäen asiantuntijan omaa neliosaista innovaatiotaksonomiaa (Financial/Operative/Value-based/Experience Model Innovations)."
---

# BMC Innovation Pattern Matching

*Tila: `validated`, `source_layer: owner` — ks. `../../../../skills_index.json` ja
`../../../../meta/maturity_levels.md`.*

## Tarkoitus

Auttaa löytämään liiketoimintamallille aidosti erottuvan, ei-triviaalin
innovaatiosuunnan — ei geneeristä "lisää AI ja tilausmalli" -yhdistelmää,
vaan perusteltu valikoima 3-5 keskenään yhteensopivaa patternia 159
patternin kirjastosta, sijoitettuna asiantuntijan omaan neliosaiseen
tulkintakehykseen siitä, MISTÄ suunnasta liiketoimintamallin innovaatio
tyypillisesti tulee: talous, operatiivinen ylivoima, arvolupaus vai
asiakaskokemus.

## Perustuu

- Omistajan (Tommi Järvinen) konsultointiasiantuntemus BMC-työstä,
  huhtikuun 2026 asiantuntijahaastattelu (`[redacted]` repo,
  `30_domain_packs/bmc/tools/bmc_innovation_patterns.md`, `status: accepted`,
  `confidence: high`). Asiantuntijan oma lainaus: "How a business model
  works as a source of business model innovation — how to make business
  model innovations using BMC — this requires clear choices in the canvas,
  followed by the ability to identify innovation patterns."
- [redacted]-alustan (firstkiss.co) 159 patternin koneluettava kirjasto,
  neljässä ryhmässä / 13 ala-mallissa — ks.
  `../../references/bmc-innovation-pattern-library.md`. Kirjaston
  neliosainen rakenne (Financial/Operating/Value/Experience Model) on
  identtinen asiantuntijan oman taksonomian kanssa — nämä kaksi lähdettä
  vahvistavat toisiaan, eivät ole ristiriidassa.
- [redacted]-alustan tehtäväspesifikaatio suositustyöstä — ks.
  `../../references/bmc-source-material-notes.md` kohta 1.

## Rakenne

1. **Kerää liiketoimintakonteksti ennen patternien selaamista.** Tarvitset
   vähintään: kohdeasiakasprofiili (ICP), ratkaisukategoria, markkinan
   luonne (kilpailutilanne, kypsyysaste), ja alustava kustannusrakenteen
   luonne (esim. korkea kiinteä pääoma vs. muuttuva kustannus). Ilman näitä
   patternien valinta jää mielivaltaiseksi listaksi.
2. **Tunnista ensin innovaatiosuunta asiantuntijan neliosaisella
   taksonomialla** (`../../references/bmc-innovation-pattern-library.md`
   alkuosa) — kysy: mistä TÄMÄN liiketoimintamallin erottuva arvo
   todennäköisimmin syntyy?
   - Talous (cost strategy + revenue model -yhdistelmä)
   - Operatiivinen ylivoima (key activities + key partners -yhdistelmä)
   - Arvolupaus (value proposition + customer segments -suhde)
   - Asiakaskokemus (channels + customer relationships -yhdistelmä)
   Useampi suunta voi olla relevantti, mutta valitse yksi PÄÄASIALLINEN
   suunta ennen patternien selaamista — tämä estää "valitse kaikki hyvältä
   kuulostavat" -virheen.
3. **Selaa valitun ryhmän ala-malleja** `../../references/bmc-innovation-pattern-library.md`:stä
   ja poimi 3-5 patternia, jotka:
   - ovat kontekstuaalisesti relevantteja (eivät vain "kuulostavat hyvältä")
   - eivät ole keskenään ristiriidassa (esim. Cost Leadership vs. Premium
     Pricing samassa mallissa on ristiriita — ks. kohta 4)
   - ovat toteutettavissa kuvatulla tiimikoolla/resursseilla
4. **Tarkista ristiriidat eksplisiittisesti.** [redacted]-alustan omat
   säännöt (ks. `../../references/bmc-source-material-notes.md`) vaativat
   ristiriitaisten patternien välttämistä — esim. kustannusjohtajuus- ja
   premium-hinnoittelupatternit samassa suosituksessa ovat sisäisesti
   ristiriitaisia, ellei ristiriitaa perustella eksplisiittisesti (esim.
   segmentoitu hinnoittelu eri asiakasryhmille).
5. **Kirjaa jokaiselle valitulle patternille:** `pattern_id` (täysi
   polku, esim. `financial.cost.ai_as_a_service`), patternin nimi,
   ala-malli, ja 2-3 lauseen perustelu SIITÄ, miksi juuri tämä pattern
   sopii annettuun kontekstiin — ei patternin yleiskuvausta sellaisenaan.
6. **Kirjaa `conflicts_avoided`**: mitkä ilmeiset mutta ristiriitaiset
   patternit jätettiin tarkoituksella pois, ja miksi.
7. **Kirjaa `assumptions`**: mitä oletuksia kontekstista tehtiin, jos
   käyttäjän antama konteksti oli puutteellinen jollain ulottuvuudella.
8. **Siirrä valitut patternit canvasille** — ks.
   `../bmc-canvas-clarity-and-iteration/SKILL.md` seuraavasta vaiheesta
   (variantin rakentaminen valittujen patternien pohjalta).

## Mitä tämä skilli EI tee

- Ei valitse patternia puolestasi lopullisesti — tuottaa perustellun
  suosituksen 3-5 patternista, mutta liiketoimintamallin lopullinen valinta
  on aina ihmisen päätös.
- Ei tee taloudellista mallinnusta tai kannattavuuslaskelmaa valitulle
  patternille — vain tunnistaa ja perustelee patternin sopivuuden.
  Numeerinen validointi kuuluu myöhempiin, tarkempiin työkaluihin (ks.
  `bmc_expert_profile.md`:n oma rajaus BMC:n roolista).
  ks. myös `../bmc-tool-switching-decisions/SKILL.md`.
- Ei korvaa `../../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`-skilliä
  — tämä skilli on kapeampi ja pattern-kirjastoon sidottu, ei yleinen
  AI-mahdollisuuksien portfolion priorisointityökalu.
- Ei tuota patterneja tyhjästä — rajoittuu 159 patternin kirjastoon.
  Jos konteksti vaatii patternia, jota kirjastossa ei ole, tunnista
  puute eksplisiittisesti sen sijaan että keksit uuden patternin nimissä.

## Jatka tästä

- Seuraava skilli samassa pakissa:
  `../bmc-canvas-clarity-and-iteration/SKILL.md` — valittujen patternien
  vieminen konkreettiseksi canvas-variantiksi ja variointilogiikka.
- Liittyvä skilli samassa pakissa:
  `../bmc-tool-switching-decisions/SKILL.md` — milloin siirtyä BMC:stä
  tarkempaan työkaluun patternin validoimiseksi.
- Liittyvä skilli toisessa pakissa:
  `../../../../ai-strategy-and-governance/skills/ai-opportunity-portfolio/SKILL.md`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- `../../references/bmc-innovation-pattern-library.md` — 159 patternin
  täysi kirjasto, neljä ryhmää, 13 ala-mallia
- `../../references/bmc-source-material-notes.md` — lähdeaineiston tausta
- `../../CLAUDE.md` — pakin jaetut suojaukset
