code_month = int(input("请输入一个月份"))
if code_month > 12 or code_month < 1:
    print("输入有误")
elif code_month == 2:
    print("28天")
elif code_month == 4 or code_month == 6 or \
     code_month == 9 or code_month == 11:
    print("30天")
else:
    print("31天")
