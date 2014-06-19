from flask_wtf import Form
from wtforms.ext.sqlalchemy.orm import model_form
from .models import Sensor

SensorForm = model_form(Sensor)
