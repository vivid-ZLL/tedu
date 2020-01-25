from socket import *
#创建udp套接字
sockfd = socket(AF_INET,SOCK_DGRAM)

server_addr = ("127.0.0.2",9990)
sockfd.bind(server_addr)  #Placeholder


while True:     # Placeholder
    data,addr = sockfd.recvfrom(1024)
    target = data.decode()
    print("收到消息:",data.decode())
    import word_checker
    re = word_checker.word_check(target)
    if not re:
        re = "未找到该单词"
    re = re.encode()
    sockfd.sendto(re,addr)
