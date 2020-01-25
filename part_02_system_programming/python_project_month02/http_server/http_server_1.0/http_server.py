"""
httpserver v1.0
基本要求：1.获取来自浏览器的请求
　　　　　2.判断如果请求内容是/ 将index.html返回给客户端
　　　　　3.如果请求的是其他内容则返回404　
"""

from socket import *


# 　客户端(浏览器)处理
def request(info):
    # 获取请求将请求内容提取出来

    # 判断是/ 则返回index.html 不是则返回404
    if info == '/':
        f = open("index.html")
        response = "HTTP/1.1 200 OK\r\n"
        response += "Content-Type:text/html\r\n"
        response+= "\r\n"
        response += f.read()
        # print(response)
        f.close()
    else:
        response = "HTTP/1.1 404 Not Found\r\n"
        response += "Content-Type:text/html\r\n"
        response += "\r\n"
        response += "<h1>not found</h1>"
    return response.encode()


# 　搭建ｔｃｐ网络
sockfd = socket()
sockfd.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
sockfd.bind(('127.0.0.1', 8001))
sockfd.listen(3)

while True:
    connfd, addr = sockfd.accept()
    data = connfd.recv(1024).decode()
    # print(data)
    data = data.split("\n")[0]
    # data--> GET / HTTP/1.1
    print("data:",data)

    if not data:
        print("进程失去同步,获得空字符串")
        continue

    info = data.split(" ")[1]

    connfd.send(request(info))  # 处理客户端请求

#  客户端退出,此时recv()会收到一个None