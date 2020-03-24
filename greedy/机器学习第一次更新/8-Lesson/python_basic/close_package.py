__author__ = "zhou"
__date__ = "2019-05-09 20:47"


"""
闭包: 简单来说，就是一个外部函数的返回值是内部函数的引用
"""

def outer(a):
    b = 10
    def inner():
        print(a + b)
    # 外部函数的返回值是内部函数的引用
    return inner

inner_func = outer(5)
inner_func()

