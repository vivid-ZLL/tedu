"""
    集合set
    练习:exercise03
    练习:exercise04
"""
# 1. 创建集合
set01 = set()
# set --> str
set01 = set("abcac")
list01 = list(set01)
str01 = "".join(list01)
print(str01)  # "bca"
# 创建具有默认值的集合
set02 = {"a", "b", "a"}

# 2. 添加元素
set02.add("qtx")

# 3. 删除元素
set02.remove("a")

# 4. 获取所有元素
for item in set02:
    print(item)

# 5. 数学运算
set01 = {1, 2, 3}
set02 = {2, 3, 4}
# 交集
print(set01 & set02)  # {2,3}
# 并集
print(set01 | set02)  # {1, 2, 3, 4}
# 补集
print(set01 ^ set02)  # {1, 4}
print(set01 - set02) # {1}
print(set02 - set01) # {4}

# 子集
set03 = {1, 2}
print(set03 < set01)
# 超集
print(set01 > set03)

