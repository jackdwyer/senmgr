import requests
data = {"sensor_key":"test_senagaagaga"}

r = requests.post("http://localhost:5000/sensor/register", data=data)
print r.text
import redis
import time
sen1 = {"sensor_key":"test_ssensor", "description":"hey im a sensor"}
sen2 = {"sensor_key":"test_2", "description":"hey im a sensor"}
requests.post("http://localhost:5000/sensor/register", data=sen1)
requests.post("http://localhost:5000/sensor/register", data=sen2)

r = redis.Redis()
i = 0
j = 10000000000000
while True:
    r.publish(sen1["sensor_key"], str(i))
    r.publish(sen2["sensor_key"], str(j))
    i += 1
    j -= 1
    time.sleep(0.1)


print r.text

