"""
    核心数据类型
"""
# 1. Ｎｏｎｅ
a01 = "苏大强"
# 解除变量与数据的绑定关系
a01 = None
# 使用Ｎｏｎ占位
sex = None

# 2. 整形int
# 十进制
num01 = 20
# 二进制：０　　１　　１０　　１１　　 　１００　
print(0b10)# 2
# 八进制：0  1　．．7  10   11 ..
print(0o10)# 8
# 十六进制：0 -- 9   a(10) - f(15)
print(0x10)# 16

# 3.　浮点数float
print(1.5)
# 科学计数法:表示过小或过大的值很明确
# 1.23e-25
print(0.000000000000000000000000123)

# 4. 字符串str
print("1.5")
a = 10
print(a)# 打印变量　　10
print("a")# 打印字符串 a
