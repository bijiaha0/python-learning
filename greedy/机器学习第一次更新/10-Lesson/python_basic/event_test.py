__author__ = "zhou"
__date__ = "2019-05-14 21:59"

# 事件 (Event)
"""
线程间的通信
"""
import threading, time



class Boss(threading.Thread):
    def run(self):
        print("BOSS: 从现在开始咱们就要996啦，欢呼吧")
        # 事件设置
        print(event.isSet())
        event.set()
        time.sleep(3)
        print("BOSS: 大家干完了，以后就不996啦！！！！")
        print(event.isSet())
        event.set()
class Worker(threading.Thread):
    def run(self):
        event.wait()
        print("Worker: 哎妈呀，咋还996了呢，命这么苦，抓紧干吧")
        event.clear()
        event.wait()
        print("Worker: Oh Yeah !!!!!!")


if __name__ == "__main__":
    event = threading.Event()

    threads = []
    for i in range(5):
        threads.append(Worker())

    threads.append(Boss())

    for t in threads:
        t.start()
