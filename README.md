# dream-tracker
En enkel social plattform för att mäta och dokumentera sömnkvalitet samt de dynamiska scenerna som eventuellt uppstår under drömsömn.

[Dokumentaatio on myös saatavilla suomeksi](/docs/README.fin.md).
[Documentation also available in English](/docs/README.eng.md).

Det finns en [seed-rapport](/docs/seed_report.swe.md) nu.

## Funktioner
Användare kan
- skapa ett konto och logga in
- skapa nya inlägg samt redigera och radera sina egna inlägg
- se sina egna likväl andra användares inlägg
- följa andra användare och få deras inlägg i en behändig plats på hemsidan
- ange synlighetsvillkor för sina inlägg (ex. offentlig, enbart följare, privat...)
- välja lämpliga kategorier till sina egna inlägg
- söka efter inlägg enligt sökord, filterkategorier och/eller statistik
- se användares profilsidor, som visar deras inlägg samt aktuell statistik om dem
- svara på samt gilla inlägg

## Noteringar

En del förbättringar är möjliga:
- Egentligen bör CSRF bekräftas även vid registrering och inloggning. Tumregeln är att POST-metoder alltid bör bekräftas med en hemlig token.
- Användbarheten kan förbättras marginellt genom att visa felmeddelanden på samma sida som de sker. Detta anses dock utgöra en låg prioritet.
- Länkar kan visas på ett tydligare sätt, men utvecklaren anser att applikationens användbarhet är tillräckligt god och intuitiv med den stil som redan används.
- Radbrytningar (och annan markdown-stils texthantering) behandlas enbart på sidorna som visar hela inlägg, men exempelvis inte på framsidan eller i kommentar. Detta beteendet är avsiktligt, eftersom enbart hela inlägg är avsedda för längre brödtext med styckeindelning.
- Kommentar på inlägg som är privata eller avsedda enbart för vänner (användare som publiceraren följer) är offentliga för alla användare. Detta anses inte utgöra ett stort problem, eftersom enbart kommentar (och inte hela inlägg) syns.
- För programmets prestanda är det möjligt att behandla likes på ett annat sätt, som presenteras i [seed-rapporten](/docs/seed_report.swe.md).

# Installation

1. Ladda ner repon och navigera till dess mapp med en valfri terminal
2. Installera `flask`:

```
$ pip install flask
```

eller i en `venv`-virtualomgivning:

```
$ python -m venv venv
$ venv/bin/activate
$ pip install flask
```

3. Starta servern och navigera till `localhost:5000` med en valfri webbläsare

```
$ flask run
```

Programmet skapar databasen och konfigureringar automatiskt.
