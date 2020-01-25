from socket import *
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('127.0.0.1', 8002))
sockfd.listen(3)

connfd , addr = sockfd.accept()
data = connfd.recv(1024)
print("data:",data.decode())
