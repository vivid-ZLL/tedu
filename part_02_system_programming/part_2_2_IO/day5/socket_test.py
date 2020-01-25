import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定地址
sockfd.bind(("127.0.0.1", 7777))

# 设置监听
sockfd.listen(5)

# 阻塞等待处理连接
print("Please Wait....")

connfd, addr = sockfd.accept()

print("Connect from", addr)  # 打印连接客户端的地址

data = connfd.recv(1024)
print("收到:", data)

n = connfd.send(b"Thanks")  # 发送字节串
print("发送%d字节" % n)


# 关闭套接字
connfd.close()
sockfd.close()

