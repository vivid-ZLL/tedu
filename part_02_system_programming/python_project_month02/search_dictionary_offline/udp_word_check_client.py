"""
    udp 客户端流程
"""

from socket import *

# 服务端地址
ADDR = ("127.0.0.2",9990)  # 邻座ip"176.209.103.32"

# 创建套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

# 循环收发消息
while True:
    data = input("请输入发送信息:")
    if not data:
        print("connection is over")
        break
    sockfd.sendto(data.encode(),ADDR)
    msg,addr = sockfd.recvfrom(1024)

    print("Msg from server:",addr,"\n"+msg.decode())

sockfd.close()