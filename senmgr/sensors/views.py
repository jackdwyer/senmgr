from flask import Blueprint

sensors = Blueprint('sensors', __name__,
    template_folder='templates')

@sensors.route('/')
def index():
    return "sensor blueprint"

@sensors.route('/register')
def register():
    return "basic page to handle sensor registeration"
