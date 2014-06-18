from gevent import monkey
monkey.patch_all()
from threading import Thread
from flask import render_template
from flask.ext.socketio import emit
from sensors.comms import subscribe, get_sensor_list
from . import app, con, ws

@app.route('/')
def index():
    Thread(target=subscribe, args=[con, get_sensor_list(con), ws]).start()
    return render_template('index.html')

@ws.on('disconnected')
def on_disconnect():
    print 'Client disconnected'

@ws.on('connect')
def on_connect():
    emit('my response', {'data': 'connected'}) #, 'count': 0})

