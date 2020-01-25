from socket import *

s = socket()
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("0.0.0.0",12412))
s.listen(3)


def handle_c():
    while True:
        c, addr = s.accept()
        data = c.recv(1024).decode()
        if not data:
            break
        print("data")
        c.send(b'Ok')


handle_c()

