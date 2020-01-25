"""
多项式拟合
多项式拟合的目的是为了找到一组p0-pn，使得拟合方程尽可能的与实际样本数据相符合。

X = [x1, x2, ..., xn] - 自变量
Y = [y1, y2, ..., yn] - 实际函数值
Y'= [y1',y2',...,yn'] - 拟合函数值
P = [p0, p1, ..., pn] - 多项式函数中的系数

根据一组样本，并给出最高次幂，求出拟合系数
np.polyfit(X, Y, 最高次幂)->P
多项式运算相关API：

根据拟合系数与自变量求出拟合值, 由此可得拟合曲线坐标样本数据 [X, Y']
np.polyval(P, X)->Y'

多项式函数求导，根据拟合系数求出多项式函数导函数的系数
np.polyder(P)->Q

已知多项式系数Q 求多项式函数的根（与x轴交点的横坐标）
xs = np.roots(Q)

两个多项式函数的差函数的系数（可以通过差函数的根求取两个曲线的交点）
Q = np.polysub(P1, P2)
"""
import numpy as np
import matplotlib.pyplot as mp

# 求多项式 y = 4x3 + 3x2 - 1000x + 1曲线拐点的坐标
P = [4, 3, -1000, 1]
x = np.linspace(-20, 20, 1000)
y = np.polyval(P, x)

# 求多项式函数的导函数
Q = np.polyder(P)
xs = np.roots(Q)
ys = np.polyval(P, xs)

mp.scatter(xs, ys, color='red', s=60)
mp.plot(x, y)
mp.show()


