from multiprocessing import Process
from multiprocessing import Array
"""
应用:在进程之间传递信息
方法:通过遍历obj可以得到每个值,直接可以通过索引序号修改任意值。
        * 可以使用obj.value直接打印共享内存中的字节串
"""
shm = Array("i", [1, 2, 3, 4])

shm_ex = Array("i", 5)   # 实际意义为shm_ex = [0,0,0,0,0]

shm_c = Array("c",b"Alice")

def fun():
    for i in shm:
        print(i)
    shm[1] = 233
    print("-------------------")
    for i in shm_ex:
        print(i)
    print('------------------')



print(shm[1])
p = Process(target=fun)
p.start()
p.join()
print(shm[1])
print(shm_c.value.decode())