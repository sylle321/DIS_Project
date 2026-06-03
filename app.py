from flask import Flask
from database import init_db
from controllers.chess import bp as chess_bp

init_db()

app = Flask(__name__)


@app.route("/")
def hello_world():
    return '<a href="/chess">Go to chess app</a>'


app.register_blueprint(chess_bp)


if __name__ == "__main__":
    app.run(debug=True)