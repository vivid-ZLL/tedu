from socket import *
import signal
import time
s01 = socket()
s01.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s01.bind(("127.0.0.1",12421))
s01.listen(5)

print("please wait...........")

data,addr = s01.accept()

while True:
    # print("data",data)
    # print("type data:",type(data))
    # if not data:
    #     continue

    data01 = data.recv(1024)
    if not data01:
        break
    print("data, addr:",data01,addr)
