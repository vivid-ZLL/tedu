# code_1 = float(input("请输入数字"))
# operator = input("请输入运算符")
# code_2 = float(input("请输入数字"))
#
# if operator == "+":
#     print(code_1 + code_2)
# elif operator == "-":
#     print(code_1 - code_2)
# elif operator == "*":
#     print(code_1 * code_2)
# elif operator == "/":
#     print(code_1 / code_2)
# else:
#     print("运算符有误")

code_1 = float(input("请输入第一个数字"))
code_2 = float(input("请输入第二个数字"))
code_3 = float(input("请输入第三个数字"))
code_4 = float(input("请输入第四个数字"))
code_max = code_1

if code_max < code_2:
    code_max = code_2

if code_max < code_3:
    code_max = code_3

if code_max < code_4:
    code_max = code_4

print(code_max)
