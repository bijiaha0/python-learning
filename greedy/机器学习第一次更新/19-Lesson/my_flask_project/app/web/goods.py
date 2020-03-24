from flask import jsonify, Blueprint

__author__ = "zhou"
__date__ = "2019-06-06 21:37"

# 实例化蓝图对象。
web = Blueprint('web', __name__)


@web.route("/getgoods")
def get_goods():
    result = {
        "computer": 9800,
        "brand": 1.8
    }

    return jsonify(result)



