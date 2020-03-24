if False:
    print("True")
elif True:
    print("elif")
else:
    print("else")

"""
比较运算符
===  地址和值都比较
==  判断两个值是否相等
>
<
>=
<=
!=
"""

if 1 == 2:
    print("相等")

a = [1,2,3]
b = a
c = [1,2,3]
print(a)
print(b)
print(c)

if a == b:
    print("a和b相等")
if a == c:
    print("a和c相等")
if b == c:
    print("b和c相等")

print(id(a))
print(id(b))
print(id(c))

if a is b:
    print("a和b相等")
if a is c:
    print("a和c相等")
if b is c:
    print("b和c相等")

if "ab" > "ac":
    print("a大于b")
else:
    print("a小于b")

"""
in 
not in 
"""

print("a" in "ab")
print("a" not in "ab")

"""
and
or
not
"""

# if 1 and 2 and 3
print(1 and 0)
print(1 or 0)
print(not 0)

"""
身份运算
is
is not
"""

a = [1,2,3]
b = a
c = [1,2,3]
print(a is b)
print(a is not b)
