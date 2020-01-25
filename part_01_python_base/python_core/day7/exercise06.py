list01 = ["香蕉", "苹果", "哈密瓜"]
result = ["可乐", "牛奶"]
list03 = []
list04 = []
for c in list01:
    for r in result:
        list03.append(r + c)
        list04.append(c + r)
print(list03)
print(list04)

