# 练习:使用range生成1--10之间的数字,将数字的平方存入list01中
# 将list01中所有奇数存入list02
# 将list01中所有偶数存入list03
# 将list01中所有偶数大于5的数字增加1后存入list04

# list01 = []
# for item in range(1, 11):
#     list01.append(item ** 2)

list01 = [item ** 2 for item in range(1, 11)]

# list02 = []
# for item in list01:
#     if item % 2 == 1:
#         list02.append(item)
result = [item for item in list01 if item % 2 == 1]

list03 = [item for item in list01 if item % 2 == 0]

# list04 = []
# for item in list01:
#     if item % 2 == 0 and item > 5:
#         list04.append(item + 1)
list04 = [item + 1 for item in list01 if item % 2 == 0 and item > 5]
print(list04)


