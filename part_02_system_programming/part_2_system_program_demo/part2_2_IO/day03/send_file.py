from socket import *

s =socket()
s.connect(('127.0.0.1',8888))

#　读取目标文件，循环发送
f = open('timg.jpg','rb')
while True:
    #　边读取，边发送
    data = f.read(1024)
    if not data:
        break
    s.send(data)

f.close()
s.close()