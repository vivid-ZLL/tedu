"""
模拟僵尸进程产生
"""

import os, sys

pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:  # 这个是子进程

    print("Child PID:", os.getpid())
    sys.exit("子进程退出")

else:  # 这个是父进程

    while True:  # 父进程不退出
        pass
