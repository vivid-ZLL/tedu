# 发送端广播

from socket import *
from time import *

# 广播地址
dest = ("0.0.0.0", 11224)
s = socket(AF_INET, SOCK_DGRAM)

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)

data = """
      ========================
          ^_^   O(∩_∩)O
                         (⊙o⊙)
      ========================                          
"""
while True:
    sleep(5)
    s.sendto(data.encode(), dest)
