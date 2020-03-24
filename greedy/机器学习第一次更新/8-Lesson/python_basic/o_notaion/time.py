__author__ = "zhou"
__date__ = "2019-05-09 20:32"


a = 0
n = 100
while a < n:
    a = a + 1

# 这个例子的时间复杂度就是O(N)  N为常数  计算量为n 括号里放的其实就是计算量

a = 0
b = 0
c = 1
n = 100
while a < n:
    while b < n:
        c = (c + 1) ** 2  # 计算表达式   时间复杂度是O(N^2)
        b = b + 1
    a = a + 1


a = 0
b = 0
n = 100
while a < n:
    while b < n:
        c = (c + 1) ** 2
        b = b * 2
    a = a + 1

# 上边例子时间复杂度的标识  O(NlogN)



