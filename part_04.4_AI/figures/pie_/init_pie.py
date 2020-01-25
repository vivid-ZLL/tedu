"""
初始化饼状图
"""

import numpy as  np
import matplotlib.pyplot as mp

mp.figure('pie', facecolor='lightgray')
# 整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.08, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)

# 画图
mp.figure('Pie Chart')
# 设置x与y轴等比例输出
mp.axis('equal')
mp.pie(values,spaces,labels,colors,'%d%%',shadow=True)

mp.show()
