__author__ = "zhou"
__date__ = "2019-04-20 21:09"

"""
list列表 : ["a","b",[1,2,3],{1,2,3},{"df":"vv"}]
set集合 : {}
tuple元组 : ()
"""""

# t = ("1")
#t = () # 声明一个空的元组
# t = (1,"2")
# t = (1,)
# print(t)
# print(type(t))
#
# t = (1, 2, 3, 4, 5)
# print(t)
# print(type(t))
# print(t[1])
# t[1] = 6  这一行代码会报错，不让修改
l = ["a",'b']
t = (1, 2, 3, 4, l)
print(t)
l.append("c")
print(t)


