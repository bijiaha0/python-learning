__author__ = "zhou"
__date__ = "2019-05-11 21:14"

def demo1():
    l = [x for x in range(1000)]
    return l

# a = demo1()
# print(a)


def yield_demo2():
    for x in range(3):
        yield x
        print("生成器后一行代码")
    print("生成器外层")

a = yield_demo2()
print(a)

# for i in a:
#     print(i)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# 多生成器

def yield_demo3():
    a = 10
    b = 20
    c = 30
    for x in range(3):
        yield a
        print("生成a之后")
        yield b
        print("生成b之后")
        yield c
        print("生成c之后")

g = yield_demo3()
# for gg in g:
#     print(gg)
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
print(g.__next__())
