__author__ = "zhou"
__date__ = "2019-06-11 20:57"

class Config:
    DEBUG = True
    # 数据库的参数设置
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://192.168.1.35/my_test_db?user=admin&password=123456'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 连接池的设置
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOUT = 10
    SQLALCHEMY_POOL_RECYCLE = 10

    @staticmethod
    def init_app(app):
        pass



class TestConfig:
    DEBUG = True
    # 数据库的参数设置
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://192.168.1.35/my_test_db?user=admin&password=123456'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # 连接池的设置
    SQLALCHEMY_POOL_SIZE = 10
    SQLALCHEMY_POOL_TIMEOURT = 10
    SQLALCHEMY_POOL_RECYCLE = 10



config = {
    "production": Config,
    "testing": TestConfig
}







