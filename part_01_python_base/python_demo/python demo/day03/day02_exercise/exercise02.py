"""
    温度转换器
　　摄氏度 = (华氏度 - 32) / 1.8
　　华氏度 = 摄氏度 * 1.8  + 32
   开氏度＝ 摄氏度　＋　273.15
"""
# (1)在控制台中获取华氏度，计算摄氏度。
# fahrenheit = float(input("请输入华氏度:"))
# centigrade = (fahrenheit - 32) / 1.8
# print("摄氏度是:"+str(centigrade))

# (2)在控制台中获取摄氏度，计算华氏度。
# centigrade = float(input("请输入摄氏度:"))
# fahrenheit =centigrade * 1.8 + 32
# print("华氏度是:"+str(fahrenheit))

# (3)在控制台中获取摄氏度，计算开氏度。
centigrade = float(input("请输入摄氏度:"))
kelvin = centigrade + 273.15
print("开氏度是"+str(kelvin))