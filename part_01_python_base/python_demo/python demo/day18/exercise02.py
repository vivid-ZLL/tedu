"""
    练习１：
    在list_helper.py中增加通用的求和方法.
    案例1:计算敌人列表中所有敌人的总血量.
    案例2:计算敌人列表中所有敌人的总攻击力.
    案例3:计算敌人列表中所有敌人的总防御力.
    步骤：
    实现具体功能/提取变化/提取不变/组合

    练习2:
    在list_helper.py中增加通用的筛选方法.
    案例1:获取敌人列表中所有敌人的名称.
    案例2:计算敌人列表中所有敌人的攻击力.
    案例3:计算敌人列表中所有敌人的名称和血量.

    练习3:
    在list_helper.py中增加通用的获取最大值方法.
    案例1:获取敌人列表中攻击力最大的敌人.
    案例2:获取敌人列表中防御力最大的敌人.
    案例3:获取敌人列表中血量最高的敌人.

    练习4:
    在list_helper.py中增加通用的升序排列方法.
    案例1:将敌人列表按照攻击力进行升序排列.
    案例2:将敌人列表按照防御力进行升序排列.
    案例3:将敌人列表按照血量进行升序排列.
"""
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

# 练习1:
"""
# 实现具体功能......
def sum01():
    sum_value = 0
    for item in list01:
        sum_value += item.atk
    return sum_value

def sum02():
    sum_value = 0
    for item in list01:
        sum_value += item.hp
    return sum_value

def sum03():
    sum_value = 0
    for item in list01:
        sum_value += item.defense
    return sum_value

# 提取变化.....
def handle01(item):
    return item.atk

def handle02(item):
    return item.hp

def handle03(item):
    return item.defense

# 提取不变....
def sum(func_handle):
    sum_value = 0
    for item in list01:
        # sum_value += item.defense
        # sum_value += handle03(item)
        sum_value += func_handle(item)
    return sum_value

print(sum(handle03))
"""
print(ListHelper.sum(list01, lambda item: item.atk))

# 练习2:
"""
def select01():
    result = []
    for item in list01:
        result.append(item.name)
    return result

def select02():
    result = []
    for item in list01:
        result.append(item.atk)
    return result

def select03():
    result = []
    for item in list01:
        result.append((item.name,item.hp))
    return result

def handle01(item):
    return item.name

def handle02(item):
    return item.atk

def handle03(item):
    return (item.name,item.hp)

# def select(func_handle):
#     result = []
#     for item in list01:
#         # result.append((item.name,item.hp))
#         # result.append(handle03(item))
#         result.append(func_handle(item))
#     return result

def select(func_handle):
    for item in list01:
        yield func_handle(item)

for item in select(handle01):
    print(item)
"""
for item in ListHelper.select(list01, lambda item: (item.name, item.hp)):
    print(item)

# 练习3:
"""
def get_max01():
    max_value = list01[0]
    for i in range(1, len(list01)):
        if max_value.atk < list01[i].atk:
            max_value = list01[i]
    return max_value


def get_max02():
    max_value = list01[0]
    for i in range(1, len(list01)):
        if max_value.defense < list01[i].defense:
            max_value = list01[i]
    return max_value


def get_max03():
    max_value = list01[0]
    for i in range(1, len(list01)):
        if max_value.hp < list01[i].hp:
            max_value = list01[i]
    return max_value


def handle01(item):
    return item.atk


def handle02(item):
    return item.defense


def handle03(item):
    return item.hp


def get_max(func_handle):
    max_value = list01[0]
    for i in range(1, len(list01)):
        # if max_value.hp < list01[i].hp:
        # if handle03(max_value) < handle03(list01[i]):
        if func_handle(max_value) < func_handle(list01[i]):
            max_value = list01[i]
    return max_value

print(get_max(handle02))
"""
print(ListHelper.get_max(list01, lambda item: item.atk))

# 练习4:
"""
def order_by01():
    # 取出前几个数据
    for r in range(len(list01) - 1):
        # 与后面进行对比
        for c in range(r + 1, len(list01)):
            if list01[r].atk > list01[c].atk:
                list01[r], list01[c] = list01[c], list01[r]

def order_by02():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r].defense > list01[c].defense:
                list01[r], list01[c] = list01[c], list01[r]

def order_by03():
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            if list01[r].hp > list01[c].hp:
                list01[r], list01[c] = list01[c], list01[r]

def handle01(item):
    return item.hp
def handle02(item):
    return item.defense
def handle03(item):
    return item.atk

def order_by(func_handle):
    for r in range(len(list01) - 1):
        for c in range(r + 1, len(list01)):
            # if list01[r].hp > list01[c].hp:
            # if handle03(list01[r]) > handle03(list01[c]):
            if func_handle(list01[r]) > func_handle(list01[c]):
                list01[r], list01[c] = list01[c], list01[r]

order_by(handle01)

for item in list01:
    print(item)
"""
ListHelper.order_by(list01, lambda item: item.hp)
for item in list01:
    print(item)
# 15:20
