from threading import Thread
from time import sleep, ctime
"""
自定义线程类(含有多种参数的情况)
作用:根据需求,在原有线程类的基础上自定义添加线程对象的实例方法
    当一个线程需要有很多步骤,或者需要在线程内添加方法时,使用自定义线程可以时线程的逻辑清晰,增加代码可读性
做法:在self.run()方法中调用所有要执行的方法

"""

class MyThread(Thread):
    def __init__(self, target=None, args=(), kwargs=None):
        super().__init__()  # 此行不许传参
        self.target = target
        self.args = args
        self.kwargs = kwargs

    def run(self):
        self.target(*self.args, **self.kwargs)

    ###################################################


def player(sec, song):
    for i in range(3):
        print("Playing %s : %s" % (song, ctime()))
        sleep(sec)


t = MyThread(target=player, args=(3,),
             kwargs={'song': '凉凉'})
t.start()
t.join()
