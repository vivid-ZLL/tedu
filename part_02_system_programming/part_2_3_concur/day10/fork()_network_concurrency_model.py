from socket import *
import os
import signal

"""
### 基于fork的多进程网络并发模型

#### 实现步骤

1. 创建监听套接字
2. 等待接收客户端请求
3. 客户端连接创建新的进程处理客户端请求
4. 原进程继续等待其他客户端连接
5. 如果客户端退出，则销毁对应的进程

"""

# 全局变量

HOST = "0.0.0.0"
PORT = 11224
ADDR = (HOST, PORT)


# 具体处理客户端请求
def handle(c):
    while True:
        data = c.recv(1024)
        if not data:
            break
        print("data recived:", data.decode())
        c.send(b"OK")
    c.close()


# 创建tcp 套接字


s = socket()
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(ADDR)
s.listen(5)

# 处理僵尸进程
signal.signal(signal.SIGCHLD, signal.SIG_IGN)
print("listen the port 8888...........")

while True:
    # 循环处理客户端连接
    c = None
    try:
        c, addr = s.accept()
        print("connect from", addr)
    except KeyboardInterrupt:
        os._exit(0)
    except Exception as e:
        print(e)
        continue

    # 创建子进程处理客户端连接
    pid = os.fork()
    # 创建的套接字s 和 接受的套接字c 在子进程和父进程中都需要关闭
    # 子进程不需要自己创建的套接字s,提前关闭
    # 父进程不需要接受的套接字c,提前关闭

    if pid == 0:

        s.close()
        handle(c)  # 处理具体事物
        os._exit(0)  # 子进程销毁
    # 无论是pid < 0 还是 pid > 0 都要回去处理连接
    else:
        c.close()  # 父进程不需要和客户端通信
        # 主线程只负责建立连接
