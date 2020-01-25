"""
计算移动均线
"""

import numpy as np
import datetime as dt
import matplotlib.pyplot as mp


# 日期转换函数


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t


dates, opening_prices, highest_prices, lowest_prices, closing_prices, volumes = np.loadtxt(
    'aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7),
    dtype='M8[D], f8, f8, f8, f8, f8',
    unpack=True, converters={1: dmy2ymd})

ma5 = np.zeros(closing_prices.size - 4)
for i in range(ma5.size):
    ma5[i] = closing_prices[i:i + 5].mean()
    # print(ma5[i])
# print(ma5)  # [341.642 343.722 346.234 ...]

mp.plot(dates[4:], ma5)
mp.gcf().autofmt_xdate()
mp.show()
