"""
    列表内存图
    １５：４０
    练习:exercise04.py
        exercise05.py
        exercise06.py
"""

list01 = ["张无忌","赵敏"]
result = list01
# 修改的是列表第一个元素
list01[0] = "无忌"
print(result[0])

list01 = ["张无忌","赵敏"]
result = list01
# 修改的是list01变量
list01 = ["无忌"]
print(result[0])#张无忌

list01 = [800,1000]
# 通过切片获取元素，会创建新列表.
result = list01[:]
list01[0] = 900
print(result[0])#?800
list01 = [500]
print(result[0])#?800

# 列表套列表



list01 = [800,[1000,500]]
# 浅拷贝
# list02 = list01[:]
result = list01.copy()
list01[1][0] = 900
print(result[1][0])#?900


import copy

list01 = [800,[1000,500]]
# 深拷贝
result =copy.deepcopy(list01)
list01[1][0] = 900
print(result[1][0])#?
