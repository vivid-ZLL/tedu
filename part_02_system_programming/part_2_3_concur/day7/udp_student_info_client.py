"""
    udp 客户端流程
"""

from socket import *

# 服务端地址
ADDR = ("127.0.0.2", 9999)

# 创建套接字
sockfd = socket(AF_INET, SOCK_DGRAM)


def converse_data():
    global data
    student_id = int(input("请输入编号"))
    name = input("请输入姓名:").encode()
    age = int(input("请输入年龄:"))
    score = float(input("请输入分数:"))
    import struct
    st = struct.Struct("i16sif")
    data = st.pack(student_id,name,age,score)
    # print(data)
    # data = st.unpack(data)

    print(data)

# 循环收发消息
while True:


    converse_data()




    if not data:
        print("connection is over")
        break
    sockfd.sendto(data, ADDR)
    msg, addr = sockfd.recvfrom(1024)
    print("Msg from server:", addr, msg.decode())

sockfd.close()
