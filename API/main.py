from flask import Flask, render_template, redirect, url_for, request, session
import hashlib, os
import connection

app = Flask(__name__)
app.secret_key = os.urandom(12)


# Go to login page
@app.route('/', methods=['GET', 'POST'])
def login():
    if connection.logged_in():
        return redirect(url_for('hello'))

    error = None
    if request.method == 'POST':        
        if connection.validate(request.form['username'], request.form['password']) is False:
            error = "Nom d'utilisateur ou mot de passe incorrect. Merci de reessayer."
        else:
            connection.log_in()
            return redirect(url_for('hello'))

    return render_template('login.html', error=error, connected=True)


@app.route('/logout')
def logout():
    connection.logout()
    return redirect(url_for('login'))


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    if not session.get('logged_in'):
        return redirect(url_for('login'))
    else:
        return render_template('hello.html', name=name)


def check_password(hashed_password, user_password):
    return hashed_password == hashlib.md5(user_password.encode()).hexdigest()

if __name__ == '__main__':
    app.run()