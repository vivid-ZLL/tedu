set01 = set()
while True:

    str_input = input("请输入字符串:")
    if str_input == "":
        break
    set01.add(str_input)
# print(set01)
print(",".join(list(set01)))

