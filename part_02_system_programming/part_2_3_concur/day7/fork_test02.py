import os
import time
print("==============================")
a = 1
pid = os.fork()

if pid < 0:
    print("Create process failed")
if pid == 0:

    print("The new process")
    print("子进程a= ", a) # 子进程会拷贝a = 1 , 但不会执行print语句

    a = 10000
if pid > 0 :
    time.sleep(2)
    print("The old process")
    print("父进程a=",a)

print("all a -->",a)