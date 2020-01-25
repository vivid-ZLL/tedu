"""
多图像
"""
import matplotlib.pyplot as mp

mp.subplot(1, 2, 1)
mp.plot([0, 1], [1, 2])
mp.subplot(1, 2, 2)
mp.plot([0, 0], [1, 2])

mp.show()
