__author__ = "zhou"
__date__ = "2019-05-07 21:39"

class A(object):
    def test(self):
        print("A类")
class B(A):
    # def test(self):
    #     print("B类")
    pass

class C(A):
    def test(self):
        print("C类")
class D(B):
    # def test(self):
    #     print("D类")
    pass

class E(C):
    def test(self):
        print("E类")

class F(D,E):
    pass

f = F()
f.test()

print(F.__mro__)

"""
(<class '__main__.F'>, <class '__main__.D'>, <class '__main__.B'>, <class '__main__.E'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>)
F-->D-->B--E--C--A

"""



