__author__ = "zhou"
__date__ = "2019-04-20 21:43"

# 函数的参数
"""
形参：形式参数。 是一种意义上的参数。在定义的时候并不占用具体的内存地址
实参：实际参数
"""

# 这种也叫做关键字参数
def my_func_1(name,age):

    print(name)
    print(age)

#
# my_func_1(name=1, age="2")
# my_func_1(age=1, name=3)


# 默认参数
def my_func_2(name="zhou", age=30):
    print(name)
    print(age)

# my_func_2()
# my_func_2("li",40)  # 这里边传的具体的值就是实参

def my_func_3(name,age=50):
    print(name)
    print(age)
# my_func_3()  这种调用会报错，缺少了一个必须的参数name
# my_func_3(2,3)


# 递归：自己调用自己(在函数内部进行调用)
#
# def my_func_4(x):
#     print(x)
#     my_func_4(x+1)
#
# my_func_4(1)


# 函数的返回值
# def f(x):
#     return "你传入的参数是"+ str(x)
#     print("return下边的一行")
# r = f(1)
# print(r)



def f(x):
    # 明确递归结束条件
    if x == 1:
        return 1
    print("计算" + str(x) + "+" + "f("+str(x-1)+")")
    return x + f(x-1)
# r = f(997)
# print(r)



i = 1
def func_1():
    print(i)

func_1()

