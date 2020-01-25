import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
sockfd.bind(("127.0.0.1", 8008))

# 设置监听
sockfd.listen(5)

# 阻塞等待处理连接
while True:
    print("Please Wait....")
    try:
        connfd, addr = sockfd.accept()

        print("Connect from", addr)  # 打印连接客户端的地址
    except KeyboardInterrupt:
        print("Program exit")
        break

    while True:
        data = connfd.recv(1024)
        print("收到:", data)
        if not data:
            print("connect interrupt")
            break

        word = input('send:').encode()
        n = connfd.send(word)  # 发送字节串
        print("发送%d字节" % n)

    # 关闭套接字
    connfd.close()

sockfd.close()
