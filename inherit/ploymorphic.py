from abc import ABCMeta, abstractmethod

"""
多态
多态指的是一类事物有多种形态

多态性
"""

class Animal:
    def run(self):
        raise AttributeError("子类必须实现这个方法")

class Person(Animal):
    def run(self):
        print("人 跑")

class Pig(Animal):
    def run(self):
        print("pig 跑")

class Dog(Animal):
    def run(self):
        print("dog run")

# person = Person()
# # person.run()
# pig = Pig()
# # pig.run()
# dog = Dog()
# dog.run()


"""
多态性

"""

def func(obj):
    obj.run()


# person = Person()
# pig = Pig()
# dog = Dog()
#
# # 这里就相当于我们往usb接口上插入了一些个设备
# func(person)
# func(pig)
# func(dog)

# 我是电脑的厂商，比如联想、苹果、戴尔
class Computer(metaclass=ABCMeta):

    @abstractmethod
    def usb_insert(self):
        pass

class ThinkPad(Computer):

    def usb_insert(self):
        pass

    def usb_run(self,sub_computer):
        sub_computer.usb_insert()


# 这是鼠标生产商，比如雷蛇
class Mouse(Computer):
    def usb_insert(self):
        print("插入了鼠标")


# 这是键盘生产商，比如樱花
class Keyboard(Computer):
    def usb_insert(self):
        print("插入了键盘")

c = Computer()

# 我买了一个电脑
computer = ThinkPad()

# 我买了一个鼠标
m = Mouse()
# 插入电脑上
computer.usb_run(m)
# 我又买了一个键盘
k = Keyboard()
# 把键盘插入电脑上
computer.usb_run(k)





