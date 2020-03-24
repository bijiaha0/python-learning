__author__ = "zhou"
__date__ = "2019-06-01 20:37"

class Person():
    pass


# p = Person()
# print(type(p))


class Sheep():
    def __init__(self):
        print("构造函数运行.....")

    def __new__(cls, *args, **kwargs):
        print("__new__方法运行")
        return Dog()

    def __del__(self):
        print("析构函数运行......")


class Dog():
    def run(self):
        print("dog run")
#
# sheep = Sheep()
# print(type(sheep))
# sheep.run()


def get_class(name):
    if name=="dog":
        class Dog():
            def run(self):
                print("dog run")
        return Dog
    else:
        class Cat():
            def run(self):
                print("cat run")
        return Cat


# c = get_class("aaa")
# print(c)
# c.run(c)
#
# print(type(1))
# print(type("aaaa"))
# print(type(c))

# 使用type来动态创建类
# Person2 = type("Person2",(),{})
# print(Person2)
# p2 = Person2()
# print(p2)

class Person3():
    name = "张三"

# print(Person3.name)
#
# Person3 = type("Person3", (), {"name":"李四"})
# print(Person3.name)
#
# Person4 = type("Person4", (Person3,), {})
# print(Person4.name)
#

def person4_run(self):
    print("person4 run")
Person4 = type("Person4", (Person3,),{'person4_run':person4_run})

# p = Person4()
# p.person4_run()

# 元类

# Person4 = type("Person4", (Person3), {})

# 声明一个元类，必须继承type

class MyMetaClass(type):
    """
    当前准备创建类的对象，3个参数分别代表着
    name: 代表着类的名字
    bases: 代表着类继承父类的集合
    attrs: 代表着类的属性和方法的集合
    """
    def __new__(cls, name, bases, attrs):
        print("元类new方法运行")
        print(name)
        print(bases)
        attrs['name'] = "张三"
        attrs['add'] = lambda self, value: value + value
        print(attrs)
        attrs.pop("name")
        print(attrs)

        return type.__new__(cls, name, bases, attrs)
#
class MyClass(metaclass=MyMetaClass):
    def run(self):
        print("my class run")
# my_class = MyClass()
# r = my_class.add(2)
print(MyClass.name)
# print(r)
# my_class.run()
# my_class = MyClass()
# print(my_class.name)

