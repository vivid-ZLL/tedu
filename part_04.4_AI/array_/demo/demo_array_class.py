"""
设置dtype的方式
"""
import numpy as np

data = [
    ('alice', [99, 99, 99], 18),
    ('alicinya', [80, 75, 95], 20),
    ('lovince', [90, 90, 95], 18),
]
print('---------第一种设置dtype的方式---------')
a = np.array(data, dtype='U16,3int32,int32')
print(a)
print(type(a[1]))

print('---------第二种设置dtype的方式---------')
b = np.array(data,
             dtype=[
                 ('name', 'str', 16),
                 ('score', 'int32', 3),
                 ('age', 'int32',),
             ]
             )
print(b)
print(b[2]['age'])

print('---推荐------第三种设置dtype的方式-------')
c = np.array(data,
             dtype={
                 'names': ['name', 'score', 'age'],
                 'formats': ['U16', '3int32', 'int32']
             })
print(c)

print('----第四种设置dtype的方式----')
# 第四种设置dtype的方式
d = np.array(data, dtype={'names': ('U5', 0),
                          'scores': ('3int32', 8),
                          'ages': ('int32', 28)})
# 加入数据的存储地址发生重合,那么旧数据会被覆盖,仍可读取部分数据
print(d[0]['names'], d[0]['scores'], d.itemsize)

print('--------存储日期和数据类型-----------')
dates = [
    '2010-11-24', '2011', '2012-02',
    '2010-11-24', '2012-02-01 10:00:00',
]
dates = np.array(dates)
print(dates, dates.dtype)
print('-----------转换时间格式---------------')
dates = dates.astype('M8[D]')
print(dates, dates.dtype)
print(dates[2] - dates[1])
