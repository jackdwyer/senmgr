import requests
import json
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
data = "{u'data': {u'sensors': [{u'sensor_key': u'test_sensor_unittest', u'description': u'', u'id': 1}]}}"
r = requests.post("http://localhost:5000/sensor/load", data=json.dumps(data), headers=headers)
