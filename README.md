# Chess Statistics Web App

This project is a Flask web application that uses PostgreSQL to find historically successful chess moves based on:

* the moves played so far
* the player's rating
* the opponent's rating
* the player's color

The user can enter chess moves such as:

```text
e4
e4 e5
e4 e5 Nf3
```

The application converts the moves into a chess position, looks up matching positions in the database, and returns the historically best-scoring moves.

---

## 1. Requirements

Before running the project, make sure you have installed:

* Python 3
* Git
* PostgreSQL / pgAdmin
* pip

Optional but recommended:

* pgAdmin for inspecting the PostgreSQL database visually

---

## 2. Clone the project

### Windows PowerShell

```powershell
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME
```

### macOS / Linux

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME
```

Example:

```bash
git clone https://github.com/syllevest/DIS_Project.git
cd DIS_Project
```

---

## 3. Create a virtual environment

### Windows PowerShell

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.venv\Scripts\activate
```

If PowerShell blocks activation, run this first:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

Then activate again:

```powershell
.venv\Scripts\activate
```

### macOS / Linux

```bash
python3 -m venv .venv
```

Activate the virtual environment:

```bash
source .venv/bin/activate
```

When it works, the terminal should show:

```text
(.venv)
```

---

## 4. Install Python packages

### Windows PowerShell

```powershell
pip install flask psycopg2-binary chess
```

### macOS / Linux

```bash
pip install flask psycopg2-binary chess
```

If `pip` does not work on macOS/Linux, try:

```bash
pip3 install flask psycopg2-binary chess
```

---

## 5. Create the PostgreSQL database

The project expects a PostgreSQL database named:

```text
chess
```

---

### Option A: Create the database from the terminal

If PostgreSQL is running on port `2003`, use:

#### Windows PowerShell

```powershell
createdb -U postgres -h 127.0.0.1 -p 2003 chess
```

#### macOS / Linux

```bash
createdb -U postgres -h 127.0.0.1 -p 2003 chess
```

If PostgreSQL uses the default port `5432`, use:

#### Windows PowerShell

```powershell
createdb -U postgres -h 127.0.0.1 -p 5432 chess
```

#### macOS / Linux

```bash
createdb -U postgres -h 127.0.0.1 -p 5432 chess
```

You may be asked for your PostgreSQL password.

---

### Option B: Create the database in pgAdmin

1. Open pgAdmin.
2. Find your PostgreSQL server in the left sidebar.
3. Right-click `Databases`.
4. Select `Create`.
5. Select `Database`.
6. Enter the database name:

```text
chess
```

7. Click `Save`.

---

## 6. Set the database password in the terminal

For security reasons, the database password is not stored directly in the code.

The password is read from an environment variable called:

```text
PGPASSWORD
```

---

### Windows PowerShell

```powershell
$env:PGPASSWORD="YOUR_POSTGRES_PASSWORD"
```

Example:

```powershell
$env:PGPASSWORD="my_password"
```

If your PostgreSQL server uses port `2003`, run:

```powershell
$env:PGPORT="2003"
```

If your PostgreSQL server uses port `5432`, run:

```powershell
$env:PGPORT="5432"
```

---

### macOS / Linux

```bash
export PGPASSWORD="YOUR_POSTGRES_PASSWORD"
```

Example:

```bash
export PGPASSWORD="my_password"
```

If your PostgreSQL server uses port `2003`, run:

```bash
export PGPORT="2003"
```

If your PostgreSQL server uses port `5432`, run:

```bash
export PGPORT="5432"
```

---

The project defaults are:

```text
host: 127.0.0.1
port: 2003
database: chess
user: postgres
```

If your PostgreSQL installation uses the default port `5432`, remember to set:

### Windows PowerShell

```powershell
$env:PGPORT="5432"
```

### macOS / Linux

```bash
export PGPORT="5432"
```

---

## 7. Go into the app folder

### Windows PowerShell

```powershell
cd DIS_Project
```

### macOS / Linux

```bash
cd DIS_Project
```

---

## 8. Create the database tables

The app automatically calls `init_db()` when it starts.

This creates the required tables:

* `games`
* `position_moves`

Start the app once.

### Windows PowerShell

```powershell
python app.py
```

### macOS / Linux

```bash
python3 app.py
```

If `python3` does not work, try:

```bash
python app.py
```

If everything works, you should see something like:

```text
Running on http://127.0.0.1:5000
```

Stop the app again with:

```text
Ctrl + C
```

---

## 9. Import the dataset

The PGN dataset should be located at:

```text
data/sample_500.pgn
```

The project structure should look like this:

```text
DIS_Project/
├── data/
│   └── games.pgn
└── chess_app/
    ├── app.py
    ├── database.py
    └── import_games.py
```

From inside the `DIS_project` folder, run the import script.

### Windows PowerShell

```powershell
python import_games.py
```

### macOS / Linux

```bash
python3 games_import.py
```

If `python3` does not work, try:

```bash
python games_import.py
```

The script reads the PGN file and stores games, positions, moves, ratings, and results in PostgreSQL.

If the import works, the terminal will show something like:

```text
Imported 100 games and 6500 moves
Imported 200 games and 13200 moves
Done
```

---

## 10. Check that the data was imported

Open pgAdmin.

Go to the database:

```text
chess
```

Open the `Query Tool` and run:

```sql
SELECT COUNT(*) FROM games;
```

Then run:

```sql
SELECT COUNT(*) FROM position_moves;
```

If `position_moves` is greater than `0`, the dataset has been imported correctly.

You can also check from the terminal.

### Windows PowerShell

```powershell
psql -U postgres -h 127.0.0.1 -p 2003 -d chess
```

### macOS / Linux

```bash
psql -U postgres -h 127.0.0.1 -p 2003 -d chess
```

Then run:

```sql
SELECT COUNT(*) FROM position_moves;
```

Exit `psql` with:

```sql
\q
```

---

## 11. Start the web app

From the `DIS_Project` folder, run:

### Windows PowerShell

```powershell
python app.py
```

### macOS / Linux

```bash
python3 app.py
```

If `python3` does not work, try:

```bash
python app.py
```

Then open this URL in your browser:

```text
http://127.0.0.1:5000/chess
```

---

## 12. How to use the app

In the field called `Moves played so far`, enter chess moves.

Example:

```text
e4
```

This means:

```text
The position after 1. e4.
It is Black's turn.
```

So choose:

```text
Your color: Black
```

---

Example:

```text
e4 e5
```

This means:

```text
The position after 1. e4 e5.
It is White's turn.
```

So choose:

```text
Your color: White
```

---

Example:

```text
e4 e5 Nf3
```

This means:

```text
The position after 1. e4 e5 2. Nf3.
It is Black's turn.
```

So choose:

```text
Your color: Black
```

---

## 13. Important note about move input

You cannot start with:

```text
e5
```

because White cannot play `e5` as the first move from the starting position.

If you want to analyze the position after Black has played `e5`, enter:

```text
e4 e5
```

---

## 14. Regular expressions

The project uses regular expressions to check whether the user's input looks like valid chess notation.

The regex validates the format of moves such as:

```text
e4
Nf3
Bb5
O-O
Qxe7+
```

After that, the project uses `python-chess` to check whether the moves are actually legal in the current chess position.

In other words:

```text
Regex checks the format.
python-chess checks the legality.
PostgreSQL stores and searches the historical statistics.
```

---

## 15. Common errors

### Error: database "chess" does not exist

Create the database.

#### Windows PowerShell

```powershell
createdb -U postgres -h 127.0.0.1 -p 2003 chess
```

#### macOS / Linux

```bash
createdb -U postgres -h 127.0.0.1 -p 2003 chess
```

Or create the database manually in pgAdmin.

---

### Error: no password supplied

Set the PostgreSQL password.

#### Windows PowerShell

```powershell
$env:PGPASSWORD="YOUR_POSTGRES_PASSWORD"
python app.py
```

#### macOS / Linux

```bash
export PGPASSWORD="YOUR_POSTGRES_PASSWORD"
python3 app.py
```

---

### Error: connection refused

This usually means PostgreSQL is not running on the port the app is using.

Check the port in pgAdmin under the server properties.

If PostgreSQL uses port `5432`, run:

#### Windows PowerShell

```powershell
$env:PGPORT="5432"
```

#### macOS / Linux

```bash
export PGPORT="5432"
```

If PostgreSQL uses port `2003`, run:

#### Windows PowerShell

```powershell
$env:PGPORT="2003"
```

#### macOS / Linux

```bash
export PGPORT="2003"
```

---

### No results found

Possible causes:

1. The dataset has not been imported.
2. The `position_moves` table is empty.
3. The rating filter does not match any games.
4. The wrong color was selected.
5. The dataset does not contain games with the selected position.

Check the database:

```sql
SELECT COUNT(*) FROM position_moves;
```

---

## 16. Full setup from start to finish

### Windows PowerShell

```powershell
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME

python -m venv .venv
.venv\Scripts\activate

pip install flask psycopg2-binary chess

createdb -U postgres -h 127.0.0.1 -p 2003 chess

$env:PGPASSWORD="YOUR_POSTGRES_PASSWORD"
$env:PGPORT="2003"

cd chess_app

python app.py
```

Stop the app with:

```text
Ctrl + C
```

Import the dataset:

```powershell
python import_games.py
```

Start the app again:

```powershell
python app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000/chess
```

---

### macOS / Linux

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPOSITORY-NAME.git
cd YOUR-REPOSITORY-NAME

python3 -m venv .venv
source .venv/bin/activate

pip install flask psycopg2-binary chess

createdb -U postgres -h 127.0.0.1 -p 2003 chess

export PGPASSWORD="YOUR_POSTGRES_PASSWORD"
export PGPORT="2003"

cd chess_app

python3 app.py
```

Stop the app with:

```text
Ctrl + C
```

Import the dataset:

```bash
python3 import_games.py
```

Start the app again:

```bash
python3 app.py
```

Open the app in your browser:

```text
http://127.0.0.1:5000/chess
```

---

## 17. Notes for GitHub

Do not commit real passwords to GitHub.

The database password should be set through an environment variable.

### Windows PowerShell

```powershell
$env:PGPASSWORD="YOUR_POSTGRES_PASSWORD"
```

### macOS / Linux

```bash
export PGPASSWORD="YOUR_POSTGRES_PASSWORD"
```

The `.gitignore` file should include:

```text
.venv/
__pycache__/
*.pyc
.env
```

If the PGN dataset is large, it should usually not be committed to GitHub.

If your project requires the dataset to be included, make sure the file path matches:

```text
data/games.pgn
```
