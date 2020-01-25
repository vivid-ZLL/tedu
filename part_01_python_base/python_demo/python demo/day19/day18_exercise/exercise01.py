from common.list_helper import *


class Enemy:
    def __init__(self, name, hp, atk, defense):
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defense = defense

    def __str__(self):
        return "%s--%d--%d--%d" % (self.name, self.hp, self.atk, self.defense)


list01 = [
    Enemy("玄冥二老", 86, 120, 58),
    Enemy("成昆", 0, 100, 5),
    Enemy("谢逊", 120, 130, 60),
    Enemy("灭霸", 0, 1309, 690),
]

print(ListHelper.get_min(list01, lambda item: item.hp))
ListHelper.order_by_descending(list01, lambda item: item.hp)
for item in list01:
    print(item)


# 案例:在敌人列表中，删除所有死人.
def del01():
    for i in range(len(list01)-1,-1, -1):
        print(i)
        if list01[i].hp == 0:
            del list01[i]

del01()


# 案例:在敌人列表中，攻击力小于50的所有敌人.
def del02():
    # 3  2  1  0
    for i in range(len(list01)-1,-1, -1):
        if list01[i].atk < 50:
            del list01[i]


# 案例:在敌人列表中，防御力大于100的所有敌人.
def del03():
    # 3  2  1  0
    for i in range(len(list01)-1,-1, -1):
        if list01[i].defense > 100:
            del list01[i]


def condition01(item):
    return item.hp == 0


def condition02(item):
    return item.atk < 50


def condition03(item):
    return item.defense > 100

def delete_all(func_condition):
    # 使用正向索引，倒序删除.
    for i in range(-1,-len(list01)-1,-1):
        print(i)
        # if list01[i].defense > 100:
        # if condition03(list01[i]):
        if func_condition(list01[i]):
            del list01[i]

# delete_all(condition01)


# ListHelper.delete_all(list01, lambda item: item.hp == 0)
for item in list01:
    print(item)
