"""
协方差可以简单反映两组统计样本的相关性，值为正，则为正相关；值为负，则为负相关

绝对值越大相关性越强
"""

import numpy as np
import matplotlib.pyplot as mp
import datetime as dt
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t


dates, bhp_opening_prices, bhp_highest_prices, bhp_lowest_prices, bhp_closing_prices, bhp_volumes = np.loadtxt(
    'files/bhp.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7),
    dtype='M8[D], f8, f8, f8, f8, f8',
    unpack=True, converters={1: dmy2ymd})

dates_, vale_opening_prices, vale_highest_prices, vale_lowest_prices, vale_closing_prices, vale_volumes = np.loadtxt(
    'files/vale.csv', delimiter=',',
    usecols=(1, 3, 4, 5, 6, 7),
    dtype='M8[D], f8, f8, f8, f8, f8',
    unpack=True, converters={1: dmy2ymd})

# 绘制收盘价的折线图
mp.figure('COV', facecolor='lightgray')
mp.title('COV', fontsize=16)
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

mp.plot(dates, bhp_closing_prices, color='dodgerblue',
        label='BHP', linestyle='--',
        linewidth=2, alpha=0.3)

mp.plot(dates, vale_closing_prices, color='orangered',
        label='VALE', linestyle='--',
        linewidth=2, alpha=0.3)

# -----------------------------------------------------------------------------------------
# 手动计算协方差
ave_bhp = np.mean(bhp_closing_prices)
ave_vale = np.mean(vale_closing_prices)

# 离差
dev_bhp = bhp_closing_prices - ave_bhp
dev_vale = vale_closing_prices - ave_vale
# 协方差
cov = np.mean(dev_bhp * dev_vale)
print('协方差:',cov)  # 3.135577333333333

# 参考 : 相关系数
# coef:协方差除去两组统计样本标准差的乘积是一个[-1, 1]之间的数。该结果称为统计样本的相关系数。
coef = cov / (np.std(bhp_closing_prices) * np.std(vale_closing_prices))
print('相关系数:',coef)

# -----------------------------------------------------------------------------------------
# 　相关矩阵api
m = np.corrcoef(bhp_closing_prices,vale_closing_prices)
print('--------------')
print('相关矩阵api')
print(m)
print(m[0][1])


mp.legend()
mp.show()
