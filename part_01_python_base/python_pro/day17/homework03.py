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

re = ListHelper.find_single(list01, lambda item: item.name == "灭霸")
print(re)
print("--------------------------------------------")

re = ListHelper.find_all(list01, lambda item: item.atk > 10)

for item in re:
    print(item)
print("--------------------------------------------")
re = ListHelper.get_count(list01, lambda item: item.hp > 0)
print(re)
