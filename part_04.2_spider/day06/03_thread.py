import random
import time
from threading import Thread


def run():

    time.sleep(random.randint(1, 2))
    print('how may I serve you,Lord Alice?')
    time.sleep(random.randint(1, 2))

t_list = []

for i in range(10):
    t = Thread(target=run)
    t_list.append(t)
    t.start()


for t in t_list:
    t.join()
