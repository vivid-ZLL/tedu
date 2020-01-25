"""
    列表
    练习:exercise01.py
        exercise02.py
        exercise03.py
"""
# 1. 创建列表
# 空
list01 = []
list01 = list()

# 默认值
result = ["悟空", 100, True]
result = list("我是齐天大圣")

# 2. 获取元素
# 索引
print(result[2])  # 齐
# 切片
print(result[-4:])  # ['齐', '天', '大', '圣']

# 3. 添加元素
# 追加(在末尾添加)
result.append("八戒")
# 插入(在指定位置添加)
result.insert(1, True)  # 在索引为１(第二个)的位置添加True

# 4. 删除元素
# 根据元素删除
result.remove("是")
# 根据位置删除

del result[0]
print(result)

# 5.定义元素，目的：可以增删改查元素。
# 切片
del result[1:3]
print(result)
# [True, '大', '圣', '八戒']
# [True, 'a', 'b', '八戒']
result[1:3] = ["a", "b"]
# [True,'八戒']
# list02[1:3] = []
print(result)

# 遍历列表
# 获取列表中所有元素
for item in result:
    print(item)

# 倒序获取所有元素
# 不建议
# list02[::-1] 通过切片拿元素，会重新创建新列表.
# for item in list02[::-1]:
#     print(item)

# 3  2  1  0
for i in range(len(result) - 1, -1, -1):
    print(result[i])

# -1  -2  -3  -4
for i in range(-1, -len(result) - 1, -1):
    print(result[i])
