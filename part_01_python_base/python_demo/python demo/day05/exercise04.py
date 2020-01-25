"""
    练习１:
        将列表[54,25,12,42,35,17]中，
        大于30的数字存入另外一个列表.
        并画出内存图.

    练习２：
        在控制台中录入５个数字，
        打印最大值（不适用max）.
"""
# 练习１：
list01 = [54, 25, 12, 42, 35, 17]
result = []
for item in list01:
    if item > 30:
        result.append(item)
print(result)

# 练习2:
# 假设的最大值
max_value = 0
for item in range(5):
    number = int(input("请输入第%d个数字:" % (item + 1)))
    if max_value < number:
        max_value = number
print(max_value)
