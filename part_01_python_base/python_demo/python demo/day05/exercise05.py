# 练习３:
# 在列表中[54, 25, 12, 42, 35, 17]，选出最大值(不使用max).
list01 = [54, 25, 12, 42, 100, 17]
# 假设第一个是最大的
max_value = list01[0]
# 与后面（从第二个开始）元素进行比较
# 1 2 3 4 5
for i in range(1, len(list01)):
    if max_value < list01[i]:
        # 如果发现更大的，则替换假设的.
        max_value = list01[i]

print(max_value)


