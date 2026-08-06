---
name: opportunity-visioning-with-pr-faq
description: "Kommunikoi ja näyttää AI-mahdollisuuden Amazonin Working Backwards -menetelmällä ennen kuin mitään on rakennettu: kirjoittaa lyhyen tulevaisuuden lehdistötiedotteen (PR) ja kysymys-vastausosion (FAQ) siitä, miltä valmis ratkaisu näyttäisi asiakkaan näkökulmasta. Käytä kun mahdollisuus pitää tehdä konkreettiseksi ja keskustelunalaiseksi ennen protoilua, tai kun proto ei vielä ole mahdollinen/kannattava mutta visio pitää silti kommunikoida vakuuttavasti."
---

# Opportunity Visioning with PR-FAQ

*Tila: `scaffold` — ks. `../../../skills_index.json` ja `../../../meta/maturity_levels.md`.*

## Tarkoitus

Tehdä AI-mahdollisuus konkreettiseksi ja arvioitavaksi **ilman että mitään
on vielä rakennettu.** Moni AI-mahdollisuus jää abstraktiksi ("voisimme
käyttää tekoälyä X:ään") koska kukaan ei ole pakottanut itseään kuvaamaan
tarkasti, miltä valmis ratkaisu näyttäisi asiakkaan/käyttäjän näkökulmasta.
Tämä skilli soveltaa Amazonin Working Backwards -menetelmää ja sen PR-FAQ-
dokumenttia: kirjoita ensin lyhyt, tulevaisuudesta päivätty lehdistötiedote
siitä kuin ratkaisu olisi jo julkaistu, ja kysymys-vastausosio joka käy läpi
asiakashyödyt, riskit ja mittarit. Tämä on nopeampaa ja halvempaa kuin
protoilu, ja se paljastaa usein, ettei visio olekaan vielä selkeä — ennen
kuin kalliimpi protoilukierros alkaa.

## Ankkurointi tutkimukseen

- Amazon "Working Backwards" -menetelmä ja PR-FAQ-dokumentti (Bryar &
  Carr, *Working Backwards*, 2021): aloita asiakkaasta ja valmiista
  kokemuksesta, työskentele takaperin siihen mitä pitää rakentaa.
  PR-FAQ on lyhyt (n. 6 sivua) narratiivinen dokumentti kahdessa osassa:
  yhden sivun mock-lehdistötiedote tulevaisuuden julkaisupäivästä, ja
  kysymys-vastausosio joka käy läpi asiakasongelman, ratkaisun,
  riskit ja onnistumisen mittarit.

## Rakenne (luonnos — täydennettävä)

1. **Kirjoita yhden sivun mock-lehdistötiedote**, päivätty tulevaisuuteen
   (esim. "julkaistu [pvm], jolloin ratkaisu on käytössä"), ikään kuin
   ratkaisu olisi jo olemassa ja onnistunut:
   - Otsikko ja yhden lauseen tiivistelmä.
   - Asiakasongelma, joka ratkesi (konkreettinen, ei geneerinen).
   - Miten ratkaisu toimii asiakkaan näkökulmasta (ei teknisiä
     yksityiskohtia — mitä asiakas KOKEE).
   - Yksi lainaus kuvitteelliselta asiakkaalta, joka kuvaa hyötyä konkreettisesti.
   - Miten asiakas pääsee alkuun.
2. **Kirjoita FAQ-osio, joka käy läpi vaikeat kysymykset rehellisesti:**
   - Asiakaskysymykset: mitä tämä maksaa, miten tämä eroaa nykyisestä
     tavasta tehdä sama asia, mitä jos ratkaisu on väärässä.
   - Sisäiset kysymykset: mitä dataa/kyvykkyyttä tarvitaan jota ei vielä
     ole, mitkä ovat suurimmat tekniset ja organisatoriset riskit, miten
     onnistuminen mitataan, mitä TÄMÄ ratkaisu EI tee (rajaa laajuutta
     tietoisesti).
   Rehellisyys vaikeissa kysymyksissä on koko menetelmän ydin — PR-FAQ:n
   tarkoitus ei ole myydä ideaa itselle, vaan paljastaa sen heikkoudet
   ennen kuin niihin investoidaan.
3. **Käytä PR-FAQ:ta keskustelun pohjana, ei lopputuotteena.** Vie
   dokumentti sidosryhmille ja kysy erityisesti: onko asiakasongelma
   oikea, onko ratkaisu uskottava heidän näkökulmastaan, puuttuuko jokin
   olennainen este FAQ:sta. Päivitä dokumenttia palautteen perusteella
   ennen kuin siirryt protoiluun.
4. **Käytä PR-FAQ:ta myös silloin kun protoilu ei vielä ole järkevää** —
   esim. kun tekninen toteutettavuus on hyvin epävarma tai kustannus
   rakentaa mitään on korkea. PR-FAQ antaa tavan kommunikoida ja testata
   visio halvalla ennen sitoutumista.
5. **Kun PR-FAQ on vakaa ja sidosryhmät ovat samaa mieltä visiosta**, vie se
   syötteeksi `../rapid-prototype-and-vibe-coding-craft/SKILL.md`-skilliin:
   PR-FAQ:n "miten asiakas kokee ratkaisun" -kuvaus muuttuu prototyypin
   hypoteesiksi (skilli kohta 1).
6. **Älä sekoita PR-FAQ:ta business caseen** — PR-FAQ testaa VISION
   selkeyttä ja houkuttelevuutta, ei taloudellista kannattavuutta. Kun
   visio on selvä, talousperustelu tehdään erikseen
   `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
   -skillillä.

## Mitä tämä skilli EI tee

- Ei rakenna prototyyppiä tai koodia — tuottaa sanallisen vision ennen
  protoilua, ei protoilun korvaajaa.
- Ei laske ROI:ta tai kustannuksia — PR-FAQ:n FAQ-osio voi mainita
  kustannusarvion karkeasti, mutta täsmällinen talouslaskenta tehdään
  `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
  -skillillä.
- Ei ole markkinointimateriaalia asiakkaalle — PR-FAQ on sisäinen
  ajattelu- ja keskusteluväline, ei julkaistava dokumentti (vaikka sen
  muoto muistuttaa lehdistötiedotetta).
- Ei takaa että visio on oikea vain koska se on kirjoitettu vakuuttavasti
  — FAQ-osion rehellisten, vaikeiden kysymysten tarkoitus on nimenomaan
  testata visiota, ei kaunistella sitä.

## [OWNER INPUT — täydennettävä]

Tämä skilli on rakenteellinen luonnos (`maturity: scaffold`). Se ei vielä sisällä omaa
kokemustasi, heuristiikkojasi tai case-esimerkkejä. Täydennä tähän:

- oma PR-FAQ-mallipohja tarkalla rakenteella (`../../references/`-kansioon)
- konkreettisia esimerkkejä PR-FAQ:sta joka paljasti vision heikkouden
  ennen kalliimpaa protoilua
- nyrkkisääntöjä siitä, milloin PR-FAQ riittää ja milloin pitää siirtyä
  suoraan protoiluun

Kun tämä osio on täytetty ja validoitu käytännössä, päivitä `skills_index.json`:n
`maturity`-kenttä arvoon `draft`, `validated` tai `canonical`
(ks. `../../../meta/maturity_levels.md`). **Frontmatteriin ei lisätä uusia kenttiä** —
`name` ja `description` ovat ainoat sallitut (ks. `../../../meta/frontmatter_schema.md`).

## Jatka tästä

- Ennen tätä (jos toimialaan sopiva pattern puuttuu vielä):
  `../../../ai-strategy-and-governance/skills/ai-capability-pattern-matching/SKILL.md`
- Samassa pakissa seuraavaksi: `../rapid-prototype-and-vibe-coding-craft/SKILL.md`
- Syvempi tarina johdolle: `../../../change-and-communication/skills/executive-narrative-and-storyline/SKILL.md`
- Talousperustelu kun visio on vakaa: `../../../business-case-and-analysis/skills/business-case-builder/SKILL.md`
- Valmis skilliketju tähän tilanteeseen: ks. `../../../playbooks/`
- Pakin jaetut suojaukset: `../../CLAUDE.md`

## Referenssit

- Bryar, Colin & Carr, Bill — *Working Backwards: Insights, Stories, and
  Secrets from Inside Amazon* (2021) — Working Backwards -menetelmä ja
  PR-FAQ-dokumentti
- `../../references/` — pakin yhteinen taustamateriaali
- `../../CLAUDE.md` — pakin jaetut suojaukset
