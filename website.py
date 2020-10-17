from cheroot.wsgi import Server as WSGIServer
from credentials import flask_app_secret
from flask import Flask, render_template

app = Flask(__name__, static_url_path='')

app.secret_key = flask_app_secret


@app.route('/')
def mainpage():
    return render_template('mainpage.html')


@app.route('/prices')
def prices():
    return render_template('mainpage-2.html')


@app.route('/order')
def order():
    return render_template('mainpage-3.html')


server = WSGIServer(bind_addr=('0.0.0.0', 8021), wsgi_app=app, numthreads=1)
try:
    server.start()
except KeyboardInterrupt:
    server.stop()
except Exception as e:
    print(e)
