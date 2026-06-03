import chess.pgn
from database import db_connection


PGN_FILE = "/data/sample_500.pgn"


def position_key_from_board(board):
    fen = board.fen()
    parts = fen.split(" ")
    return " ".join(parts[:4])


def insert_game(cur, lichess_id, white_elo, black_elo, result, pgn_text):
    cur.execute(
        """
        INSERT INTO games (
            lichess_id,
            white_elo,
            black_elo,
            result,
            pgn
        )
        VALUES (%s, %s, %s, %s, %s)
        ON CONFLICT (lichess_id) DO NOTHING
        RETURNING id
        """,
        (lichess_id, white_elo, black_elo, result, pgn_text)
    )

    row = cur.fetchone()

    if row:
        return row[0]

    cur.execute(
        "SELECT id FROM games WHERE lichess_id = %s",
        (lichess_id,)
    )

    return cur.fetchone()[0]


def insert_position_move(
    cur,
    game_id,
    position_key,
    move_uci,
    move_san,
    white_elo,
    black_elo,
    result
):
    cur.execute(
        """
        INSERT INTO position_moves (
            game_id,
            position_key,
            move_uci,
            move_san,
            white_elo,
            black_elo,
            result
        )
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            game_id,
            position_key,
            move_uci,
            move_san,
            white_elo,
            black_elo,
            result
        )
    )


def import_games():
    conn = db_connection()
    cur = conn.cursor()

    imported_games = 0
    imported_moves = 0

    with open(PGN_FILE, encoding="utf-8") as pgn:
        while True:
            game = chess.pgn.read_game(pgn)

            if game is None:
                break

            headers = game.headers

            lichess_id = headers.get("Site", f"unknown_{imported_games}")
            white_elo = headers.get("WhiteElo")
            black_elo = headers.get("BlackElo")
            result = headers.get("Result")

            if white_elo is None or black_elo is None:
                continue

            if result not in ["1-0", "0-1", "1/2-1/2"]:
                continue

            try:
                white_elo = int(white_elo)
                black_elo = int(black_elo)
            except ValueError:
                continue

            pgn_text = str(game)

            game_id = insert_game(
                cur,
                lichess_id,
                white_elo,
                black_elo,
                result,
                pgn_text
            )

            board = game.board()

            for move in game.mainline_moves():
                position_key = position_key_from_board(board)
                move_uci = move.uci()
                move_san = board.san(move)

                insert_position_move(
                    cur,
                    game_id,
                    position_key,
                    move_uci,
                    move_san,
                    white_elo,
                    black_elo,
                    result
                )

                board.push(move)
                imported_moves += 1

            imported_games += 1

            if imported_games % 100 == 0:
                conn.commit()
                print(f"Imported {imported_games} games and {imported_moves} moves")

    conn.commit()
    cur.close()
    conn.close()

    print("Done")
    print(f"Imported games: {imported_games}")
    print(f"Imported moves: {imported_moves}")


if __name__ == "__main__":
    import_games()
