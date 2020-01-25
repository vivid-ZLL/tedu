import time


def get_week(year, month, day):
    """
    根据年月日获取星期数
    :param year: 年份数
    :param month: 月份数
    :param day: 天数
    :return: 星期数的字符串
    """
    str_time = "%s/%s/%s" % (year, month, day)
    re = time.strptime(str_time, "%Y/%m/%d")
    dict_weeks = {0: "星期一",
                  1: "星期二",
                  2: "星期三",
                  3: "星期四",
                  4: "星期五",
                  5: "星期六",
                  6: "星期日",
                  }
    return dict_weeks[re.tm_wday]


tuple_time = (2019, 6, 20)
print(get_week(*tuple_time))