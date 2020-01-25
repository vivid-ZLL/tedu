# 温度
# 　　摄氏度 = (华氏度 - 32) / 1.8
# 　　华氏度 = 摄氏度 * 1.8  + 32
#    开氏度＝ 摄氏度　＋　273.15
#    (1)在控制台中获取华氏度，计算摄氏度。
#    (1)在控制台中获取开氏度，计算华氏度。
#    (1)在控制台中获取摄氏度，计算开氏度。
fahrenheit = float(input("请输入华氏度："))
kelvin = float(input("请输入开氏度："))
centigrade = float(input("请输入摄氏度："))

centigrade_result = (fahrenheit - 32) / 1.8
fahrenheit_result = 32 + 1.8 * (kelvin - 273.15)
kelvin_result = centigrade + 273.15

print("摄氏度为：",centigrade_result)
print("华氏度为：",fahrenheit_result)
print("摄氏度为：",centigrade_result)

