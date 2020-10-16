from credentials import flask_app_secret
from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

app.secret_key = flask_app_secret


@app.route('/')
def mainpage():
    return render_template('mainpage.html')


app.run(host='0.0.0.0', port=5000, debug=True)
