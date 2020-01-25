from multiprocessing import Process, Semaphore
from time import sleep
import os
"""
应用:很多个进程同时执行时,控制任务最大同时执行数
原理:给定一个数量对多个进程可见。多个进程都可以操作该数量增减,并根据数量值决定自己的行
    为。
方法:创建Semaphore()对象,
        sem.acquire() 将信号量减1 当信号量为0时阻塞
        sem.release() 将信号量加1
        sem.get_value() 获取信号量数量
"""

# 创建信号量 (最多允许三个任务同时执行)
sem = Semaphore(3)


# 任务函数
def handle():
    sem.acquire()
    print("%s 执行任务" % os.getpid())
    sleep(4)
    print("%s 执行完毕" % os.getpid())
    sem.release()
    

for i in range(10):
    p = Process(target=handle)
    p.start()
