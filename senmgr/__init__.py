from gevent import monkey
monkey.patch_all()
from flask import Flask
from flask.ext.socketio import SocketIO
from flask.ext.sqlalchemy import SQLAlchemy
import redis
from config import Default

app = Flask(__name__)
app.config.from_object(Default)
con = redis.StrictRedis()

ws = SocketIO(app)

db = SQLAlchemy()

from . import views
from sensors import models
