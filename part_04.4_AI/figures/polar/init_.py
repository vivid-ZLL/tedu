"""
初始化一个极坐标系
"""
import matplotlib.pyplot as mp

mp.figure("Polar", facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Porlar', fontsize=20)
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.show()