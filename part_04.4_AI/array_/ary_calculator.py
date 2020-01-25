"""
sign 和 piecewise 的使用
"""

import numpy as np
import math as m
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md


def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    t = time.strftime('%Y-%m-%d')
    return t


class Ary:
    def __init__(self):
        self.dates, self.opening_prices, self.highest_prices, self.lowest_prices, \
        self.closing_prices, self.volumes = np.loadtxt(
            'aapl.csv',
            delimiter=',',
            usecols=(1, 3, 4, 5, 6, 7),
            dtype='M8[D], f8, f8, f8, f8, f8',
            unpack=True,
            converters={1: dmy2ymd}
        )

    def _profit(self, opening_prices, highest_prices, lowest_prices, closing_price):
        """
            定义买入卖出策略,计算当天收益
        """
        buying_price = opening_prices * 0.99
        # mp.plot(self.dates, lowest_prices, label='low', color='orangered')
        # mp.plot(self.dates, buying_price, label='buy', color='dodgerblue')
        # mp.plot(self.dates, highest_prices, label='high', color='violet')
        # mp.legend()
        # mp.show()

        if lowest_prices < buying_price < highest_prices:
            return (closing_price - buying_price) / buying_price
        else:
            return np.nan

    def vec_profit(self):
        """
            以开盘价的99%,当天买入,当天卖出
            矢量化策略
            计算收益
        """
        profits = np.vectorize(self._profit)(self.opening_prices, self.highest_prices, self.lowest_prices,
                                             self.closing_prices, )

        # res = self._profit(self.opening_prices, self.highest_prices, self.lowest_prices,
        #                    self.closing_prices, )
        nan = np.isnan(profits)
        dates, profits = self.dates[~nan], profits[~nan]
        gain_dates, gain_profits = dates[profits > 0], profits[profits > 0]
        loss_dates, loss_profits = dates[profits < 0], profits[profits < 0]
        mp.figure('Trading Simulation', facecolor='lightgray')
        mp.title('Trading Simulation', fontsize=20)
        mp.xlabel('Date', fontsize=14)
        mp.ylabel('Profit', fontsize=14)
        ax = mp.gca()
        ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
        ax.xaxis.set_minor_locator(md.DayLocator())
        ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
        mp.tick_params(labelsize=10)
        mp.grid(linestyle=':')
        if dates.size > 0:
            dates = dates.astype(md.datetime.datetime)
            mp.plot(dates, profits, c='gray',
                    label='Profit')
            mp.axhline(y=profits.mean(), linestyle='--',
                       color='gray')
        if gain_dates.size > 0:
            gain_dates = gain_dates.astype(md.datetime.datetime)
            mp.plot(gain_dates, gain_profits, 'o',
                    c='orangered', label='Gain Profit')
            mp.axhline(y=gain_profits.mean(), linestyle='--',
                       color='orangered')
        if loss_dates.size > 0:
            loss_dates = loss_dates.astype(md.datetime.datetime)
            mp.plot(loss_dates, loss_profits, 'o',
                    c='limegreen', label='Loss Profit')
            mp.axhline(y=loss_profits.mean(), linestyle='--',
                       color='limegreen')
        mp.legend()
        mp.gcf().autofmt_xdate()
        mp.show()

    @staticmethod
    def funcs():
        ary = np.array([45, -89, 561, 36, 45, 75, -15])

        sign = np.sign(ary)

        a = np.array([70, 80, 60, 30, 40])
        d = np.piecewise(
            a,
            [a < 60, a == 60, a > 60],
            [-1, 0, 1])
        print('sign-->', sign)
        print('piecewise-->', d)
        # d = [ 1  1  0 -1 -1]

    def vectorize(self):
        """
            math方法不能处理适量数据
            使用np.vectorize方法将函数矢量化
        """
        x, y = np.array([5, 4, 5]), np.array([4, 21, 11])  # 1对1配对

        res = np.vectorize(self._fun01)(x, y)
        print(res)

    @staticmethod
    def _fun01(x, y):
        return m.sqrt(x + y)


if __name__ == '__main__':
    a01 = Ary()
    # a01.funcs()
    # a01.vectorize()
    a01.vec_profit()
