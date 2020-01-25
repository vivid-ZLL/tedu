"""
线性插值算法
"""
"""
scipy提供了常见的插值算法可以通过 一定规律插值器函数。若我们给插值器函数更多的散点x坐标序列，该函数将会返回相应的y坐标序列。

func = si.interp1d(
    离散水平坐标, 
    离散垂直坐标,
    kind=插值算法(缺省为线性插值)
)
"""
# scipy.interpolate
import numpy as np
import scipy.interpolate as si
import matplotlib.pyplot as mp

# 原始数据 11组数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 11)
dis_y = np.sinc(dis_x)
mp.subplot(131)
mp.plot(dis_x, dis_y, label='dis')
mp.legend()
# 通过一系列的散点设计出符合一定规律插值器函数，使用线性插值（kind缺省值）
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 200)
lin_y = linear(lin_x)
mp.subplot(132)
mp.plot(lin_x, lin_y, label='lin', color='red')
mp.legend()
# 三次样条插值 （CUbic Spline Interpolation） 获得一条光滑曲线
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 200)
cub_y = cubic(cub_x)
mp.subplot(133)
mp.plot(cub_x, cub_y, label='cubic', color='violet')
mp.legend()
mp.show()
