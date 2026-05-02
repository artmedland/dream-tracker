# dream-tracker
Yksinkertainen some unen laadun kirjaamiseen sekä unten tarinoiden jakamiseen muiden käyttäjien kanssa.

Lue [seed-raportti](/docs/seed_report.fin.md)

## Toiminnot
Käyttäjät voivat
- luoda tunnuksen ja kirjautua sisään
- julkaista omia päivityksiä sekä muokata ja poistaa omia päivityksiään
- katsella sekä omia että muiden käyttäjien päivityksiä
- seurata toisia käyttäjiä ja nähdä näiden päivityksiä ohjelman etusivulla
- määritellä omille päivityksilleen yksilöllisen näkyvyysmääreen (esim. julkinen, yksityinen, vain seuraajille...)
- valita sopivia luokitteluja omille päivityksilleen
- hakea päivityksiä hakusanojen, luokittelujen ja/tai tilastojen perusteella
- tarkastella käyttäjien profiilisivuja, jotka sisältävät kyseenomaisen käyttäjän päivitykset sekä olennaisia tilastoja
- vastata päivityksiin sekä tykätä niistä

## Huomioitavaa

Sovelluksen käyttökokemusta voi parantaa muutamalla tiedostetulla tavalla:
- CSRF-aukko tulisi oikeaoppisesti estää myös rekisteröinti- ja kirjautumissivuilla. Nyrkkisääntö on, että POST-metodit tulisi aina varmistaa.
- Käytettävyyttä voisi parantaa näyttämällä virheviestit samalla sivulla, jotka on nämä aiheuttanut. Tämä katsotaan kuitenkin alhaiseksi prioriteetiksi.
- Linkit voisi merkitä selkeämmin. Kehittäjä kuitenkin kokee, että linkit ovat jo riittävän selkeästi merkittyjä ja sivu on helppokäyttöinen jo nykyisellä tyyliasulla.
- Rivinvaitoja ja muuta markdown-tyyppistä tekstinkäsittelyä käsitellään ainoastaan julkaisujen kokonaisilla sivuilla, eikä esimerkiksi etusivulla, kommenteissa tai käyttäjäsivuilla. Tämä on tahallista — rivinvaihtoja ei tueta esimerkiksi kommenteissa, koska nämä on tarkoitettu lyhyemmille tekstinpätkille.
- Yksityisten ja ainoastaan ystäville näkyvien julkaisujen kommentit näkyvät kommentoijan käyttäjäsivulla, joka voidaan katsoa haavoittavan julkaisun yksityisyysmääreitä. Tätä ei kuitenkaan katsota suureksi ongelmaksi, koska profiilisivu ainoastaan näyttää julkaisun otsikon ja kommentin sisällön, eikä mitään julkaisulle keskeistä tietoa.
- Sovellusta voi nopeuttaa käsittelemällä tykkäyksiä toisenlaisella tavalla, joka mainitaan lyhyesti [seed-raportissa](/docs/seed_report.fin.md).

# Asennus

1. Kloonaa repon sisältö ja avaa kansio valinnaisessa terminaalissa
2. Asenna `flask`:

```
$ pip install flask
```

tai virtuaaliympäristössä

```
$ python -m venv venv
$ venv/bin/activate
$ pip install flask
```

3. Käynnistä palvelin ja avaa osoite `localhost:5000` valinnaisella verkkoselaimella

```
$ flask run
```

Applikaatio alustaa tietokannan ja asetukset automaattisesti.