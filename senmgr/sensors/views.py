from flask import Blueprint, jsonify, request
from models import Sensor
from forms import SensorForm
from . import db

sensors = Blueprint('sensors', __name__,
    template_folder='templates')

@sensors.route('/')
def index():
    return "sensor blueprint"

@sensors.route('/all')
def get_all_sensors():
    return jsonify(sensors=[val.serialise for val in Sensor.query.all()])

@sensors.route('/register/<sensor_name>', methods=['POST'])
def register(sensor_name):
    form = SensorForm(request.form)
    if form.validate():
        return "Sensor: {0} added".format(sensor_name)
    #sensor = Sensor(sensor_name, "description place holder")
    #db.session.add(sensor)
    #db.session.commit()
    return "nope" 


