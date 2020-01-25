"""
    list-->str
    练习:exercise07.py
"""

# 需求：根据ｘｘ逻辑，拼接一个字符串.
# "0123456789"
# 缺点：每次循环形成（+=）一个新的字符串对象,替换变量引用result。
# result = ""
# for item in range(10):
#     #""
#     #"0"
#     #"01"
#     #"012"
#     result = result + str(item)
# 优点：每次循环只向列表添加字符串，没有创建列表对象。
list_temp = []
for item in range(10):
    list_temp.append(str(item))
# join : list --> str
result = " ".join(list_temp)
print(type(result))
print(result)

