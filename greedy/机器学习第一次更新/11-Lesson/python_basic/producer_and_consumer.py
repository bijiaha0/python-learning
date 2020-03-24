__author__ = "zhou"
__date__ = "2019-05-16 20:32"

import threading
import time


condition = threading.Condition()
products = 0


class Producer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products <= 10:
                    products += 1
                    print("{}:{}库存不足商品数量小于等于0.努力生产商品，现在产品总数量是{}".format("生产者",threading.currentThread().getName(),products))
                    condition.notify()  # 这个函数的意思是唤醒一个等待的线程  notifyall 这个方法是唤醒所有线程
                else:
                    print("{}:{}库存充足商品数量大于10.让我休息一会，现在产品总数量是{}".format("生产者",threading.currentThread().getName(),products))
                    condition.wait()  # 线程等待
                condition.release()
                time.sleep(2)


class Consumer(threading.Thread):
    def run(self):
        global condition, products
        while True:
            if condition.acquire():
                if products >= 1:
                    products -= 1
                    print("{}:{}->我消费了一件商品, 现在商品的数量是{}".format("消费者",threading.currentThread().getName(),products))
                    condition.notify()
                else:
                    print("{}:{}->没有库存了，不卖了，停止消费，现在商品数量是{}".format("消费者",threading.currentThread().getName(),products))
                    condition.wait()
                condition.release()
                time.sleep(2)


if __name__ == "__main__":
    for i in range(3):
        p = Producer()
        p.start()

    for i in range(2):
        c = Consumer()
        c.start()



