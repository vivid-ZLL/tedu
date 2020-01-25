"""
初始化热成像图
以图形的方式显示矩阵
"""
import numpy as np
import matplotlib.pyplot as mp

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)
print(z)

# 二维数组,每个值表示该位置值的颜色
mp.imshow(z,cmap='jet',origin='lower')
mp.show()




