
# 定义Field类，是用来保存数据库表的字段名字和字段类型的
class Field(object):
    def __init__(self, cloumn_name, cloumn_type):
        self.cloumn_name = cloumn_name
        self.cloumn_type = cloumn_type


