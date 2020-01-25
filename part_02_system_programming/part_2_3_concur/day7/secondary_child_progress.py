from time import sleep
import os


def f1():
    for i in range(3):
        sleep(2)
        print("写代码")


def f2():
    for i in range(2):
        sleep(4)
        print("测代码")


pid = os.fork()

if pid < 0:
    print("Create process failed")

if pid == 0:  # 这是子进程
    print("The new process")
    p = os.fork()
    if p == 0:
        f1()
    else:
        os._exit(0)

if pid > 0:  # 这是父进程
    os.wait()
    f2()
    print("The old process")
