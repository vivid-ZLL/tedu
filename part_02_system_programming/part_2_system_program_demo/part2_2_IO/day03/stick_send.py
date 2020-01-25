from socket import *
from time import sleep

sockfd = socket()
server_addr = ('127.0.0.1',8889) #服务端地址
sockfd.connect(server_addr)

for i in range(10):
    sockfd.send(b'msg#')

