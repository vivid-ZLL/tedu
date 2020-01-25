"""
初始化3d图形
"""
import numpy as np
import matplotlib.pyplot as mp
from mpl_toolkits.mplot3d import axes3d

n = 300
x = np.random.normal(0,1,n)
y = np.random.normal(0,1,n)
z = np.random.normal(0,1,n)

# 绘制三维点阵
mp.figure('3D',facecolor='lightgray')
ax3d = mp.gca(projection='3d')
d = x**2+y**2+z**2
print(d)
ax3d.scatter(x,y,z,s=70,marker='o',c=d,cmap='jet')
ax3d.set_xlabel('x')
ax3d.set_ylabel('y')
ax3d.set_zlabel('z')
mp.show()
