from flask import Blueprint, jsonify, request, render_template
from sqlalchemy.orm.exc import NoResultFound
from models import Sensor
from forms import SensorForm
from .utils import json
from . import db

sensors = Blueprint('sensors', __name__,
    template_folder='templates')


@sensors.route('/')
def index():
    return "sensor blueprint"


@sensors.route('/all')
@json
def get_all_sensors():
    return {'sensors': [val.serialise for val in Sensor.query.all()]}


@sensors.route('/register', methods=['POST'])
@json
def register():
    form = SensorForm(request.form)
    if form.validate():
        try:
            sensor = Sensor.query.filter(Sensor.sensor_key == form.data.get('sensor_key')).one()
            return {"sensor_id": str(sensor.id)}, 202
        except NoResultFound:
            sensor = Sensor(form.data.get('sensor_key'), form.data.get('description'))
            db.session.add(sensor)
            db.session.commit()
            return {"sensor_id": str(sensor.id)}, 201
    return {"error": "invalid"}, 400
