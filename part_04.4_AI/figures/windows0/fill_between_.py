"""
以某种颜色填充两条曲线的闭合区域
"""
import matplotlib.pyplot as mp
import numpy as np

# 绘制两条曲线 sin(x) cos(x/2)/2
x = np.linspace(0,6 * np.pi,1000)
sinx = np.sin(x)
cosx = np.cos(x/2)/2

mp.figure('Fill',facecolor='lightgray')
mp.title('Fill',size = 18)
mp.grid(linestyle = ":")
mp.plot(x,sinx,color = 'dodgerblue',label = r'$y = sin(x)$')
mp.plot(x,cosx,color = 'orangered',label = r'$y = \frac{1}{2}cos(\frac{x}{2}$)')
mp.fill_between(x,sinx,cosx,sinx > cosx,color = 'dodgerblue',alpha = 0.3)
mp.fill_between(x,sinx,cosx,sinx < cosx,color = 'orangered',alpha = 0.3)
mp.legend()
mp.show()
