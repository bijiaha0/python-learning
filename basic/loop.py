__author__ = "zhou"
__date__ = "2019-04-18 21:42"

# list1 = [1,2,3]
# for l in list1:
#     print(l)
#
# i = 1
# while i < 100:
#     i = i + 1
#     print(i)


a = [13, 24, 1, 54, 2, 65, 36]
# a.sort(reverse=True)
# print(a)

for i in range(len(a)-1):
    for j in range(len(a)-1-i):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]

























