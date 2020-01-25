"""
刻度网格线
"""
import matplotlib.pyplot as mp

mp.figure('Grid Line', facecolor='lightgray')
ax = mp.gca()

ax.grid(
    which='major',  # 表示主刻度有网格线
    axis='both',    # 默认是both,表示网格线的绘制点
    color='orangered',  #
    linewidth=0.75
)
# 绘制曲线
y = [1, 10, 100, 1000, 100, 10, 1]
mp.plot(y, 'o-', color='blue')
mp.show()
