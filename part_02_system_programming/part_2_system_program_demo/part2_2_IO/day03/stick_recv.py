"""
粘包演示
"""
from socket import *
from time import sleep

sockfd = socket()
sockfd.bind(('0.0.0.0', 8889))
sockfd.listen(5)
connfd,addr = sockfd.accept()

while True:
    data = connfd.recv(1024)
    if not data:
        break
    print(data.decode())