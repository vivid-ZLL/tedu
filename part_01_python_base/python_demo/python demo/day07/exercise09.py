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
