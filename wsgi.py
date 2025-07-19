from flask import Flask, render_template, request
from game import Game
from wsgi import app

app = Flask(__name__)

@app.route('/')
def home():
    game = Game()
    return render_template('home.html', grid=game.grid)

@app.route('/check', methods=["POST"])
def check():
    game = Game()
    game.grid = list(request.form['grid'])
    word = request.form['word']
    is_valid = game.is_valid(word)
    return render_template('check.html', is_valid=is_valid, grid=game.grid, word=word)

if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process will serve the app
    app.run(host='127.0.0.1', port=8080, debug=True)