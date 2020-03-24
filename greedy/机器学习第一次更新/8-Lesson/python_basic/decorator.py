__author__ = "zhou"
__date__ = "2019-05-09 20:56"

"""
装饰器  (语法糖、注解)
"""

def func_1(x):
    return x * 2

def func_2(x):
    return x * 3

def func_3(x,y,i,j):
    return x(i) + y(j)

#
# r = func_3(func_1, func_2, 2, 3)
# print(r)

import time
def runtime_noargs(function_name):
    def wrapper():
        start_time = time.time()
        print("函数运行前")
        function_name()
        print("函数运行后")
        end_time = time.time()
        print(end_time-start_time)
    return wrapper


@runtime_noargs
def function_demo1():
    time.sleep(1)
    print("demo1函数运行")


# function_demo1()


def args_is_str(function_name):
    def wrapper(a):
        t = type(a)
        if not isinstance(t(), str):
            print("参数错误")
        else:
            function_name(a)
    def aa():
        print("aaaaaaaaaa")

    return wrapper


def runtime_noargs(function_name):
    def wrapper(a):
        start_time = time.time()
        print("函数运行前")
        function_name(a)
        print("函数运行后")
        end_time = time.time()
        print(end_time-start_time)
    return wrapper


# @runtime_noargs   在python中，装饰器不可以同时写多个。如果同时写了多个，那么只有第一个生效
@args_is_str
def function_demo2(args):
    print(args)

@args_is_str
def function_demo22(args):
    print(args)

# function_demo2(1)
# function_demo2("aaaa")
# function_demo22(111)

# 多个参数

def many_args(function_name):
    def a(*args):
        print(*args)
        function_name(*args)
    return a

@many_args
def function_demo3(*args):
    print(*args)


# function_demo3(1,2,3,4,5,6)

def dict_args(function_name):
    def aaa(**dict):
        print(dict)
    return aaa

@dict_args
def function_demo4(**kwargs):
    # print(kwargs)
    pass

# function_demo4(name="aaa", age=10, address="北京")

def combo_args(function_name):
    def w(*args, **kwargs):
        print(*args, kwargs)
    return w
@combo_args
def function_demo5(*args, **kwargs):
    pass


# function_demo5(1, 2, name="aaa", age=10, address="北京")


def max_runtime(timeout):
    def out_warpper(function_name):
        def warrper(*args, **kwargs):
            start_time = time.time()
            i = function_name()
            end_time = time.time()
            use_time = end_time - start_time

            if use_time > timeout:
                print("函数运行超时")
                raise RuntimeError("函数运行超时")
            return i  # 这里是函数的返回值
        return warrper
    return out_warpper

@max_runtime(timeout=3)
def function_demo6(*args, **kwargs):
    time.sleep(2)
    print("demo6运行")
    # raise RuntimeError("函数运行卡死了")
    return 1

r = function_demo6()
print(r)












