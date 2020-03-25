from config.mysql_config import set_mysql_config
from DBUtils.PooledDB import PooledDB
import pymysql
__author__ = "zhou"
__date__ = "2019-06-01 21:47"



def create_pool():
    db_config = set_mysql_config("dev")

    return PooledDB(pymysql,
                    5,
                    host=db_config["host"],
                    user=db_config["user"],
                    passwd=db_config["passwd"],
                    db=db_config["db"],
                    port=db_config["port"],
                    charset=db_config["charset"]).connection()