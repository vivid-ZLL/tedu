# 练习２:在控制台中录入一个数字,
# 再录入一个运算符(+ - * /)，最后录入一个数字。
# 根据运算符，计算两个数字。
# 要求:如果运算符，不是加减乘除，则提示"运算符有误"

number_one = float(input("请输入第一个数字："))
operator = input("请输入运算符:")
number_two = float(input("请输入第二个数字："))
if operator == "+":
    print(number_one + number_two)
elif operator == "-":
    print(number_one - number_two)
elif operator == "*":
    print(number_one * number_two)
elif operator == "/":
    print(number_one / number_two)
else:
    print("运算符输入有误")






