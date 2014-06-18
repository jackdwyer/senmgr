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

db = SQLAlchemy(app)

from . import views

from sensors.models import Sensor
from sensors.views import sensors
app.register_blueprint(sensors, url_prefix='/sensor')
