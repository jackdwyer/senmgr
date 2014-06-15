def get_sensor_list(redis):
    #TODO return list of sensors that have been registered
    sensor_list = ['test']
    return sensor_list

def subscribe(redis, sensor_list, ws):
    r = redis.pubsub()
    r.subscribe(sensor_list)
    for item in r.listen():
        ws.emit('sensor_data',
                        {'data': item['data'], 'type':'sensor'})
