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


def get_max(list_target, func_handle):
    max_value = list_target[0]
    for i in range(1,len(list_target)):
        if func_handle(list_target[i]) > func_handle(max_value):
            max_value= list_target[i]
    return func_handle(max_value)

def func_handle(item):
    return item.hp

re = get_max(list01, func_handle)
print(re)

from list_helper import *
re = ListHelper.get_max(list01,lambda item:item.atk)
print(re)