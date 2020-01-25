# ndarray 数据的掩码操作
import numpy as np

a = np.arange(100)
mask = a % 3 == 0  # mask =  [True False False .......]
print(a[mask])

mask = (a % 3 == 0) & (a % 7 == 0)  # 既是3又是7的整除
mask_ = (a % 3 == 0) | (a % 7 == 0)  # 既是3或者是7的整除

# 　基于索引的掩码
name = np.array(['Alice', 'lovince', 'iris', 'Roy'])
rank = [0, 1, 2, 3]
print(name[rank])
