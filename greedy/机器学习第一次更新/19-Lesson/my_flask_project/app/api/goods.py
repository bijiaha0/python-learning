from flask import jsonify, Blueprint

__author__ = "zhou"
__date__ = "2019-06-06 21:37"

# 实例化蓝图对象。
# api = Blueprint('api', __name__)
#
from . import api

@api.route("/goods")
def goods():
    result = {
        "computer": 1119800,
        "brand": 11111.8
    }

    return jsonify(result)



