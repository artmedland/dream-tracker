# Pylint-rapport

Pylint skriver ut följare rapport:

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

## Motiveringar

### Docstrings

Pylint skriver flera gånger att docstrings för moduler, funktioner och metoder fattas. I regel har programmets utvecklare tillsatt dokumentation för funktioner, metoder och moduler där det har varit nyttigt, särskilt i stället för traditionella kommentar. Det finns dock vissa undantag:

- Hos dekorerade funktioner, huvudsakligen `@app.route`-metoder, anges inga docstrings. Programutvecklaren anser att dessa funktioners syften är självklara.
- Enbart hjälpmoduler anges docstrings på modulnivå. Programmets huvudmodul `app.py` – samt programfunktioner hos den som omfaktorerats till andra moduler – har medvetet lämnats utan docstrings.
- Modulen `db.py` anges inga docstrings för att den motsvarar nära kursmaterialens implementering.
- Hjälpfunktionen `logged_in()` anses vara oerhört självklar i dess funktion.

### Bibliotek

Nu och då skriver Pylint exempelvis att `standard import "datetime.datetime" should be placed before third-party imports "werkzeug..."`.
Programutvecklaren anser att en bristfällig eller icke-standard gruppering och ordning är bättre än ingen alls, och att den ordningen som använts är logisk samt estetiskt tilltalande. 

Därjämte är det möjligt att gruppera import-uttryck med hjälp av kommatecken, exempelvis på följande sätt:

```
*** users.py
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash

from werkzeug.security import generate_password_hash, check_password_hash

```

Programutvecklaren anser att nyttan som denna teknik framför är marginell jämfört med skadan som en onödigt lång rad innebär.

Till sist varnar Pylint att en del externa moduler inte kunde tillsättas – `unable to import 'flask'`. Detta är antagligen en biverkning som orsakas av användningen av virtualomgivningen `venv`, och har ingen inverkan på programmets funktionalitet.

### Felbehandling

Pylint skriver `catching too general exception Exception`. Detta tyder på att feltypen i ett `except`-block sällan bör fånga hela basklassen – och således alla underklasser som ärver dess egenskaper – utan föredra mer specifika underklasser. Lämpligare feltyper här kunde exempelvis vara `sqlite3.IntegrityError`. I regel skall man aldrig fånga allmänna felfall, särskilt om inte man planerar att behandla dessa fall för någon särskild orsak. 

Emellertid anser programutvecklaren att modulen `seed.py`, som innehåller alla sådana felfall, används huvudsakligen för programmets utveckling och inte i en äkta tjänstsituation. Dessa felfall är inte relevanta för programmets funktion, utan samlas enbart för programmerarens förmån. 

### Farliga standardvärden

Pylint varnar att standardvärden på argumenten hos vissa metoder är otillförlitlig: 

`dangerous default value [] as argument`

Detta innebär att argumentet `params=[]` initialiserar en tom lista. Bland Pythons underligare egenskaper är att en tom lista initialiseras som en hänvisning till ett objekt, som delas mellan dess anrop. Detta kan orsaka problem om en metod ändrar listans innehåll. Eftersom ingen metod gör detta har dock detta problem ingen verklig inverkan på programmet.

### Namngivning hos konstantvärden

I `seed.py` varnar Pylint att `constant name "errs" doesn't conform to UPPER_CASE naming style`. Samma stora bokstävers `snake_case`-stil har använts annanstans i programmet, huvudsakligen i `seed` och `config`-modulerna. Variablen `seed:~errs` är dock ingen konstant, eftersom den används och uppdateras i programmet! 
> Om den ser ut som en variabel, beter sig som en variabel, och kvackar som en variabel -- är det sannolikt en variabel!