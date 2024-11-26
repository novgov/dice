import json
import random
import shelve
import secrets
from datetime import datetime

from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)

app.secret_key = secrets.token_hex(16)


def random_dice():
    return str(random.randint(1, 6))


db = shelve.open('users.db')


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        username = request.form['username']
        date = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S")
        db[username] = date
        flash(f'Пользователь {username} сохранен {date}')
        return redirect(url_for('index'))
    return render_template('index.html')


@app.route('/roll', methods=['GET'])
def roll():
    return random_dice()


if __name__ == "__main__":
    app.run(debug=True, port=5000)

