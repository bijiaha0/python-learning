from crm.shared.models import metadata

__author__ = "zhou"
__date__ = "2019-06-11 20:55"

from flask import Flask
from config import config


def create_app(environment='production'):
    app = Flask(__name__)
    # 添加配置
    app.config.from_object(config[environment])

    # 导入数据库的基本设置，并且加载设置
    from .shared.db import db
    db.init_app(app)
    app.app_context().push()

    # 获取引擎
    metadata.create_all(db.get_engine())

    # 蓝图
    from .api import api_blueprint
    app.register_blueprint(api_blueprint, url_prefix="/api")

    return app


