"""
刻度操作
"""
import matplotlib.pyplot as mp
import matplotlib.gridspec as mg

locators = [
    'mp.NullLocator()',
    'mp.MaxNLocator(nbins=4)',
]

ax = mp.gca()
for i,locator in enumerate(locators):
    mp.subplot(len(locators),1,i+1)
    mp.figure('locators',facecolor='lightgrey')
    mp.xlim(1,10)  # x方向可视距离
    mp.yticks()
    ax.xaxis.set_major_locator(mp.NullLocator())  # 设置x的刻度定位
    # todo 遍历locators


mp.show()