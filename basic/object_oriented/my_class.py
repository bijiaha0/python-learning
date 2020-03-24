"""
名词: 类、对象、实例、实例化
类： 类代表了具有相同特征的一类事物(人)
对象和实例: 具体的某一个事物或者是人 (张三、李四)
实例化: 将类变成对象的这么一个过程， new一个对象
"""

"""
python的命名规范
类: 驼峰命名法  PersonStudyEnglish
其他: 包名、模块名、方法名、函数名、变量名，全部采用 小蛇儿命名法  person_study_english
"""


# 函数、方法

def func1(): # 这样定义的咱们叫做函数，它的特点是在模块中声明的
    pass

class Person:

    def func1(self):  #这样的定义的，咱们叫做方法，它的特点是在类中声明的
        pass
    # 类变量
    name = "女娲"
    age = 10000

    # 类私有变量
    __private_args = "class private"

    # 无参数的构造函数
    # def __init__(self):
    #     print('构造函数运行')

    def __init__(self, name, age, sex):
        # print(name)
        # print(age)
        # print(sex)
        self.name = name
        self.age = age
        self.sex = sex
        # print(self.name)
        # print(self.age)
        # print(self.sex)

    def get_private_args(self):
        # print(self)
        return self.__private_args

    def __my_private_method(self):
        print("私有方法")

    def _my_protected_method(self):
        # self.__my_private_method()
        print("保护方法")

    @classmethod
    def my_class_method(cls):
        print(cls)
        print(cls.name)
        print("类方法")

    @staticmethod
    def my_static_method():
        print("静态方法")

# p = Person()
# print(p.name)
# print(p.age)

p = Person("伏羲", 12000 ,"man")
print(p.get_private_args())
r = Person.get_private_args(p)
# print(r)

# 静态方法调用
# Person.my_static_method()
# p.my_static_method()

# 类方法调用
# Person.my_class_method()
# p.my_class_method()

# 在Python中,私有方法能访问么？？

print(Person.__dict__)
print(p._Person__private_args)

print(p._Person__my_private_method)