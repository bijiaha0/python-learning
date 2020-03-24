from crm.api.user_api import User, UserList

__author__ = "zhou"
__date__ = "2019-06-11 21:14"

from flask import Blueprint
from flask_restful import Api


def register_views(app):
    api = Api(app)
    api.add_resource(User, "/user")
    api.add_resource(UserList, "/users")


api_blueprint = Blueprint("api", __name__)
register_views(api_blueprint)

# 导入视图函数模块
from . import user_api


