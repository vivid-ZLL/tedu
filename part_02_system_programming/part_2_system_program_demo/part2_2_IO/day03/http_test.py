"""
http 请求响应测试
"""

from socket import *

# http 使用ｔｃｐ传输
s = socket()
s.bind(('0.0.0.0',8000))
s.listen(3)

c,addr = s.accept()
print("Connect from",addr)
data = c.recv(4096) # 接收ｈｔｔｐ请求
print(data)


c.close()
s.close()