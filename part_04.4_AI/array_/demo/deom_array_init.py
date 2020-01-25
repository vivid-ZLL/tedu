"""
初始化一个二维数组
"""
import numpy as np

ary = np.array([1, 2, 3, 4, 5, 6])
print(ary, type(ary))
ary.shape = (2, 3)
print('-----shape  size   dtype  data------')
print(ary.shape)  # 维度
print(ary.size)
print(ary.dtype)
print(ary.data)

print('-----------------ary  ---------------')
print(ary)
print('-----------------ary * 3 ---------------')
print(ary * 3)
print('-----------------ary > 3 ---------------')
print(ary > 3)
print('-------------ary + ary----------------')
print(ary + ary)
print('-----------arange------------')
print(np.arange(0, 10, 1))  # [0 1 2 3 4]
print(np.arange(0, 10, 2))  # [0 2 4 6 8]
print('-----------np.zeros-----------')
print(np.zeros(10, dtype='int32'), )
print('-----------np.ones-----------')
print(np.ones((2, 3), dtype='float32'))
print(np.ones(5, dtype='float32') / 5)
print('-----------np.like----模仿参数维度-------')
print(np.zeros_like(ary))
print(np.ones_like(ary))
