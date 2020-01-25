count_min = float(input("请输入分钟数"))
count_hour = float(input("请输入小时数"))
count_day = float(input("请输入天数"))
result = count_min * 60 \
         + count_hour * 60 ** 2 \
         + count_day * 24 * 60 ** 2
print("总秒数：",result)
