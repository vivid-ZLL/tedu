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


def order_list(list_target):
    for r in range(len(list_target) - 1):  # 0,1,2,3
        for c in range(r + 1, len(list_target)):  # 1,2,3,4
            if func_handle(list_target[r]) > func_handle(list_target[c]):
                list_target[r], list_target[c] = list_target[c], list_target[r]


def func_handle(item):
    return item.atk


from list_helper import *

ListHelper.order_by_(list01,lambda item: item.hp)

for item in list01:
    print(item)

