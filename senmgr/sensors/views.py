from flask import Blueprint, jsonify
from .models import Sensor
from . import db

sensors = Blueprint('sensors', __name__,
    template_folder='templates')

@sensors.route('/')
def index():
    return "sensor blueprint"

#basic register function
@sensors.route('/register/<sensor_name>')
def register(sensor_name):
    sensor = Sensor(sensor_name, "description place holder")
    db.session.add(sensor)
    db.session.commit()
    return "Sensor: {0} added".format(sensor_name) 

@sensors.route('/all')
def get_all_sensors():
    return jsonify(sensors=[val.serialise for val in Sensor.query.all()])
