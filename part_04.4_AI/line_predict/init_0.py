"""
线性预测

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
        linewidth=2)
mp.gcf().autofmt_xdate()
# mp.show()

# ----------------------------------------------------
# 整理A与B
A = np.zeros((3, 3))
for j in range(3):
    A[j] = closing_prices[j:j + 3]
"""
[[336.1  339.32 345.03]
 [339.32 345.03 344.32]
 [345.03 344.32 343.44]]
"""

B = closing_prices[3:6]
"""
[344.32 343.44 346.5 ]
"""

# 整理五元一次方程组    最终获取一组股票走势预测值
N = 5
pred_prices = np.zeros(closing_prices.size - 2 * N + 1)
for i in range(pred_prices.size):
    a = np.zeros((N, N))
    for j in range(N):
        a[j, ] = closing_prices[i + j:i + j + N]
    b = closing_prices[i + N:i + N * 2]
    x = np.linalg.lstsq(a, b)[0]
    pred_prices[i] = b.dot(x)
# 由于预测的是下一天的收盘价，所以想日期数组中追加一个元素，为下一个工作日的日期
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, 'o-', c='lightgray', label='Closing Price')
dates = np.append(dates, dates[-1] + pd.tseries.offsets.BDay())
mp.plot(dates[2 * N:], pred_prices, 'o-',c='orangered',
        linewidth=3,label='Predicted Price')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()