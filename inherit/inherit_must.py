
from abc import ABCMeta, abstractmethod

class Tester(metaclass=ABCMeta):

    @abstractmethod
    def test(self):
        pass

class FunctionTester(Tester):
    def test(self):
        print("功能测试")

f = FunctionTester()
# f.test()