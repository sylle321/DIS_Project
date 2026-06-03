import psycopg2
import os

user = os.environ.get("PGUSER", "postgres")
password = os.environ.get("PGPASSWORD", "")
host = os.environ.get("HOST", "127.0.0.1")
port = os.environ.get("PGPORT", "port")
dbname = os.environ.get("PGDATABASE", "chess")


def db_connection():
    return psycopg2.connect(
        dbname=dbname,
        user=user,
        host=host,
        port=port,
        password=password
    )


def init_db():
    conn = db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS games (
            id SERIAL PRIMARY KEY,
            lichess_id TEXT UNIQUE,
            white_elo INTEGER,
            black_elo INTEGER,
            result TEXT NOT NULL,
            pgn TEXT
        )
    """)

    cur.execute("""
        CREATE TABLE IF NOT EXISTS position_moves (
            id SERIAL PRIMARY KEY,
            game_id INTEGER REFERENCES games(id),
            position_key TEXT NOT NULL,
            move_uci TEXT NOT NULL,
            move_san TEXT,
            white_elo INTEGER,
            black_elo INTEGER,
            result TEXT NOT NULL
        )
    """)

    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_position_moves_position
        ON position_moves(position_key)
    """)

    cur.execute("""
        CREATE INDEX IF NOT EXISTS idx_position_moves_ratings
        ON position_moves(white_elo, black_elo)
    """)

    conn.commit()
    cur.close()
    conn.close()
    
