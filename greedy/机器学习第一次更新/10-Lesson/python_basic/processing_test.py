__author__ = "zhou"
__date__ = "2019-05-14 21:53"
import os


# 导入线程
from threading import Thread
# 导入进程
from multiprocessing import Process
def work():
    print(os.getpid())

if __name__ == "__main__":
    # 在主进程下开启多个线程   每个线程的pid都一样，所以呢他们就是都在一个进程下工作
    t1 = Thread(target=work)
    t2 = Thread(target=work)
    t1.start()
    t2.start()
    print("主进程-----》线程 PID", os.getpid())

    # 开启多个进程   每个进程都有独立的pid
    p1 = Process(target=work)
    p2 = Process(target=work)
    p1.start()
    p2.start()
    print("主进程-----》线程 PID", os.getpid())





