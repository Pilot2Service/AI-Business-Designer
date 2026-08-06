# Lähde: [redacted] — AI-first SaaS Product Workshop

Tämä on toinen lähde tässä pakissa `AI-training-P6`-työpajan
(`workshop-source.md`) rinnalla. Se syventää erityisesti pakin
keskivaihetta — tarveteemojen pisteytystä, ratkaisusuuntien ideointia,
MVP:n valintaa ja tekoälynatiivin tuotteen käyttöliittymäarkkitehtuuria —
askelilla, joita alkuperäinen `day1.md`-työpaja ei käsitellyt yhtä
tarkasti.

## Mikä tämä on

- **Nimi:** "Ai-first SaaS Product workshop"
- **Järjestäjä:** [redacted]
- **Muoto:** omistajan (Tommi Järvinen) muistiinpanot työpajan
  menetelmästä + omistajan itse AI-ajattelukumppanin kanssa läpikäymä
  **täysi sovellusesimerkki omaan [redacted]-tuotteeseensa**
  (ks. alla "Miksi tämä on arvokas kaksoislähde").
- **Ladattu:** 6.8.2026 (`[redacted] – Ai-first SaaS Product workshop.md`)

## Menetelmän 8 askelta

1. **Jobs To Be Done (JTBD)** — verbi-vetoiset, "progress not features"
   -muotoiset työt, ICP:n kautta rajattuna.
2. **5+2 tarveteemaa (Need Themes)** — JTBD:t tiivistettynä 5
   funktionaaliseksi + 2 psykologiseksi tarpeeksi, yhden/kahden sanan
   substantiivilauseina (esim. *relevanssi*, *luottamus*).
3. **NMB + AI-advantage-pisteytys** — jokainen tarveteema pisteytetään
   5 kriteerillä (1–5): Need Depth, Frequency, Market Coverage, Business
   Strength, AI Advantage → kokonaispistemäärä (max 25) →
   Differentiator vs. Table Stakes -luokittelu.
4. **AI-differentiaattoritarpeen valinta ("AI wedge")** — tarveteema
   jolla on samanaikaisesti korkea syvyys, korkea toistuvuus, heikko
   kilpailijakattavuus, oma vahvuus JA korkea AI-etu.
5. **3 ratkaisusuunnan ideointi** valitulle differentiaattoritarpeelle —
   kolmella eri linssillä (kilpailija-, tulevaisuus-, "yhdistä pisteet"
   -linssi), jotta ei rakasta ensimmäistä ideaa.
6. **RICE-pisteytys** kolmesta ratkaisusuunnasta — Reach, Impact,
   Confidence, Effort (käänteinen) → MVP-valinta.
7. **MVP-synteesi** — MVP-määritelmä (2–3 lausetta), yhden lauseen
   positiointilause, 3 "miksi voitamme" -väittämää.
8. **AI-first-tuoteperiaatteet ("5 shifts")** ja **keskusteleva
   käyttöliittymäarkkitehtuuri** (Intent → Strategy Cards →
   Clarification → Output Cards → Mission → Agent Execution).

## Miksi tämä on arvokas kaksoislähde

Toisin kuin `AI-training-P6`, joka on geneerinen menetelmä ilman yhtä
tiettyä sovelluscasea, tämä muistiinpano sisältää omistajan OMAN,
täyden sovelluksen: [redacted]-tuotteen JTBD:stä RICE-valittuun
MVP:hen ("Decision Coach") ja sen keskustelu-OS-arkkitehtuuriin asti.
Tämä worked example on tallennettu erikseen:
`../cases/[redacted]-decision-coach-mvp.md` — käytä sitä konkreettisena
mallina kun sovellat tämän pakin skillejä uuteen caseen.

## Miksi `maturity: draft` uusille skilleille (ei `validated`)

`AI-training-P6`-työpaja on **pidetty useille osallistujille**
(1.–2.6.2026, ryhmäsessio) — siksi sen pohjalta rakennetut skillit ovat
`validated`. Tämä [redacted]-menetelmä on toistaiseksi **sovellettu
kerran, yhteen caseen** ([redacted]) omistajan itsensä toimesta — ei vielä
testattu useammalla eri liiketoiminnalla tai ulkopuolisella tiimillä.
Tämä vastaa täsmälleen `maturity_levels.md`:n `draft`-määritelmää:
"[OWNER INPUT] täytetty, käytetty kerran käytännössä, ei vielä
validoitu laajemmin." Kun menetelmää on sovellettu useampaan eri
caseen, nosta `skills_index.json`:ssa asianomaisten skillien
`maturity` arvoon `validated`.

## Ajantasaisuus

Menetelmä (JTBD→Need Themes→NMB-pisteytys→AI wedge→ratkaisuideointi→
RICE→MVP-synteesi→OS-arkkitehtuuri) on pysyvää sisältöä, ei sidottu
mihinkään tiettyyn työkaluun tai tuotenimeen — samalla periaatteella
kuin `AI-training-P6`:n menetelmäskillit (ks. `workshop-source.md`
"Ajantasaisuus").
