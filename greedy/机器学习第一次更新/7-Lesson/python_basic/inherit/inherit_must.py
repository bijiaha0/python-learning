__author__ = "zhou"
__date__ = "2019-05-07 21:29"

from abc import ABCMeta, abstractmethod


class Tester(metaclass=ABCMeta):

    @abstractmethod
    def test(self):
        pass

class FunctionTester(Tester):
    # def test(self):
    #     print("功能测试")
    pass

f = FunctionTester()
# f.test()





