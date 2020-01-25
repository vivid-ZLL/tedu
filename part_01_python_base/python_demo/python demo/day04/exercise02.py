# 练习:一张纸的厚度是0.01毫米，
#  请计算对折多少次，超过珠穆朗玛峰8844.43米。
# 10:30

thickness = 0.01 / 1000
count = 0
while thickness < 8844.43:
    count += 1
    thickness *= 2
    # print(thickness)
print(count)
