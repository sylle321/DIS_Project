# Chess Statistics Web App

A small Flask web app that uses a PostgreSQL database to recommend chess moves based on historical game statistics.

The included sample dataset is:

```text
data/sample_500.pgn
```

## Requirements

Install these before running the project:

- Python 3
- pip
- PostgreSQL
- Git

## Setup

Clone the repository and enter the project folder:

```bash
git clone https://github.com/sylle321/DIS_Project.git
cd DIS_Project
```

Create and activate a virtual environment.

### Windows PowerShell

Create the virtual environment:

```powershell
python -m venv .venv
```

Activate it:

```powershell
.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation with an execution policy error, run:

```powershell
Set-ExecutionPolicy -ExecutionPolicy Unrestricted -Scope Process
```

Then activate it again:

```powershell
.venv\Scripts\Activate.ps1
```

### macOS / Linux

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install flask psycopg2-binary chess
```

## Start PostgreSQL

Before creating the database, the PostgreSQL server must be running.

### Windows

Open **Services**, find the PostgreSQL service, and click **Start**.

The service is usually called something like:

```text
postgresql-x64-16
```

If PostgreSQL was installed with pgAdmin, opening pgAdmin can also help confirm whether the server is running.

### macOS with Postgres.app

Open **Postgres.app** and make sure the server is running.

### macOS with Homebrew

```bash
brew services start postgresql
```

If that does not work, try the versioned service name, for example:

```bash
brew services start postgresql@16
```

### Linux

```bash
sudo service postgresql start
```

or:

```bash
sudo systemctl start postgresql
```

## Database setup

Create a PostgreSQL database called `chess`.

Set your PostgreSQL password and port before running the app.

Use port `2003` if that is your PostgreSQL port, otherwise use `5432`.

### Windows PowerShell

```powershell
$env:PGPASSWORD="YOUR_POSTGRES_PASSWORD"
$env:PGPORT="2003"
```

For default PostgreSQL port:

```powershell
$env:PGPORT="5432"
```

Create the database:

```powershell
createdb -U postgres -h 127.0.0.1 -p $env:PGPORT chess
```
If PowerShell says that `createdb` is not recognized, create the database manually in pgAdmin instead:

1. Open pgAdmin.
2. Right-click `Databases`.
3. Click `Create` > `Database`.
4. Name the database `chess`.
5. Click `Save`.

Then continue with the next step.

If the database already exists, continue to the next step.

### macOS / Linux

```bash
export PGPASSWORD="YOUR_POSTGRES_PASSWORD"
export PGPORT="2003"
```

For default PostgreSQL port:

```bash
export PGPORT="5432"
```

Create the database:

```bash
createdb -U postgres -h 127.0.0.1 -p $PGPORT chess
```

If the database already exists, continue to the next step.

## Create tables

Run the app once. It automatically creates the database tables.

### Windows PowerShell

```powershell
pip install flask
pip install psycopg2-binary
pip install chess
flask run --debug
```

### macOS / Linux

```bash
python3 app.py
```

When you see something like this, stop the app with `Ctrl + C`:

```text
Running on http://127.0.0.1:5000
```

## Import sample data

From the project root folder, run:

### Windows PowerShell

```powershell
python games_import.py
```

### macOS / Linux

```bash
python3 games_import.py
```

This imports the games from:

```text
data/sample_500.pgn
```

## Run the app

Start the app again:

### Windows PowerShell

```powershell
python app.py
```

### macOS / Linux

```bash
python3 app.py
```

Open in browser:

```text
http://127.0.0.1:5000/chess
```

## Test inputs

Try these move sequences:

```text
e4
e4 e5
e4 e5 Nf3
```

Choose the color whose move should be recommended.

Examples:

- `e4` means Black is to move.
- `e4 e5` means White is to move.
- `e4 e5 Nf3` means Black is to move.

## Check database content

You can check that data was imported with:

### Windows PowerShell

```powershell
psql -U postgres -h 127.0.0.1 -p $env:PGPORT -d chess
```

### macOS / Linux

```bash
psql -U postgres -h 127.0.0.1 -p $PGPORT -d chess
```

Then run:

```sql
SELECT COUNT(*) FROM games;
SELECT COUNT(*) FROM position_moves;
```

Exit with:

```sql
\q
```
