from multiprocessing import Pipe, Process
import time
"""
应用:在亲缘关系进程中传递参数
方法:创建管道对象Pipe(),使用send和recv方法进行传输
注意:recv是阻塞函数,避免并发阻塞造成程序锁死

"""

fd1, fd2 = Pipe()


def app1():
    print("启动app 1,请登录")
    print("请求app2 授权")

    fd1.send("app1 请求登录")


    data = fd1.recv()
    if data:
        print("登录成功", data)


def app2():

    data = fd2.recv()  # 阻塞等待管道读取内容
    print(data)

    fd2.send(("Dave", "123"))


p1 = Process(target=app1)
p2 = Process(target=app2)
p1.start()
p2.start()
p1.join()
p2.join()
