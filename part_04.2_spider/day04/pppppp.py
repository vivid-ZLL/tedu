import time
from multiprocessing import Process


def test01():
    print(111)
    time.sleep(2000)


while True:
    p = Process(target=test01)
    p.daemon = True
    time.sleep(1)
    p.start()


