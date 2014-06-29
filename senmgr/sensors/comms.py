from models import Sensor


def get_sensor_list(redis):
    return [val.sensor_key for val in Sensor.query.all()]


def subscribe(redis, sensor_list, ws):
    r = redis.pubsub()
    r.subscribe(sensor_list)
    for item in r.listen():
        print item
        ws.emit('sensor_data',
                        {'data': item['data'], 'type':item['channel']})
