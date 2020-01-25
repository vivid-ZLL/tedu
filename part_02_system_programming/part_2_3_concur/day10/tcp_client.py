from socket import *
socketfd = socket()
# socketfd.bind(("0.0.0.0",7779))

socketfd.connect(("127.0.0.1",11224))
print("Connect Ok....")
while True:
    data = input("send:").encode()
    if not data:
        print("connect interrupt")
        break
    socketfd.send(data)

    data_01 = socketfd.recv(1024)
    print(data_01)



socketfd.close()
