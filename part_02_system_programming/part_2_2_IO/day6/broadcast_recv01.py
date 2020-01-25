# 广播地址  192.168.135.255
"""
广播接受
1. 创建udp套接字
2. 设置套接字可以发送接收广播
3. 选择接受端
4. 接收广播

"""

from socket import *

s = socket(AF_INET, SOCK_DGRAM)

# 设置套接字接收广播
s.setsockopt(SOL_SOCKET,SO_BROADCAST,1)

s.bind(("0.0.0.0",11224))

while True:
    msg ,addr = s.recvfrom(1024)
    print(msg.decode())
