from flask import Blueprint, jsonify, request, render_template
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

@sensors.route('/register', methods=['POST'])
def register():
    form = SensorForm(request.form)
    if form.validate():
        #sensor = Sensor(sensor_name, "description place holder")
        #db.session.add(sensor)
        #db.session.commit()
        return "valid"
        #return 201 - created
        #return 202 if already exists
    return "invalid", 400


