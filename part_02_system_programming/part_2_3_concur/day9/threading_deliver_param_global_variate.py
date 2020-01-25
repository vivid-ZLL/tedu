"""
event 线程互斥方法演示
"""
"""
实现多个线程之间的通信,就使用全局变量
但要防止共享资源的无序争夺,共享资源被有序存取
    做法:全局变量可能被多个线程使用,用Event()对象的 set() 和 wait()(阻塞) 实现线程的同步互斥
"""
from threading import Thread, Event

s = None  # 用于通信
e = Event()  # 事件对象


def 杨子荣():
    print("杨子荣前来拜山头")
    global s
    s = "天王盖地虎"
    e.set()  # 操作完共享资源 e 设置



t = Thread(target=杨子荣)
t.start()
print("说对口令就是自己人")
e.wait()  # 阻塞等待
if s == '天王盖地虎':
    print("宝塔镇河妖")
    print("确认过眼神，你是对的人")
else:
    print("打死他...")

t.join()
