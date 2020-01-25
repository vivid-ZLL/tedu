# code_month = int(input("请输入月份："))
# if 0 < int(code_month) < 13 :
#     if code_month <= 3:
#         print("春天")
#     elif code_month <= 6:
#         print("夏天")
#     elif code_month <= 9:
#         print("秋天")
#     else:
#         print("冬天")
# else:
#     print("输入错误")
while True:
    code_month = int(input("请输入月份："))
    tuple_spring = 1,2,3
    tuple_summer = 4,5,6
    tuple_autumn = 7,8,9
    tuple_winter = 10,11,12
    if code_month in tuple_spring:
        print("春天")
    elif code_month in tuple_summer:
        print("夏天")
    elif code_month in tuple_autumn:
        print("秋天")
    elif code_month in tuple_winter:
        print("冬天")
    else:
        print("输入有误")
