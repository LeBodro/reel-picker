from flask import Flask, redirect, url_for, session
import sqlite3
import hashlib
import os


app = Flask(__name__)
app.secret_key = os.urandom(12)


def login(username:str, password:str):
    if session.get('logged_in'):
        return redirect(url_for('hello'))

    username = username
    password = password
    validate(username, password)


def logged_in():
    return session.get('logged_in')


def logout():
    session['logged_in'] = False


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
