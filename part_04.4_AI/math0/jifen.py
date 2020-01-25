"""
求定积分
定积分,固定区间围成的面积
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc


def f(x):
    return 2 * x ** 2 + 3 * x + 4


class Intergral:
    @staticmethod
    def basic():
        """
        绘制[-5,5]区间  y = 2x ** 2 + 3x + 4 的曲线
        手动计算定积分
        """
        a, b = -5, 5

        x = np.linspace(a, b, 1000)
        y = f(x)
        mp.plot(x, y, linewidth=5)
        # 微元法求定积分
        n = 50
        px = np.linspace(a, b, n + 1)
        py = f(px)
        print(px)  # npary * 50
        print(py)  # npary * 50
        # 遍历每个梯形,求梯形面积
        area = 0
        for i in range(n):
            area += (py[i + 1] + py[i]) * (px[i + 1] - px[i]) / 2
        print(area)

        mp.show()

    def integrate(self):
        """
        调用API求定积分
        """
        import scipy.integrate as si
        a, b = -5, 5
        r = si.quad(f, a, b)
        #  r  返回值(积分值，最大误差)
        print(r)

    @staticmethod
    def add_patch():
        a, b = -5, 5
        n = 50
        x2 = np.linspace(a, b, n + 1)
        y2 = f(x2)
        mp.plot(x2, y2, linewidth=5)
        for i in range(n):
            mp.gca().add_patch(mc.Polygon([
                [x2[i], 0], [x2[i], y2[i]],
                [x2[i + 1], y2[i + 1]], [x2[i + 1], 0]],
                fc='deepskyblue', ec='dodgerblue',
                alpha=0.5))
        mp.show()


if __name__ == '__main__':
    i01 = Intergral()
    # i01.basic()
    # i01.integrate()
    i01.add_patch()
