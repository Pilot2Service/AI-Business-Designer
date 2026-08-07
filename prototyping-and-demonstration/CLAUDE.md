# Prototyping & Demonstration — jaetut suojaukset

Yleiset suojaukset (vastuuvapaus, ei keksittyjä lukuja, premissien tarkistus,
kypsyystason näkyväksi tekemisen periaate) ovat koostettu yhteen paikkaan:
**ks. `../meta/shared-guardrails.md` — lue se ensin.** Tämä tiedosto sisältää vain
sen, mikä on aidosti pakkikohtaista tässä pakissa.

---

## Demo ei ole tuote — sano se ääneen aina

Tämän pakin ydinriski on **proto/demo-menestyksen sekoittaminen tuotantovalmiuteen.**
Nopeasti rakennettu, "vibe coodattu" proto todistaa idean toimivan periaatteessa —
se ei todista, että ratkaisu on turvallinen, skaalautuva, ylläpidettävä tai
tietoturvallinen tuotannossa. Jokaisessa tämän pakin tuotoksessa:

- Merkitse selvästi, mikä on demo-tason löydös ("toimi 3 testitapauksessa
  hallitussa ympäristössä") vastaan tuotantotason väite ("toimii luotettavasti
  kaikissa tapauksissa") — älä koskaan anna näiden sekoittua.
- Muistuta, että AI-avusteisesti ("vibe coodaten") tuotettu koodi sisältää
  tyypillisesti hallusinoituja rajapintoja, puutteellista virhekäsittelyä ja
  heikkoja autentikointi-/oikeustarkistuksia, kunnes ihminen on ne erikseen
  tarkistanut — tämä koskee erityisesti mitä tahansa demoa, jossa käsitellään
  oikeaa dataa tai esitetään live-ympäristössä.
- Älä koskaan esitä demoa asiakkaalle "melkein valmiina tuotteena" — kehystä se
  aina sen mukaan, mitä se todella on (konseptin todistus, ei tuotantosovellus).

## PoC / Pilotti / MVP — eri termit, eri kysymykset

Näitä käytetään usein virheellisesti synonyymeinä. Ne vastaavat eri
epävarmuuksiin, älä sekoita niitä:

- **PoC (Proof of Concept)** — vastaa "toimiiko tämä teknisesti ylipäätään
  edustavalla datalla?" Aikarajattu, matalariskinen, ei vielä tuotantodataa
  tai -kuormaa.
- **Pilotti** — vastaa "toimiiko tämä oikeiden ihmisten ja oikeiden
  operatiivisten olosuhteiden kanssa?" Olettaa, että tekninen toteutettavuus
  ja arvo on jo ennustettu — pilotti vahvistaa sen käytännössä.
- **MVP (Minimum Viable Product)** — vastaa "mitä pitäisi rakentaa seuraavaksi
  oikean käyttäjäpalautteen perusteella?" Tuotekehitysote, ei
  todistamisvaihe.

Käytä oikeaa termiä äläkä käytä niitä toistensa synonyymeinä asiakasviestinnässä
— väärä termi luo väärän odotuksen budjetista, aikataulusta ja siitä mitä
seuraavaksi tapahtuu.

## Pilot purgatory -riski on todellinen ja se torjutaan framingilla, ei koodilla

Tutkimus (mm. McKinsey, BCG, IDC, MIT) osoittaa toistuvasti, että suuri osa
(arviot vaihtelevat lähteittäin, karkeasti 80–95 %) yrityssektorin AI-piloteista
ei koskaan etene tuotantoon — pullonkaula on tyypillisesti operatiivinen
(työnkulun uudelleensuunnittelu, johdon sitoutuminen, mittakaavan investointi),
ei tekninen. Tämän pakin skillit eivät voi ratkaista tätä demo-vaiheessa, mutta
niiden PITÄÄ tehdä riski näkyväksi jo demo-/PoC-vaiheen kehystyksessä (ks.
`skills/demo-framing-and-expectation-setting/SKILL.md`) — älä anna asiakkaan
uskoa, että onnistunut demo tarkoittaa automaattista tuotantoon etenemistä.

## Ei keksitä lukuja tässä pakissa — skaalautumisoletus erikseen

Yleisen periaatteen (`shared-guardrails.md`) lisäksi: PoC-mittakaavan tulos
(esim. "säästi 2 tuntia 10 tapauksessa") ei ekstrapoloidu suoraviivaisesti
tuotantomittakaavaan ilman selkeää, näkyväksi merkittyä oletusta siitä, miksi
skaalautuminen olisi lineaarista.

## Kypsyystaso tässä pakissa

Tämän pakin skillit ovat tällä hetkellä `maturity: scaffold` -tasolla (ks.
`../skills_index.json` ja `../meta/maturity_levels.md`) — rakenne ja ankkurointi ovat
tutkimuspohjaisia (Great Demo! -metodologia, vibe coding -käytännöt, PoC/Pilot/MVP-
kirjallisuus, Amazon Working Backwards, prototyyppifideliteetti-tutkimus), mutta omaa
validoitua konsultointikokemusta ei vielä ole liitetty.

## Jaetut standardit

Katso `../meta/frontmatter_schema.md` (mitä SKILL.md-frontmatteriin saa laittaa) ja
`../meta/skill_design_principles.md` (mitä hyvä skilli tässä repossa läpäisee).
