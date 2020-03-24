__author__ = "zhou"
__date__ = "2019-06-01 21:43"

def set_mysql_config(environment):
    if environment == "dev":
        db_config = {
            'host': "192.168.1.35",
            "user": "admin",
            "passwd": "123456",
            "db": "python_ai_basic",
            "port": 3306,
            "charset": "utf8"
        }

    if environment == "pro":
        db_config = {
            'host': "192.168.1.35",
            "user": "admin",
            "passwd": "123456",
            "db": "python_ai_basic",
            "port": 3306,
            "charset": "utf8"
        }
    return db_config
