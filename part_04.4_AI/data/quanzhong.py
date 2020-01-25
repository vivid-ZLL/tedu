"""
成交量加权重
交易日加权重
自定义函数加权
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


dates, opening_prices, highest_prices, \
lowest_prices, closing_prices, volumes = np.loadtxt(
    'aapl.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7),
    dtype='M8[D], f8, f8, f8, f8, f8',
    unpack=True, converters={1: dmy2ymd})

# -----------------------------------------------


# VWAP 成交量加权平均价格（成交量体现了市场对当前交易价格的认可度，成交量加权平均价格将会更接近这支股票的真实价值）
vwap = np.average(closing_prices, weights=volumes)
mp.hlines(vwap, dates[0], dates[-1],
          color='red', label='VWAP')

# TWAP  时间加权平均价格（时间越晚权重越高，参考意义越大）
times = np.linspace(1, 10, closing_prices.size)
twap = np.average(closing_prices, weights=times)
mp.hlines(twap, dates[0], dates[-1],
          color='blue', label='TWAP')

# 截取
# 函数曲线加权
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
# print(weights) # 权重[0.11405072 0.14644403 0.18803785 0.24144538 0.31002201]

em5 = np.convolve(closing_prices, weights[::-1], 'valid')
