"""
    lambda 匿名函数
        语法:lambda 参数列表:函数体
        注意:函数体自带return
    练习1:将exercise06.py中,使用def定义的函数,
          改为使用lambda.

"""
from common.list_helper import *

list01 = [43, 4, 5, 5, 6, 7, 87]

# def condition01(item):
#     return item % 2 == 0
#
# def condition02(item):
#     return item > 10
#
# def condition03(item):
#     return 10 < item < 50

# for item in ListHelper.find_all(list01, condition02):
#     print(item)

for item in ListHelper.find_all(list01, lambda item: item % 2 == 0):
    print(item)


# ------------------------------
# 无参数函数 --> lambda
def fun01():
    return 100


a = lambda: 100
re = a()
print(re)


# 多参数函数 --> lambda
def fun02(p1, p2):
    return p1 > p2


b = lambda p1, p2: p1 > p2
re = b(1, 2)
print(re)

# 无返回值函数 --> lambda
def fun03(p1):
    print("参数是:", p1)


c = lambda p1: print("参数是:", p1)
c(100)

# 方法体只能有一条语句，且不支持赋值语句
def fun04(p1):
    p1 = 2

# d = lambda p1:p1 = 2
