"""
    for: 适合执行预定次数。
    while:适合根据条件循环执行。
    练习:exercise05.py
        exercise06.py
        exercise07.py
"""

# for 变量 in 可迭代对象:
#     循环体

str01 = "我叫苏大强!"

# item 存储的是字符串中每个字符的地址
for item in str01:
    print(id(item))

# 整数生成器:  range(开始值,结束值,间隔)
# for + range ：　更善于执行预定次数。
for item in range(5):#01234
    print(item)

# 需求：折纸１０次
thickness = 0.0001
for item in range(10):
    thickness*=2
print(thickness)


