"""
读取数据
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


class StockView:

    def __init__(self):
        self.dates, self.opening_prices, self.highest_prices, self.lowest_prices, \
        self.closing_prices, self.volumes = np.loadtxt(
            'files/aapl.csv',
            delimiter=',',
            usecols=(1, 3, 4, 5, 6, 7),
            dtype='M8[D], f8, f8, f8, f8, f8',
            unpack=True,
            converters={1: dmy2ymd}
        )
        self.bhp_dates, self.bhp_opening_prices, self.bhp_highest_prices, self.bhp_lowest_prices, \
        self.bhp_closing_prices, self.bhp_volumes = np.loadtxt(
            'files/bhp.csv',
            delimiter=',',
            usecols=(1, 3, 4, 5, 6, 7),
            dtype='M8[D], f8, f8, f8, f8, f8',
            unpack=True,
            converters={1: dmy2ymd}
        )
        self.vale_dates, self.vale_opening_prices, self.vale_highest_prices, self.vale_lowest_prices, \
        self.vale_closing_prices, self.vale_volumes = np.loadtxt(
            'files/vale.csv',
            delimiter=',',
            usecols=(1, 3, 4, 5, 6, 7),
            dtype='M8[D], f8, f8, f8, f8, f8',
            unpack=True,
            converters={1: dmy2ymd}
        )

    def rate(self):
        """
        绘制两支股票的收益率曲线
        数据平滑处理
        """
        # np.diff([3,4,6,7])  ----> [1,2,3]

        bhp_returns = np.diff(self.bhp_closing_prices) / self.bhp_closing_prices[:-1]
        vale_returns = np.diff(self.vale_closing_prices) / self.vale_closing_prices[:-1]
        dates = self.bhp_dates[:-1]

        # 卷积降噪
        convolve_core = np.hanning(8)
        """
        汉宁卷积,更关系中间,元素权重大
        """
        # print(convolve_core)
        """ [0.          0.1882551  0.61126047 
             0.95048443  0.95048443 0.61126047
             0.1882551   0.        ]
        """
        convolve_core /= convolve_core.sum()
        bhp_returns_convolved = np.convolve(bhp_returns, convolve_core, 'valid')
        vale_returns_convolved = np.convolve(vale_returns, convolve_core, 'valid')
        # 绘制这条曲线
        mp.figure('BHP VALE RETURNS', facecolor='lightgray')
        mp.title('BHP VALE RETURNS', fontsize=20)
        mp.xlabel('Date')
        mp.ylabel('Price')
        self.set_axis()
        dates = dates.astype('M8[D]')
        # 绘制收益线
        mp.plot(dates, bhp_returns, color='dodgerblue', linestyle='--', label='bhp_returns', alpha=0.3)
        mp.plot(dates, vale_returns, color='orangered', linestyle='--', label='vale_returns', alpha=0.3)
        # 绘制卷积降噪线
        mp.plot(dates[7:], bhp_returns_convolved, color='dodgerblue', label='bhp_returns_convolved', alpha=0.5)
        mp.plot(dates[7:], vale_returns_convolved, color='orangered', label='vale_returns_convolved', alpha=0.5)
        mp.plot(dates, np.zeros(29), color='black', linestyle="--")

        mp.gcf().autofmt_xdate()
        mp.legend()
        mp.show()

    def polyfit(self):
        """
            绘制两支股票的差价函数曲线
            拟合差价
            区别欠拟合和过拟合,理解为什么二者的预测结果都不好
        """
        mp.figure('Prices', facecolor='lightgray')
        mp.title('Prices', fontsize=16)
        mp.xlabel('Date', fontsize=14)
        mp.ylabel('Price', fontsize=14)
        mp.grid(linestyle=":")

        self.set_axis()

        dates = self.dates.astype(md.datetime.datetime)
        diff_prices = self.bhp_closing_prices - self.vale_closing_prices
        mp.plot(dates, diff_prices, color='dodgerblue', label='diff prices')

        # 拟合差价函数
        days = dates.astype('M8[D]').astype('int32')
        P = np.polyfit(days, diff_prices, 4)
        # print(P)
        # [ 6.87966990e-05 -4.13383459e+00  9.31471804e+04 -9.32832499e+08  3.50323076e+12]
        poly_prices = np.polyval(P, days)
        # print(poly_prices) # [60.60742188 58.57910156 58.29101562...
        mp.plot(dates, poly_prices, color='orangered', label='Polyfit Line', linewidth=2)

        mp.gcf().autofmt_xdate()

        mp.legend()
        mp.show()

    def plot_prices(self):
        """
            绘制收盘价的折线图
            基本绘制图线
        """

        mp.figure('Prices', facecolor='lightgray')
        mp.title('Prices', fontsize=16)
        mp.xlabel('Date', fontsize=14)
        mp.ylabel('Price', fontsize=14)
        mp.grid(linestyle=":")

        self.set_axis()

        dates = self.dates.astype(md.datetime.datetime)

        mp.plot(dates, self.closing_prices, color='dodgerblue',
                label='closing price', linestyle='--',
                linewidth=2, alpha=0.6)

        mp.legend()
        mp.show()

    @staticmethod
    def set_axis():
        """
            设置横坐标样式
        """
        # 拿到坐标轴
        ax = mp.gca()
        # 设置主刻度定位器为周定位器（每周一显示主刻度文本）
        ax.xaxis.set_major_locator(
            md.WeekdayLocator(byweekday=md.MO))
        ax.xaxis.set_major_formatter(
            md.DateFormatter('%d %b %Y'))
        # 设置次刻度定位器为日定位器
        ax.xaxis.set_minor_locator(md.DayLocator())

    def boll(self):
        """
            绘制股票的布林带
            填充区间
        """
        # 卷积核
        kernel = np.ones(5) / 5  # 此为5日卷积,表示5日均线
        ma52 = np.convolve(self.closing_prices, kernel, 'valid')
        mp.plot(self.dates[4:], ma52, color='red', linewidth=2, label='MA-5days')
        medios = ma52

        stds = np.zeros(self.closing_prices.size - 4)

        for i in range(self.closing_prices.size - 4):
            stds[i] = self.closing_prices[i:i + 5].std()
        stds *= 2

        lowers = medios - stds
        uppers = medios + stds

        # 填充
        mp.fill_between(
            self.dates[4:], uppers, lowers, lowers < uppers,
            color='orangered', alpha=0.2)
        mp.plot(self.dates, self.closing_prices, c='lightgray', label='Closing Price')
        mp.plot(self.dates[4:], medios, c='dodgerblue', label='Medio')
        mp.plot(self.dates[4:], lowers, c='limegreen', label='Lower')
        mp.plot(self.dates[4:], uppers, c='orangered', label='Upper')
        mp.legend()
        mp.show()

    def ave_line(self):
        """
            求
        """
        kernel = np.ones(5) / 5  # 此为5日卷积,表示5日均线
        ma52 = np.convolve(self.closing_prices, kernel, 'valid')
        mp.plot(self.dates[4:], ma52, color='red', linewidth=4, label='MA-5days')

        kernel = np.ones(10) / 10  # 此为10日卷积
        ma52_ = np.convolve(self.closing_prices, kernel, 'valid')
        mp.plot(self.dates[9:], ma52_, color='dodgerblue', linewidth=4, label='MA-10days')
        mp.gcf().autofmt_xdate()
        mp.plot(self.dates, self.closing_prices, linestyle=':', label='price')

        # 加权卷积可以使黄金分割点或死亡分割点向前平移,提前预知
        weights = np.exp(np.linspace(-1, 0, 5))
        weights /= weights.sum()
        # print(weights) # 权重[0.11405072 0.14644403 0.18803785 0.24144538 0.31002201]
        em5 = np.convolve(self.closing_prices, weights[::-1], 'valid')

        mp.legend()
        mp.show()

    def k_line(self):
        rise = self.closing_prices >= self.opening_prices
        color = np.array([('white' if x else 'limegreen') for x in rise])
        # 边框色：涨为红色，跌为绿色
        edgecolor = np.array([('red' if x else 'limegreen') for x in rise])
        # 绘制线条
        mp.bar(self.dates, self.highest_prices - self.lowest_prices, 0.1,
               self.lowest_prices, color=edgecolor)
        # 绘制方块
        mp.bar(self.dates, self.closing_prices - self.opening_prices, 0.8,
               self.opening_prices, color=color, edgecolor=edgecolor)
        mp.plot(self.dates, self.closing_prices, color='dodgerblue',
                label='closing price', linestyle='-',
                linewidth=2, alpha=0.6)
        mp.legend()
        mp.show()


    def obv(self):
        """
            绘制obv线
            柱状图的绘制
        """
        diff_closing_prices = np.diff(self.bhp_closing_prices)
        sign_closing_prices = np.sign(diff_closing_prices)
        obvs = self.bhp_volumes[1:] * sign_closing_prices
        mp.figure('On-Balance Volume', facecolor='lightgray')
        mp.title('On-Balance Volume', fontsize=20)
        mp.xlabel('Date', fontsize=14)
        mp.ylabel('OBV', fontsize=14)
        ax = mp.gca()
        ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
        ax.xaxis.set_minor_locator(md.DayLocator())
        ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
        mp.tick_params(labelsize=10)
        mp.grid(axis='y', linestyle=':')
        dates = self.bhp_dates[1:].astype(md.datetime.datetime)
        mp.bar(dates, obvs, 1.0, color='dodgerblue',
               edgecolor='white', label='OBV')
        mp.legend()
        mp.gcf().autofmt_xdate()
        mp.show()



if __name__ == '__main__':
    s01 = StockView()
    # s01.plot_prices()
    # s01.polyfit()
    # s01.rate()
    # s01.boll()
    s01.ave_line()
    # s01.k_line()
    # s01.obv()
