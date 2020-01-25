"""
套接字属性介绍
"""
from socket import *

# 创建套接字
s = socket()

# 设置端口可以立即重用，绑定地址之前
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)

s.bind(('172.40.91.108',8989))
s.listen(3)
c,addr = s.accept()

print("地址类型:",s.family)
print("套接字类型:",s.type)
print("绑定地址：",s.getsockname())
print("文件描述符：",s.fileno())
# 链接套接字调用　结果同accept返回的ａｄｄｒ
print("连接端地址:",c.getpeername())

c.recv(1024) #　提供阻塞
