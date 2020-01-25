"""
# 练习3：
# 在控制台中录入，所有学生姓名.
# 如果姓名重复，则提示"姓名已经存在",不添加到列表中.
# 如果录入空字符串，则倒叙打印所有学生.
"""

list_name = []
while True:
    name = input("请输入姓名:")
    if name == "":
        break
    # 判断变量在列表中是否存在
    if name not in list_name:
        list_name.append(name)
    else:
        print("姓名已经存在")

# -1  -2  -3
# 2  1   0
for item in range(-1, -len(list_name) - 1, -1):
    print(list_name[item])
