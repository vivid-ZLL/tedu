from socket import *
#创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

server_addr = ("127.0.0.2",9990)
sockfd.bind(server_addr)  #Placeholder


while True:     # Placeholder
    data,addr = sockfd.recvfrom(1024)
    message = data.decode()
    print("收到消息:",message)


