import multiprocessing as mp
from time import sleep


# 目标函数
def fun():
    print("开始一个进程")
    sleep(5)
    print("子进程结束")


# 创建进程对象
p = mp.Process(target=fun())  # p这个对象代表一个进程,p本身还是对象
p.start()  # 启动进程

p.join()  # 回收进程,此进程为阻塞函数,直至子进程结束位置
#

"""
pid = os.fork()
if pid == 0:
    fun()
    os._exit()
else:
    os.wait()
"""
