import requests
data = {"sensor_key":"test_senagaagaga"}

r = requests.post("http://localhost:5000/sensor/register", data=data)
print r.text
#import redis
#import time
#r = redis.Redis()
#i = 0
#while True:
#    r.publish('test', str(i))
#    i += 1
#    time.sleep(0.1)
