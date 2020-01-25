"""
pipe.py  管道通信
注意： 1. multiprocessing 中管道通信只能用于有
         亲缘关系进程中
      2. 管道对象在父进程中创建，子进程通过父进程获取
"""
from multiprocessing import Process,Pipe
import sys
import time
# 创建管道
# False单项管道，fd1->recv fd2->send
fd1,fd2 = Pipe()

def app1():
    print("启动app 1,请登录")
    print("请求app2 授权")
    # fd1.close()    # 若管道关闭,抛出异常 OSError: handle is closed
    fd1.send("app1 请求登录")   # 写入管道

#
    fd1.send("app1 请求登录x2")   # 多次send(),recv()方没有缓存机制,只读取最先send的数据
#                                 多次recv()会导致程序阻塞


    data = fd1.recv()
    print("-------------------------")
    if data:
        print("登录成功：",data)

def app2():
    time.sleep(1)
    data = fd2.recv() # 阻塞等待读取管道内容

    #多次接收
    # data += fd2.recv() # 阻塞等待读取管道内容

    print("App2 data:",data)
    fd2.send(('Dave','123')) # 可以发送任意Python类型数据

p1 = Process(target = app1)
p2 = Process(target = app2)
p1.start()
p2.start()
p1.join()
p2.join()

