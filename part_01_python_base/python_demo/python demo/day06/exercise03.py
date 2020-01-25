"""
    练习:在控制台中录入日期(月日)，计算这是这一年的第几天.
    例如：３月５日
         1月天数 + 2月天数 + 5

         5月8日
         1月天数 + 2月天数 +3月天数 + 4月天数+ 8


    14:10
"""
day_of_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
month = int(input("请输入月份"))
day = int(input("请输入日："))
# 方法一：
# # 累加前几个月天数
total_day = 0
for i in range(month - 1):
    total_day += day_of_month[i]
# 累加当月天数
total_day += day
print("是这年的第%d天." % total_day)

# 方法二:
# 累加前几个月天数
total_day = sum(day_of_month[:month - 1])
total_day += day
print("是这年的第%d天." % total_day)
