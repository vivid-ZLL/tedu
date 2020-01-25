"""
    练习１：
    在控制台中录入，西游记中你喜欢的人物.
    输入空字符串，打印(一行一个)所有人物.
    11:25
"""

list_person = []
# 录入过程
while True:
    str_input = input("输入在西游记中喜欢的人物:")
    if str_input == "":
        break
    list_person.append(str_input)

# 输出过程
for item in list_person:
    print(item)


