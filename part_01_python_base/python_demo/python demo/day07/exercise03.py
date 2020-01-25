# 练习1: 在控制台中循环录入字符串，输入空字符停止.
#       打印所有不重复的文字

set_result = set()
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    set_result.add(str_input)

print(set_result)