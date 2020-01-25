"""
queue_0.py  消息队列演示
注意 ： 消息队列符合先进先出原则
"""
from multiprocessing import Queue,Process
from time import sleep
from random import randint
"""
应用:存入复数数量的消息,存入的数据类型变化多
    但是取数据时只能一个一个取
原理:在内存中建立队列模型,进程通过队列将消息存入,或者从队列取出完成进程间通信。

"""
# 创建消息队列
q = Queue(5) # 最大长度5

def handle():
    for i in range(6):
        x = randint(1,33)
        q.put(x)  # 消息入队
    q.put(randint(1,16))

def request():
    l = []
    for i in range(6):
        l.append(q.get())
    l.sort()
    l.append(q.get())
    print(l)


p1 = Process(target = handle)
p2 = Process(target = request)
p1.start()
p2.start()
p1.join()
p2.join()




