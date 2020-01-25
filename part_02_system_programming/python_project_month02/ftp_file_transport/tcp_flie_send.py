from socket import *
import signal
import multiprocessing as mp

signal.signal(signal.SIGCHLD,signal.SIG_IGN)
socketfd = socket()
socketfd.connect(("127.0.0.1",12421))
print("Connection ok......")



def send_file():
    taget_file = input("输入文件路径(例如alice.jpg):")

    data = open(taget_file, "rb")
    while True:
        data01 = data.read(1024)
        if not data01:
            break
        print(data01)
        socketfd.send(data01)

    print("sending is over")
    data.close()


def download_file():
    target_file = input("请输入文件名称(例如alice.jpg):").encode()
    socketfd.send(target_file)
    save_file = open(target_file,"wb")


    while True:
        data = socketfd.recv(4096)
        if not data:
            print("文件下载完毕")
            break
        save_file.write(data)


def seek_file():
    # while True:
    recv_data = socketfd.recv(4096)
    # if not recv_data:
    #     print("文件下载完毕")
        # break

    print("文件列表:",recv_data.decode())


##-------测试代码------
seek_file()


