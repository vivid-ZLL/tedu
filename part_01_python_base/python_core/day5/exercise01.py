list01 = []
while True:
    str_input = input("请输入在西游记中你喜欢的人物：")
    list01.append(str_input)
    if str_input == "":
        for item in list01:
            print(item)
        break
