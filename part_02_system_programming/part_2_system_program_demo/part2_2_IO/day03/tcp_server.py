"""
tcp_server.py  tcp套接字服务端流程
重点代码

注意：　功能性代码，注重流程和函数使用
"""

import socket

# 创建ｔｃｐ套接字
sockfd = socket.socket(socket.AF_INET,
                       socket.SOCK_STREAM)

# 　绑定地址
sockfd.bind(('0.0.0.0', 8888))

# 设置监听
sockfd.listen(5)

while True:
    # 　阻塞等待处理连接
    print("Waiting for connect...")
    try:
        connfd, addr = sockfd.accept()
        print("Connect from", addr)  # 打印链接的客户端地址
    except KeyboardInterrupt:
        print("Server exit")
        break
    except Exception as e:
        print(e)
        continue

    while True:
        # 　收发消息
        data = connfd.recv(1024)
        if not data: #　如果data 为空的话说明客户端退出
            break
        print("收到:", data.decode())
        n = connfd.send(b'Thanks')  # 发送字节串
        print("发送%d字节" % n)
    connfd.close()

# 　关闭套接字
sockfd.close()
