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

from list_helper import *
re = ListHelper.is_exist(list01, lambda item: item.name == "成昆")

print(re)
re = ListHelper.is_exist(list01, lambda item: item.name == "大妖精")

print(re)

re = ListHelper.is_exist(list01, lambda item: item.atk < 5 or item.defence < 10)

print(re)

