"""
thread_lock.py
线程锁演示
"""
"""
thread_lock.py
使用Lock()对象的 .acquire() 和 .release()  方法实现线程的同步互斥
线程锁演示
"""

from threading import Thread, Lock

a = b = 0
lock = Lock()  # 定义锁


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock:  # 上锁
        a += 1
        b += 1
        # 解锁

t.join()

from threading import Thread, Lock

a = b = 0
lock = Lock()  # 定义锁


def value():
    while True:
        lock.acquire()  # 上锁
        if a != b:
            print("a = %d,b = %d" % (a, b))
        lock.release()  # 解锁


t = Thread(target=value)
t.start()
while True:
    with lock:  # 上锁
        a += 1
        b += 1
        # 解锁

t.join()
