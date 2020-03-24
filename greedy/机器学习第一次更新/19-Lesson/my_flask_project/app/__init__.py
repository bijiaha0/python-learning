__author__ = "zhou"
__date__ = "2019-06-06 21:34"

from flask import Flask
from app.models.user import db

def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    #  蓝图注册
    register_buleprint(app)

    # 数据库的初始化
    db.init_app(app)
    db.create_all(app=app)
    return app


def register_buleprint(app):
    from app.web.goods import web
    from app.api import api

    app.register_blueprint(web)
    app.register_blueprint(api)
