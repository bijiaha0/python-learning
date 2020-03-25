"""
什么是异常?
运行的时候发生了错误，其实是代码抛出了一个错误
BaseException是所有异常的基类
异常的处理方式:
try:
    代码块
except 异常名字
    代码块: 你要如何去处理这个异常
else:
    代码块
"""

# try:
#     file = open("aaaa", "r")
#     # i = 1
# except:
#     print("发生异常了")
# else:
#     print("没有发生异常")

# try:
#     file = open("aaaa", "r")
#     # i = 1
# except FileNotFoundError as e:
#     print("发生异常了: 文件没有发现，请检查")
#     print(e)
# else:
#     print("没有发生异常")

# try:
#     file = open("aaaa", "r")
#     # i = 1
#
# except FileNotFoundError as e:
#     print("发生异常了: 文件没有发现，请检查")
#     print(e)
# except ReferenceError as e:
#     print("异常2")
# except Exception:
#     print("发生异常了")
# else:
#     print("没有发生异常")

"""
异常的处理原则:
什么时候我们才能进行异常的捕获
你能处理的你再捕获，不能处理的就直接抛出去
"""

# try:
#     # file = open("aaaa", "r")
#     i = 1
#
# except FileNotFoundError as e:
#     print("发生异常了: 文件没有发现，请检查")
#     print(e)
# except ReferenceError as e:
#     print("异常2")
# except Exception:
#     print("发生异常了")
# else:
#     print("没有发生异常")
# finally:
#     print("这个无论如何都会被打印，也就是说这个代码块无论如何都会被执行")

# 手动抛出异常
# try:
#     raise Exception("手动抛出一个异常")
# except:
#     print("捕获了一个异常")

# 自定义异常
class MyDefineError(BaseException):
    pass

try:
    raise MyDefineError("抛出去一个自己定义的异常")
except MyDefineError as e:
    print(e)