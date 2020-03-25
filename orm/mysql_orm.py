from orm.field import Field
from utils.mysql_database import create_pool

__author__ = "zhou"
__date__ = "2019-06-01 21:12"

"""
ORM:对象关系映射
"""


class ModelMetaClass(type):
    def __new__(cls, table_name, bases, attrs):
        if table_name == "Model":
            return super(ModelMetaClass, cls).__new__(cls, table_name,bases, attrs)

        mappings = dict()
        for k,v in attrs.items():
            # 保存类属性和列的映射关系到mappings字典中
            if isinstance(v, Field):
                # 这样操作，就将mappings这个变量中，放入了属性名称--> 字段名，列名。
                mappings[k] = v
        for k in mappings.keys():
            # 将类属性移除。 使定义类的字段不污染类属性。 只有实例中才可以访问这些key
            attrs.pop(k)
        attrs["__table__"] = table_name.lower()
        attrs["__mappings__"] = mappings

        return super(ModelMetaClass, cls).__new__(cls, table_name, bases, attrs)


class Model(dict, metaclass=ModelMetaClass):
    def __init__(self, **kwargs):
        super(Model, self).__init__(**kwargs)

    def insert(self, column_list, param_list):
        print("insert 方法运行")
        fields = []
        for k, v in self.__mappings__.items():
            fields.append(k)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        args = self.__check_params(param_list)

        sql = "insert into %s (%s)  values (%s) " % (self.__table__, ','.join(fields), ','.join(args))

        res = self.__do_execute(sql)
        print(res)


    def __check_params(self, param_list):
        args = []
        for param in param_list:
            if "\"" in param:
                param = param.replace("\"", "\\\"")
            param = "\"" + param + "\""
            args.append(param)

        return args

    def __do_execute(self, sql):
        conn = create_pool()
        cur = conn.cursor()
        if "select" in sql:
            cur.execute(sql)
            rs = cur.fetchall()
        else:
            rs = cur.execute(sql)
        conn.commit()
        cur.close()
        return rs

    def select(self, column_list, where_list):
        print("select 方法被调用")
        args = []
        fields = []

        for k, v in self.__mappings__.items():
            fields.append(k)

        for key in where_list:
            args.append(key)

        for key in column_list:
            if key not in fields:
                raise RuntimeError("field not found")

        sql = "select %s from %s where %s" % (','.join(column_list),self.__table__, "and".join(args))
        res = self.__do_execute(sql)
        return res

