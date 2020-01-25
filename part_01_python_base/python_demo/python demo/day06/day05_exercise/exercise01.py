"""
    计算列表中最小值(不使用min)
"""
list01 = [43, 54, 5]
min_value = list01[0]
for i in range(1, len(list01)):
    if min_value > list01[i]:
        min_value = list01[i]
print(min_value)
