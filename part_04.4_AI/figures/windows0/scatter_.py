"""
正态分布的散点图
应用:记忆学习,线性回归
"""

import numpy as np
import matplotlib.pyplot as mp

n = 500
# 172 期望均值
# 20  震荡标准差  正负三倍标准差区间 = 绝大部分样本的值
# n   生成个数
x = np.random.normal(175, 5, n)

y = np.random.normal(70, 7, n)

mp.figure('Persons')
mp.title('Persons')
mp.xlabel('height', fontsize=18)
mp.ylabel('weight', fontsize=14)
mp.grid(linestyle=':')
d = (x - 175) ** 2 + (y - 70) ** 2

mp.scatter(
    x,  # x轴坐标数组
    y,  # y轴坐标数组
    marker='o',  # 点型
    s=70,  # 大小
    label='persons',
    # color='dodgerblue',  # 颜色
    c=d,  # 与均值越近颜色越暗,不能与color参数连用
    cmap='jet'  # 渐变颜色条
)
mp.legend()
mp.show()
