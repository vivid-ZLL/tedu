"""
    字典推导式
    练习:exercise01.py
    练习:exercise02.py
"""
# 1 2 3 4 ... 10 -> 平方
dict01 = {}
for item in range(1, 11):
    dict01[item] = item ** 2
print(dict01)
# 推导式:
dict02 = {item: item ** 2
          for item in range(1, 11)}
print(dict02)

# 只记录大于５的数字
dict01 = {}
for item in range(1, 11):
    if item >5:
        dict01[item] = item ** 2

print(dict01)

dict02 = {item: item ** 2
          for item in range(1, 11) if item >5}
print(dict02)
