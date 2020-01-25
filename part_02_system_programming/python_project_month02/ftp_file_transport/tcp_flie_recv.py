import socket
import os
import signal

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.bind(("127.0.0.1", 12421))
sockfd.listen(5)
print("Please Wait....")

#-------------阻塞等待连接---------------

connfd, addr = sockfd.accept()
print("Connect from", addr)  # 打印连接客户端的地址



#------------------------下载--------------------
def download_file():
    save = open("save.jpg", "wb")
    count = 0
    while True:
        data = connfd.recv(4096)
        if not data:
            print("接收完毕")
            break
        save.write(data)
        count += 1
        print("收到数据:%d" % count)

    n = connfd.send("收到,over".encode())  # 发送字节串
    print("发送%d字节" % n)

#--------------------------------------------------


#-------------------查看----------------------------
def seek_file():
    file_info = []
    for root,dirs,files in os.walk("."):
        # print(files)
        file_info = str(files)
    print(file_info)

    connfd.send(file_info.encode())

seek_file()






# connfd.close()
# sockfd.close()
