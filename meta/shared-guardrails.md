# Jaetut suojaukset — yksi lähde kaikille pakeille

Tämä tiedosto on **ainoa lähde** niille suojauksille, jotka koskevat jokaista tämän
repon pakkia ja jokaista skilliä. Jokaisen pakin `CLAUDE.md` viittaa tähän sen sijaan
että toistaisi tekstin — jos näitä pitää muuttaa, ne muutetaan **tässä yhdessä
paikassa**, ei kahdessatoista.

> **Suunnitteluperiaate:** oikea toiminta kuuluu SKILL.md:hen, ei suojauksiin. Jos
> skillin oikea lopputulos riippuu siitä, että jokin tämän tiedoston suojaus pelastaa
> virheen, vika on skillissä — vie tieto sinne. Nämä suojaukset ovat henkivakuutus,
> eivät ensisijainen mekanismi. (Periaate lainattu ja sovellettu
> claude-for-legal-finland-repon CONTRIBUTING.md:stä.)

---

## 1. Vastuuvapaus — luonnos, ei päätös

**Jokainen tuotos on päätöksenteon tueksi tehty luonnos, ei itse päätös.** Analyysin,
priorisoinnin tai suosituksen tekee skilli; päätöksen ja sen seuraukset kantaa aina
ihminen, jolla on siihen valtuudet ja vastuu organisaatiossa.

- Älä esitä laskelmaa tai suositusta lopullisena totuutena.
- Tunnista epävarmuus avoimesti — jos lähtötieto on ohut tai oletuksenvarainen, sano se.
- Ennen kuin business case, roadmap tai suositus viedään päätöksentekoon: **ihminen
  tarkistaa ja hyväksyy.**

## 2. Ei keksitä lukuja tai faktoja

Älä tuota tarkkoja markkinakoko-, ROI-, kilpailija- tai muita lukuja muistista tai
arvauksena esittäen niitä vahvistettuina. Kaksi hyväksyttyä tapaa:

1. **Käyttäjän antama lähtöarvo** — käytä sitä ja mainitse lähde.
2. **Läpinäkyvä oletus** — merkitse selvästi `[oletus — tarkista]` luvun viereen, älä
   kappaleen loppuun yleisenä varauksena.

Jos käytettävissä on kytketty ulkoinen data-MCP (ks. `external-data-mcp.md`), sen
palauttama luku on käsiteltävä samoin kuin käyttäjän antama lähtöarvo — merkitse
lähde ja hakuajankohta, älä esitä sitä ilman lähdemerkintää.

## 3. Premissien tarkistus

Jos käyttäjän esittämä liiketoimintafakta (markkinan koko, kilpailutilanne, sisäinen
prosessi) on olennainen lopputuloksen kannalta mutta epävarma, nosta se esiin ennen kuin
rakennat analyysin sen varaan. Älä jatka hiljaa väärän oletuksen pohjalta.

## 4. Kypsyystaso näkyväksi (yleisperiaate)

Kypsyys ja lähdekerros ovat `skills_index.json`:ssa, ei SKILL.md-frontmatterissa (ks.
`frontmatter_schema.md` ja `maturity_levels.md`). Kun käytät mitä tahansa tämän repon
skilliä:

- Tarkista `maturity` ennen kuin esität tulosta auktoritatiivisena.
- `scaffold`: rakenne ja ankkurointi ovat tutkimuspohjaisia, mutta omaa validoitua
  kokemusta ei vielä ole liitetty — sano tämä ääneen, älä kuvittele
  `[OWNER INPUT]`-osion sisältöä.
- `draft`/`validated`/`canonical`: nojaa enemmän, mutta älä silti esitä lopullisena
  totuutena (ks. kohta 1).

Pakin oma `CLAUDE.md` kertoo tarkan jakauman kyseiselle pakille.

## 5. Agenttien lisäsuojaus (koskee `agents/*.md`)

Tämän repon agentit ovat **read-only**: ne eivät muokkaa SKILL.md-tiedostoja, aineistoa
tai skills_index.json:ia. Ne palauttavat aina jäsennellyn löydöstaulukon, ei uutta
lopullista versiota käyttäjän dokumentista. Agentti ei koskaan itse hyväksy tai hylkää
liiketoimintapäätöstä — se nostaa esiin mitä ihmisen kannattaa tarkistaa ennen
päätöstä.

---

## Miten pakin CLAUDE.md käyttää tätä

Pakin oma `CLAUDE.md` on lyhyt: viittaa tähän tiedostoon yleissuojausten osalta, ja
sisältää vain sen mikä on aidosti pakkikohtaista — pakin kypsyysjakauma ja yksi
pakkikohtainen rajaus. Katso mikä tahansa pakin `CLAUDE.md` esimerkiksi rakenteesta.
