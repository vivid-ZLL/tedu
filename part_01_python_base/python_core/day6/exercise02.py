# code_month = int(input("请输入一个月份"))
# if code_month > 12 or code_month < 1:
#     print("输入有误")
# elif code_month == 2:
#     print("28天")
# elif code_month in (4, 6, 9, 11):
#     print("30天")
# else:
#     print("31天")
while True:
    code_month = int(input("请输入一个月份"))
    if code_month > 12 or code_month < 1:
        print("输入有误")
    else:
        day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
        print(day_of_month[code_month - 1])

