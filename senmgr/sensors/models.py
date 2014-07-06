from uuid import uuid4, UUID
from datetime import datetime
from . import db


class Timestamp(object):
    created_at = db.Column(db.DateTime, default=datetime.utcnow())
    updated_at = db.Column(db.DateTime, default=datetime.utcnow(), onupdate=datetime.utcnow())


class Sensor(db.Model, Timestamp):
    __tablename__ = "sensors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    key = db.Column(db.String(36), default=str(uuid4()))
    description = db.Column(db.String(255))
    _type = db.Column(db.Integer, db.ForeignKey('type.id'))

    def __init__(self, name, description):
        self.name = name
        self.description = description

    @property
    def uuid(self):
        return UUID(self.key)

    @property
    def serialise(self):
        dic = {}
        for val in [v for v in vars(self) if not v.startswith('_')]:
            dic[val] = getattr(self, val)
        return dic

    def __repr__(self):
        return '<Sensor id:{0} name:{1}>'.format(self.id, self.name)


class Type(db.Model):
    __tablename__ = 'type'

    id = db.Column(db.Integer, primary_key=True)
    _type = db.Column(db.String(), unique=True, nullable=False)

    def __init__(self, _type):
        self._type = _type

    @property
    def serialise(self):
        return {
            'id': self.id,
            'type': self._type
            }

    def __repr__(self):
        return '<Sensor Type id:{0} type:{1}>'.format(self.id, self._type)



