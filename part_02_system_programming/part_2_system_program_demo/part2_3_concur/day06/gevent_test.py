"""
gevent 协程模块 示例
"""

import gevent
from gevent import monkey
monkey.patch_time()
from time import sleep

# 协程函数
def foo(a,b):
    print("Running foo ...",a,b)
    sleep(2)
    print("Foo again..")

def bar():
    print("Running bar ...")
    sleep(3)
    print("Bar again..")

# 生成协程对象
f = gevent.spawn(foo,1,2)
b = gevent.spawn(bar)

gevent.joinall([f,b]) # 阻塞等待f,b两个协成执行完毕




