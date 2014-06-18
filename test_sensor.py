import redis
import time
r = redis.Redis()
i = 0
while True:
    r.publish('test', str(i))
    i += 1
    time.sleep(0.1)
