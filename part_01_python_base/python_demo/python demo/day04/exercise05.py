# 练习1:累加1--100的和  1+2+3+..+100

# 用于存储累加和的变量
sum_value = 0
for item in range(1,101):
    #0 += 1
    #1 += 2
    #3 += 3
    #6 += 4
    sum_value += item
print(sum_value)

# 练习2:累加1--100之间偶数和  2+4+6+8+...+100
sum_value = 0
for item in range(2,101,2):
    sum_value += item
print(sum_value)

# 练习3:累加10--36之间的和
sum_value = 0
for item in range(10,37):
    sum_value += item
print(sum_value)

# 如果不懂，断点调试　＋　内存图



