import logging

# 1、debug 调试级别的日志
# 2、info   信息级别的日志
# 3、warning  警告级别的日志
# 4、error    错误级别的日志
# logging.basicConfig(level=logging.DEBUG)
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")


# LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
# DATE_FORMAT = "%Y/%m/%d %H:%M:%S"
#
# logging.basicConfig(filename="my.log", level=logging.DEBUG, format=LOG_FORMAT, datefmt=DATE_FORMAT)
# logging.debug("This is a debug log")
# logging.info("This is a info log")
# logging.warning("This is a warning log")
# logging.error("This is a error log")


LOG_FORMAT = "%(asctime)s - %(levelname)s - %(message)s"
DATE_FORMAT = "%Y/%m/%d %H:%M:%S"

logger = logging.getLogger()
logger.setLevel("DEBUG")

# 文件处理器，输入到文件
file_handler = logging.FileHandler("all_greeyai.log", mode='a', encoding="UTF-8")

# 流处理器，控制输入到控制台
steam_handler = logging.StreamHandler()

# 错误日志单独输出到一个文件中
error_handler = logging.FileHandler("error.log",mode='a', encoding="UTF-8")
error_handler.setLevel(logging.ERROR)

# 将所有的处理器添加到 logger中
logger.addHandler(file_handler)
logger.addHandler(steam_handler)
logger.addHandler(error_handler)

# 格式化
formatter = logging.Formatter(fmt="%(asctime)s - %(levelname)s - %(message)s",datefmt="%Y/%m/%d %H:%M:%S")

# 设置格式化器。 需要针对每一个处理器进行分别设置
file_handler.setFormatter(formatter)
steam_handler.setFormatter(formatter)
error_handler.setFormatter(formatter)

# 过滤器
my_filter = logging.Filter("greedy")
file_handler.addFilter(my_filter)
steam_handler.addFilter(my_filter)

logger.info("贪心学院日志打印")
logger.info("greedy info ")
logger.error("这里是一个错误日志")




