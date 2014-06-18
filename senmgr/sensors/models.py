from . import db
class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    sensor_key = db.Column(db.String(50), unique=True)
    description = db.Column(db.String(255))

    def __init__(self, sensor_key, description):
        self.sensor_key = sensor_key
        self.description = description

    @property
    def serialise(self):
        return {
            'id': self.id,
            'sensor_key': self.sensor_key,
            'description': self.description
            }

    def __repr__(self):
        return '<Sensor id:{0} key:{1}>'.format(self.id, self.sensor_key)
    
