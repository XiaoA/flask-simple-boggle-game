from flask import Flask, request, render_template, session
from boggle import Boggle

app = Flask(__name__)
app.config["SECRET_KEY"] = "nam6a3das7xma"

boggle_game = Boggle()


@app.route("/")
def homepage():
    """Display board."""

    board = boggle_game.make_board()
    session['board'] = board
    highscore = session.get("highscore", 0)
    nplays = session.get("nplays", 0)

    return render_template("index.html", board=board,
                           highscore=highscore,
                           nplays=nplays)
