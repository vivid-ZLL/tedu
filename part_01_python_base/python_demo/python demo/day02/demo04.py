"""
    数据类型转换
    运算符
        算数运算符
        增强运算符
    练习:exercise03.py
        exercise04.py
        exercise05.py
        exercise06.py
        exercise07.py
"""
# 1. 数据类型转换
# int  float  str
str_usd = input("请输入美元：")
# 类型转换str --> int
int_usd = int(str_usd)
result = int_usd * 6.9
# str + 数值 --> str + str(数值)
# result = str(result)
# print("结果是："+result)
print("结果是："+str(result))

# 2. 算数运算符
# print(1+2)
# print(1-2.5)

# 地板除（保留整数）
print(5 // 2)# 商2
# 余
print(5 % 2)# 余1
# 除
print(5 / 2)# 2.5
# 获取整数的个位
print(27 % 10 )# 7
# 幂运算
# 5的2次方:5*5
print(5**2)
# 5的3次方:5*5*5
print(5**3)

# 3. 增强运算符
# number01 = 200
# print(number01 + 1)
# print(number01)# 200

number01 = 200
# 变量加上另外一个数，再赋值给自身
# number01 = number01 + 1
# 累加(在自身基础上增加)
number01 += 1
print(number01)# 201








