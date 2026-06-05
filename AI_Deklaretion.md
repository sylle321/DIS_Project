# Deklaration for anvendelse af generative AI-værktøjer (studerende)

## 1. Brugserklæring

- [x] **Jeg/vi har benyttet generativ AI som hjælpemiddel/værktøj**
- [ ] Jeg/vi har **IKKE** benyttet generativ AI som hjælpemiddel/værktøj

> Hvis brug af generativ AI er tilladt til eksamen, men du ikke har benyttet det i din opgave, skal du blot krydse af, at du ikke har brugt GAI, og behøver ikke at udfylde resten.

## 2. Oplistning af GAI-værktøjer

| Værktøj | Platform / Link |
|---------|-----------------|
| Microsoft Copilot | https://copilot.microsoft.com/ |
| ChatGPT | https://chat.openai.com |

## 3. Beskrivelse af anvendelse

### 1. Formål (hvad har du brugt værktøjerne til)
- **Copilot**: Kodeforslag og autocompletion i VS Code under udvikling af Flask-controllers, modeller, database-skema og import-scripts.
- **ChatGPT **: Diskussion af database-design (E/R-diagram, normalisering vs. denormalisering), fejlfinding af SQL-queries.

### 2. Arbejdsfase (hvornår i processen)
- **Tidlig fase**: Database-design og skema-valg (ChatGPT)
- **Udviklingsfasen**: Daglig kodning i `controllers/`, `models/`, `database.py`, `games_import.py` (Copilot)
- **Dokumentationsfasen**: README.md

### 3. Håndtering af output
- Alt AI-genereret kodes er gennemgået, forstået og ofte redigeret inden det blev pushet.
- SQL-queries og database-skema er valideret mod PostgreSQL-dokumentationen og testet.
- Dokumentation er skrevet/redigeret manuelt baseret på AI-forslag.
- alle designbeslutninger (fx denormalisering af `position_moves`, valg af `position_key`, ±500 rating-vindue) er taget af os efter overvejelse.

---

**NB.** GAI-genereret indhold brugt som kilde i opgaven kræver korrekt brug af citationstegn og kildehenvisning. Læs retningslinjer fra Københavns Universitetsbibliotek på KUnet.
