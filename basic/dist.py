__author__ = "zhou"
__date__ = "2019-04-20 20:45"

"""
字典是一种可变容器模型，它可以存储任意类型的对象
"""
# set_param = {"1","2","3"}
# d = {k1:v1,k2:v2}
d = {1: "zhangsan", 2: "lisi"}
print(d)

keys = d.keys()
print(keys)
for i in keys:
    print(i)
    print(d[i])
# print(d[2])
print(d.values())
# 添加
d[3] = "test"
print(d)
d.setdefault(4, "aaa")
print(d)

# 更新
d[4] = 'bbb'
print(d)

#删除
# r = d.pop(4)
# print(r)
# print(d)

d["a"] = 1
print(d)
del d["a"]
print(d)

