from gevent import monkey
monkey.patch_all()
from threading import Thread
import unittest
import requests
import os

from senmgr import app, db, ws
try:
    os.remove('/tmp/unittest-senmgr.db')
except OSError:
    pass

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:////tmp/unittest-senmgr.db'
db.create_all()

Thread(target=ws.run, args=[app]).start()

class CreateSensor(unittest.TestCase):
    def test_create_sensor(self):
        data = {"sensor_key":"test_sensor_unittest"}
        r = requests.post("http://localhost:5000/sensor/register", data=data)
        self.assertEqual(r.status_code, 201)    

    def test_duplicate_sensor(self):
        data = {"sensor_key":"test_sensor_unittest"}
        r = requests.post("http://localhost:5000/sensor/register", data=data)
        self.assertEqual(r.status_code, 202)    

        

if __name__ == "__main__":
    print dir(ws)
    unittest.main()
    exit()
    

