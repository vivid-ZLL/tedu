from socket import *

# 创建udp套接字
sockfd = socket(AF_INET, SOCK_DGRAM)

server_addr = ("127.0.0.2", 9999)
sockfd.bind(server_addr)  # Placeholder

while True:  # Placeholder
    data, addr = sockfd.recvfrom(1024)
    import struct

    st = struct.Struct("i16sif")
    data = st.unpack(data)

    # 测试代码------
    print("data:",data)
    print("data:",data[1].decode())
    # ---------

    print("收到消息:", "%d - %s - %d - %.1f" % data)
    sockfd.sendto(b"msg got,thank you", addr)
