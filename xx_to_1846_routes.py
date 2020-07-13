from app import app

if __name__ == '__main__':
    app.run()


"""
from flask import Flask, render_template, request, redirect

app = Flask(__name__)


@app.route('/', methods=('GET', 'POST'))
def xx_to_1846_routes():
    if request.method == 'POST':
        game_data = request.form['game-data']
        print(game_data)
        return redirect(request.url)

    return render_template('index.html')


if __name__ == '__main__':
    app.run()
"""