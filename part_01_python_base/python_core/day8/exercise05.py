def judge_year(year):
    """
    判断一年是否是闰年
    :param year: 年数
    :return: 是闰年返回True,不是闰年返回False
    """
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


def judge_month(year, month):
    """
    判断一月有多少天
    :param year: 年数
    :param month: 月份数
    :return: 一月的天数
    """
    if month > 12 or month < 1:
        return None
    if month in (4, 6, 9, 11):
        return 30
    if month == 2:
        return 29 if judge_year(year) else 28
        # if judge_year(year):
        #     return 29
        # else:
        #     print("456413")
    return 31


print(judge_month(2018, 2))
