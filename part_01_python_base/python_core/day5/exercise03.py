list_name = []
while True:
    str_input = input("请输入学生姓名：")
    if str_input == "":
        break
    for item in list_name:
        if str_input == item:
            print("姓名已经存在，请重新输入")
            break
    # if str_input not in list_name:
    #     list_name.append(str_input)
    # else:
    #     print("姓名已经存在，请重新输入")

    else:
        list_name.append(str_input)
print(len(list_name))
print(list_name)
for item_01 in range(-1, -len(list_name)-1, -1):
    print(list_name[item_01])
