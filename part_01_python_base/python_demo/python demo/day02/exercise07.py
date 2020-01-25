# 练习：
# 在控制台中录入一个四位整数：1234
# 计算每位相加和。　　１＋２＋３＋４
# 显示结果。10

number = int(input("请输入４位整数："))  # 1234
# 方法１：分别计算出每位，再相加
# 个位 17:00
unit01 = number % 10
# 十位 1234 // 10 -> 123 % 10 -> 3
unit02 = number // 10 % 10
# 百位 1234 // 100 -> 12 % 10 -> 2
unit03 = number // 100 % 10
# 千位
unit04 = number // 1000
result = unit01 + unit02 + unit03 + unit04
print("结果是：" + str(result))
# 方法２：累加每位
# 个位
result = number % 10
# 累加十位
result += number // 10 % 10
# 累加百位
result += number // 100 % 10
# 累加千位
result += number // 1000
print("结果是：" + str(result))
# 练习：分别画出方法１与方法２的内存图.