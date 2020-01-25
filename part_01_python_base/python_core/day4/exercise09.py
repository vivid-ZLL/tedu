code_str = input("请输入字符")
for item in code_str:
    print(ord(item))


while True:
    code_str = input("请输入编码值：")
    if code_str == "":
        break
    code_int = int(code_str)
    print(chr(code_int))
