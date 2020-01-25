"""
多窗口
"""

import matplotlib.pyplot as mp

mp.plot([0, 1], [1, 2])
mp.figure('A', facecolor='gray')
mp.plot([0, 1], [3, 2])
mp.figure('B', facecolor='lightgray')

mp.plot([1, 2], [2, 1])
mp.figure('C', facecolor='gray')
mp.show()
