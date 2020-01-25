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


# def count_all(list_target,func_handle):
#     result = 0
#     for item in list_target:
#         result += func_handle(item)
#     return result


# def f01():
#     result = 0
#     for item in list01:
#         result += item.hp
#     return result
# def func_handle(item):
#     return item.hp

from list_helper import *
re = ListHelper.count_all(list01, lambda item: item.atk)
print(re)
