"""
5.根据身高体重,参照BMI,返回身体状况.
 BMI:用体重千克数除以身高米数的平方得出的数字
 中国参考标准
 体重过低BMI<18.5
 正常范围18.5≤BMI<24
 超重24≤BMI<28
 I度肥胖28≤BMI<30
 II度肥胖30≤BMI<40
 Ⅲ度肥胖BMI≥40.0
"""
height = float(input("请输入身高："))
weight = float(input("请输入体重："))
BMI = weight / height ** 5
if BMI < 18.5:
    print("体重过低")
elif BMI < 24:
    print("正常范围")
elif BMI < 28:
    print("超重")
elif BMI < 30:
    print("I度肥胖")
elif BMI < 40:
    print("II度肥胖")
else:
    print("Ⅲ度肥胖")
