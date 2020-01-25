# import os
# re = os.listdir("./")
#
# #  re = ['sudoku.py', 'tcp_flie_send.py', 'tcp_flie_server_demo.py', 'tcp_flie_recv.py', 'tcp_file_client_demo.py',
# #  'project_technical_spot']
# # <class 'list'>
#
#
# re = open("temp","w")
#
# os.chdir("./test")
# re = open("temp","w")

from socket import *
import signal
import time

s01 =socket()
s01.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s01.connect(("127.0.0.1",12421))
print("connection is ok...........")


# s01.send(b"a")
# s01.send(b"b")
#
# time.sleep(0.5)
#
# s01.send(b"c")
# s01.send(b"d")
print(type(bin(2)))
#
# count = 0
# for i in range(200):
#     count += 1
#     s01.send(bin(count))
#




