list01 = []
while True:
    str_input = input("请输入任意字符串：")
    if str_input == "":
        break
    list01.append(str_input)
result = "".join(list01)
print(result)

