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


def fun01():
    list02 = []
    for item in list01:
        list02.append((item.name))
    return list02


re = fun01()
print(re)


def fun02():
    list02 = []
    for item in list01:
        list02.append((item.name, item.hp))
    return list02


re = fun02()
print(re)
print("----------------------------")


def select(list_target, func_handle):
    list_temp = []
    for item in list_target:
        list_temp.append(func_handle(item))
    return list_temp


def func_handle(item):
    return item.name, item.hp


re = select(list01, func_handle)
print(re)
print('-------------------------')

re = select(list01, lambda item: (item.name, item.atk))
print(re)
print('-------------------------')

from list_helper import *

re = ListHelper.select(list01, lambda item: (item.name, item.atk))
for item in re:
    print(item)
