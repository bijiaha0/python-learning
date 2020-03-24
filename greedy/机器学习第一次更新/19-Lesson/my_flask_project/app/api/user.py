from flask import jsonify, Blueprint

from app.forms.user import UserForm

__author__ = "zhou"
__date__ = "2019-06-06 21:37"

# 实例化蓝图对象。
# user = Blueprint('user', __name__)
from . import api
#
@api.route("/users")
def users():
    result = {
        "computer": 123123,
        "brand": 123123123.8
    }

    return jsonify(result)

from flask import request
@api.route("/login")
def login():

    username = request.args["username"]
    print(username)

    result = {
        "computer": 123123,
        "brand": 123123123.8
    }

    return jsonify(result)

@api.route("/login2")
def login2():

    # username = request.args["username"]
    # print(username)
    form = UserForm(request.args)

    if form.validate():
        username = form.username.data.strip()
        print(username)
        result = {
            "status": 2001,
            "message": "校验通过"
        }
        return jsonify(result)
    else:
        return jsonify(form.errors)

from app.models.user import db,User

@api.route("/getUserInfo", methods = ["GET","POST"])
def get_user_info():
    if request.method == "GET":
        form = UserForm(request.args)
    #     数据库的链接
        user = db.session.query(User).filter(User.user_name == form.username.data.strip()).first()
        print(user.user_name)
        print(user.id)

    if request.method == "POST":
        print("POST请求来了")
        print(request.json)
        user = db.session.query(User).filter(User.user_name == request.json["username"]).first()
        print(user.id)



    return "这把有效了"

