__author__ = "zhou"
__date__ = "2019-04-25 21:04"

"""
安装  pip3 install aiml

"""

import aiml

k = aiml.Kernel()
k.learn("std-startup.xml")
k.respond("load aiml b")
while True:
    # print(k.respond(input("请输入内容>>")))
    question = input("请输入内容>>")
    answer = k.respond(question)
    a = answer.replace(" ","")
    print(a)


