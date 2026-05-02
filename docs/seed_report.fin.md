## Suuret tietomäärät

Kokeillaan, miten applikaatio reagoi suureen testidataan. Varmista, että tietokanta on alustettu, ja suorita komento

```$ python seed.py```

Testidatan luominen kestää noin 30 sekuntia. Data luodaan näillä arvoilla:

```
USER_COUNT = 10_000
POST_COUNT = 1_000_000
COMMENT_COUNT = 3_000_000
LIKE_COUNT = 50_000_000
TAG_COUNT = 600_000
FRIEND_COUNT = 70_000
```

### Mittaukset

Lisätään mittauslogiikkaa pääsovellukseen (`app.py`):

```
from flask import g
from time import time

@app.before_request
def before_request():
    g.start_time = time()

@app.after_request
def after_request(response):
    t = round(time() - g.start_time, 2)
    print(f">> Request time: {t} seconds")
    return response
```

Ohjelma tulostaa ajanmittauksen terminaaliin käyttäjän tehdessä minkä tahansa HTML-pyynnon.

### Tulokset

Tulokset on ilmoitettu kolmen mittauksen keskiarvona, pyöristettynä kahteen desimaalilukuun. Sivu pyydettiin joka kerta ilman välimuistissa olevia tietoja (`CTRL+F5`).

#### Kontrolli

Luodaan aluksi vain yksi käyttäjä ja yksi tietokohde.

| Sivu | Aika |
| -----| --- |
| etusivu | 0.05 s |
| tietokohde | 0.03 s |
| käyttäjäsivu | 0.04 s |
| muut | 0.02 s |

#### Testidata

Luodaan testidata `seed.py`-tiedoston avulla, mutta ilman tehostavia tekniikoita, kuten indeksejä tai sivutusta.

| Sivu | Aika |
| -----| --- |
| etusivu | 10.34 s |
| tietokohde | 0.07 s |
| käyttäjäsivu | 0.23 s |
| muut | 0.03 s |

Applikaatio on käyttökelvottoman hidas.

#### Testidata sivutuksella

Identtisen testidatan kanssa sivutetaan tiedot. Sivut ovat jaettu kahdenkymmenen julkaisun alasivuihin. Tietokannassa ei kuitenkaan vielä ole indeksejä.

| Sivu | Aika |
| -----| --- |
| etusivu | 0.74 s |
| tietokohde | 0.04 s |
| käyttäjäsivu | 0.05 s |
| muut | 0.03 s |

#### Testidata sivutuksella ja indekseillä

Viimeinen mittaus tehdään samoin olosuhtein kuin yllä, mutta tietokantaan on lisätty kyselyjä nopeuttavia indeksejä.

| Sivu | Aika |
| -----| --- |
| etusivu | 0.32 s |
| tietokohde | 0.02 s |
| käyttäjäsivu | 0.03 s |
| muut | 0.02 s |

### Johtopäätökset

Applikaatio toimii suhteellisen hyvin jopa kymmenien miljoonien tietokantarivien kanssa. Indeksit ja sivutus auttoivat paljon, ja osoittautuivat käytännössä pakollisiksi suuren tietomäärän kanssa.

Sivu latautuu nopeammin jos ei ole kirjautuneena sisään, koska applikaation ei tarvitse verrata julkaisujen näkyvyysmääreiden ja käyttäjän näköluvan relaatiota. Kehittäjä katsoo, että tämä on näkyvyystoimivuuden väistämätön ominaisuus.

Etusivun lataamisen nopeutta voi vielä tehostaa sillä, että tykkäysten määrä säilytettäisi suoraan tietokannassa, esimerkiksi `Posts`-taulukon rivissä `like_count` joka päivitetään SQL `TRIGGER`-komennon avulla. Kehittäjä katsoo kuitenkin, että tämänlainen muutos tässä vaiheessa ohjelman kehitystä on turhan suuri verrattuna muutoksen hyötyasteeseen.