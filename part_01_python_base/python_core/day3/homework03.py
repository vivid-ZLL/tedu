code_height = float(input("请输入身高(m)："))
code_weight = float(input("请输入体重(kg)："))
code_bmi = code_weight / code_height ** 2
if code_bmi < 18.5:
    print("体重过低")
elif code_bmi < 24:
    print("正常范围")
elif code_bmi < 28:
    print("超重")
elif code_bmi < 30:
    print("I度肥胖")
elif code_bmi < 40:
    print("II度肥胖")
else:
    print("Ⅲ度肥胖")

