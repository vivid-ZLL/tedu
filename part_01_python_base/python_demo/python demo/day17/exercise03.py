# 练习:1. 获取列表中所有字符串
#     2. 获取列表中所有小数
# 要求:分别使用生成器函数/生成器表达式/列表推导式完成.
list01 = [3, "54", True, 6, "76", 1.6, False, 3.5]
# 练习:1
def find01():
    for itme in list01:
        if type(itme) == str:
            yield itme

re = find01()
for item in re:
    print(item)

re = (itme for itme in list01 if type(itme) == str)
for item in re:
    print(item)

re = [itme for itme in list01 if type(itme) == str]
for item in re:
    print(item)

# 练习:2
def find02():
    for itme in list01:
        if type(itme) == float:
            yield itme

for item in find02():
    print(item)

for item in (item for item in list01 if type(item) == float):
    print(item)

for item in [item for item in list01 if type(item) == float]:
    print(item)


