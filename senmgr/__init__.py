from gevent import monkey
monkey.patch_all()
from flask import Flask
from flask.ext.socketio import SocketIO
import redis

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev'
con = redis.StrictRedis()

ws = SocketIO(app)

from . import views
