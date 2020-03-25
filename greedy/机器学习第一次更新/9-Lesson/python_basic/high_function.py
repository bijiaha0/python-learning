
# lambda表达式    又叫匿名函数
# 格式：   lambda 参数列表: 表达式
#
# def f(x):
#     return x+x

f = lambda x: x + x

r = f(2)
# print(r)

# map 函数
map_demo = map(lambda x: x + x, [1, 2, 3, 4])
print(map_demo)
print(list(map_demo))
print(list(map(str, [1, 2, 3, 4])))


# reduce函数
from functools import reduce
r = reduce(lambda x, y: x+y, [1, 2, 3, 4], 10)
print(r)


# filter函数
print(list(filter(lambda x: x % 2 == 1, [1, 2, 3, 4, 5, 6, 7, 8])))
print(list(filter(lambda x: x and x.strip(), ["1", "aa", " ", None])))