import os
import time
pid = os.fork()

if pid < 0:
    print("Error")
elif pid == 0:  # 这个是子进程
    time.sleep(1.5)
    print("Child PID:", os.getpid())
    print("Get parent PID:", os.getppid())

else:  # 这个是父进程

    print("Get child PID:", pid)
    print("Parent PID:", os.getpid())

# 一般子进程PID比父进程PID大1
