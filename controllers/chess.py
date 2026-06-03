from flask import Blueprint, render_template, request
from models.chess_stats import get_best_moves, get_position_key_from_fen

bp = Blueprint('chess', __name__, url_prefix='/')

@bp.route('/chess', methods=['GET', 'POST'])
def chess():
    moves = []
    fen = ""
    my_rating = ""
    opponent_rating = ""
    my_color = "white"

    if request.method == 'POST':
        fen = request.form['fen']
        my_rating = int(request.form['my_rating'])
        opponent_rating = int(request.form['opponent_rating'])
        my_color = request.form['my_color']

        position_key = get_position_key_from_fen(fen)

        moves = get_best_moves(
            position_key,
            my_rating,
            opponent_rating,
            my_color
        )

    return render_template(
        'chess.html',
        moves=moves,
        fen=fen,
        my_rating=my_rating,
        opponent_rating=opponent_rating,
        my_color=my_color
    )