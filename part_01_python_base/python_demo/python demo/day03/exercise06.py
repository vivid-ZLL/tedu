# 在控制台中获取一个月份
# 打印天数,或者提示"输入有误".
# 1 3 5 7 8 10 12  --> 31天
# 4 6 9 11 --> 30天
# 2 --> 28天
# 16:05

month = int(input("请输入月份："))

if month < 1 or month > 12:
    print("输入有误")
elif month == 2:
    print("２８天")
elif month == 4 or month == 6 or month == 9\
        or month == 11:
    print("３０天")
else:
    print("３１天")







