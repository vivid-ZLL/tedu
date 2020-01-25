class Enemy:
    def __init__(self, name, hp, atk, defence):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defence = defence

    def __str__(self):
        return "名字:%s, hp:%s, atk:%s, defence:%s" % (self.name, self.hp, self.atk, self.defence)


list01 = [
    Enemy("毛玉", 0, 15, 10),
    Enemy("小妖精", 120, 20, 5),
    Enemy("大妖精", 400, 30, 20),
    Enemy("灭霸", 5000, 100, 200)
]

"""
def remove(list_target, func_handle):
    for i in range(len(list_target) - 1, -1, -1):
        if func_handle(list_target[i]):
            list_target.remove(list_target[i])


def func_handle(item):
    return item.atk < 50


# remove(list01, lambda item: item)
"""
from list_helper import *

ListHelper.remove(list01, lambda item: True)
for item in list01:
    print(item)
