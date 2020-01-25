# 定义函数,根据年月，计算有多少天。考虑闰年29天，平年28天
# month = int(input("请输入月份："))
# if month < 1 or month > 12:
#     print("输入有误")
# elif month == 2:
#     print("２８天")
# elif month in (4,6,9,11):
#     print("３０天")
# else:
#     print("３１天")

# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return "输入有误"
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return "29天"
#         else:
#             return "28天"
#     if month in (4, 6, 9, 11):
#         return "３０天"
#     return "３１天"

# 不建议方法的返回值类型可能是多种
# bool  int
# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return False
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         else:
#             return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:
#         if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#             return 29
#         else:
#             return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

def is_leap_year(year):
    #     if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    #         return True
    #     else:
    #         return False
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


# def get_day_by_month(year, month):
#     if month < 1 or month > 12:
#         return 0
#     if month == 2:
#         if is_leap_year(year):
#             return 29
#         else:
#             return 28
#     if month in (4, 6, 9, 11):
#         return 30
#     return 31

def get_day_by_month(year, month):
    if month < 1 or month > 12:
        return 0
    if month == 2:
        return 29 if is_leap_year(year) else 28
    if month in (4, 6, 9, 11):
        return 30
    return 31

print(get_day_by_month(2019,5))