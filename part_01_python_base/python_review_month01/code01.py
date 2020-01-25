"""
    容器
"""
str01 = "最后一堂课"
# 预留空间
list01 = [4, 5, 5, 5, 6]
# 按需分配
tuple01 = (5, 6, 7, 8)
dict01 = {"键": "值"}

# 容器相互转换
# 容器名称(可迭代对象)
list02 = list(str01)
print(list02)

str02 = "".join(list02)
print(str02)

tuple02 = tuple(list01)
print(tuple02)

# 通用操作
# print(id(list01))
# list01 += ["a"]# 在原有对象基础上　累加
# print(list01)
# print(id(list01))

print(id(tuple01))
tuple01 += ("b",)  # 由于元组不可变，所以创建新对象
print(tuple01)
print(id(tuple01))

if "键2" in dict01:
    print(dict01["键2"])

# 获取所有元素
for item in str01:
    print(item)

# 正向索引正序获取
# 0  1  2 3 4
for i in range(len(str01)):
    print(str01[i],end = " ")

# 反向索引正序获取
# -5 -4 -2 -2 -1
for i in range(-len(str01),0):
    print(str01[i],end = " ")

# 正向索引倒序获取
# 4 3  2  1  0
# for i in range(len(list01)-1,-1,-1):
#     del list01[i]

# 反向索引正序获取
# -5  -4  -3  -2  -1
for i in range(-len(list01),0):
    del list01[i]

print(list01)


