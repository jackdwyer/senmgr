from functools import wraps
from flask import jsonify


def json(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        ret_val = func(*args, **kwargs)
        if len(ret_val) == 2:
            return jsonify({"data": ret_val[0]}), ret_val[1]
        return jsonify({"data": ret_val})
    return wrapper
