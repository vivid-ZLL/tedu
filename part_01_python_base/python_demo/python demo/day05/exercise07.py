# 练习:在控制台中循环输入字符串,如果输入空则停止。
#      最后打印所有内容（拼接后的字符串）.

list_result = []
while True:
    str_input = input("请输入：")
    if str_input == "":
        break
    list_result.append(str_input)

str_result = "".join(list_result)
print(str_result)


