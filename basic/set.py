__author__ = "zhou"
__date__ = "2019-04-20 20:33"

'''
set数据类型的特点: 无序的不重复元素的序列
第一种声明方式使用大括号{} 
第二种声明方式   set_param1 = set()
'''

# set_param = {"1","2","3"}
# print(set_param)
# print(type(set_param))
# set_param1 = set()
#
# print("1" in set_param)
#
a = set("abcd")
print(a)
# b = set("aqwe")
# 并集
# print(a | b)
# 交集
# print(a & b)

# 集合的CRUD
my_set = set(("tony", "jack", "robbin"))
print(my_set)
my_set.add("ni")
print(my_set)

my_set.remove("tony")
print(my_set)

# print(my_set[0])


print(len(my_set))
my_set.clear()
print(my_set)

my_set = set(("tony", "jack", "robbin"))
print(my_set)








