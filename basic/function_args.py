
"""
函数的参数
- 必须参数、 默认参数、 组合参数
- 函数作为参数
- 对象作为参数
- **kwargs 叫做关键字参数
- *args  可变参数

"""

def function(a, b, c=1, d=2, *args, **kwargs):
    print(c)
    print(d)
    print(a,b)
    print(args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

# function(1,2,3,4,5,6, name=1, value=2)


# 命名关键字参数, *后边的必须写名字
# 命名关键字参数是必须参数，如果不需要他是必须参数，那么可以给一个默认值
def func2(a,b,*,c,d):
    print(a)
    print(b)
    print(c)
    print(d)

# func2(1,2,c=3,d=4)
# func2(1,2,d=3,c=4)


def func3(a,b,c):
    print(a)
    print(b)
    print(c)

# s = (1,2,3)
# func3(*s)
# s1 = [4,5,6]
# func3(*s1)


kw = {"a":1, "b":2, "c":3}
func3(*kw)
func3(**kw)  # 一般我们传字典类型的时候，用这种方式 **












