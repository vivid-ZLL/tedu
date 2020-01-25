"""
卷积运算
"""

"""
a = [1 2 3 4 5]
b = [8 7 6]
使用b为核  
         44 65 86          有效卷积(valid)全部核心元素生效
      23 44 65 86 59       同维卷积(same) 中间核心元素生效
    8 23 44 65 86 59  30   完全卷积(full) 有一个核心元素生效
0 0 1 2  3  4  5  0   0
6 7 8
  6 7 8
    6 7  8
      6  7  8
         6  7  8
            6  7  8
               6  7   8

c = numpy.convolve(a,b,卷积类型)
"""
# 以卷积求均线
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

# 卷积核
kernel = np.ones(5) / 5  # 此为5日卷积,表示5日均线
ma52 = np.convolve(closing_prices, kernel, 'valid')
mp.plot(dates[4:], ma52, color='red', linewidth=4, label='MA-52')

kernel = np.ones(10) / 10  # 此为10日卷积
ma52_ = np.convolve(closing_prices, kernel, 'valid')
mp.plot(dates[9:], ma52_, color='dodgerblue', linewidth=4, label='MA-52')
mp.gcf().autofmt_xdate()
mp.plot(dates, closing_prices, linestyle=':', label='price')


# 加权卷积可以使黄金分割点或死亡分割点向前平移,提前预知
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
# print(weights) # 权重[0.11405072 0.14644403 0.18803785 0.24144538 0.31002201]
em5 = np.convolve(closing_prices, weights[::-1], 'valid')


mp.legend()
mp.show()
