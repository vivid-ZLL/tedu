import datetime as dt
import numpy as np


# 转换器函数：将日-月-年格式的日期字符串转换为星期
def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = date.weekday()  # 用 周日
    return wday


wdays, closing_prices = np.loadtxt('../data/aapl.csv', delimiter=',',
                                   usecols=(1, 6), unpack=True, converters={1: dmy2wday})

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = closing_prices[wdays == wday].mean()
    """
    [351.79       0.            0.              0.               0.  ]
    [351.79       350.635       0.              0.              0.   ]
    [351.79       350.635      352.13666667   0.           0.        ]
    [351.79       350.635      352.13666667 350.89833333   0.        ]
    [351.79       350.635      352.13666667 350.89833333 350.02285714]  
    """

for wday, ave_closing_price in zip(
        ['MON', 'TUE', 'WED', 'THU', 'FRI'],
        ave_closing_prices):
    print(wday, np.round(ave_closing_price, 2))
