
"""
平均数
中位数
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
    'files/aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7),
    dtype='M8[D], f8, f8, f8, f8, f8',
    unpack=True, converters={1: dmy2ymd})

# 求算数平均数
# mean = np.mean(closing_prices)
mean = closing_prices.mean()
mp.hlines(mean, dates[0], dates[-1], color='green',
          label='Mean')

# 中位数
median = np.median(closing_prices)
mp.hlines(median, dates[0], dates[-1],
          color='violet', label='median')
# 自己算
sorted_prices = np.msort(closing_prices)
size = sorted_prices.size
m = (sorted_prices[int((size - 1) / 2)] +
     sorted_prices[int(size / 2)]) / 2
print(median, '~', m)

mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
