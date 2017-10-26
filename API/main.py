from flask import Flask, render_template, redirect, url_for, request, session
import sqlite3, hashlib, os

app = Flask(__name__)
app.secret_key = os.urandom(12)


# Go to login page
@app.route('/', methods=['GET', 'POST'])
def login():
    # already logged ?
    if session.get('logged_in'):
        return redirect(url_for('hello'))
    error = None
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        completion = validate(username, password)
        if completion ==False:
            error = 'Identifiants incorrect, merci de ressayer.'
        else:
            session['logged_in'] = True
            return redirect(url_for('hello'))
    return render_template('login.html', error=error, connected=False)


@app.route('/logout')
def logout():
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        session['logged_in'] = False
        return redirect(url_for('login'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('hello.html', name=name)


# TODO change this into an other file
# CHECK the user imput with the db value
def validate(username, password):
    con = sqlite3.connect('static/user.db')
    completion = False
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM Users")
        rows = cur.fetchall()
        for row in rows:
            db_user = row[0]
            db_pass = row[1]
            if db_user == username:
                completion=check_password(db_pass, password)
    return completion


def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()
