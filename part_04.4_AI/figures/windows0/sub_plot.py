"""
合并九宫格
"""

import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

mp.figure('Subplot Layout', facecolor='lightgray')
# 拆分矩阵
rows = 3  # rows:	行数
cols = 3  # cols:	列数
num = 1  # num:	编号
"""
1 2 3
4 5 6
7 8 9
"""
# mp.subplot(3, 3, 1)  # 操作3*3的矩阵中编号为5的子图
#  创建9宫格
for i in range(1, 10):
    mp.subplot(rows, cols, i)
    mp.text(0.5, 0.5, 'alice', ha='center', va='center', size=36, alpha=0.6)
    mp.xticks([])
    mp.yticks([])

# 合并九宫格
gs = mg.GridSpec(3, 3)
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, 'Margatroid',
        ha='center', va='center',  # 文字中心定位,默认定位是第一个字的左下角
        size=18)
mp.xticks([])
mp.yticks([])
# ----------------------

gs = mg.GridSpec(3, 3)
mp.subplot(gs[:2,2 ])
mp.text(0.5, 0.5, 'Margatroid',
        ha='center', va='center',  # 文字中心定位,默认定位是第一个字的左下角
        size=18)
mp.xticks([])
mp.yticks([])
# ----------------------

gs = mg.GridSpec(3, 3)
mp.subplot(gs[2,1: ])
mp.text(0.5, 0.5, 'Margatroid',
        ha='center', va='center',  # 文字中心定位,默认定位是第一个字的左下角
        size=18)
mp.xticks([])
mp.yticks([])
# ----------------------

gs = mg.GridSpec(3, 3)
mp.subplot(gs[ 1: ,0])
mp.text(0.5, 0.5, 'Margatroid',
        ha='center', va='center',  # 文字中心定位,默认定位是第一个字的左下角
        size=18)
mp.xticks([])
mp.yticks([])
# ----------------------




mp.show()
