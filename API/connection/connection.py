"""
    Connection functions
"""
import sqlite3
import hashlib
from flask import session

def logged_in():
    return session.get('logged_in')

def log_in():
    session['logged_in'] = True

def logout():
    session['logged_in'] = False


def validate(username, password):
    con = sqlite3.connect("User.db")
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
