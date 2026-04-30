# Pylint-raportti

Pylint tuottaa seuraavanlaisen raportin:

```
************* Module app
app.py:1:0: C0114: Missing module docstring (missing-module-docstring)
app.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:50:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:125:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:170:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:183:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:193:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:244:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:254:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:306:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:324:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:341:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:367:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:423:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:442:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:446:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:475:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:498:0: C0116: Missing function or method docstring (missing-function-docstring)
app.py:505:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module db
db.py:6:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:12:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:19:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:19:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:26:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:29:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:29:0: W0102: Dangerous default value [] as argument (dangerous-default-value)
db.py:35:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:45:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:53:0: C0116: Missing function or method docstring (missing-function-docstring)
db.py:58:0: C0116: Missing function or method docstring (missing-function-docstring)
************* Module posts
posts.py:1:0: C0114: Missing module docstring (missing-module-docstring)
posts.py:14:0: R0913: Too many arguments (8/5) (too-many-arguments)
posts.py:14:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
posts.py:28:0: R0913: Too many arguments (6/5) (too-many-arguments)
posts.py:28:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
posts.py:97:0: R0913: Too many arguments (8/5) (too-many-arguments)
posts.py:97:0: R0917: Too many positional arguments (8/5) (too-many-positional-arguments)
posts.py:132:0: R0913: Too many arguments (6/5) (too-many-arguments)
posts.py:132:0: R0917: Too many positional arguments (6/5) (too-many-positional-arguments)
posts.py:163:0: R0913: Too many arguments (7/5) (too-many-arguments)
posts.py:163:0: R0917: Too many positional arguments (7/5) (too-many-positional-arguments)
************* Module seed
seed.py:45:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:63:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:77:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:88:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:99:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:123:11: W0718: Catching too general exception Exception (broad-exception-caught)
seed.py:140:11: W0718: Catching too general exception Exception (broad-exception-caught)
************* Module users
users.py:1:0: C0114: Missing module docstring (missing-module-docstring)
users.py:4:0: C0411: standard import "datetime.datetime" should be placed before third party imports "werkzeug.security.generate_password_hash", "werkzeug.security.check_password_hash" (wrong-import-order)

------------------------------------------------------------------
Your code has been rated at 9.06/10 (previous run: 9.06/10, +0.00)
```

## Perustelut

### Dokumentaatio

Pylint varoittaa useaan otteeseen, että moduulien, funktioiden ja metodien docstring-dokumentaatiomerkkijonot puuttuvat. Yleisesti ottaen tämänlaista dokumentaatiota on käytetty runsaasti ohjelman kehityksessä, etenkin perinteisten kommenttien sijasta. Tähän liittyy toisaalta huomattavia poikkeuksia:

- Dekoraattorin, kuten `@app.route`, edeltämät funktiot eivät sisällä docstringeja. Kehittäjä pitää näiden funktioiden tarkoitusta itsestään selvänä.
- Vain apumoduuleille (`ezformat`, `db.py`) sisältävät moduulitason dokumentaatiotekstit. Päämoduuli, sekä kaikki refaktoroidut toissijaiset moduulit (kuten `users.py`), on tietoisesti jätetty ilman dokumentaatiota.
- Moduulin `db.py` docstring-kommentit on tarkoituksella jätetty pois, koska tämä moduuli vastaa läheisesti kurssimateriaalin toteutusta.
- Kehittäjä pitää apufunktiota `logged_in()` itsestään selvänä.

### Kirjastot

Toisinaan, Pylint herjaa, että `standard import "datetime.datetime" should be placed before third-party imports "werkzeug..."`. Standardikirjaston moduulit tulisi siis Pythonin käytäntöjen mukaan määrittää ja alustaa ennen ulkoisten kirjastojen moduuleja. Kehittäjä katsoo toisaalta, että epästandardinen järjestys tai ryhmittely on puuttuvaa järjestystä parempi vaihtoehto, ja että ohjelmassa käytetty tyyli on looginen ja esteettisesti mieluisa.

On käytännössä mahdollista, että kolmannen osapuolen moduuli on standardikirjastosta riippuvainen, mutta ei itse tuo sitä mukaan. Tällöin epästandardi järjestys voisi tuottaa odottamattomia tuloksia, etenkin ohjelman ensimmäisten millisekuntien aikana. Tällä ei katsota olevan vaikutusta ohjelman toimintaan.

Huomaa, että `import`-lauseet voidaan ryhmitellä ja yhdistää seuraavanlaisesti:


```
*** users.py
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from werkzeug.security import generate_password_hash, check_password_hash
```

Kehittäjä pitää tämän tekniikan tuomia hyötyjä vähäisinä verrattuna tarpeettoman pitkien rivien tuomiin haittoihin. Lausekkeet on jaettu tällä tavalla, jotta rivien pituus ei ylittäisi 72 merkkiä (mukaanlukien välilyönnit).

Lopuksi Pylint varoittaa, että joitakin ulkoisia moduuleja ei voitu hakea – `unable to import 'flask'`. Tämä on ilmeisesti `venv`-virtuaaliympäristön sivuvaikutus, jolla ei kuitenkaan ole vaikutusta ohjelman toiminnallisuuteen.

### Virhetilanteet

Pylint väittää, että ohjelma vastaanottaa liian yleisen virhetilanteen, eli `catching too general exception Exception`. Tämä viittaa siihen, että `except`-lohkossa tulisi pääsääntöisesti vastaanottaa tarkempia alaluokkia perusluokan `Exception` sijaan. Yleensä yleisen virheen sieppaaminen ei ole suotavaa, sillä se ei yleisesti anna tietoa virhetilanteen syystä tai tyypistä. Virhetilanne kannattaa myös siepata vain, jos tämän aikoo käsitellä jollain sopivalla ja tarkoituksenmukaisella tavalla.

Kehittäjä kuitenkin katsoo, että näitä virheitä sisältävä moduuli `seed.py` on tarkoitettu ensisijaisesti ohjelman kehitykseen ja testaukseen. Tämän moduulin puutteet eivät heijasta ohjelman puutteita. Käsitellyt virheet kerätään näin ottaen yksinomaan helpottamaan ohjelman debuggausta.

### Vaaralliset oletusarvot

Pylint varoittaa, että argumentin oletusarvo joissakin metodikutsuissa voi aiheuttaa odottamattomia ongelmia:

`dangerous default value [] as argument`

Tämä viittaa epätavalliseen Pythonin ominaisuuteen – tyhjä lista alustetaan viittauksena listaolioon, joka jaetaan kaikkien kutsujen välillä. `[]`:n alustaminen funktion parametrin oletusarvona voi aiheuttaa epätavallisia ongelmia, jos jokin funktio muuttaa listan sisältöä. Mikään metodi ei kuitenkaan tee näin, joten tällä ongelmalla ei ole vaikutusta ohjelman toiminnallisuuteen.

### Vakion nimeämistyyli

`seed.py`-tiedostossa, Pylint varoittaa, että vakion nimeämistyyli ei seuraa PÖLKKYKIRJOITUS_TYYLIÄ – `constant name "errs" doesn't conform to UPPER_CASE naming style`. Kyseistä tyyliä on käytetty muualla ohjelmassa, etenkin `seed`- ja `config`-moduuleissa. Huomaa, että `seed:~errs` *ei ole vakio, vaan muuttuja, jonka arvo haetaan ja päivitetään moneen kertaan ohjelman aikana*.

### Parametrien lukumäärä

Posts-moduulissa Pylint herjaa, että argumenttien määrä on liian suuri. Tämä viittaa esimerkiksi metodiin

```
def create_filters(user_id=None, tab="latest", q=None,
                   sleep_quality=None, tags=None, cats=None):
    ...
```

joka ottaa kuusi (6) parametria. Jos metodi sisältää liian monta parametria, on helpompi tehdä virhe funktiokutsun yhteydessä, esimerkiksi listaamalla parametrit väärässä järjestyksessä.

Parempi käytäntö olisi ehdottomasti faktoroida funktio useampaan pienempään apufunktioon. Kehittäjä kuitenkin katsoo, että koodin toimivuus ja muokattavuus on siitä huolimatta hyväksyttävällä tasolla.
