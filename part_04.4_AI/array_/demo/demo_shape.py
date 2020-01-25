"""
数组的变维
"""
import numpy as np

a = np.arange(1, 10)
print(a, a.shape)

print('----------共享数据模式-------------')
b = a.reshape(3,3)
a[0] = 998
print('--------a----------')
print(a, )
print('--------b----------')
print(b, )

print('-------------复制变维模式---------------')
c = b.flatten()
print('--------c----------')
print(c, )
c[2] = 998
print('----------b-------------')
print(b)
print('----------c------------')
print(c)
