"""
演示线程的创建与回收
"""

import threading
from time import sleep
import os

a = 1


# 线程函数
def music():
    for i in range(3):
        sleep(2)
        print(os.getpid(), "播放：黄河大合唱")
    global a
    print("local a = ", a)
    a = 10000


# 创建线程对象
t = threading.Thread(target=music)
t.start()  # 启动线程

for i in range(4):
    sleep(1)
    print(os.getpid(), "播放：葫芦娃")

t.join()  # 回收线程
print("main a = ", a)
