"""
thread1.py  线程基础使用
步骤 ： 基本同Process
      1. 封装线程函数
      2. 创建线程对象
      3. 启动线程
      4. 回收线程
"""
"""
应用:把一个函数提取出来成为线程,使其独立运行
使用:创建Tread()对象,该对象的"target= "属性为提取出的方法名
                            若提取出的方法需要传参,在创建对象时把传参一并完成                                                                                            
     Tread()对象的一些属性
        Name属性,默认为Thread - 1
            通过setName()修改
            通过getName()获取
        Daemon属性,默认为False
            为True时,主线程退出分支线程也退出
            为False时,两者互不影响
        
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
    print("a = ", a)
    a = 10000


# 创建线程对象
t = threading.Thread(target=music)
t.start()  # 启动线程

for i in range(4):
    sleep(1)
    print(os.getpid(), "播放：葫芦娃")

t.join()  # 回收线程
print("main a:", a)
