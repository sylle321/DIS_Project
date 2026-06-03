from flask import Blueprint, render_template, request
from models.chess_stats import get_best_moves, get_position_key_from_moves

bp = Blueprint('chess', __name__, url_prefix='/')


@bp.route('/chess', methods=['GET', 'POST'])
def chess():
    moves = []
    moves_text = ""
    my_rating = ""
    opponent_rating = ""
    my_color = "white"
    error = ""

    if request.method == 'POST':
        moves_text = request.form['moves_text']
        my_rating = int(request.form['my_rating'])
        opponent_rating = int(request.form['opponent_rating'])
        my_color = request.form['my_color']

        try:
            position_key = get_position_key_from_moves(moves_text)

            moves = get_best_moves(
                position_key,
                my_rating,
                opponent_rating,
                my_color
            )

        except ValueError:
            error = "Ugyldigt træk. Prøv fx: e4, e4 e5 eller e4 e5 Nf3"

    return render_template(
        'chess.html',
        moves=moves,
        moves_text=moves_text,
        my_rating=my_rating,
        opponent_rating=opponent_rating,
        my_color=my_color,
        error=error
    )
