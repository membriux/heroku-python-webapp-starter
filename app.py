# Basic flask imports
from flask import Flask, url_for, render_template, request, session

import os

app = Flask(__name__)
app.secret_key = os.urandom(40)

# Setup site for new users using cookies/sessions
@app.before_request
def setup():
    if 'user' not in session:
        pass # add things to do for each new user


@app.route('/')
def index():
    # set session
    session['user'] = app.secret_key

    return render_template('index.html', name='new user', title='Main Page')


if __name__ == '__main__':
    app.run()
