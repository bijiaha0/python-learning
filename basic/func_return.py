__author__ = "zhou"
__date__ = "2019-04-23 20:31"


def func1():
    print("函数被调用")

# f = func1()

# print(f)
# print(type(f))

def func2():
    return "a"

f = func2()
# print(f)
# print(type(f))

def func3(x,y):
    z = x + y
    return z

f = func3(3,2)
# print(f)
# print(type(f))

def func4():
    return 1,2
x ,y = func4()
# print(x)
# print(y)


# 函数的返回值是一个函数

def func5(x):
    if x == 2:
        def inner_func(y):
            print("inner 1 被调用")
            return y * y
    if x == 3:
        def inner_func(y):
            print("inner 2 被调用")
            return y * y * y
    return inner_func

calc = func5(2)
print(type(calc))
z = calc(4)
print(z)


