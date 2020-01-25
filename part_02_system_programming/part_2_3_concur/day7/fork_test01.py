import os
import time
print("for test start")
print("for test start")
pid = os.fork()

if pid < 0:
    print("Create process failed")

if pid == 0: # 这是子进程
    # time.sleep(2)
    print("The new process")
if pid > 0 : # 这是父进程
    print("The old process")

print("fork test over")