"""
数组的组合操作
"""
import numpy as np

#
# a = np.arange(1, 7).reshape(2, 3)
# b = np.arange(7, 13).reshape(2, 3)
# 垂直方向完成组合操作，生成新数组
# print('--------a------------')
# print(a)
# print('--------b------------')
# print(b)
#
# c = np.vstack((a, b))
# print('--------c------------')
# print(c)
# # 垂直方向完成拆分操作，生成两个数组
# print('--------d---e---------')
# d ,e = np.vsplit(c, 2)
# print(d)
# print(e)

# 水平方向操作：
# a = np.arange(1, 7).reshape(2, 3)
# b = np.arange(7, 13).reshape(2, 3)
# # 水平方向完成组合操作，生成新数组
# c = np.hstack((a, b))
# # 水平方向完成拆分操作，生成两个数组
# d, e = np.hsplit(c, 2)


# # 深度方向（3维）完成组合操作，生成新数组
# a = np.arange(1, 7).reshape(2, 3)
# b = np.arange(7, 13).reshape(2, 3)
# print('-----------a----------')
# print(a)
# print('-----------b-----------')
# print(b)
# i = np.dstack((a, b))
# print('-----------i-----------')
# print(i)
# # 深度方向（3维）完成拆分操作，生成两个数组
# # k, l = np.dsplit(i, 2)
# # print(k)
# # print(l)
# ------------------------------------------------

# 一维数组的组合操作
a = np.arange(1, 9)
b = np.arange(9, 17)
print('a:', a)
print('b:', b)
print('-----------行组合-------------')
print(np.row_stack((a, b)))
print('-----------列组合-------------')
print(np.column_stack((a, b)))


