str_input = input("请输入字符串：")
str_slice = str_input[::-1]
print(str_input)
print(str_slice)
if str_input == str_slice:
    print("是回文")
else:
    print("不是回文")
