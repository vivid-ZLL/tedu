"""
    列表推导式嵌套
    练习:exercise09.py
    16:55
"""
list01 = ["a", "b", "c"]
result = ["A", "B", "C"]
list03 = []
for r in list01:
    for c in result:
        list03.append(r + c)

print(list03)

list04 = [r + c for r in list01 for c in result]
print(list04)

# 练习:列表的全排列
# [“香蕉”,"苹果","哈密瓜"]
# [“可乐”,"牛奶"]
list01 = ["香蕉","苹果","哈密瓜"]
result = ["可乐", "牛奶"]
list03 = []
for r in list01:
    for c in result:
        list03.append(r+c)
list04 = [r + c for r in list01 for c in result]
print(list03)
print(list03)








