"""
二维数组的属性
"""
import numpy as np

a = np.arange(1, 9)
print(a, a.shape)
a.shape = (2, 4)
print(a, a.shape)
print(a.dtype)
# a.dtype = 'float32'  # 错误的修改方式
print(a, a.dtype)
b = a.astype('float32')
print(b, b.dtype)
print('-----------len    size  --------------')
print(len(b), b.size)
print('-------------------index-------------------')
c = np.arange(1, 19)
c.shape = (3, 2, 3)
print(c)
print('--------定位4的位置----------')
print(c[0, 1, 0])

print('-------------转回一维列表,注意元素数量------------')
c.shape = (18)
print(c)

print('--------------属性测试---------------')

a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print('shape - 维度', a.shape)
print('dtype - 元素类型', a.dtype)
print('size - 元素数量', a.ndim)
print('ndim - 维数，len(shape)', a.size)
print('itemsize - 元素字节数', a.itemsize)
print('nbytes - 总字节数 = size x itemsize', a.nbytes)
print('real imag- 复数数组的实,虚部数组', a.real, a.imag, sep='\n')
print('T - 数组对象的转置视图', a.T)
print('扁平迭代器', [elem for elem in a.flat])
b = a.tolist()  # 转为python的列表
print(b)
