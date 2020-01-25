from socket import *
socketfd = socket()
socketfd.connect(("127.0.0.1",22385))
print("Connection ok......")

data = open("alice.jpg","rb")

while True:

    data01 = data.read(1024)
    if not data01:
        break
    print(data01)
    socketfd.send(data01)

print("sending is over")

# data_01 = socketfd.recv(1024):
# print(data_01)




# socketfd.close()
