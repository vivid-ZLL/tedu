import time


def get_sec(year, month, day):
    """
    根据年月日获取时间戳
    :param year: 年份数
    :param month: 月份数
    :param day: 天数
    :return: 星期数的字符串
    """
    str_time = "%s/%s/%s" % (year, month, day)
    re = time.strptime(str_time, "%Y/%m/%d")
    return (time.mktime(re))


re = get_sec(2019, 6, 18)

print(time.time())
print(re)

live_sec = time.time() - re
print(live_sec)

live_min = live_sec // 60
print(live_min)

live_hour = live_min // 60
print(live_hour)

live_day = live_hour // 24
print(live_day)
