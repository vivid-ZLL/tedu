"""
初始化3d曲面图
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 1000
x, y = np.meshgrid(np.linspace(-3, 3, n), np.linspace(-3, 3, n))
z = (1 - x / 2 + x ** 5 + y ** 3) * np.exp(-x ** 2 - y ** 2)

# 上述代码可以得到二维数组x,y直接组成坐标点阵
"""
n = 3 
[[-3.  0.  3.]
 [-3.  0.  3.]
 [-3.  0.  3.]]
[[-3. -3. -3.]
 [ 0.  0.  0.]
 [ 3.  3.  3.]]

"""
# z 通过每个坐标的x与y计算而得的高度值
# 模拟采集的海拔高度
mp.figure('I am filename', facecolor='lightgray')
ax3d = mp.gca(projection = '3d')
ax3d.set_xlabel('x')
ax3d.set_ylabel('x')
ax3d.set_zlabel('x')
ax3d.plot_surface(x,y,z,cstride=25,rstride=25,cmap='jet')

mp.show()
