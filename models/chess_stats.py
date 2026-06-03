from database import db_connection
import chess
import re


class MoveStat:
    def __init__(self, move_uci, move_san, games, wins, draws, losses, score):
        self.move_uci = move_uci
        self.move_san = move_san
        self.games = games
        self.wins = wins
        self.draws = draws
        self.losses = losses
        self.score = score


def get_position_key_from_fen(fen):
    parts = fen.split(" ")
    return " ".join(parts[:4])


def validate_moves_with_regex(moves_text):
    moves_text = moves_text.strip()

    if moves_text == "":
        return True

    move_pattern = r"^(O-O-O|O-O|[KQRBN]?[a-h]?[1-8]?x?[a-h][1-8](=[QRBN])?[+#]?)$"

    moves = moves_text.split()

    for move in moves:
        if not re.match(move_pattern, move):
            return False

    return True


def get_position_key_from_moves(moves_text):
    board = chess.Board()

    moves_text = moves_text.strip()

    if moves_text == "":
        return get_position_key_from_fen(board.fen())

    if not validate_moves_with_regex(moves_text):
        raise ValueError("Input contains invalid chess notation")

    moves = moves_text.split()

    for move_text in moves:
        board.push_san(move_text)

    return get_position_key_from_fen(board.fen())


def get_best_moves(position_key, my_rating, opponent_rating, my_color):
    conn = db_connection()
    cur = conn.cursor()

    my_min = my_rating - 500
    my_max = my_rating + 500

    opponent_min = opponent_rating - 500
    opponent_max = opponent_rating + 500

    if my_color == "white":
        query = """
            SELECT
                move_uci,
                move_san,
                COUNT(*) AS games,

                SUM(CASE WHEN result = '1-0' THEN 1 ELSE 0 END) AS wins,
                SUM(CASE WHEN result = '1/2-1/2' THEN 1 ELSE 0 END) AS draws,
                SUM(CASE WHEN result = '0-1' THEN 1 ELSE 0 END) AS losses,

                (
                    SUM(
                        CASE
                            WHEN result = '1-0' THEN 1
                            WHEN result = '1/2-1/2' THEN 0.5
                            ELSE 0
                        END
                    )::float / COUNT(*)
                ) AS score

            FROM position_moves
            WHERE position_key = %s
              AND white_elo BETWEEN %s AND %s
              AND black_elo BETWEEN %s AND %s

            GROUP BY move_uci, move_san
            HAVING COUNT(*) >= 1
            ORDER BY score DESC, games DESC
            LIMIT 10
        """

        values = (
            position_key,
            my_min,
            my_max,
            opponent_min,
            opponent_max
        )

    else:
        query = """
            SELECT
                move_uci,
                move_san,
                COUNT(*) AS games,

                SUM(CASE WHEN result = '0-1' THEN 1 ELSE 0 END) AS wins,
                SUM(CASE WHEN result = '1/2-1/2' THEN 1 ELSE 0 END) AS draws,
                SUM(CASE WHEN result = '1-0' THEN 1 ELSE 0 END) AS losses,

                (
                    SUM(
                        CASE
                            WHEN result = '0-1' THEN 1
                            WHEN result = '1/2-1/2' THEN 0.5
                            ELSE 0
                        END
                    )::float / COUNT(*)
                ) AS score

            FROM position_moves
            WHERE position_key = %s
              AND black_elo BETWEEN %s AND %s
              AND white_elo BETWEEN %s AND %s

            GROUP BY move_uci, move_san
            HAVING COUNT(*) >= 1
            ORDER BY score DESC, games DESC
            LIMIT 10
        """

        values = (
            position_key,
            my_min,
            my_max,
            opponent_min,
            opponent_max
        )

    print("POSITION KEY:", position_key)
    print("SQL VALUES:", values)

    cur.execute(query, values)
    rows = cur.fetchall()

    moves = []

    for row in rows:
        moves.append(
            MoveStat(
                move_uci=row[0],
                move_san=row[1],
                games=row[2],
                wins=row[3],
                draws=row[4],
                losses=row[5],
                score=round(row[6] * 100, 2)
            )
        )

    cur.close()
    conn.close()

    return moves
