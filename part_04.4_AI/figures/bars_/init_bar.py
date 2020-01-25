"""
初始化一个柱状图
"""
import numpy as np
import matplotlib.pyplot as mp

apples = np.array([12, 25, 68, 7, 87, 56, 23, 14])
oranges = np.array([21, 89, 74, 23, 65, 85, 7, 54, 12, 45])

# 开始绘制
mp.figure('Bar', facecolor='lightgray')
mp.title('Bar Chart', fontsize=18)
mp.grid(linestyle=":")
x = np.arange(apples.size)
y = np.arange(oranges.size)


mp.bar(x-0.2, apples, 0.4, color='lightgreen', label='Apples')
mp.bar(y+0.2, oranges, 0.4, color='orangered', label='Oranges')
# 设置刻度
mp.xticks(y,['Jan','Feb','Mar',"Apr",'May','Jun',"Jul",'Aug','Sep','Oct','Nov','Dec'])

mp.legend()
mp.show()
