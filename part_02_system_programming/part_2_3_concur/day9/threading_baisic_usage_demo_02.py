"""
thread 2  线程函数传参


"""

from threading import Thread
from time import  sleep


# 含有参数的线程函数传参
def fun(sec,name):
    print("")