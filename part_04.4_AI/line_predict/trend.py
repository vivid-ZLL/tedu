"""
绘制线性拟合趋势线
"""

import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


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

# 绘制收盘价的折线图
mp.figure('AAPL', facecolor='lightgray')
mp.title('AAPL', fontsize=16)
mp.xlabel('Date', fontsize=14)
mp.ylabel('closing price', fontsize=14)
mp.grid(linestyle=":")

# 拿到坐标轴
ax = mp.gca()
# 设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator(
    md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_major_formatter(
    md.DateFormatter('%d %b %Y'))
# 设置次刻度定位器为日定位器
ax.xaxis.set_minor_locator(md.DayLocator())

dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, color='dodgerblue',
        label='AAPL', linestyle='--',
        linewidth=2, alpha=0.3)

# 绘制散点图
trend_prices = (highest_prices + lowest_prices + closing_prices) / 3
mp.scatter(dates, trend_prices, marker='o', color='orangered', s=80, label='Trend Points')

# 绘制趋势线,整理A和B
days = dates.astype('M8[D]').astype('int32')
# print(days) #[15002 15005 15006 15007...
A = np.column_stack((days,np.ones_like(days)))
# print(A)
"""
[[15002     1]
 [15005     1]
 [15006     1]
    ...
"""
B = trend_prices

x = np.linalg.lstsq(A,B)[0]
trend_line = x[0] * days + x[1]
# print(trend_line) # [346.81031342 347.35526241 347.53691208...
mp.plot(dates,trend_line,color='orangered',label='Trend line')


mp.gcf().autofmt_xdate()
mp.legend()
mp.show()
