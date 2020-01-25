# 练习2：根据生日(年月日)，计算活了多少天。
# 思路：
# 年月日 --> 出生时间
# 当前时间 --> 出生时间
# 计算天

import time


def life_days(year, month, day):
    """
        根据生日计算活了多少天
    :param year: 年
    :param month: 月
    :param day: 日
    :return: 活的天数
    """
    tuple_time = time.strptime("%d-%d-%d" % (year, month, day), "%Y-%m-%d")
    life_second = time.time() - time.mktime(tuple_time)
    return int(life_second / 60 / 60 // 24)


print(life_days(1998, 5, 19))
