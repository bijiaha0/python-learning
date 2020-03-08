"""
正则表达式
正则表达式是用来操作字符串的一种逻辑公式
"""

import re

s = "贪心学院的官网是http://www.greedyai123.com"
reg = "http://[w]{3}\.[a-z0-9]*\.com"
result = re.findall(reg,s)
# print(result)
# --------------------------------------------------

s = "hello greedyaihello"
reg = "hello"
# print(re.findall(reg,s))
# print(re.findall(reg,s)[0])
# --------------------------------------------------
# 元字符
"""
. 代表的是换行符以外的任意的字符 
\w 匹配字母或数字或下划线或汉字
\s 匹配任意的空白符
\d 匹配任意的数字 0-9  
^ 匹配字符串的开始
$ 匹配字符串的结束
"""
s = "fのasdflk水电@#￥！~费s说的jd f12_31    2_34ass"
# print(re.findall("\w", s))
# print(re.findall("\d", s))
# print(re.findall("\s", s))
# ^放在开头
# print(re.findall("^\w", s))
# $放在后面
# print(re.findall("\w$", s))

# 反义代码
"""
\W: 不是\w匹配的那些
\S: 不是\s匹配的那些
\D: 不是\d匹配的那些
"""
# 限定符
"""
s = "贪心学院的官网是http://www.greedyai123.com"
reg = "http://[w]{3}\.[a-z0-9]*\.com"

* 它代表的是它前面的正则表达式重复0次或多次
+ 它代表的是它前面的正则表达式重复1次或多次
? 它代表的是它前面的正则表达式重复0次或1次
{n} 它代表的是它前面的正则表达式重复n次
{n,} 它代表的是它前面的正则表达式重复n次或多次 ，  最小重复n次
{n,m} 它代表的是它前面的正则表达式重复n次到m次
"""

s = "hhh123hsd12342....答复sdfff532"
# print(re.findall("\d{3}", s))
# print(re.findall("[\da-z]+", s))

s1 = "我的qq是42197393"
reg = "\d{5,12}"
# print(re.findall(reg,s1))

#分组匹配
s = "我的qq号码是:42197393, 我的邮编是:10000"
reg = "(\d{8}).*(\d{5})"
# print(re.findall(reg,s))
# 下边这一行的分组匹配就以为组1和组2是连续的内容，中间没有任何的字符
reg = "(\d{3})(\d{2})"
# print(re.findall(reg,s))
# print(re.search(reg,s))
# print(re.search(reg,s).group())
# print(re.search(reg,s).group(0))
# print(re.search(reg,s).group(1))
# print(re.search(reg,s).group(2))

"""
正则表达式的高级应用
贪婪与懒惰    贪婪与非贪婪
非贪婪: 尽可能少的匹配
非贪婪操作符? 
这个非贪婪操作符可以使用在  *  +  ?  后边   
* 重复0次或者是多次     *?
+ 重复1次或者是多次      +?
? 重复0次或1次     ??
"""

s = "greedyaiiiiiii"
# reg = "greedyai*"
reg = "greedyai+?"
print(re.findall(reg,s))

"""
分之条件匹配
操作符  |
"""

s = "我的电话号码: 010-89832343 0431-89847345 0432-7842342"
# reg = "0\d{2}-\d{8}"
reg = "0\d{2}-\d{8}|0\d{3}-\d{8}|0\d{3}-\d{7}"
# print(re.findall(reg,s))
s1 = "010-89832343"
s2 = "0431-89847345"
s3 = "0432-7842342"
reg = "^0\d{2,3}"
# print(re.findall(reg,s2))

#零宽断言
"""
(?=reg)  匹配reg前边的位置
(?<=reg)  匹配reg后边的位置
(?!=reg)  匹配后边跟的不是reg的位置
(?<!reg)  匹配前边跟的不是reg的位置
"""

s = "hellogreedyailoove"
# reg = "l{2}o(?=greedyai)"
# print(re.findall(reg,s))
reg = "(?<=greedyai)[a-z]*"
# print(re.findall(reg,s))



