__author__ = "zhou"
__date__ = "2019-05-07 20:58"



class Father:
    name = "李雷"
    sex = "男"
    def __init__(self):
        print("Father构造函数运行")

    def speak_english(self):
        print("father讲英语")

    def __juehuo(self):
        print("老爸的绝活")

class Mother():
    name = "韩梅梅"
    sex = "女"
    def __init__(self):
        print("Mother构造函数运行")


    def speak_chinese(self):
        print("mother speak chinses")


class Child(Father, Mother):
    # def __init__(self):
    #     print("Child构造函数运行")

    def study(self):
        print("child study")

c = Child()
c.speak_english()
c.study()
c.speak_chinese()
print(Child.__bases__)
print(c.name)

