input_str = input("请输入字符串：")
print(input_str[0])
print(input_str[-1])
print(input_str[-3])
print(input_str[0:2])
print(input_str[::-1])

str_len = len(input_str)
code_mid = str_len // 2
if str_len % 2 == 1:
    print(input_str[code_mid])
