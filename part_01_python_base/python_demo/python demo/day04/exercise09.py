# 练习1:在控制台中，获取一个字符串.
# 打印每个字符的编码值
str_input = input("请输入文字：")
for item in str_input:
    print(ord(item))

# 练习2:在控制台中，重复录入一个编码值，然后打印字符.
#      如果输入空字符串，则退出程序.
while True:
    str_code = input("请输入编码值:")
    if str_code == "":
        break
    code_value = int(str_code)
    print(chr(code_value))
