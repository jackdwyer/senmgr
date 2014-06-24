from gevent import monkey
monkey.patch_all()
from threading import Thread
import unittest
import requests
import os

from senmgr import app, db, ws

app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///memory'
app.config["DEBUG"] = False 
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

    def test_kill_server(self):
        requests.get("http://localhost:5000/die")

        

if __name__ == "__main__":
    unittest.main()
    

