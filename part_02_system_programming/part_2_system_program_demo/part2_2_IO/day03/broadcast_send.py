"""
广播发送
1. 创建ｕｄｐ套接字
2. 设置可以发送广播
3. 循环向广播地址发送
"""
from socket import *
from time import sleep

# 广播地址
dest = ('172.40.91.255',9999)

s = socket(AF_INET,SOCK_DGRAM)

s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

data = """
          ******************
          北京　7.4  盛夏
          温度 : 38.6
          状态 : 没有四块五的妞
          *******************
"""

while True:
    sleep(2)
    s.sendto(data.encode(),dest) #目标地址＝广播地址







