"""
二维数组轴向汇总
"""

import numpy as np

ary = np.arange(1, 37).reshape(6, 6)
print(ary)


def apply(data):
    """
        求data均值
    """
    return data.mean()


r = np.apply_along_axis(apply, 1, ary)
# 方法
# 方向 1水平 0垂直
# 对象 ary
print(r)
