import sqlite3
from GetCardImg import getImg
from flask import Flask, render_template, request, url_for, flash, redirect
import webbrowser
from werkzeug.exceptions import abort

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

def get_card(card_id):
    conn = get_db_connection()
    card = conn.execute('SELECT * FROM cards WHERE id = ?',
                        (card_id,)).fetchone()
    conn.close()
    if card is None:
        abort(404)
    return card

app = Flask(__name__)
app.config['SECRET_KEY'] = 'very_secret_key'

@app.route('/')
def index():
    conn = get_db_connection()
    cards = conn.execute('SELECT * FROM cards').fetchall()
    conn.close()
    return render_template('index.html', cards=cards)

@app.route('/<int:card_id>')
def card(card_id):
    card = get_card(card_id)
    return render_template('card.html', card=card)

@app.route('/create', methods=('GET', 'POST'))
def create():
    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        url = request.form['url']

        if not name:
            flash('Card name is required!')
        if not url:
            flash('Card url is required !')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO cards (name, status, link, img) VALUES (?, ?, ?, ?)',
                         (name, status, url, getImg(url)))
            conn.commit()
            conn.close()
            flash('"{}" was successfully deleted!'.format(name), 'info')
            return redirect(url_for('index'))
    return render_template('create.html')

@app.route('/<int:id>/edit', methods=('GET', 'POST'))
def edit(id):
    card = get_card(id)

    if request.method == 'POST':
        name = request.form['name']
        status = request.form['status']
        url = request.form['url']
        price = request.form['price']

        if not name:
            flash('Card name is required !')
        if not url:
            flash('Card url is required !')
        else:
            conn = get_db_connection()
            conn.execute('UPDATE cards SET name = ?, status = ?, link = ?, img = ?, price = ?'
                         ' WHERE id = ?',
                         (name, status, url, getImg(url), price, id))
            conn.commit()
            conn.close()
            return redirect(url_for('card', card_id=card['id']))

    return render_template('edit.html', card=card)

@app.route('/<int:id>/delete', methods=('POST',))
def delete(id):
    card = get_card(id)
    conn = get_db_connection()
    conn.execute('DELETE FROM cards WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('"{}" was successfully deleted!'.format(card['name']), 'info')
    return redirect(url_for('index'))

webbrowser.open_new("http://127.0.0.1:5000")
app.run()