# Systemövervakningsapplikation

## Vad programmet gör
Ett program som kollar hur mycket CPU, minne och disk som används. Man kan också skapa larm som ska varna när det används för mycket.

## Vad som funkar just nu

# Klart
- [x] **Val 1:** Starta övervakning (sätter en flagga)
- [x] **Val 2:** Visa CPU, minne och disk
- [x] **Val 3:** Skapa larm
- [x] **Val 4:** Visa alla larm
- [x] **Val 5:** Övervakningsläge med larm

# Om jag hinner (VG)
- [ ] Spara larm till fil
- [ ] Loggning
- [ ] Ta bort larm

# Förberedelse
- Skapade mappar (src/, data/, logs/) för att organisera projektet
- Tittade på YouTube-tutorials om Python
- Gick igenom delar av "100 days of code: The Complete Python Pro Bootcamp" på Udemy för att förstå grunderna bättre
- Testade psutil-funktioner i en separat test.py fil för att lära mig hur de fungerar


# Start
Jag började med att skapa mappar (src/, data/, logs/) för att det skulle se organiserat ut. Men sen bestämde jag mig för att jobba i en fil först (simple_menu.py) för att det var enklare att se allt på en gång.

- Lättare att testa - allt är på samma ställe
- Kunde få det att fungera snabbare
- Sen kan jag dela upp det senare om jag vill

# Val 1-3: Få det att fungera
 Jag började med att få menyn att fungera, sen la jag till en del i taget:

- Val 1 var enklast - bara sätta en variabel till True
- Val 2 var lite svårare - fick googla hur psutil fungerar- 
- Val 3 tog längst tid - behövde kolla så användaren inte skriver fel saker

# Problem jag stött på
 1) Problem att jobba i en fil. Glömde committa efter varje del! Var så fokuserad på att få det att fungera. Från val 4 ska jag komma ihåg att committa oftare.

2) Input-validering var svårt, då jag innan if statement försökte med case, då jag såg många andra klasskamrater jobba med det. vilket blev även att jag hade problem med erorrhanteringar.

3) En stor utmaning jag har vart indenteringar, med vad som ska vara innaför vilka block för att fungera.

4) jag har även haft problem med att gå vidare när jag inte förstår mig på saker, vilket vart tidskrävande. t.ex kunde jag slösa timmar på att förstå mig på något så simpelt att man sparade `mem = psutil.virtual_memory()` i en variabel men körde `psutil.cpu_percent()` direkt. Sen lägga timmar på att förstå varför skillnad? eller  Hittade två sätt att räkna om bytes till GB:
- `/ 1024**3` (binärt)
- `/ 1e9` (decimalt)
- Fattade inte vilken som var "rätt".

5) Glömde committa Var så inne i att få koden att fungera att jag glömde helt att committa mellan val 1, 2 och 3.

6) i meny val 4 så stötte jag på problem med larm inte ville visa sig vid val pga citatttecken, 

- Jag hade svårt att förstå hur `sorted(larm_lista, key=hämta_typ)` fungerade.

7) i val 5, för uppgiften:

 - Avbrott: Hur jag exakt ska implementera att man kan trycka på valfri tagent för att avbryta i konsolen utan att blockera time.sleep(1)

# jag tänkte
- "key=hämta_typ" betyder "hämta alla keys från larm_lista"
- Funktionen hämta_typ hämtar alla keys från dictionaryn

# lösning/ Vad jag lärt mig
- slutade jämföra mig och jobbade med det som jag kände trygast med t.ex if statement, dock så hade jag forsatt svårt med erorhantering och indenteringar osv.

- Googlade och youtubade. Vissa saker känns fortfarande lite konstigt men jag tror och hoppas jag fattar principen, men valde att inte fastna då det var så energikrävvande. 

- Commits är viktiga för att visa hur man jobbar, inte bara för backup. Från nu (val 4+) ska jag komma ihåg att committa efter varje del som fungerar.

-virtual_memory()` ger tillbaka massa saker (procent, använt, totalt) så det är smartare att spara det en gång istället för att anropa det tre gånger. `cpu_percent()` ger bara EN sak så då behövs ingen variabel.

- i val 5 för uppgiften har jag använt mig av bibloteket import.time för time.sleep för att kuna mäta nivår som är satta av användare i realtid.

# Hur jag löste misförståelse om sorted() och key=
jag youtubade och fråga chatgbt och förtod Python anropar `hämta_typ()` för VARJE dictionary i listan
 Varje dictionary blir parametern `larm` EN gång
 Funktionen returnerar det värde som ska användas för sortering
Python sorterar sedan på dessa returvärden
 
 key= tar en FUNKTION som parameter, inte en nyckel från dictionaryn!

# Struktur just nu

uppgiftpython/
├── simple_menu.py      # Allt är här än så länge
├── src/                # Tom, ska använda senare kanske
├── data/               # Tom, för JSON senare
├── logs/               # Tom, för loggfiler senare
├── requirements.txt    
└── README.md          
ur

Delade upp simple_menu.py i fyra separata klasser för att koden skulle bli tydligare:

- `src/alarm.py` - Alarm och AlarmManager klasser (logik)
- `src/monitoring.py` - Monitor klass (läser systemet med psutil)
- `src/menu.py` - Menu klass (all I/O och användarinteraktion)
- `src/main.py` - Entry point

**Varför?** Mycket lättare att läsa, testa och underhålla när allt är separerat.

## Problem under refaktoreringen och lösningar

1) **Blandat svenska/engelska** - Skrev ibland `"Minne"` och ibland `"Memory"` → CRASHES!
   - Lösning: All kod är nu på ENGELSKA (CPU, Memory, Disk överallt)

2) **Val 5 blockerade menyn** - `while True` loopen gjorde att man inte kunde gå tillbaka
   - Lösning: Använde threading för att köra övervakningen i bakgrunden

3) **Sortering av larm** - Förstod inte hur `sorted(larm, key=hämta_typ)` fungerade
   - Min felaktig tanke: key= hämtar från dictionaryn
   - Rätt: key= tar en FUNKTION som parameter!

4) **Dictionary keys måste matcha** - Skrev `values["Memory"]` men det var `values["memory"]`
   - Lösning: Case-sensitive! Var noga med stavning

## Vad jag lärt mig denna gång

**Nya koncept:**
- Threading - köra kod i bakgrunden utan att blockera menyn
- Separation of Concerns - varje klass gör EN sak
- Ren logik vs I/O - klasserna returnerar data, Menu visar den

**Från buggar:**
- Stavningsfel och case-sensitivity tar timmar att debug
- Konsekvent engelska överallt sparar många fel
- Importer måste vara rätt för att klasser hittas


# Reflektioner 

 Tekniskt:
- Hur man använder try/except (typ)
- psutil för att kolla CPU, minne, disk
- Hur man sparar saker i dictionaries och listor
- Att indentering är jätteviktigt i Python

- Generellt:
- Det är okej att inte fatta allt direkt
- Googla är inte fusk, det är hur man lär sig
- Testa en liten del i taget istället för allt på en gång
- Committa oftare!

- Saker jag fortfarande är osäker på:
- Exakt hur try/except fungerar "under huven"
- När man ska använda funktioner vs bara skriva i main
- Om min kod är "bra" eller bara "funkar"

 Varför simple_menu.py först?
Jag tänkte att det var enklare att se allt på ett ställe medan jag lär mig. När allt fungerar kan jag alltid dela upp det senare om jag vill. Är inte säker på om det är "rätt" sätt men det funkar för mig just nu.

 Varför dictionary för larm?
larm = {"typ": "CPU", "nivå": 80}

För att det är tydligt vad som är vad. Kunde ha använt en lista typ `["CPU", 80]` men då vet man inte vad 80 betyder utan att komma ihåg ordningen.

#  Reflektioner för val 5:
- Mina reflektioner kring uppgiften
 **Larmutlösning:** Om flera nivåer är satta (t.ex. CPU 60%, 70%, 80%), är tanken att **alla** larm ska triggas, eller enbart det med **högsta** nivån (80%) när användningen överstiger det? 
 
 - När användaren ska tillbaka till huvudmenyn ska larmen vara fortstt aktiverade.

# Vad jag har kvar

- Val 5 är nu klar med threading!

 Om jag har tid (VG-nivå):

- Spara larm till JSON
- Loggning
- Ta bort larm