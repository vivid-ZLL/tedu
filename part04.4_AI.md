## 数据分析 

**什么是数据分析？**

数据分析是指用适当的统计分析方法对收集来的大量数据进行分析，提取有用信息和形成结论而对数据加以详细研究和概括总结的过程。

**典型案例:股票价格分析**

"历史总是惊人的相似",用真实数据论证分析的结果

**使用python做数据分析的常用库**

1. numpy		基础数值算法
2. scipy         科学计算
3. matplotlib      数据可视化
4. pandas           序列高级函数

## numpy概述

1. Numerical Python，数值的Python，补充了Python语言所欠缺的数值计算能力。
2. Numpy是其它数据分析及机器学习库的底层库。
3. Numpy完全标准C语言实现，运行效率充分优化。
4. Numpy开源免费。

### numpy`历史`

1. 1995年，Numeric，Python语言数值计算扩充。
2. 2001年，Scipy->Numarray，多维数组运算。
3. 2005年，Numeric+Numarray->Numpy。
4. 2006年，Numpy脱离Scipy成为独立的项目。

### numpy的核心：多维数组

1. 代码简洁：减少Python代码中的循环。
2. 底层实现：厚内核(C)+薄接口(Python)，保证性能。

## numpy基础

### ndarray数组

用np.ndarray类的对象表示n维数组

```python
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary))
```

#### 内存中的ndarray对象

**元数据（metadata）**

存储对目标数组的描述信息，如：dim count、dimensions、dtype、data等。

**实际数据**

完整的数组数据

将实际数据与元数据分开存放，一方面提高了内存空间的使用效率，另一方面减少对实际数据的访问频率，提高性能。

#### ndarray数组对象的特点

1. Numpy数组是同质数组，即所有元素的数据类型必须相同
2. Numpy数组的下标从0开始，最后一个元素的下标为数组长度减1

#### ndarray数组对象的创建

np.array(任何可被解释为Numpy数组的逻辑结构)

```python
import numpy as np
a = np.array([1, 2, 3, 4, 5, 6])
print(a)
```

np.arange(起始值(0),终止值,步长(1))

```python
import numpy as np
a = np.arange(0, 5, 1)
print(a)
b = np.arange(0, 10, 2)
print(b)
```

np.zeros(数组元素个数, dtype='类型')

```python
import numpy as np
a = np.zeros(10)
print(a)
```

np.ones(数组元素个数, dtype='类型')

```python
import numpy as np
a = np.ones(10)
print(a)
```

#### ndarray对象属性的基本操作

**数组的维度：**np.ndarray.shape       

```python
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary), ary, ary.shape)
#二维数组
ary = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
print(type(ary), ary, ary.shape)
```

**元素的类型：**np.ndarray.dtype

```python
import numpy as np
ary = np.array([1, 2, 3, 4, 5, 6])
print(type(ary), ary, ary.dtype)
#转换ary元素的类型
b = ary.astype(float)
print(type(b), b, b.dtype)
#转换ary元素的类型
c = ary.astype(str)
print(type(c), c, c.dtype)
```

**数组元素的个数：**np.ndarray.size

```python
import numpy as np
ary = np.array([
    [1,2,3,4],
    [5,6,7,8]
])
#观察维度，size，len的区别
print(ary.shape, ary.size, len(ary))
```

**数组元素索引(下标)**

数组对象[..., 页号, 行号, 列号]

下标从0开始，到数组len-1结束。

```python
import numpy as np
a = np.array([[[1, 2],
               [3, 4]],
              [[5, 6],
               [7, 8]]])
print(a, a.shape)
print(a[0])
print(a[0][0])
print(a[0][0][0])
print(a[0, 0, 0])
for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        for k in range(a.shape[2]):
            print(a[i, j, k])
```

#### ndarray对象属性操作详解

**Numpy的内部基本数据类型**

| 类型名       | 类型表示符                          |
| ------------ | ----------------------------------- |
| 布尔型       | bool_                               |
| 有符号整数型 | int8(-128~127)/int16/int32/int64    |
| 无符号整数型 | uint8(0~255)/uint16/uint32/uint64   |
| 浮点型       | float16/float32/float64             |
| 复数型       | complex64/complex128                |
| 字串型       | str_，每个字符用32位Unicode编码表示 |

**自定义复合类型**

```python
# 自定义复合类型
import numpy as np

data=[
	('zs', [90, 80, 85], 15),
	('ls', [92, 81, 83], 16),
	('ww', [95, 85, 95], 15)
]
#第一种设置dtype的方式
a = np.array(data, dtype='U3, 3int32, int32')
print(a)
print(a[0]['f0'], ":", a[1]['f1'])
print("=====================================")
#第二种设置dtype的方式
b = np.array(data, dtype=[('name', 'str_', 2),
                    ('scores', 'int32', 3),
                    ('ages', 'int32', 1)])
print(b[0]['name'], ":", b[0]['scores'])
print("=====================================")

#第三种设置dtype的方式
c = np.array(data, dtype={'names': ['name', 'scores', 'ages'],
                    'formats': ['U3', '3int32', 'int32']})
print(c[0]['name'], ":", c[0]['scores'], ":", c.itemsize)
print("=====================================")

#第四种设置dtype的方式  
d = np.array(data, dtype={'names': ('U3', 0),
                    'scores': ('3int32', 16),
                    'ages': ('int32', 28)})
print(d[0]['names'], d[0]['scores'], d.itemsize)

print("=====================================")

#第五种设置dtype的方式
e = np.array([0x1234, 0x5667],
             dtype=('u2', {'lowc': ('u1', 0),
                            'hignc': ('u1', 1)}))
print('%x' % e[0])
print('%x %x' % (e['lowc'][0], e['hignc'][0]))

print("=====================================")
#测试日期类型数组
f = np.array(['2011', '2012-01-01', '2013-01-01 01:01:01','2011-02-01'])
f = f.astype('M8[D]')
f = f.astype('int32')
print(f[3]-f[0])

print("=====================================")
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print(a.T)

for x in a.flat:
	print(x.imag)

```

**类型字符码**

| 类型              | 字符码                              |
| ----------------- | ----------------------------------- |
| np.bool_          | ?                                   |
| np.int8/16/32/64  | i1/i2/i4/i8                         |
| np.uint8/16/32/64 | u1/u2/u4/u8                         |
| np.float/16/32/64 | f2/f4/f8                            |
| np.complex64/128  | c8/c16                              |
| np.str_           | U<字符数>                           |
| np.datetime64     | M8[Y] M8[M] M8[D] M8[h] M8[m] M8[s] |

**字节序前缀，用于多字节整数和字符串：**
`</>/[=]分别表示小端/大端/硬件字节序。`

**类型字符码格式**

<字节序前缀><维度><类型><字节数或字符数>

| 3i4      | 释义                                                         |
| -------- | ------------------------------------------------------------ |
| 3i4      | 大端字节序，3个元素的一维数组，每个元素都是整型，每个整型元素占4个字节。 |
| <(2,3)u8 | 小端字节序，6个元素2行3列的二维数组，每个元素都是无符号整型，每个无符号整型元素占8个字节。 |
| U7       | 包含7个字符的Unicode字符串，每个字符占4个字节，采用默认字节序。 |

##### ndarray数组对象的维度操作

**视图变维（数据共享）：** reshape() 与 ravel() 

```python
import numpy as np
a = np.arange(1, 9)
print(a)		# [1 2 3 4 5 6 7 8]
b = a.reshape(2, 4)	#视图变维  : 变为2行4列的二维数组
print(b)
c = b.reshape(2, 2, 2) #视图变维    变为2页2行2列的三维数组
print(c)
d = c.ravel()	#视图变维	变为1维数组
print(d)
```

**复制变维（数据独立）：**flatten()

```python
e = c.flatten()
print(e)
a += 10
print(a, e, sep='\n')
```

**就地变维：直接改变原数组对象的维度，不返回新数组**

```python
a.shape = (2, 4)
print(a)
a.resize(2, 2, 2)
print(a)
```

##### ndarray数组切片操作

```python
#数组对象切片的参数设置与列表切面参数类似
#  步长+：默认切从首到尾
#  步长-：默认切从尾到首
数组对象[起始位置:终止位置:步长, ...]
#默认位置步长：1
```

```python
import numpy as np
a = np.arange(1, 10)
print(a)  # 1 2 3 4 5 6 7 8 9
print(a[:3])  # 1 2 3
print(a[3:6])   # 4 5 6
print(a[6:])  # 7 8 9
print(a[::-1])  # 9 8 7 6 5 4 3 2 1
print(a[:-4:-1])  # 9 8 7
print(a[-4:-7:-1])  # 6 5 4
print(a[-7::-1])  # 3 2 1
print(a[::])  # 1 2 3 4 5 6 7 8 9
print(a[:])  # 1 2 3 4 5 6 7 8 9
print(a[::3])  # 1 4 7
print(a[1::3])  # 2 5 8
print(a[2::3])  # 3 6 9
```

**多维数组的切片操作**

```python
import numpy as np
a = np.arange(1, 28)
a.resize(3,3,3)
print(a)
#切出1页 
print(a[1, :, :])		
#切出所有页的1行
print(a[:, 1, :])		
#切出0页的1行1列
print(a[0, :, 1])		
```

##### **ndarray数组的掩码操作**

> 掩码用于获得大数组的一个子集
```python
import numpy as np
a = np.arange(1, 10)
mask = [True, False,True, False,True, False,True, False,True, False]
print(a[mask])
```

##### 多维数组的组合与拆分

垂直方向操作：

```python
import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 垂直方向完成组合操作，生成新数组
c = np.vstack((a, b))
# 垂直方向完成拆分操作，生成两个数组
d, e = np.vsplit(c, 2)
```

水平方向操作：

```python
import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 水平方向完成组合操作，生成新数组 
c = np.hstack((a, b))
# 水平方向完成拆分操作，生成两个数组
d, e = np.hsplit(c, 2)
```

长度不等的数组组合：

```python
import numpy as np
a = np.array([1,2,3,4,5])
b = np.array([1,2,3,4])
# 填充b数组使其长度与a相同
b = np.pad(b, pad_width=(0, 1), mode='constant', constant_values=-1)
print(b)
# 垂直方向完成组合操作，生成新数组
c = np.vstack((a, b))
print(c)
```

深度方向操作：（3维）

```python
import numpy as np
a = np.arange(1, 7).reshape(2, 3)
b = np.arange(7, 13).reshape(2, 3)
# 深度方向（3维）完成组合操作，生成新数组
i = np.dstack((a, b))
# 深度方向（3维）完成拆分操作，生成两个数组
k, l = np.dsplit(i, 2)
```

多维数组组合与拆分的相关函数：

```python
# 通过axis作为关键字参数指定组合的方向，取值如下：
# 若待组合的数组都是二维数组：
#	0: 垂直方向组合
#	1: 水平方向组合
# 若待组合的数组都是三维数组：
#	0: 垂直方向组合
#	1: 水平方向组合
#	2: 深度方向组合
np.concatenate((a, b), axis=0)
# 通过给出的数组与要拆分的份数，按照某个方向进行拆分，axis的取值同上
np.split(c, 2, axis=0)
```

简单的一维数组组合方案

```python
a = np.arange(1,9)		#[1, 2, 3, 4, 5, 6, 7, 8]
b = np.arange(9,17)		#[9,10,11,12,13,14,15,16]
#把两个数组摞在一起成两行
c = np.row_stack((a, b))
print(c)
#把两个数组组合在一起成两列
d = np.column_stack((a, b))
print(d)
```

#### ndarray类的其他属性

- shape - 维度
- dtype - 元素类型
- size - 元素数量
- ndim - 维数，len(shape)
- itemsize - 元素字节数
- nbytes - 总字节数 = size x itemsize
- real - 复数数组的实部数组
- imag - 复数数组的虚部数组
- T - 数组对象的转置视图
- flat - 扁平迭代器

```python
import numpy as np
a = np.array([[1 + 1j, 2 + 4j, 3 + 7j],
              [4 + 2j, 5 + 5j, 6 + 8j],
              [7 + 3j, 8 + 6j, 9 + 9j]])
print('shape:',a.shape)
print('dtype:',a.dtype)
print('ndim:',a.ndim)
print('size:',a.size)
print('itemsize:',a.itemsize)
print('nbytes:',a.nbytes)
print('real,:',a.real, a.imag, sep='\n')
print(a.T)
print([elem for elem in a.flat])
b = a.tolist()
print(b)
```







## matplotlib概述

matplotlib是python的一个绘图库。使用它可以很方便的绘制出版质量级别的图形。

### matplotlib基本功能

1. 基本绘图 （在二维平面坐标系中绘制连续的线）
   1. 设置线型、线宽和颜色  
   2. 设置坐标轴范围
   3. 设置坐标刻度
   4. 设置坐标轴
   5. 图例
   6. 特殊点
   7. 备注
2. 图形对象(图形窗口)
   1. 子图
   2. 刻度定位器
   3. 刻度网格线
   4. 半对数坐标
   5. 散点图
   6. 填充
   7. 条形图
   8. 饼图
   9. 等高线图
   10. 热成像图
   11. 极坐标系
   12. 三维曲面
   13. 简单动画



## matplotlib基本功能详解

### 基本绘图

#### 绘图核心API

案例：绘制一条余弦曲线

```python
import numpy as np
import matplotlib.pyplot as mp

# xarray: <序列> 水平坐标序列
# yarray: <序列> 垂直坐标序列
mp.plot(xarray, yarray)
#显示图表
mp.show()
```

绘制水平线与垂直线：

```python
import numpy as np
import matplotlib.pyplot as mp

# vertical 绘制垂直线
mp.vlines(vval, ymin, ymax, ...)
# horizotal 绘制水平线
mp.hlines(xval, xmin, xmax, ...)
#显示图表
mp.show()
```

#### 线型、线宽和颜色

案例：绘制一条正弦曲线

```python
 
	#	数字
#color: <关键字参数> 颜色
	#	英文颜色单词 或 常见颜色英文单词首字母 或 #495434 或 (1,1,1) 或 (1,1,1,1)
#alpha: <关键字参数> 透明度
	#	浮点数值
mp.plot(xarray, yarray, linestyle='', linewidth=1, color='', alpha=0.5)
```

#### 设置坐标轴范围 

案例：把坐标轴范围设置为 -π ~ π

```python
#x_limt_min:	<float> x轴范围最小值
#x_limit_max:	<float> x轴范围最大值
mp.xlim(x_limt_min, x_limit_max)
#y_limt_min:	<float> y轴范围最小值
#y_limit_max:	<float> y轴范围最大值
mp.ylim(y_limt_min, y_limit_max)
```

#### 设置坐标刻度

案例：把横坐标的刻度显示为：0, π/2, π, 3π/2, 2π

```python
#x_val_list: 	x轴刻度值序列
#x_text_list:	x轴刻度标签文本序列 [可选]
mp.xticks(x_val_list , x_text_list )
#y_val_list: 	y轴刻度值序列
#y_text_list:	y轴刻度标签文本序列 [可选]
mp.yticks(y_val_list , y_text_list )
```

***刻度文本的特殊语法*** -- *LaTex排版语法字符串*

```python
r'$x^n+y^n=z^n$',   r'$\int\frac{1}{x} dx = \ln |x| + C$',     r'$-\frac{\pi}{2}$'
```

$$
x^n+y^n=z^n,  \int\frac{1}{x} dx = \ln |x| + C,     -\frac{\pi}{2}
$$

#### 设置坐标轴  

坐标轴名：left / right / bottom / top

```python
# 获取当前坐标轴字典，{'left':左轴,'right':右轴,'bottom':下轴,'top':上轴 }
ax = mp.gca()
# 获取其中某个坐标轴
axis = ax.spines['坐标轴名']
# 设置坐标轴的位置。 该方法需要传入2个元素的元组作为参数
# type: <str> 移动坐标轴的参照类型  一般为'data' (以数据的值作为移动参照值)
# val:  参照值
axis.set_position((type, val))
# 设置坐标轴的颜色
# color: <str> 颜色值字符串
axis.set_color(color)
```

案例：设置坐标轴至中心。

```python
#设置坐标轴
ax = mp.gca()
axis_b = ax.spines['bottom']
axis_b.set_position(('data', 0))
axis_l = ax.spines['left']
axis_l.set_position(('data', 0))
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
```

#### 图例

显示两条曲线的图例，并测试loc属性。

```python
# 再绘制曲线时定义曲线的label
# label: <关键字参数 str> 支持LaTex排版语法字符串
mp.plot(xarray, yarray ... label='', ...)
# 设置图例的位置
# loc: <关键字参数> 制定图例的显示位置 (若不设置loc，则显示默认位置)
#	 ===============   =============
#    Location String   Location Code
#    ===============   =============
#    'best'            0
#    'upper right'     1
#    'upper left'      2
#    'lower left'      3
#    'lower right'     4
#    'right'           5
#    'center left'     6
#    'center right'    7
#    'lower center'    8
#    'upper center'    9
#    'center'          10
#    ===============   =============
mp.legend(loc='')
```

#### 特殊点

案例：绘制当x=3π/4时两条曲线上的特殊点。

```python
# xarray: <序列> 所有需要标注点的水平坐标组成的序列
# yarray: <序列> 所有需要标注点的垂直坐标组成的序列
mp.scatter(xarray, yarray, 
           marker='', 		#点型 ~ matplotlib.markers
           s='', 			#大小
           edgecolor='', 	#边缘色
           facecolor='',	#填充色
           zorder=3			#绘制图层编号 （编号越大，图层越靠上）
)
```

*marker点型可参照：help(matplotlib.markers)*

*也可参照附录： matplotlib point样式*



#### 备注

案例：为在某条曲线上的点添加备注，指明函数方程与值。

```python
# 在图表中为某个点添加备注。包含备注文本，备注箭头等图像的设置。
mp.annotate(
    r'$\frac{\pi}{2}$',			#备注中显示的文本内容
    xycoords='data',			#备注目标点所使用的坐标系（data表示数据坐标系）
    xy=(x, y),	 				#备注目标点的坐标
    textcoords='offset points',	#备注文本所使用的坐标系（offset points表示参照点的偏移坐标系）
    xytext=(x, y),				#备注文本的坐标
    fontsize=14,				#备注文本的字体大小
    arrowprops=dict()			#使用字典定义文本指向目标点的箭头样式
)
```

arrowprops参数使用字典定义指向目标点的箭头样式

```python
#arrowprops字典参数的常用key
arrowprops=dict(
	arrowstyle='',		#定义箭头样式
    connectionstyle=''	#定义连接线的样式
)
```

箭头样式（arrowstyle）字符串如下

```
============   =============================================
Name           Attrs
============   =============================================
  '-'          None
  '->'         head_length=0.4,head_width=0.2
  '-['         widthB=1.0,lengthB=0.2,angleB=None
  '|-|'        widthA=1.0,widthB=1.0
  '-|>'        head_length=0.4,head_width=0.2
  '<-'         head_length=0.4,head_width=0.2
  '<->'        head_length=0.4,head_width=0.2
  '<|-'        head_length=0.4,head_width=0.2
  '<|-|>'      head_length=0.4,head_width=0.2
  'fancy'      head_length=0.4,head_width=0.4,tail_width=0.4
  'simple'     head_length=0.5,head_width=0.5,tail_width=0.2
  'wedge'      tail_width=0.3,shrink_factor=0.5
============   =============================================
```

连接线样式（connectionstyle）字符串如下

```
============   =============================================
Name           Attrs
============   =============================================
  'angle' 		angleA=90,angleB=0,rad=0.0
  'angle3' 		angleA=90,angleB=0`   
  'arc'			angleA=0,angleB=0,armA=None,armB=None,rad=0.0
  'arc3' 		rad=0.0
  'bar' 		armA=0.0,armB=0.0,fraction=0.3,angle=None
============   =============================================
```



### 图形对象（图形窗口）

案例：绘制两个窗口，一起显示。

```python
# 手动构建 matplotlib 窗口
mp.figure(
    '',					#窗口标题栏文本 
    figsize=(4, 3),		#窗口大小 <元组>
    dpi=120,			#像素密度
	facecolor=''		#图表背景色
)
mp.show()
```

mp.figure方法不仅可以构建一个新窗口，如果已经构建过title='xxx'的窗口，又使用figure方法构建了title='xxx' 的窗口的话，mp将不会创建新的窗口，而是把title='xxx'的窗口置为当前操作窗口。

**设置当前窗口的参数**

案例：测试窗口相关参数

```python
# 设置图表标题 显示在图表上方
mp.title(title, fontsize=12)
# 设置水平轴的文本
mp.xlabel(x_label_str, fontsize=12)
# 设置垂直轴的文本
mp.ylabel(y_label_str, fontsize=12)
# 设置刻度参数   labelsize设置刻度字体大小
mp.tick_params(..., labelsize=8, ...)
# 设置图表网格线  linestyle设置网格线的样式
	#	-  or solid 粗线
	#   -- or dashed 虚线
	#   -. or dashdot 点虚线
	#   :  or dotted 点线
mp.grid(linestyle='')
# 设置紧凑布局，把图表相关参数都显示在窗口中
mp.tight_layout() 
```

#### 子图

**矩阵式布局**

绘制矩阵式子图布局相关API：

```python
mp.figure('Subplot Layout', facecolor='lightgray')
# 拆分矩阵
	# rows:	行数
    # cols:	列数
    # num:	编号
mp.subplot(rows, cols, num)
	#	1 2 3
	#	4 5 6
	#	7 8 9 
mp.subplot(3, 3, 5)		#操作3*3的矩阵中编号为5的子图
mp.subplot(335)			#简写
```

案例：绘制9宫格矩阵式子图，每个子图中写一个数字。

```python
mp.figure('Subplot Layout', facecolor='lightgray')

for i in range(9):
	mp.subplot(3, 3, i+1)
	mp.text(
		0.5, 0.5, i+1, 
		ha='center',
		va='center',
		size=36,
		alpha=0.5,
		withdash=False
	)
	mp.xticks([])
	mp.yticks([])

mp.tight_layout()
mp.show()
```

**网格式布局**

网格式布局支持单元格的合并。

绘制网格式子图布局相关API：

```python
import matplotlib.gridspec as mg
mp.figure('Grid Layout', facecolor='lightgray')
# 调用GridSpec方法拆分网格式布局
# rows:	行数
# cols:	列数
# gs = mg.GridSpec(rows, cols)	拆分成3行3列
gs = mg.GridSpec(3, 3)	
# 合并0行与0、1列为一个子图表
mp.subplot(gs[0, :2])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()
```

案例：绘制一个自定义网格布局。

```python
import matplotlib.gridspec as mg
mp.figure('GridLayout', facecolor='lightgray')
gridsubs = mp.GridSpec(3, 3)
# 合并0行、0/1列为一个子图
mp.subplot(gridsubs[0, :2])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36)
mp.tight_layout()
mp.xticks([])
mp.yticks([])
```

**自由式布局**

自由式布局相关API：

```python
mp.figure('Flow Layout', facecolor='lightgray')
# 设置图标的位置，给出左下角点坐标与宽高即可
# left_bottom_x: 坐下角点x坐标
# left_bottom_x: 坐下角点y坐标
# width:		 宽度
# height:		 高度
# mp.axes([left_bottom_x, left_bottom_y, width, height])
mp.axes([0.03, 0.03, 0.94, 0.94])
mp.text(0.5, 0.5, '1', ha='center', va='center', size=36)
mp.show()
```

案例：测试自由式布局，定位子图。

```python
mp.figure('FlowLayout', facecolor='lightgray')

mp.axes([0.1, 0.2, 0.5, 0.3])
mp.text(0.5, 0.5, 1, ha='center', va='center', size=36)
mp.show()
```

#### 刻度定位器

刻度定位器相关API：

```python
# 获取当前坐标轴
ax = mp.gca()
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.NullLocator())
# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
```

案例：绘制一个数轴。

```python
mp.figure('Locators', face
ax.gridcolor='lightgray')
# 获取当前坐标轴
ax = mp.gca()
# 隐藏除底轴以外的所有坐标轴
ax.spines['left'].set_color('none')
ax.spines['top'].set_color('none')
ax.spines['right'].set_color('none')
# 将底坐标轴调整到子图中心位置
ax.spines['bottom'].set_position(('data', 0))
# 设置水平坐标轴的主刻度定位器
ax.xaxis.set_major_locator(mp.NullLocator())
# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
# 标记所用刻度定位器类名 
mp.text(5, 0.3, 'NullLocator()', ha='center', size=12)
```

案例：使用for循环测试刻度器样式：

```python
locators = ['mp.NullLocator()', 'mp.MaxNLocator(nbins=4)']
	
for i, locator in enumerate(locators):
    mp.subplot(len(locators), 1, i+1)
	mp.xlim(0, 10)
	mp.ylim(-1, 1)
	mp.yticks([])
	# 获取当前坐标轴
	ax = mp.gca()
	# 隐藏除底轴以外的所有坐标轴
	ax.spines['left'].set_color('none')
	ax.spines['top'].set_color('none')
	ax.spines['right'].set_color('none')
	# 将底坐标轴调整到子图中心位置
	ax.spines['bottom'].set_position(('data', 0))
	# 设置水平坐标轴的主刻度定位器
	ax.xaxis.set_major_locator(eval( ))
	# 设置水平坐标轴的次刻度定位器为多点定位器，间隔0.1
	ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
	mp.plot(np.arange(11), np.zeros(11), c='none')
	# 标记所用刻度定位器类名
	mp.text(5, 0.3, locator, ha='center', size=12)
```

常用刻度器如下

```python
# 空定位器：不绘制刻度
mp.NullLocator()
# 最大值定位器：
# 最多绘制nbins+1个刻度
mp.MaxNLocator(nbins=3)
# 定点定位器：根据locs参数中的位置绘制刻度
mp.FixedLocator(locs=[0, 2.5, 5, 7.5, 10])
# 自动定位器：由系统自动选择刻度的绘制位置
mp.AutoLocator()
# 索引定位器：由offset确定起始刻度，由base确定相邻刻度的间隔
mp.IndexLocator(offset=0.5, base=1.5)
# 多点定位器：从0开始，按照参数指定的间隔(缺省1)绘制刻度
mp.MultipleLocator()
# 线性定位器：等分numticks-1份，绘制numticks个刻度
mp.LinearLocator(numticks=21)
# 对数定位器：以base为底，绘制刻度
mp.LogLocator(base=2)
```

#### 刻度网格线

绘制刻度网格线的相关API：

```python
ax = mp.gca()
#绘制刻度网格线
ax.grid(
    which='',		# 'major'/'minor' <-> '主刻度'/'次刻度' 
    axis='',		# 'x'/'y'/'both' <-> 绘制x或y轴
    linewidth=1, 	# 线宽
    linestyle='', 	# 线型
    color='',		# 颜色
	alpha=0.5		# 透明度
)
```

案例：绘制曲线 [1, 10, 100, 1000, 100, 10, 1]，然后设置刻度网格线，测试刻度网格线的参数。

```python
y = np.array([1, 10, 100, 1000, 100, 10, 1])
mp.figure('Normal & Log', facecolor='lightgray')
mp.subplot(211)
mp.title('Normal', fontsize=20)
mp.ylabel('y', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(mp.MultipleLocator(1.0))
ax.xaxis.set_minor_locator(mp.MultipleLocator(0.1))
ax.yaxis.set_major_locator(mp.MultipleLocator(250))
ax.yaxis.set_minor_locator(mp.MultipleLocator(50))
mp.tick_params(labelsize=10)
ax.grid(which='major', axis='both', linewidth=0.75,
        linestyle='-', color='orange')
ax.grid(which='minor', axis='both', linewidth=0.25,
        linestyle='-', color='orange')
mp.plot(y, 'o-', c='dodgerblue', label='plot')
mp.legend()
```

#### 半对数坐标 

y轴将以指数方式递增。 基于半对数坐标绘制第二个子图，表示曲线：[1, 10, 100, 1000, 100, 10, 1]。

```python
mp.figure('Grid', facecolor='lightgray')
y = [1, 10, 100, 1000, 100, 10, 1]
mp.semilogy(y)
mp.show()
```

#### 散点图

可以通过每个点的坐标、颜色、大小和形状表示不同的特征值。

| 身高 | 体重 | 性别 | 年龄段 | 种族 |
| ---- | ---- | ---- | ------ | ---- |
| 180  | 80   | 男   | 中年   | 亚洲 |
| 160  | 50   | 女   | 青少   | 美洲 |

绘制散点图的相关API：

```python
mp.scatter(
    x, 					# x轴坐标数组
    y,					# y轴坐标数组
    marker='', 			# 点型
    s=10,				# 大小
    color='',			# 颜色
    edgecolor='', 		# 边缘颜色
    facecolor='',		# 填充色
    zorder=''			# 图层序号
)
```

numpy.random提供了normal函数用于产生符合 正态分布 的随机数 

```python
n = 100
# 172:	期望值
# 10:	标准差
# n:	数字生成数量
x = np.random.normal(172, 20, n)
y = np.random.normal(60, 10, n)
```

案例：绘制平面散点图。

```python
mp.figure('scatter', facecolor='lightgray')
mp.title('scatter')
mp.scatter(x, y)
mp.show()
```

设置点的颜色

```python
mp.scatter(x, y, c='red')			#直接设置颜色
d = (x-172)**2 + (y-60)**2
mp.scatter(x, y, c=d, cmap='jet')	#以c作为参数，取cmap颜色映射表中的颜色值
```

*cmap颜色映射表参照附件：cmap颜色映射表*

#### 填充

以某种颜色自动填充两条曲线的闭合区域。

```python
mp.fill_between(
	x,				# x轴的水平坐标
    sin_x,			# 下边界曲线上点的垂直坐标
    cos_x,			# 上边界曲线上点的垂直坐标
    sin_x<cos_x, 	# 填充条件，为True时填充
    color='', 		# 填充颜色
    alpha=0.2		# 透明度
)
```

案例：绘制两条曲线： sin_x = sin(x)    cos_x = cos(x / 2) / 2	[0-8π]  

```python
n = 1000
x = np.linspace(0, 8 * np.pi, n)
sin_y = np.sin(x)
cos_y = np.cos(x / 2) / 2
mp.figure('Fill', facecolor='lightgray')
mp.title('Fill', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x, sin_y, c='dodgerblue',
        label=r'$y=sin(x)$')
mp.plot(x, cos_y, c='orangered',
        label=r'$y=\frac{1}{2}cos(\frac{x}{2})$')
mp.fill_between(x, cos_y, sin_y, cos_y < sin_y,
                color='dodgerblue', alpha=0.5)
mp.fill_between(x, cos_y, sin_y, cos_y > sin_y,
                color='orangered', alpha=0.5)
mp.legend()
mp.show()
```

#### 条形图（柱状图）

绘制柱状图的相关API：

```python
mp.figure('Bar', facecolor='lightgray')
mp.bar(
	x,				# 水平坐标数组
    y,				# 柱状图高度数组
    width,			# 柱子的宽度
    color='', 		# 填充颜色
    label='',		#
    alpha=0.2		#
)
```

案例：先以柱状图绘制苹果12个月的销量，然后再绘制橘子的销量。

```python
apples = np.array([30, 25, 22, 36, 21, 29, 20, 24, 33, 19, 27, 15])
oranges = np.array([24, 33, 19, 27, 35, 20, 15, 27, 20, 32, 20, 22])
mp.figure('Bar'  , facecolor='lightgray')
mp.title('Bar', font size=20)
mp.xlabel('Month', fontsize=14)
mp.ylabel('Price', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
mp.ylim((0, 40))
x = np.arange(len(apples))
mp.bar(x-0.2, apples, 0.4, color='dodgerblue',label='Apple')
mp.bar(x + 0.2, oranges, 0.4, color='orangered',label='Orange', alpha=0.75)
mp.xticks(x, [
    'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'])
mp.legend()
mp.show()
```

#### 饼图

绘制饼状图的基本API：

```python
mp.pie(
    values, 		# 值列表		
    spaces, 		# 扇形之间的间距列表
    labels, 		# 标签列表
    colors, 		# 颜色列表
    '%d%%',			# 标签所占比例格式
	shadow=True, 	# 是否显示阴影
    startangle=90	# 逆时针绘制饼状图时的起始角度
    radius=1		# 半径
)
```

案例：绘制饼状图显示5门语言的流行程度：

```python
mp.figure('pie', facecolor='lightgray')
#整理数据
values = [26, 17, 21, 29, 11]
spaces = [0.05, 0.01, 0.01, 0.01, 0.01]
labels = ['Python', 'JavaScript',
          'C++', 'Java', 'PHP']
colors = ['dodgerblue', 'orangered',
          'limegreen', 'violet', 'gold']
mp.figure('Pie', facecolor='lightgray')
mp.title('Pie', fontsize=20)
# 等轴比例
mp.axis('equal')
mp.pie(
    values, 		# 值列表		
    spaces, 		# 扇形之间的间距列表
    labels, 		# 标签列表
    colors, 		# 颜色列表
    '%d%%',			# 标签所占比例格式
	shadow=True, 	# 是否显示阴影
    startanle=90	# 逆时针绘制饼状图时的起始角度
    radius=1		# 半径
)
```



## 附录



### matplotlib colors颜色字符串



![matplotlib_colors](C:/Users/Administrator/Desktop/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%AC%94%E8%AE%B0/matplotlib_images/matplotlib_colors.png)





### matplotlib point样式

![matplotlib_markers](C:/Users/Administrator/Desktop/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%AC%94%E8%AE%B0/matplotlib_images/matplotlib_markers.png)



### laTeX语法表示数学符号示例

![LaTeX_eg](C:/Users/Administrator/Desktop/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%AC%94%E8%AE%B0/matplotlib_images/LaTeX_eg.gif)



### LaTeX语法集合

![laTex_](C:/Users/Administrator/Desktop/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%AC%94%E8%AE%B0/matplotlib_images/laTex_.png)

### cmap颜色映射表

![matplotlib_cmap](C:/Users/Administrator/Desktop/%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90%E7%AC%94%E8%AE%B0/matplotlib_images/matplotlib_cmap.png)





#### 等高线图

组成等高线需要网格点坐标矩阵，也需要每个点的高度。所以等高线属于3D数学模型范畴。

绘制等高线的相关API：

```python
mp.contourf(x, y, z, 8, cmap='jet')
cntr = mp.contour(
    x, 					# 网格坐标矩阵的x坐标 （2维数组）
    y, 					# 网格坐标矩阵的y坐标 （2维数组）
    z, 					# 网格坐标矩阵的z坐标 （2维数组）
    8, 					# 把等高线绘制成8部分
    colors='black',		# 等高线的颜色
	linewidths=0.5		# 线宽
)
```

案例：生成网格坐标矩阵，并且绘制等高线：

```python
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('Contour', facecolor='lightgray')
mp.title('Contour', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
# 绘制等高线图
mp.contourf(x, y, z, 8, cmap='jet')
cntr = mp.contour(x, y, z, 8, colors='black',
                  linewidths=0.5)
# 为等高线图添加高度标签
mp.clabel(cntr, inline_spacing=1, fmt='%.1f',
          fontsize=10)
mp.show()
```

#### 热成像图

用图形的方式显示矩阵及矩阵中值的大小
1 2 3
4 5 6
7 8 9

绘制热成像图的相关API：

```python
# 把矩阵z图形化，使用cmap表示矩阵中每个元素值的大小
# origin: 坐标轴方向
#    upper: 缺省值，原点在左上角
#    lower: 原点在左下角
mp.imshow(z, cmap='jet', origin='low')
```

使用颜色条显示热度值：

```python
mp.colorbar()
```

#### 极坐标系

与笛卡尔坐标系不同，某些情况下极坐标系适合显示与角度有关的图像。例如雷达等。极坐标系可以描述极径&rho;与极角&theta;的线性关系。

```python
mp.figure("Polar", facecolor='lightgray')
mp.gca(projection='polar')
mp.title('Porlar', fontsize=20)
mp.xlabel(r'$\theta$', fontsize=14)
mp.ylabel(r'$\rho$', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.show()
```

在极坐标系中绘制曲线：

```python
#准备数据
t = np.linspace(0, 4*np.pi, 1000)
r = 0.8 * t
mp.plot(t, r)
mp.show()
```

案例，在极坐标系中绘制正弦函数。 y=3 sin(6x)

```python
x = np.linspace(0, 6*np.pi, 1000)
y = 3*np.sin(6*x)
mp.plot(x, y)
```

#### 3D图像绘制

 matplotlib支持绘制三维曲面。若希望绘制三维曲面，需要使用axes3d提供的3d坐标系。

```python
from mpl_toolkits.mplot3d import axes3d
ax3d = mp.gca(projection='3d')   # class axes3d
```

matplotlib支持绘制三维点阵、三维曲面、三维线框图：

```python
ax3d.scatter(..)		# 绘制三维点阵
ax3d.plot_surface(..)	# 绘制三维曲面
ax3d.plot_wireframe(..)	# 绘制三维线框图
```

3d散点图的绘制相关API：

```python
ax3d.scatter(
    x, 				# x轴坐标数组
    y,				# y轴坐标数组
    marker='', 		# 点型
    s=10,			# 大小
    zorder='',		# 图层序号
    color='',		# 颜色
    edgecolor='', 	# 边缘颜色
    facecolor='',	# 填充色
    c=v,			# 颜色值 根据cmap映射应用相应颜色
    cmap=''			# 
)
```

案例：随机生成3组坐标，程标准正态分布规则，并且绘制它们。

```python
n = 1000
x = np.random.normal(0, 1, n)
y = np.random.normal(0, 1, n)
z = np.random.normal(0, 1, n)
d = np.sqrt(x ** 2 + y ** 2 + z ** 2)
mp.figure('3D Scatter')
ax = mp.gca(projection='3d')  # 创建三维坐标系
mp.title('3D Scatter', fontsize=20)
ax.set_xlabel('x', fontsize=14)
ax.set_ylabel('y', fontsize=14)
ax.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
ax.scatter(x, y, z, s=60, c=d, cmap='jet_r', alpha=0.5)
mp.show()
```

3d平面图的绘制相关API：

```python
ax3d.plot_surface(
    x, 					# 网格坐标矩阵的x坐标 （2维数组）
    y, 					# 网格坐标矩阵的y坐标 （2维数组）
    z, 					# 网格坐标矩阵的z坐标 （2维数组）
    rstride=30,			# 行跨距
    cstride=30, 		# 列跨距
    cmap='jet'			# 颜色映射
)
```

案例：绘制3d平面图

```python
n = 1000
# 生成网格化坐标矩阵
x, y = np.meshgrid(np.linspace(-3, 3, n),
                   np.linspace(-3, 3, n))
# 根据每个网格点坐标，通过某个公式计算z高度坐标
z = (1 - x/2 + x**5 + y**3) * np.exp(-x**2 - y**2)
mp.figure('3D', facecolor='lightgray')

ax3d = mp.gca(projection='3d')
mp.title('3D', fontsize=20)
ax3d.set_xlabel('x', fontsize=14)
ax3d.set_ylabel('y', fontsize=14)
ax3d.set_zlabel('z', fontsize=14)
mp.tick_params(labelsize=10)
# 绘制3D平面图
# rstride: 行跨距
# cstride: 列跨距 
ax3d.plot_surface(x,y,z,rstride=30,cstride=30, cmap='jet')
```

案例：3d线框图的绘制

```python
# 绘制3D平面图 
# rstride: 行跨距
# cstride: 列跨距 
ax3d.plot_wireframe(x,y,z,rstride=30,cstride=30, 
	linewidth=1, color='dodgerblue')
```

#### 简单动画

动画即是在一段时间内快速连续的重新绘制图像的过程。

matplotlib提供了方法用于处理简单动画的绘制。定义update函数用于即时更新图像。

```python
import matplotlib.animation as ma
#定义更新函数行为
def update(number):
    pass
# 每隔10毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：	获取当前窗口
# update：	更新函数
# interval：	间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=10)
mp.show()
```

案例：随机生成各种颜色的100个气泡。让他们不断的增大。

```python
#自定义一种可以存放在ndarray里的类型，用于保存一个球
ball_type = np.dtype([
	('position', float, 2),  # 位置(水平和垂直坐标)
    ('size', float, 1),      # 大小
    ('growth', float, 1),    # 生长速度
    ('color', float, 4)])    # 颜色(红、绿、蓝和透明度)

#随机生成100个点对象
n = 100
balls = np.zeros(100, dtype=ball_type)
balls['position']=np.random.uniform(0, 1, (n, 2))
balls['size']=np.random.uniform(40, 70, n)
balls['growth']=np.random.uniform(10, 20, n)
balls['color']=np.random.uniform(0, 1, (n, 4))

mp.figure("Animation", facecolor='lightgray')
mp.title("Animation", fontsize=14)
mp.xticks 
mp.yticks(())

sc = mp.scatter(
	balls['position'][:, 0], 
	balls['position'][:, 1], 
	balls['size'], 
	color=balls['color'], alpha=0.5)
	
#定义更新函数行为
def update(number):
	balls['size'] += balls['growth']
	#每次让一个气泡破裂，随机生成一个新的
	boom_ind = number % n
	balls[boom_ind]['size']=np.random.uniform(40, 70, 1)
	balls[boom_ind]['position']=np.random.uniform(0, 1, (1, 2))
	# 重新设置属性
	sc.set_sizes(balls['size'])
	sc.set_offsets(balls['position'])
	
# 每隔30毫秒执行一次update更新函数，作用于mp.gcf()当前窗口对象
# mp.gcf()：	获取当前窗口
# update：		更新函数
# interval：	间隔时间（单位：毫秒）
anim = ma.FuncAnimation(mp.gcf(), update, interval=30)
mp.show()
```

使用生成器函数提供数据，实现动画绘制

在很多情况下，绘制动画的参数是动态获取的，matplotlib支持定义generator生成器函数，用于生成数据，把生成的数据交给update函数更新图像：

```python
import matplotlib.animation as ma
#定义更新函数行为
def update(data):
    t, v = data
    ...
    pass

def generator():
	yield t, v
        
# 每隔10毫秒将会先调用生成器，获取生成器返回的数据，
# 把生成器返回的数据交给并且调用update函数，执行更新图像函数
anim = ma.FuncAnimation(mp.gcf(), update, generator,interval=10)
```

案例：绘制信号曲线：y=sin(2 * π * t) * exp(sin(0.2 * π * t))，数据通过生成器函数生成，在update函数中绘制曲线。

```python
mp.figure("Signal", facecolor='lightgray')
mp.title("Signal", fontsize=14)
mp.xlim(0, 10)
mp.ylim(-3, 3)
mp.grid(linestyle='--', color='lightgray', alpha=0.5)
pl = mp.plot([], [], color='dodgerblue', label='Signal')[0]
pl.set_data([],[])

x = 0

def update(data):
	t, v = data
	x, y = pl.get_data()
	x.append(t)
	y.append(v)
	#重新设置数据源
	pl.set_data(x, y)
	#移动坐标轴
	if(x[-1]>10):
		mp.xlim(x[-1]-10, x[-1])

def y_generator():
	global x
	y = np.sin(2 * np.pi * x) * np.exp(np.sin(0.2 * np.pi * x))
	yield (x, y)
	x += 0.05

anim = ma.FuncAnimation(mp.gcf(), update, y_generator, interval=20)
mp.tight_layout()
mp.show()
```



## numpy常用函数

### 加载文件

numpy提供了函数用于加载逻辑上可被解释为二维数组的文本文件，格式如下：

```
数据项1 <分隔符> 数据项2 <分隔符> ... <分隔符> 数据项n
例如：
AA,AA,AA,AA,AA
BB,BB,BB,BB,BB
...
或：
AA:AA:AA:AA:AA
BB:BB:BB:BB:BB
...
```

调用numpy.loadtxt()函数可以直接读取该文件并且获取ndarray数组对象：

```python
import numpy as np
# 直接读取该文件并且获取ndarray数组对象 
# 返回值：
#     unpack=False：返回一个二维数组
#     unpack=True： 多个一维数组
np.loadtxt(
    '../aapl.csv',			# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3),			# 读取1、3两列 （下标从0开始）
    unpack=False,			# 是否按列拆包
    dtype='U10, f8',		# 制定返回每一列数组中元素的类型
    converters={1:func}		# 转换器函数字典
)    
```

案例：读取aapl.csv文件，得到文件中的信息：

```python
import numpy as np
import datetime as dt
# 日期转换函数
def dmy2ymd(dmy):
	dmy = str(dmy, encoding='utf-8')
	time = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
	t = time.strftime('%Y-%m-%d')
	return t
dates, opening_prices,highest_prices, \
	lowest_prices, closeing_pric es  = np.loadtxt(
    '../data/aapl.csv',		# 文件路径
    delimiter=',',			# 分隔符
    usecols=(1, 3, 4, 5, 6),			# 读取1、3两列 （下标从0开始）
    unpack=True,
    dtype='M8[D], f8, f8, f8, f8',		# 制定返回每一列数组中元素的类型
    converters={1:dmy2ymd})
```

案例：使用matplotlib绘制K线图

1. 绘制dates与收盘价的折线图：

```python
import numpy as np
import datetime as dt
import matplotlib.pyplot as mp
import matplotlib.dates as md

# 绘制k线图，x为日期
mp.figure('APPL K', facecolor='lightgray')
mp.title('APPL K')
mp.xlabel('Day', fontsize=12)
mp.ylabel('Price', fontsize=12)

#拿到坐标轴
ax = mp.gca()
#设置主刻度定位器为周定位器（每周一显示主刻度文本）
ax.xaxis.set_major_locator( md.WeekdayLocator(byweekday=md.MO) )
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
#设置次刻度定位器为日定位器 
ax.xaxis.set_minor_locator(md.DayLocator())
mp.tick_params(labelsize=8)
dates = dates.astype(md.datetime.datetime)

mp.plot(dates, opening_prices, color='dodgerblue',
		linestyle='-')
mp.gcf().autofmt_xdate()
mp.show()

```

1. 绘制每一天的蜡烛图：

```python
#绘制每一天的蜡烛图
#填充色：涨为白色，跌为绿色
rise = closeing_prices >= opening_prices
color = np.array([('white' if x else 'limegreen') for x in rise])
#边框色：涨为红色，跌为绿色
edgecolor = np.array([('red' if x else 'limegreen') for x in rise])

#绘制线条
mp.bar(dates, highest_prices - lowest_prices, 0.1,
	lowest_prices, color=edgecolor)
#绘制方块
mp.bar(dates, closeing_prices - opening_prices, 0.8,
	opening_prices, color=color, edgecolor=edgecolor)
```

### 算数平均值

```
S = [s1, s2, ..., sn]
```

样本中的每个值都是真值与误差的和。

```
算数平均值：
m = (s1 + s2 + ... + sn) / n
```

算数平均值表示对真值的无偏估计。

```python
np.mean(array)
```

案例：计算收盘价的算术平均值。

```python
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6), unpack=True)
mean = 0
for closing_price in closing_prices:
    mean += closing_price
mean /= closing_prices.size
print(mean)
mean = np.mean(closing_prices)
print(mean)
```

### 加权平均值

样本：S = [s<sub>1</sub>, s<sub>2</sub>, ..., s<sub>n</sub>]

权重：W = [w<sub>1</sub>, w<sub>2</sub>, ..., w<sub>n</sub>]

加权平均值：a = (s<sub>1</sub>w<sub>1</sub>+s<sub>2</sub>w<sub>2</sub>+...+s<sub>n</sub>w<sub>n</sub>)/(w<sub>1</sub>+w<sub>2</sub>+...+w<sub>n</sub>)

```python
np.average(closing_prices, weights=volumes)
```



VWAP - 成交量加权平均价格（成交量体现了市场对当前交易价格的认可度，成交量加权平均价格将会更接近这支股票的真实价值）

```python
import numpy as np
closing_prices, volumes = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(6, 7), unpack=True)
vwap, wsum = 0, 0
for closing_price, volume in zip(
        closing_prices, volumes):
    vwap += closing_price * volume
    wsum += volume
vwap /= wsum
print(vwap)
vwap = np.average(closing_prices, weights=volumes)
print(vwap)
```

TWAP - 时间加权平均价格（时间越晚权重越高，参考意义越大）

```python
import datetime as dt
import numpy as np

def dmy2days(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    days = (date - dt.date.min).days
    return days

days, closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True,
    converters={1: dmy2days})
twap = np.average(closing_prices, weights=days)
print(twap)
```



## numpy常用函数

### 最值

**np.max()  np.min() np.ptp()：** 返回一个数组中最大值/最小值/极差

```python
import numpy as np
# 产生9个介于[10, 100)区间的随机数
a = np.random.randint(10, 100, 9)
print(a)
print(np.max(a), np.min(a), np.ptp(a))
```

**np.argmax() mp.argmin()：** 返回一个数组中最大/最小元素的下标

```python
print(np.argmax(a), np.argmin(a))
```

**np.maximum() np.minimum()：** 将两个同维数组中对应元素中最大/最小元素构成一个新的数组

```python
print(np.maximum(a, b), np.minimum(a, b), sep='\n')
```

案例：评估AAPL股票的波动性。

```python
import numpy as np
highest_prices, lowest_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(4, 5), dtype='f8, f8', unpack=True)
max_price = np.max(highest_prices)
min_price = np.min(lowest_prices)
print(min_price, '~', max_price)
```

查看AAPL股票最大最小值的日期，分析为什么这一天出现最大最小值。

```python
import numpy as np
dates, highest_prices, lowest_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 4, 5), dtype='U10, f8, f8',
    unpack=True)
max_index = np.argmax(highest_prices)
min_index = np.argmin(lowest_prices)
print(dates[min_index], dates[max_index])
```

观察最高价与最低价的**波动范围**，分析这支股票底部是否坚挺。  

```python
import numpy as np
dates, highest_prices, lowest_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',',
    usecols=(1, 4, 5), dtype='U10, f8, f8',
    unpack=True)
highest_ptp = np.ptp(highest_prices)
lowest_ptp = np.ptp(lowest_prices)
print(lowest_ptp, highest_ptp)
```

### 中位数

将多个样本按照大小排序，取中间位置的元素。

**若样本数量为奇数，中位数为最中间的元素**

1 2000 3000 4000 10000000

**若样本数量为偶数，中位数为最中间的两个元素的平均值**

1 2000 3000 4000 5000 10000000

案例：分析中位数的算法，测试numpy提供的中位数API：

```python
import numpy as np
closing_prices = np.loadtxt( '../../data/aapl.csv', 
	delimiter=',', usecols=(6), unpack=True)
size = closing_prices.size
sorted_prices = np.msort(closing_prices)
median = (sorted_prices[int((size - 1) / 2)] + sorted_prices[int(size / 2)]) / 2
print(median)
median = np.median(closing_prices)
print(median)
```

### 标准差

样本：S = [s1, s2, ..., sn]
平均值：m = (s1+s2+...+sn)/n
离差：D = [d1, d2, ..., dn], di = si-m
离差方：Q = [q1, q2, ..., qn], qi = di<sup>2</sup>
总体方差：v = (q1+q2+...+qn)/n
总体标准差：s = sqrt(v)，方均根
样本方差：v' = (q1+q2+...+qn)/(n-1)
样本标准差：s' = sqrt(v')，方均根

```python
import numpy as np
closing_prices = np.loadtxt(
    '../../data/aapl.csv', delimiter=',', usecols=(6), unpack=True)
mean = np.mean(closing_prices)         # 算数平均值
devs = closing_prices - mean           # 离差
dsqs = devs ** 2                       # 离差方
pvar = np.sum(dsqs) / dsqs.size        # 总体方差
pstd = np.sqrt(pvar)                   # 总体标准差
svar = np.sum(dsqs) / (dsqs.size - 1)  # 样本方差
sstd = np.sqrt(svar)                   # 样本标准差
print(pstd, sstd)
pstd = np.std(closing_prices)          # 总体标准差
sstd = np.std(closing_prices, ddof=1)  # 样本标准差
print(pstd, sstd)
```

### 案例应用

#### 时间数据处理

案例：统计每个周一、周二、...、周五的收盘价的平均值，并放入一个数组。

```python
import datetime as dt
import numpy as np

# 转换器函数：将日-月-年格式的日期字符串转换为星期
def dmy2wday(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    wday = date.weekday()  # 用 周日
    return wday

wdays, closing_prices = np.loadtxt('../data/aapl.csv', delimiter=',',
    	usecols=(1, 6), unpack=True, converters={1: dmy2wday})

ave_closing_prices = np.zeros(5)
for wday in range(ave_closing_prices.size):
    ave_closing_prices[wday] = closing_prices[wdays == wday].mean()

for wday, ave_closing_price in zip(
    	['MON', 'TUE', 'WED', 'THU', 'FRI'],
        ave_closing_prices):
    print(wday, np.round(ave_closing_price, 2))
```

#### 数组的轴向汇总

案例：汇总每周的最高价，最低价，开盘价，收盘价。

```python
def func(data):
    pass
#func 	处理函数
#axis 	轴向 [0,1]
#array 	数组
np.apply_along_axis(func, axis, array)
```

沿着数组中所指定的轴向，调用处理函数，并将每次调用的返回值重新组织成数组返回。

#### 移动均线

收盘价5日均线：从第五天开始，每天计算最近五天的收盘价的平均值所构成的一条线。

移动均线算法：

```python
(a+b+c+d+e)/5
(b+c+d+e+f)/5
(c+d+e+f+g)/5
...
(f+g+h+i+j)/5
```

在K线图中绘制5日均线图

```python
import datetime as dt
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.dates as md

def dmy2ymd(dmy):
    dmy = str(dmy, encoding='utf-8')
    date = dt.datetime.strptime(dmy, '%d-%m-%Y').date()
    ymd = date.strftime('%Y-%m-%d')
    return ymd

dates, closing_prices = np.loadtxt('../data/aapl.csv', delimiter=',',
    usecols=(1, 6), unpack=True, dtype='M8[D], f8', converters={1: dmy2ymd})
sma51 = np.zeros(closing_prices.size - 4)
for i in range(sma51.size):
    sma51[i] = closing_prices[i:i + 5].mean()
# 开始绘制5日均线
mp.figure('Simple Moving Average', facecolor='lightgray')
mp.title('Simple Moving Average', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
# 设置水平坐标每个星期一为主刻度
ax.xaxis.set_major_locator(md.WeekdayLocator( byweekday=md.MO))
# 设置水平坐标每一天为次刻度
ax.xaxis.set_minor_locator(md.DayLocator())
# 设置水平坐标主刻度标签格式
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, c='lightgray', label='Closing Price')
mp.plot(dates[4:], sma51, c='orangered', label='SMA-5(1)')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
```

#### 卷积

激励函数：g(t)

单位激励下的响应函数：f(t)

绘制时间（t）与痛感（h）的函数关系图。

a = [1 2 3 4 5]	（理解为某单位时间的击打力度序列）

b = [6 7 8]		（理解为痛感系数序列）

```python
c = numpy.convolve(a, b, 卷积类型)

                40  61  82         - 有效卷积(valid)
            19  40  61  82  67     - 同维卷积(same)
        6   19  40  61  82  67  40 - 完全卷积(full)
0   0   1   2   3   4   5   0   0
8   7   6
    8   7   6
        8   7   6
            8   7   6
                8   7   6
                    8   7   6
                        8    7   6
```

**5日移动均线序列可以直接使用卷积实现**

```python
a = [a, b, c, d, e, f, g, h, i, j] 
b = [1/5, 1/5, 1/5, 1/5, 1/5]
```

**使用卷积函数numpy.convolve(a, b, 卷积类型)实现5日均线**

```python
sma52 = np.convolve( closing_prices, np.ones(5) / 5, 'valid')
mp.plot(dates[4:], sma52, c='limegreen', alpha=0.5,
        linewidth=6, label='SMA-5(2)')
```

**使用卷积函数numpy.convolve(a, b, 卷积类型)实现10日均线**

```python
sma10 = np.convolve(closing_prices, np.ones(10) / 10, 'valid')
mp.plot(dates[9:], sma10, c='dodgerblue', label='SMA-10')
```

**使用卷积函数numpy.convolve(a, b, 卷积类型)实现加权5日均线**

```python
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
ema5 = np.convolve(closing_prices, weights[::-1], 'valid')
mp.plot(dates[4:], sma52, c='limegreen', alpha=0.5,
        linewidth=6, label='SMA-5')
```

#### 布林带

布林带由三条线组成：

中轨：(20日)移动平均线

上轨：中轨+2x5日收盘价标准差	（顶部的压力）

下轨：中轨-2x5日收盘价标准差 	（底部的支撑力）

布林带收窄代表稳定的趋势，布林带张开代表有较大的波动空间的趋势。

**绘制5日均线的布林带**

```python
weights = np.exp(np.linspace(-1, 0, 5))
weights /= weights.sum()
em5 = np.convolve(closing_prices, weights[::-1], 'valid')
stds = np.zeros(em5.size)
for i in range(stds.size):
    stds[i] = closing_prices[i:i + 5].std()
stds *= 2
lowers = medios - stds
uppers = medios + stds

mp.plot(dates, closing_prices, c='lightgray', label='Closing Price')
mp.plot(dates[4:], medios, c='dodgerblue', label='Medio')
mp.plot(dates[4:], lowers, c='limegreen', label='Lower')
mp.plot(dates[4:], uppers, c='orangered', label='Upper')
```



## 线性模型

什么是线性关系？

1	2	3	4	5

60  65	70	75	？

#### 线性预测

假设一组数据符合一种线型规律，那么就可以预测未来将会出现的数据。

```python
a	b	c	d	e	f	?

ax + by + cz = d
bx + cy + dz = e
cx + dy + ez = f
```

$$
\left[ \begin{array}{ccc}
a & b & c\\
b & c & d\\
c & d & e\\
\end{array} 
\right ]
\times
\left[ \begin{array}{ccc}
x\\
y\\
z\\
\end{array} 
\right ]=
\left[ 
\begin{array}{ccc}
d\\
e\\
f\\
\end{array} 
\right ]
$$



根据线性模型的特点可以通过一组历史数据求出线性关系系数x, y, z，从而预测d、e、f下的一个数据是多少。

**线性预测需要使用历史数据进行检验，让预测结果可信度更高**

案例：使用线性预测，预测下一天的收盘价。

```python
# 整理五元一次方程组    最终获取一组股票走势预测值
N = 5
pred_prices = np.zeros(closing_prices.size - 2 * N + 1)
for i in range(pred_prices.size):
    a = np.zeros((N, N))
    for j in range(N):
        a[j, ] = closing_prices[i + j:i + j + N]
    b = closing_prices[i + N:i + N * 2]
    x = np.linalg.lstsq(a, b)[0]
    pred_prices[i] = b.dot(x)
# 由于预测的是下一天的收盘价，所以想日期数组中追加一个元素，为下一个工作日的日期
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, closing_prices, 'o-', c='lightgray', label='Closing Price')
dates = np.append(dates, dates[-1] + pd.tseries.offsets.BDay())
mp.plot(dates[2 * N:], pred_prices, 'o-',c='orangered', 
        linewidth=3,label='Predicted Price')
mp.legend()
mp.gcf().autofmt_xdate() 
mp.show()
```

#### 线性拟合

线性拟合可以寻求与一组散点走向趋势规律相适应的线型表达式方程。

有一组散点描述时间序列下的股价：

```python
[x1, y1], [x2, y2], [x3, y3], 
...
[xn, yn]
```

根据线型 y=kx + b 方程可得：

```python
kx1 + b = y1
kx2 + b = y2
kx3 + b = y3
...
kxn + b = yn
```


$$
\left[ \begin{array}{ccc}
x{_1} & 1\\
x{_2} & 1\\
x{_3} & 1 \\
x{_n} & 1 \\
\end{array} 
\right ]
\times
\left[ \begin{array}{ccc}
k\\
b\\
\end{array} 
\right ]
=
\left[ \begin{array}{ccc}
y{_1}\\
y{_2}\\
y{_3}\\
y{_n}\\
\end{array} 
\right ]
$$
样本过多，每两组方程即可求得一组k与b的值。np.linalg.lstsq(a, b) 可以通过最小二乘法求出所有结果中拟合误差最小的k与b的值。

案例：利用线型拟合画出股价的趋势线

1. 绘制趋势线（趋势可以表示为最高价、最低价、收盘价的均值）：

```python
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt('../data/aapl.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})
trend_points = (highest_prices + lowest_prices + closing_prices) / 3
days = dates.astype(int)
a = np.column_stack((days, np.ones_like(days)))
x = np.linalg.lstsq(a, trend_points)[0]
trend_line = days * x[0] + x[1]
mp.figure('Trend', facecolor='lightgray')
mp.title('Trend', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
rise = closing_prices - opening_prices >= 0.01
fall = opening_prices - closing_prices >= 0.01
fc = np.zeros(dates.size, dtype='3f4')
ec = np.zeros(dates.size, dtype='3f4')
fc[rise], fc[fall] = (1, 1, 1), (0.85, 0.85, 0.85)
ec[rise], ec[fall] = (0.85, 0.85, 0.85), (0.85, 0.85, 0.85)
mp.bar(dates, highest_prices - lowest_prices, 0,lowest_prices, color=fc, edgecolor=ec)
mp.bar(dates, closing_prices - opening_prices, 0.8,opening_prices, color=fc, 
       edgecolor=ec)
mp.scatter(dates, trend_points, c='dodgerblue',alpha=0.5, s=60, zorder=2)
mp.plot(dates, trend_line, linestyle='o-', c='dodgerblue',linewidth=3, label='Trend')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
```

1. 绘制顶部压力线（趋势线+(最高价 - 最低价)）

```python
trend_points = (highest_prices + lowest_prices + closing_prices) / 3
spreads = highest_prices - lowest_prices
resistance_points = trend_points + spreads
days = dates.astype(int)
x = np.linalg.lstsq(a, resistance_points)[0]
resistance_line = days * x[0] + x[1]
mp.scatter(dates, resistance_points, c='orangered', alpha=0.5, s=60, zorder=2)
mp.plot(dates, resistance_line, c='orangered', linewidth=3, label='Resistance')
```

1. 绘制底部支撑线（趋势线-(最高价 - 最低价)）

```python
trend_points = (highest_prices + lowest_prices + closing_prices) / 3
spreads = highest_prices - lowest_prices
support_points = trend_points - spreads
days = dates.astype(int)
x = np.linalg.lstsq(a, support_points)[0]
support_line = days * x[0] + x[1]
mp.scatter(dates, support_points, c='limegreen', alpha=0.5, s=60, zorder=2)
mp.plot(dates, support_line, c='limegreen', linewidth=3, label='Support')
```

## 协方差、相关矩阵、相关系数

通过两组统计数据计算而得的协方差可以评估这两组统计数据的相似程度。

**样本**：

```python
A = [a1, a2, ..., an]
B = [b1, b2, ..., bn]
```

**平均值**：

```python
ave_a = (a1 + a2 +...+ an)/n
ave_b = (b1 + b2 +...+ bn)/m
```

**离差**（用样本中的每一个元素减去平均数，求得数据的误差程度）：

```python
dev_a = [a1, a2, ..., an] - ave_a
dev_b = [b1, b2, ..., bn] - ave_b
```

**协方差**

协方差可以简单反映两组统计样本的相关性，值为正，则为正相关；值为负，则为负相关，绝对值越大相关性越强。

```
cov_ab = ave(dev_a x dev_b)
cov_ba = ave(dev_b x dev_a)
```

案例：计算两组数据的协方差，并绘图观察。

```python
import numpy as np
import matplotlib.pyplot as mp

a = np.random.randint(1, 30, 10)
b = np.random.randint(1, 30, 10)
#平均值
ave_a = np.mean(a)
ave_b = np.mean(b)
#离差
dev_a = a - ave_a
dev_b = b - ave_b
#协方差
cov_ab = np.mean(dev_a*dev_b)
cov_ba = np.mean(dev_b*dev_a)
print('a与b数组：', a, b)
print('a与b样本方差：', np.sum(dev_a**2)/(len(dev_a)-1), np.sum(dev_b**2)/(len(dev_b)-1))
print('a与b协方差：',cov_ab, cov_ba)
#绘图，查看两条图线的相关性
mp.figure('COV LINES', facecolor='lightgray')
mp.title('COV LINES', fontsize=16)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
x = np.arange(0, 10)
#a,b两条线
mp.plot(x, a, color='dodgerblue', label='Line1')
mp.plot(x, b, color='limegreen', label='Line2')
#a,b两条线的平均线
mp.plot([0, 9], [ave_a, ave_a], color='dodgerblue', linestyle='--', alpha=0.7, linewidth=3)
mp.plot([0, 9], [ave_b, ave_b], color='limegreen', linestyle='--', alpha=0.7, linewidth=3)

mp.grid(linestyle='--', alpha=0.5)
mp.legend()
mp.tight_layout()
mp.show()
```

**相关系数**

协方差除去两组统计样本的乘积是一个[-1, 1]之间的数。该结果称为统计样本的相关系数。

```python
# a组样本 与 b组样本做对照后的相关系数
cov_ab/(std_a x std_b)
# b组样本 与 a组样本做对照后的相关系数
cov_ba/(std_b x std_a)
# a样本与a样本作对照   b样本与b样本做对照   二者必然相等
cov_ab/(std_a x std_b)=cov_ba/(std_b x std_a)
```

通过相关系数可以分析两组数据的相关性：

```python
若相关系数越接近于0，越表示两组样本越不相关。
若相关系数越接近于1，越表示两组样本正相关。
若相关系数越接近于-1，越表示两组样本负相关。
```

案例：输出案例中两组数据的相关系数。

```python
print('相关系数：', cov_ab/(np.std(a)*np.std(b)), cov_ba/(np.std(a)*np.std(b)))
```

**相关矩阵**


$$
\left[ \begin{array}{c}
\frac{var\_a}{std\_a \times std\_a} & \frac{cov\_ab}{std\_a \times std\_b} \\
\frac{cov\_ba}{std\_b \times std\_a} & \frac{var\_b}{std\_b \times std\_b}\\
\end{array} 
\right ]
$$
矩阵正对角线上的值都为1。（同组样本自己相比绝对正相关）
$$
\left[ \begin{array}{ccc}
1 & \frac{cov\_ab}{std\_a \times std\_b} \\
\frac{cov\_ba}{std\_b \times std\_a} & 1\\
\end{array} 
\right ]
$$
numpy提供了求得相关矩阵的API：

```python
# 相关矩阵
numpy.corrcoef(a, b)	
# 相关矩阵的分子矩阵 
# [[a方差，ab协方差], [ba协方差, b方差]]
numpy.cov(a, b)			
```

## 多项式拟合

多项式的一般形式：
$$
y=p_{0}x^n + p_{1}x^{n-1} + p_{2}x^{n-2} + p_{3}x^{n-3} +...+p_{n}
$$
多项式拟合的目的是为了找到一组p0-pn，使得拟合方程尽可能的与实际样本数据相符合。

假设拟合得到的多项式如下：
$$
f(x)=p_{0}x^n + p_{1}x^{n-1} + p_{2}x^{n-2} + p_{3}x^{n-3} +...+p_{n}
$$
则拟合函数与真实结果的差方如下
$$
loss = (y_1-f(x_1))^2 + (y_2-f(x_2))^2 + ... + (y_n-f(x_n))^2
$$
那么多项式拟合的过程即为求取一组p<sub>0</sub>-p<sub>n</sub>,使得loss的值最小。

```
X = [x1, x2, ..., xn] - 自变量
Y = [y1, y2, ..., yn] - 实际函数值
Y'= [y1',y2',...,yn'] - 拟合函数值
P = [p0, p1, ..., pn] - 多项式函数中的系数

根据一组样本，并给出最高次幂，求出拟合系数
np.polyfit(X, Y, 最高次幂)->P
```

多项式运算相关API：

```
根据拟合系数与自变量求出拟合值, 由此可得拟合曲线坐标样本数据 [X, Y']
np.polyval(P, X)->Y'

多项式函数求导，根据拟合系数求出多项式函数导函数的系数
np.polyder(P)->Q 

已知多项式系数Q 求多项式函数的根（与x轴交点的横坐标）
xs = np.roots(Q)

两个多项式函数的差函数的系数（可以通过差函数的根求取两个曲线的交点）
Q = np.polysub(P1, P2)
```

案例：求多项式 y = 4x<sup>3</sup> + 3x<sup>2</sup> - 1000x + 1曲线拐点的坐标。

```python
'''
1. 求出多项式的导函数
2. 求出导函数的根，若导函数的根为实数，则该点则为曲线拐点。
'''
import numpy as np
import matplotlib.pyplot as mp

x = np.linspace(-20, 20, 1000)
y = 4*x**3 + 3*x**2  - 1000*x + 1
Q = np.polyder([4,3,-1000,1])
xs = np.roots(Q)
ys =  4*xs**3 + 3*xs**2  - 1000*xs + 1
mp.plot(x, y)
mp.scatter(xs, ys, s=80, c='orangered')
mp.show()
```

案例：使用多项式函数拟合两只股票bhp、vale的差价函数：

```python
'''
1. 计算两只股票的差价
2. 利用多项式拟合求出与两只股票差价相近的多项式系数，最高次为4
3. 把该曲线的拐点都标出来。
'''
dates, bhp_closing_prices = np.loadtxt('../../data/bhp.csv', 
                                       delimiter=',',usecols=(1, 6), unpack=True, 
                                       dtype='M8[D], f8', conv erters={1: dmy2ymd})
vale_closing_prices = np.loa dtxt('../../data/vale.csv', delimiter=',',
                                 usecols=(6), unpack=True)
diff_closing_prices = bhp_closing_prices - vale_closing_prices
days = dates.astype(int)
p = np.polyfit(days, diff_closing_prices, 4)
poly_closing_prices = np.polyval(p, days)
q = np.polyder(p)
roots_x = np.roots(q)
roots_y = np.polyval(p, roots_x)
mp.figure('Polynomial Fitting', facecolor='lightgray')
mp.title('Polynomial Fitting', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Difference Price', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
dates = dates.astype(md.datetime.datetime)
mp.plot(dates, poly_closing_prices, c='limegreen',
        linewidth=3, label='Polynomial Fitting')
mp.scatter(dates, diff_closing_prices, c='dodgerblue',
           alpha=0.5, s=60, label='Difference Price')
roots_x = roots_x.astype(int).astype('M8[D]').astype(
    		md.datetime.datetime)
mp.scatter(roots_x, roots_y, marker='^', s=80,
           c='orangered', label='Peek', zorder=4)
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
```

## 数据平滑

数据的平滑处理通常包含有降噪、拟合等操作。降噪的功能意在去除额外的影响因素，拟合的目的意在数学模型化，可以通过更多的数学方法识别曲线特征。

案例：绘制两只股票收益率曲线。收益率 =（后一天收盘价-前一天收盘价） / 前一天收盘价

1. 使用卷积完成数据降噪。

```python
dates, bhp_closing_prices = np.loadtxt( '../data/bhp.csv', delimiter=',', usecols=(1,6), dtype='M8[D], f8',converters={1:dmy2ymd}, unpack=True)
vale_closing_prices = np.loadtxt( '../data/vale.csv', delimiter=',', usecols=(6), dtype='f8',converters={1:dmy2ymd}, unpack=True)

bhp_returns = np.diff(bhp_closing_prices) / bhp_closing_prices[:-1]
vale_returns = np.diff(vale_closing_prices) / vale_closing_prices[:-1]
dates = dates[:-1]

#卷积降噪
convolve_core = np.hanning(8)
convolve_core /= convolve_core.sum()
bhp_returns_convolved = np.convolve(bhp_returns, convolve_core, 'valid')
vale_returns_convolved = np.convolve(vale_returns, convolve_core, 'valid')
#绘制这条曲线
mp.figure('BHP VALE RETURNS', facecolor='lightgray')
mp.title('BHP VALE RETURNS', fontsize=20)
mp.xlabel('Date')
mp.ylabel('Price')
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%Y %m %d'))
dates = dates.astype('M8[D]')
#绘制收益线
mp.plot(dates, bhp_returns, color='dodgerblue', linestyle='--', label='bhp_returns', alpha=0.3)
mp.plot(dates, vale_returns, color='orangered', linestyle='--', label='vale_returns', alpha=0.3)
#绘制卷积降噪线
mp.plot(dates[7:], bhp_returns_convolved, color='dodgerblue', label='bhp_returns_convolved', alpha=0.5)
mp.plot(dates[7:], vale_returns_convolved, color='orangered', label='vale_returns_convolved', alpha=0.5)

mp.show()

```

1. 对处理过的股票收益率做多项式拟合。

```python
#拟合这两条曲线，获取两组多项式系数
dates = dates.astype(int)
bhp_p = np.polyfit(dates[7:], bhp_returns_convolved, 3)
bhp_polyfit_y = np.polyval(bhp_p, dates[7:])
vale_p = np.polyfit(dates[7:], vale_returns_convolved, 3)
vale_polyfit_y = np.polyval(vale_p, dates[7:])
#绘制拟合线
mp.plot(dates[7:], bhp_polyfit_y, color='dodgerblue', label='bhp_returns_polyfit')
mp.plot(dates[7:], vale_polyfit_y, color='orangered', label='vale_returns_polyfit')
```

1. 通过获取两个函数的焦点可以分析两只股票的投资收益比。

```python
#求两条曲线的交点  f(bhp) = f(vale)的根
sub_p = np.polysub(bhp_p, vale_p)
roots_x = np.roots(sub_p)	# 让f(bhp) - f(vale) = 0  函数的两个根既是两个函数的焦点
roots_x = roots_x.compress( (dates[0] <= roots_x) & (roots_x <= dates[-1]))
roots_y = np.polyval(bhp_p, roots_x)
#绘制这些点
mp.scatter(roots_x, roots_y, marker='D', color='green', s=60, zorder=3)
```



## 符号数组

sign函数可以把样本数组的变成对应的符号数组，正数变为1，负数变为-1，0则变为0。

```python
ary = np.sign(源数组)
```

**净额成交量（OBV）**

成交量可以反映市场对某支股票的人气，而成交量是一只股票上涨的能量。一支股票的上涨往往需要较大的成交量。而下跌时则不然。

若相比上一天的收盘价上涨，则为正成交量；若相比上一天的收盘价下跌，则为负成交量。

 绘制OBV柱状图

```python
dates, closing_prices, volumes = np.loadtxt(
    '../../data/bhp.csv', delimiter=',',
    usecols=(1, 6, 7), unpack=True,
    dtype='M8[D], f8, f8', converters={1: dmy2ymd})
diff_closing_prices = np.diff(closing_prices)
sign_closing_prices = np.sign(diff_closing_prices)
obvs = volumes[1:] * sign_closing_prices
mp.figure('On-Balance Volume', facecolor='lightgray')
mp.title('On-Balance Volume', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('OBV', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
dates = dates[1:].astype(md.datetime.datetime)
mp.bar(dates, obvs, 1.0, color='dodgerblue',
       edgecolor='white', label='OBV')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
```

**数组处理函数**

```python
ary = np.piecewise(源数组, 条件序列, 取值序列)
```

针对源数组中的每一个元素，检测其是否符合条件序列中的每一个条件，符合哪个条件就用取值系列中与之对应的值，表示该元素，放到目标 数组中返回。

条件序列: [a < 0, a == 0, a > 0]

取值序列: [-1, 0, 1]     

```python
a = np.array([70, 80, 60, 30, 40])
d = np.piecewise(
    a, 
    [a < 60, a == 60, a > 60],
    [-1, 0, 1])
# d = [ 1  1  0 -1 -1]
```

## 矢量化

矢量化指的是用数组代替标量来操作数组里的每个元素。

numpy提供了vectorize函数，可以把处理标量的函数矢量化，返回的函数可以直接处理ndarray数组。

```python
import math as m
import numpy as np

def foo(x, y):
    return m.sqrt(x**2 + y**2)

x, y = 1, 4
print(foo(x, y))
X, Y = np.array([1, 2, 3]), np.array([4, 5, 6])
vectorized_foo = np.vectorize(foo)
print(vectorized_foo(X, Y))
print(np.vectorize(foo)(X, Y))
```

numpy还提供了frompyfuc函数，也可以完成与vectorize相同的功能：

```python
# 把foo转换成矢量函数，该矢量函数接收2个参数，返回一个结果 
fun = np.frompyfunc(foo, 2, 1)
fun(X, Y)
```

案例：定义一种买进卖出策略，通过历史数据判断这种策略是否值得实施。

```python
dates, opening_prices, highest_prices, \
    lowest_prices, closing_prices = np.loadtxt(
        '../../data/bhp.csv', delimiter=',',
        usecols=(1, 3, 4, 5, 6), unpack=True,
        dtype='M8[D], f8, f8, f8, f8',
        converters={1: dmy2ymd})
    
# 定义一种投资策略
def profit(opening_price, highest_price,
           lowest_price, closing_price):
    buying_price = opening_price * 0.99
    if lowest_price <= buying_price <= highest_price:
        return (closing_price - buying_price) * \
            100 / buying_price
    return np.nan  # 无效值

# 矢量化投资函数
profits = np.vectorize(profit)(opening_prices, 
       highest_prices, lowest_prices, closing_prices)
nan = np.isnan(profits)
dates, profits = dates[~nan], profits[~nan]
gain_dates, gain_profits = dates[profits > 0], profits[profits > 0]
loss_dates, loss_profits = dates[profits < 0], profits[profits < 0]
mp.figure('Trading Simulation', facecolor='lightgray')
mp.title('Trading Simulation', fontsize=20)
mp.xlabel('Date', fontsize=14)
mp.ylabel('Profit', fontsize=14)
ax = mp.gca()
ax.xaxis.set_major_locator(md.WeekdayLocator(byweekday=md.MO))
ax.xaxis.set_minor_locator(md.DayLocator())
ax.xaxis.set_major_formatter(md.DateFormatter('%d %b %Y'))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
if dates.size > 0:
    dates = dates.astype(md.datetime.datetime)
    mp.plot(dates, profits, c='gray',
            label='Profit')
    mp.axhline(y=profits.mean(), linestyle='--',
               color='gray')
if gain_dates.size > 0:
    gain_dates = gain_dates.astype(md.datetime.datetime)
    mp.plot(gain_dates, gain_profits, 'o',
            c='orangered', label='Gain Profit')
    mp.axhline(y=gain_profits.mean(), linestyle='--',
               color='orangered')
if loss_dates.size > 0:
    loss_dates = loss_dates.astype(md.datetime.datetime)
    mp.plot(loss_dates, loss_profits, 'o',
            c='limegreen', label='Loss Profit')
    mp.axhline(y=loss_profits.mean(), linestyle='--',
               color='limegreen')
mp.legend()
mp.gcf().autofmt_xdate()
mp.show()
```

## 矩阵

矩阵是numpy.matrix类类型的对象，该类继承自numpy.ndarray，任何针对多维数组的操作，对矩阵同样有效，但是作为子类矩阵又结合其自身的特点，做了必要的扩充，比如：乘法计算、求逆等。

**矩阵对象的创建**

```python
# 如果copy的值为True(缺省)，各自拥有独立的数据拷贝,否则，所得到的矩阵对象与参数中的源容器共享同一份数据.
numpy.matrix(
    ary,		# 任何可被解释为矩阵的二维容器
  	copy=True	# 是否复制数据(缺省值为True，即复制数据)
)
```

```python
# 等价于：numpy.matrix(..., copy=False)
# 由该函数创建的矩阵对象与参数中的源容器一定共享数据，无法拥有独立的数据拷贝
numpy.mat(任何可被解释为矩阵的二维容器)
```

```python
# 该函数可以接受字符串形式的矩阵描述：
# 数据项通过空格分隔，数据行通过分号分隔。例如：'1 2 3; 4 5 6'
numpy.mat(拼块规则)
```

**矩阵的乘法运算**

```python
# 矩阵的乘法：乘积矩阵的第i行第j列的元素等于
# 被乘数矩阵的第i行与乘数矩阵的第j列的点积
#
#           1   2   6
#    X----> 3   5   7
#    |      4   8   9
#    |
# 1  2  6   31  60  74
# 3  5  7   46  87 116
# 4  8  9   64 120 161
e = np.mat('1 2 6; 3 5 7; 4 8 9')
print(e * e)
```

**矩阵的逆矩阵**

若两个矩阵A、B满足：AB = BA = E （E为单位矩阵），则成为A、B为逆矩阵。

```python
e = np.mat('1 2 6; 3 5 7; 4 8 9')
print(e.I)
print(e * e.I)
```

ndarray提供了方法让多维数组替代矩阵的运算： 

```python
a = np.array([
    [1, 2, 6],
    [3, 5, 7],
    [4, 8, 9]])
# 点乘法求ndarray的点乘结果，与矩阵的乘法运算结果相同
k = a.dot(a)
print(k)
# linalg模块中的inv方法可以求取a的逆矩阵
l = np.linalg.inv(a)
print(l)
```

案例：假设一帮孩子和家长出去旅游，去程坐的是bus，小孩票价为3元，家长票价为3.2元，共花了118.4；回程坐的是Train，小孩票价为3.5元，家长票价为3.6元，共花了135.2。分别求小孩和家长的人数。使用矩阵求解。

$$
\left[ \begin{array}{ccc}
	3 & 3.2 \\
	3.5 & 3.6 \\
\end{array} \right]
\times
\left[ \begin{array}{ccc}
	x \\
    y \\
\end{array} \right]
=
\left[ \begin{array}{ccc}
	118.4 \\
	135.2 \\
\end{array} \right]
$$

```python
import numpy as np

prices = np.mat('3 3.2; 3.5 3.6')
totals = np.mat('118.4; 135.2')

persons = prices.I * totals
print(persons)
```

案例：斐波那契数列

1	1	 2	 3	5	8	13	21	34 ...

```python
X      1   1    1   1    1   1
       1   0    1   0    1   0
    --------------------------------
1  1   2   1    3   2    5   3
1  0   1   1    2   1    3   2
 F^1    F^2      F^3 	  F^4  ...  f^n
```

**代码**

```python
import numpy as np
n = 35

# 使用递归实现斐波那契数列
def fibo(n):
    return 1 if n < 3 else fibo(n - 1) + fibo(n - 2)
print(fibo(n))

# 使用矩阵实现斐波那契数列
print(int((np.mat('1. 1.; 1. 0.') ** (n - 1))[0, 0]))
```

## 通用函数

**数组的裁剪**

```python
# 将调用数组中小于和大于下限和上限的元素替换为下限和上限，返回裁剪后的数组，调
# 用数组保持不变。
ndarray.clip(min=下限, max=上限)
```

**数组的压缩**

```python
# 返回由调用数组中满足条件的元素组成的新数组。
ndarray.compress(条件)
```

**数组的累乘**

```python
# 返回调用数组中所有元素的乘积——累乘。
ndarray.prod()
# 返回调用数组中所有元素执行累乘的过程数组。
ndarray.cumprod()
```

案例：

```python
from __future__ import unicode_literals
import numpy as np
a = np.array([10, 20, 30, 40, 50])
print(a)
b = a.clip(min=15, max=45)
print(b)
c = a.compress((15 <= a) & (a <= 45))
print(c)
d = a.prod()
print(d)
e = a.cumprod()
print(e)

def jiecheng(n):
    return n if n == 1 else n * jiecheng(n - 1)

n = 5
print(jiecheng(n))
jc = 1
for i in range(2, n + 1):
    jc *= i
print(jc)
print(np.arange(2, n + 1).prod())
```



### 加法通用函数 

```python
add(a, a) 					# 两数组相加
add.reduce(a) 				# a数组元素累加和
add.accumulate(a) 			# 累加和过程
add.outer([10, 20, 30], a)	# 外和
```

案例：

```python
a = np.arange(1, 7)
print(a)
b = a + a
print(b)
b = np.add(a, a)
print(b)
c = np.add.reduce(a)
print(c)
d = np.add.accumulate(a)
print(d)
#  +  	 1  2  3  4  5  6   
#	   --------------------
# 10   |11 12 13 14 15 16 |
# 20   |21 22 23 24 25 26 |
# 30   |31 32 33 34 35 36 |
       --------------------
f = np.add.outer([10, 20, 30], a)
print(f)
#  x  	 1  2  3  4  5  6   
#	   -----------------------
# 10   |10 20 30  40  50  60 |
# 20   |20 40 60  80 100 120 |
# 30   |30 60 90 120 150 180 |
       -----------------------
g = np.outer([10, 20, 30], a)
print(g)
```

### 除法通用函数

```python
np.true_divide(a, b) 	# a 真除 b  （对应位置相除）
np.divide(a, b) 		# a 真除 b
np.floor_divide(a, b)	# a 地板除 b	（真除的结果向下取整）
np.ceil(a / b) 		# a 天花板除 b	（真除的结果向上取整）
np.trunc(a / b)			# a 截断除 b	（真除的结果直接干掉小数部分）
```

案例：

```python
import numpy as np

a = np.array([20, 20, -20, -20])
b = np.array([3, -3, 6, -6])
# 真除
c = np.true_divide(a, b)
c = np.divide(a, b)
c = a / b
print('array:',c)
# 对ndarray做floor操作
d = np.floor(a / b)
print('floor_divide:',d)
# 对ndarray做ceil操作
e = np.ceil(a / b)
print('ceil ndarray:',e)
# 对ndarray做trunc操作
f = np.trunc(a / b)
print('trunc ndarray:',f)
# 对ndarray做around操作
g = np.around(a / b)
print('around ndarray:',g)
```

### 三角函数通用函数

```python
numpy.sin()
```

**合成方波**

一个方波由如下参数的正弦波叠加而成：
$$
y = 4\pi \times sin(x) \\
y = \frac{4\pi}{3} \times sin(3x) \\
...\\
...\\
y = \frac{4\pi}{2n-1} \times sin((2n-1)x)
$$
曲线叠加的越多，越接近方波。所以可以设计一个函数，接收曲线的数量n作为参数，返回一个矢量函数，该函数可以接收x坐标数组，返回n个正弦波叠加得到的y坐标数组。

```python
x = np.linspace(-2*np.pi, 2*np.pi, 1000)
y = np.zeros(1000)
n = 1000
for i in range(1， n+1):
	y += 4 / ((2 * i - 1) * np.pi) * np.sin((2 * i - 1) * x)
mp.plot(x, y, label='n=1000')
mp.legend()
mp.show()
```

### 位运算通用函数

**位异或：**

```python
c = a ^ b
c = a.__xor__(b)
c = np.bitwise_xor(a, b)
```

按位异或操作可以很方便的判断两个数据是否同号。

```
0 ^ 0 = 0
0 ^ 1 = 1
1 ^ 0 = 1
1 ^ 1 = 0
```

```python
a = np.array([0, -1, 2, -3, 4, -5])
b = np.array([0, 1, 2, 3, 4, 5])
print(a, b)
c = a ^ b
# c = a.__xor__(b)
# c = np.bitwise_xor(a, b)
print(np.where(c < 0)[0])
```

**位与：**

```python
e = a & b
e = a.__and__(b)
e = np.bitwise_and(a, b)
```

```
0 & 0 = 0 
0 & 1 = 0
1 & 0 = 0
1 & 1 = 1
```

利用位与运算计算某个数字是否是2的幂

```python
#  1 2^0 00001   0 00000
#  2 2^1 00010   1 00001
#  4 2^2 00100   3 00011
#  8 2^3 01000   7 00111
# 16 2^4 10000  15 01111
# ...

d = np.arange(1, 21)
print(d)
e = d & (d - 1)
e = d.__and__(d - 1)
e = np.bitwise_and(d, d - 1)
print(e)
```

**位或：**

```python
|
__or__
bitwise_or
```

0 | 0 = 0
0 | 1 = 1
1 | 0 = 1
1 | 1 = 1
**位反：**

```python
~
__not__
bitwise_not
```

~0 = 1
~1 = 0
**移位：**

```python
<<		__lshift__		left_shift
>>		__rshift__		right_shift
```

左移1位相当于乘2，右移1位相当于除2。

```python
d = np.arange(1, 21)
print(d)
# f = d << 1
# f = d.__lshift__(1)
f = np.left_shift(d, 1)
print(f)
```

## 特征值和特征向量

对于n阶方阵A，如果存在数a和非零n维列向量x，使得Ax=ax，则称a是矩阵A的一个特征值，x是矩阵A属于特征值a的特征向量

```python
#已知n阶方阵A， 求特征值与特征数组
# eigvals: 特征值数组
# eigvecs: 特征向量数组 
eigvals, eigvecs = np.linalg.eig(A)
#已知特征值与特征向量，求方阵
S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs逆) 
```

案例：

```python
import numpy as np
A = np.mat('3 -2; 1 0')
print(A)
eigvals, eigvecs = np.linalg.eig(A)
print(eigvals)
print(eigvecs)
print(A * eigvecs[:, 0])	# 方阵*特征向量
print(eigvals[0] * eigvecs[:, 0])	#特征值*特征向量
S = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs.I)
```

案例：读取图片的亮度矩阵，提取特征值与特征向量，保留部分特征值，重新生成新的亮度矩阵，绘制图片。

```python
'''
特征值与特征向量
'''
import numpy as np
import scipy.misc as sm
import matplotlib.pyplot as mp


original = sm.imread('../data/lily.jpg', True)
#提取特征值
eigvals, eigvecs = np.linalg.eig(original)
eigvals[50:] = 0
print(np.diag(eigvals).shape)
original2 = np.mat(eigvecs) * np.mat(np.diag(eigvals)) * np.mat(eigvecs).I
mp.figure("Lily Features")
mp.subplot(121)
mp.xticks([])
mp.yticks([])
mp.imshow(original, cmap='gray')

mp.subplot(122)
mp.xticks([])
mp.yticks([])
mp.imshow(original2, cmap='gray')
mp.tight_layout()
mp.show()
```

## 奇异值分解

有一个矩阵M，可以分解为3个矩阵U、S、V，使得U x S x V等于M。U与V都是正交矩阵（乘以自身的转置矩阵结果为单位矩阵）。那么S矩阵主对角线上的元素称为矩阵M的奇异值，其它元素均为0。

```python
import numpy as np
M = np.mat('4 11 14; 8 7 -2')
print(M)
U, sv, V = np.linalg.svd(M, full_matrices=False)
print(U * U.T)
print(V * V.T)
print(sv)
S = np.diag(sv)
print(S)
print(U * S * V)
```

案例：读取图片的亮度矩阵，提取奇异值与两个正交矩阵，保留部分奇异值，重新生成新的亮度矩阵，绘制图片。

```python
original = sm.imread('../data/lily.jpg', True)
#提取奇异值  sv 	
U, sv, V = np.linalg.svd(original)
print(U.shape, sv.shape, V.shape)
sv[50:] = 0
original2 = np.mat(U) * np.mat(np.diag(sv)) * np.mat(V)
mp.figure("Lily Features")
mp.subplot(221)
mp.xticks([])
mp.yticks([])
mp.imshow(original, cmap='gray')

mp.subplot(222)
mp.xticks([])
mp.yticks([])
mp.imshow(original2, cmap='gray')
mp.tight_layout()

```

## 快速傅里叶变换模块(fft)

什么是傅里叶变换？

法国科学家傅里叶提出，任何一条周期曲线，无论多么跳跃或不规则，都能表示成一组光滑正弦曲线叠加之和。

傅里叶变换的目的是可将时域（即时间域）上的信号转变为频域（即频率域）上的信号，随着域的不同，对同一个事物的了解角度也就随之改变，因此在时域中某些不好处理的地方，在频域就可以较为简单的处理。这就可以大量减少处理信号存储量。

什么是傅里叶变换
 
即是基于傅里叶定力对一条周期曲线进行拆解的过程,最终得到一组光滑的周期曲线 

例如：弹钢琴

假设有一时间域函数：**y = f(x)**，根据傅里叶的理论它可以被分解为一系列正弦函数的叠加，他们的振幅A，频率&omega;或初相位&phi;不同：
$$
y = A_1sin(\omega_1x+\phi_1) +  A_2sin(\omega_2x+\phi_2) +  A_2sin(\omega_2x+\phi_2) + R
$$
所以傅里叶变换可以把一个比较复杂的函数转换为多个简单函数的叠加，看问题的角度也从时间域转到了频率域，有些的问题处理起来就会比较简单。

### **傅里叶变换相关函数**

导入快速傅里叶变换所需模块

```python
import numpy.fft as nf
```

通过采样数与采样周期求得傅里叶变换分解所得曲线的**频率序列**

```python
freqs = np.fft.fftfreq(采样数量, 采样周期)
```

通过原函数值的序列j经过快速傅里叶变换得到一个**复数数组**，复数的模代表的是**振幅**，复数的辐角代表**初相位**

```python
np.fft.fft(原函数值序列) -> 目标函数值序列(复数)
```

通过一个复数数组（复数的模代表的是振幅，复数的辐角代表初相位）经过逆向傅里叶变换得到**合成的函数值数组**

```python
np.fft.ifft(目标函数值序列(复数))->原函数值序列
```

案例：针对合成波做快速傅里叶变换，得到一组复数序列；再针对该复数序列做逆向傅里叶变换得到新的合成波并绘制。

```python
ffts = nf.fft(sigs6)
sigs7 = nf.ifft(ffts).real
mp.plot(times, sigs7, label=r'$\omega$='+str(round(1 / (2 * np.pi),3)), alpha=0.5, linewidth=6)
```

案例：针对合成波做快速傅里叶变换，得到分解波数组的频率、振幅、初相位数组，并绘制频域图像。

```python
# 得到分解波的频率ffts = nf.fft(sigs6)
sigs7 = nf.ifft(ffts).real
mp.plot(times, sigs7, label=r'$\omega$='+str(round(1 / (2 * np.pi),3)), alpha=0.5, linewidth=6)序列
freqs = nf.fftfreqffts = nf.fft(sigs6)
sigs7 = nf.ifft(ffts).real
mp.plot(times, sigs7, label=r'$\omega$='+str(round(1 / (2 * np.pi),3)), alpha=0.5, linewidth=6)(times.size, times[1] - times[0])
# 复数的模为信号的ffts = nf.fft(sigs6)
sigs7 = nf.ifft(ffts).real
mp.plot(times, sigs7, label=r'$\omega$='+str(round(1 / (2 * np.pi),3)), alpha=0.5, linewidth=6)振幅（能量大小）
ffts = nf.fft(sigsffts = nf.fft(sigs6)
sigs7 = nf.ifft(ffts).real
mp.plot(times, sigs7, label=r'$\omega$='+str(round(1 / (2 * np.pi),3)), alpha=0.5, linewidth=6)6)
pows = np.abs(ffts)

mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered', label='Frequency Spectrum')
mp.legend()
mp.tight_layout()
mp.show()
```

### 基于傅里叶变换的频域滤波

 含噪信号是高能信号与低能噪声叠加的信号，可以通过傅里叶变换的频域滤波实现降噪。

通过FFT使含噪信号转换为含噪频谱，去除低能噪声，留下高能频谱后再通过IFFT留下高能信号。

案例：基于傅里叶变换的频域滤波为音频文件去除噪声。

1. 读取音频文件，获取音频文件基本信息：采样个数，采样周期，与每个采样的声音信号值。绘制音频时域的：时间/位移图像。

```python
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rate, noised_sigs = wf.read('../data/noised.wav')
noised_sigs = noised_sigs / 2 ** 15
times = np.arange(len(noised_sigs)) / sample_rate
mp.figure('Filter', facecolor='lightgray')
mp.subplot(221)
mp.title('Time Domain', fontsize=16)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], noised_sigs[:178],c='orangered', label='Noised')
mp.legend()
mp.show()
```

1. 基于傅里叶变换，获取音频频域信息，绘制音频频域的：频率/能量图像。

```python
freqs = nf.fftfreq(times.size, 1 / sample_rate)
noised_ffts = nf.fft(noised_sigs)
noised_pows = np.abs(noised_ffts)
mp.subplot(222)
mp.title('Frequency Domain', fontsize=16)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.semilogy(freqs[freqs >= 0],noised_pows[freqs >= 0], c='limegreen',label='Noised')
mp.legend()
```

1. 将低能噪声去除后绘制音频频域的：频率/能量图像。

```python
fund_freq = freqs[noised_pows.argmax()]
noised_indices = np.where(freqs != fund_freq)
filter_ffts = noised_ffts.copy()
filter_ffts[noised_indices] = 0
filter_pows = np.abs(filter_ffts)

mp.subplot(224)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], filter_pows[freqs >= 0],c='dodgerblue', label='Filter')
mp.legend() 
```

1. 基于逆向傅里叶变换，生成新的音频信号，绘制音频时域的：时间/位移图像。

```python
filter_sigs = nf.ifft(filter_ffts).real
mp.subplot(223)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times[:178], filter_sigs[:178],c='hotpink', label='Filter')
mp.legend()
```

1. 重新生成音频文件。

```python
wf.write('../../data/filter.wav',sample_rate,(filter_sigs * 2 ** 15).astype(np.int16))
```

### 随机数模块(random)

生成服从特定统计规律的随机数序列。

#### 二项分布（binomial）

二项分布就是重复n次独立事件的伯努利试验。在每次试验中只有两种可能的结果，而且两种结果发生与否互相对立，并且相互独立，事件发生与否的概率在每一次独立试验中都保持不变。

```python
# 产生size个随机数，每个随机数来自n次尝试中的成功次数，其中每次尝试成功的概率为p。
np.random.binomial(n, p, size)
```

二项分布可以用于求如下场景的概率的近似值：

1. 某人投篮命中率为0.3，投10次，进5个球的概率。

```python
sum(np.random.binomial(10, 0.3, 200000) == 5) / 200000
```

1. 某人打客服电话，客服接通率是0.6，一共打了3次，都没人接的概率。

```python
sum(np.random.binomial(3, 0.6, 200000) == 0) / 200000
```

#### 超几何分布(hypergeometric)

```python
# 产生size个随机数，每个随机数t为在总样本中随机抽取nsample个样本后好样本的个数，总样本由ngood个好样本和nbad个坏样本组成
np.random.hypergeometric(ngood, nbad, nsample, size)
```

#### 正态分布(normal)  

```python
# 产生size个随机数，服从标准正态(期望=0, 标准差=1)分布。
np.random.normal(size)
# 产生size个随机数，服从正态分布(期望=1, 标准差=10)。
np.random.normal(loc=1, scale=10, size)
```

$$
标准正态分布概率密度: \frac{e^{-\frac{x^2}{2}}}{\sqrt{2\pi}}
$$

## 杂项功能

### 排序

**联合间接排序**

联合间接排序支持为待排序列排序，若待排序列值相同，则利用参考序列作为参考继续排序。最终返回排序过后的有序索引序列。

```python
indices = numpy.lexsort((参考序列, 待排序列))
```

案例：先按价格排序，再按销售量倒序排列。

```python
import numpy as np
prices = np.array([92,83,71,92,40,12,64])
volumes = np.array([100,251,4,12,709,34,75])
print(volumes)
names = ['Product1','Product2','Product3','Product4','Product5','Product6','Product7']
ind = np.lexsort((volumes*-1, prices)) 
print(ind)
for i in ind:
	print(names[i], end=' ')
```

**复数数组排序**

按照实部的升序排列，对于实部相同的元素，参考虚部的升序，直接返回排序后的结果数组。

```python
numpy.sort_complex(复数数组)
```

**插入排序**

若有需求需要向有序数组中插入元素，使数组依然有序，numpy提供了searchsorted方法查询并返回可插入位置数组。

```python
indices = numpy.searchsorted(有序序列, 待插序列)
```

调用numpy提供了insert方法将待插序列中的元素，按照位置序列中的位置，插入到被插序列中，返回插入后的结果。

```python
numpy.insert(被插序列, 位置序列, 待插序列)
```

案例：

```python
import numpy as np
#             0  1  2  3  4  5  6
a = np.array([1, 2, 4, 5, 6, 8, 9])
b = np.array([7, 3])
c = np.searchsorted(a, b)
print(c)
d = np.insert(a, c, b)
print(d)

```

### 插值

scipy提供了常见的插值算法可以通过  一定规律插值器函数。若我们给插值器函数更多的散点x坐标序列，该函数将会返回相应的y坐标序列。

```python
func = si.interp1d(
    离散水平坐标, 
    离散垂直坐标,
    kind=插值算法(缺省为线性插值)
)
```

案例：

```python
# scipy.interpolate
import scipy.interpolate as si

# 原始数据 11组数据
min_x = -50
max_x = 50
dis_x = np.linspace(min_x, max_x, 11)
dis_y = np.sinc(dis_x)

# 通过一系列的散点设计出符合一定规律插值器函数，使用线性插值（kind缺省值）
linear = si.interp1d(dis_x, dis_y)
lin_x = np.linspace(min_x, max_x, 200)
lin_y = linear(lin_x)

# 三次样条插值 （CUbic Spline Interpolation） 获得一条光滑曲线
cubic = si.interp1d(dis_x, dis_y, kind='cubic')
cub_x = np.linspace(min_x, max_x, 200)
cub_y = cubic(cub_x)
```

积分

直观地说，对于一个给定的正实值函数，在一个实数区间上的定积分可以理解为坐标平面上由曲线、直线以及轴围成的曲边梯形的面积值（一种确定的实数值）。

利用微元法认识什么是积分。

案例：

1. 在[-5, 5]区间绘制二次函数y=2x<sup>2</sup>+3x+4的曲线：

```python
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.patches as mc

def f(x):
    return 2 * x ** 2 + 3 * x + 4

a, b = -5, 5
x1 = np.linspace(a, b, 1001)
y1 = f(x1)
mp.figure('Integral', facecolor='lightgray')
mp.title('Integral', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(x1, y1, c='orangered', linewidth=6,label=r'$y=2x^2+3x+4$', zorder=0)
mp.legend()
mp.show()
```

1. 微分法绘制函数在与x轴还有[-5, 5]所组成的闭合区域中的小梯形。

```python
n = 50
x2 = np.linspace(a, b, n + 1)
y2 = f(x2)
area = 0
for i in range(n):
    area += (y2[i] + y2[i + 1]) * (x2[i + 1] - x2[i]) / 2
print(area)
for i in range(n):
    mp.gca().add_patch(mc.Polygon([
        [x2[i], 0], [x2[i], y2[i]],
        [x2[i + 1], y2[i + 1]], [x2[i + 1], 0]],
        fc='deepskyblue', ec='dodgerblue',
        alpha=0.5))
```



调用scipy.integrate模块的quad方法计算积分：

```python
import scipy.integrate as si
# 利用quad求积分 给出函数f，积分下限与积分上限[a, b]   返回(积分值，最大误差)
area = si.quad(f, a, b)[0]
print(area)
```

### 图像

scipy.ndimage中提供了一些简单的图像处理，如高斯模糊、任意角度旋转、边缘识别等功能。

```python
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import matplotlib.pyplot as mp
#读取文件
original = sm.imread('../../data/head.jpg', True)
#高斯模糊
median = sn.median_filter(original, 21)
#角度旋转
rotate = sn.rotate(original, 45)
#边缘识别
prewitt = sn.prewitt(original)
mp.figure('Image', facecolor='lightgray')
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.axis('off')
mp.imshow(original, cmap='gray')
mp.subplot(222)
mp.title('Median', fontsize=16)
mp.axis('off')
mp.imshow(median, cmap='gray')
mp.subplot(223)
mp.title('Rotate', fontsize=16)
mp.axis('off')
mp.imshow(rotate, cmap='gray')
mp.subplot(224)
mp.title('Prewitt', fontsize=16)
mp.axis('off')
mp.imshow(prewitt, cmap='gray')
mp.tight_layout()
mp.show()
```

### 金融相关

```python
import numpy as np
# 终值 = np.fv(利率, 期数, 每期支付, 现值)
# 将1000元以1%的年利率存入银行5年，每年加存100元，
# 到期后本息合计多少钱？
fv = np.fv(0.01, 5, -100, -1000)
print(round(fv, 2))
# 现值 = np.pv(利率, 期数, 每期支付, 终值)
# 将多少钱以1%的年利率存入银行5年，每年加存100元，
# 到期后本息合计fv元？
pv = np.pv(0.01, 5, -100, fv)
print(pv)
# 净现值 = np.npv(利率, 现金流)
# 将1000元以1%的年利率存入银行5年，每年加存100元，
# 相当于一次性存入多少钱？
npv = np.npv(0.01, [
    -1000, -100, -100, -100, -100, -100])
print(round(npv, 2))
fv = np.fv(0.01, 5, 0, npv)
print(round(fv, 2))
# 内部收益率 = np.irr(现金流)
# 将1000元存入银行5年，以后逐年提现100元、200元、
# 300元、400元、500元，银行利率达到多少，可在最后
# 一次提现后偿清全部本息，即净现值为0元？
irr = np.irr([-1000, 100, 200, 300, 400, 500])
print(round(irr, 2))
npv = np.npv(irr, [-1000, 100, 200, 300, 400, 500])
print(npv)
# 每期支付 = np.pmt(利率, 期数, 现值)
# 以1%的年利率从银行贷款1000元，分5年还清，
# 平均每年还多少钱？
pmt = np.pmt(0.01, 5, 1000)
print(round(pmt, 2))
# 期数 = np.nper(利率, 每期支付, 现值)
# 以1%的年利率从银行贷款1000元，平均每年还pmt元，
# 多少年还清？
nper = np.nper(0.01, pmt, 1000)
print(int(nper))
# 利率 = np.rate(期数, 每期支付, 现值, 终值)
# 从银行贷款1000元，平均每年还pmt元，nper年还清，
# 年利率多少？
rate = np.rate(nper, pmt, 1000, 0)
print(round(rate, 2))
```



# 机器学习DAY01

## 机器学习

### 概述

#### 什么是机器学习

机器学习是一门能够让编程计算机从数据中学习的计算机科学。
一个计算机程序在完成任务T之后，获得经验E，其表现效果为P，如果任务T的性能表现，也就是用以衡量的P，随着E增加而增加，那么这样计算机程序就被称为机器学习系统。
自我完善，自我增进，自我适应。

#### 为什么需要机器学习

* 自动化的升级和维护
* 解决那些算法过于复杂甚至跟本就没有已知算法的问题
* 
  在机器学习的过程中协助人类获得对事物的洞见

#### 机器学习的问题

1. 建模问题
   所谓机器学习，在形式上可这样理解：在数据对象中通过统计或推理的方法，寻找一个接受特定输入X，并给出预期输出Y的功能函数f，即Y=f(X)。
2. 评估问题
   针对已知的输入，函数给出的输出(预测值)与实际输出(目标值)之间存在一定的误差，因此需要构建一个评估体系，根据误差的大小判定函数的优劣。
3. 优化问题
   学习的核心在于改善性能，通过数据对算法的反复锤炼，不断提升函数预测的准确性，直至获得能够满足实际需求的最优解，这个过程就是机器学习。

#### 机器学习的种类

**监督学习、无监督学习、半监督学习、强化学习**

1. 有监督学习：用已知输出评估模型的性能。
2. 无监督学习：在没有已知输出的情况下，仅仅根据输入信息的相关性，进行类别的划分。
3. 半监督学习：先通过无监督学习划分类别，再根据人工标记通过有监督学习预测输出。
4. 强化学习：通过对不同决策结果的奖励和惩罚，使机器学习系统在经过足够长时间的训练以后，越来越倾向于给出接近期望结果的输出。

**批量学习和增量学习**

1. 批量学习：将学习的过程和应用的过程截然分开，用全部的训练数据训练模型，然后再在应用场景中实现预测，当预测结果不够理想时，重新回到学习过程，如此循环。
2. 增量学习：将学习的过程和应用的过程统一起来，在应用的同时以增量的方式，不断学习新的内容，边训练边预测。

**基于实例的学习和基于模型的学习**

1. 根据以往的经验，寻找与待预测输入最接近的样本，以其输出作为预测结果。

   | 年龄 | 学历 | 经验 | 性别 | 月薪  |
   | ---- | ---- | ---- | ---- | ----- |
   | 25   | 硕士 | 2    | 女   | 10000 |
   | 20   | 本科 | 3    |      | 8000  |
   | ...  | ...  | ...  | ...  | ...   |
   | 20   | 本科 | 3    | 男   | ？    |

2. 基于模型的学习：根据以往的经验，建立用于联系输出和输入的某种数学模型，将待预测输入代入该模型，预测其结果。
   输入 -> 输出
   1           2
   2           4
   3           6   Y = 2 * X
   ...
   9           ?    -> 18

#### 机器学习的一般过程

**数据处理**

1. 数据收集 （数据检索、数据挖掘、爬虫）
2. 数据清洗

**机器学习**

1. 选择模型 （算法）
2. 训练模型 （算法）
3. 评估模型 （工具、框架、算法知识）
4. 测试模型

**业务运维**

1. 应用模型
2. 维护模型



#### 机器学习的典型应用

股价预测、推荐引擎、自然语言识别、语音识别、图像识别、人脸识别

#### 机器学习的基本问题

1)回归问题：根据已知的输入和输出寻找某种性能最佳的模型，将未知输出的输入代入模型，得到连续的输出。

2)分类问题：根据已知的输入和输出寻找某种性能最佳的模型，将未知输出的输入代入模型，得到离散的输出。

3)聚类问题：根据已知输入的相似程度，将其划分为不同的群落。

4)降维问题：在性能损失尽可能小的前提下，降低数据的复杂度。

### 数据预处理

数据预处理的过程： 输入数据 -> 模型 -> 输出数据

数据样本矩阵

| 年龄 | 学历 | 经验 | 性别 | 月薪  |
| ---- | ---- | ---- | ---- | ----- |
| 25   | 硕士 | 2    | 女   | 10000 |
| 20   | 本科 | 3    | 男   | 8000  |
| ...  | ...  | ...  | ...  | ...   |

一行一样本，一列一特征。

**数据预处理相关库**

```python
# 解决机器学习问题的科学计算工具包
import sklearn.preprocessing as sp
```

#### 均值移除(标准化)

由于一个样本的不同特征值差异较大，不利于使用现有机器学习算法进行样本处理。**均值移除**可以让样本矩阵中的每一列的平均值为0，标准差为1。

如何使样本矩阵中的每一列的平均值为0呢？

```
例如有一列特征值表示年龄： 17, 20, 23
mean = (17 + 20 + 23)/3 = 20
a' = -3
b' =  0
c' =  3
完成！
```

如何使样本矩阵中的每一列的标准差为1呢？

```
a' = -3
b' =  0
c' =  3
s' = std(a', b', c') 
[a'/s',  b'/s',  c'/s']
```

均值移除API：

```python
import sklearn.preprocessing as sp
# scale函数用于对函数进行预处理，实现均值移除。
# array为原数组，返回A为均值移除后的结果。
A = sp.scale(array)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])

std_samples = sp.scale(raw_samples)
print(std_samples)
print(std_samples.mean(axis=0))
print(std_samples.std(axis=0))
```

#### 范围缩放

将样本矩阵中的每一列的最小值和最大值设定为相同的区间，统一各列特征值的范围。一般情况下会把特征值缩放至[0, 1]区间。

如何使一组特征值的最小值为0呢？

```python
例如有一列特征值表示年龄： [17, 20, 23]
每个元素减去特征值数组所有元素的最小值即可：[0, 3, 6]
```

如何使一组特征值的最大值为1呢？

```python
[0, 3, 6]
把特征值数组的每个元素除以最大值即可：[0, 1/2, 1]
```

范围缩放API：

```python
# 创建MinMax缩放器
mms = sp.MinMaxScaler(feature_range=(0, 1))
# 调用mms对象的方法执行缩放操作, 返回缩放过后的结果
result = mms.fit_transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
print(raw_samples)
mms_samples = raw_samples.copy()
for col in mms_samples.T:
    col_min = col.min()
    col_max = col.max()
    a = np.array([
        [col_min, 1],
        [col_max, 1]])
    b = np.array([0, 1])
    x = np.linalg.solve(a, b)
    col *= x[0]
    col += x[1]
print(mms_samples)
# 根据给定范围创建一个范围缩放器
mms = sp.MinMaxScaler(feature_range=(0, 1))
# 用范围缩放器实现特征值的范围缩放
mms_samples = mms.fit_transform(raw_samples)
print(mms_samples)
```

#### 归一化

有些情况每个样本的每个特征值具体的值并不重要，但是每个样本特征值的占比更加重要。

|      | Python | Java | PHP  |
| ---- | ------ | ---- | ---- |
| 2017 | 10     | 20   | 5    |
| 2018 | 8      | 5    | 0    |

所以归一化即是用每个样本的每个特征值除以该样本各个特征值绝对值的总和。变换后的样本矩阵，每个样本的特征值绝对值之和为1。

归一化相关API：

```python
# array 原始样本矩阵
# norm  范数
#    l1 - l1范数，向量中个元素绝对值之和
#    l2 - l2范数，向量中个元素平方之和
# 返回归一化预处理后的样本矩阵
sp.normalize(array, norm='l1')
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
print(raw_samples)
nor_samples = raw_samples.copy()
for row in nor_samples:
    row /= abs(row).sum()
print(nor_samples)
print(abs(nor_samples).sum(axis=1))
# 归一化预处理
nor_samples = sp.normalize(raw_samples, norm='l1')
print(nor_samples)
print(abs(nor_samples).sum(axis=1))
```

#### 二值化

有些业务并不需要分析矩阵的详细完整数据（比如图像边缘识别只需要分析出图像边缘即可），可以根据一个事先给定的阈值，用0和1表示特征值不高于或高于阈值。二值化后的数组中每个元素非0即1，达到简化数学模型的目的。

二值化相关API：

```python
# 给出阈值, 获取二值化器
bin = sp.Binarizer(threshold=阈值)
# 调用transform方法对原始样本矩阵进行二值化预处理操作
result = bin.transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
print(raw_samples)
bin_samples = raw_samples.copy()
bin_samples[bin_samples <= 80] = 0
bin_samples[bin_samples > 80] = 1
print(bin_samples)
# 根据给定的阈值创建一个二值化器
bin = sp.Binarizer(threshold=80)
# 通过二值化器进行二值化预处理
bin_samples = bin.transform(raw_samples)
print(bin_samples)
```

#### 独热编码

为样本特征的每个值建立一个由一个1和若干个0组成的序列，用该序列对所有的特征值进行编码。

```
两个数   三个数	四个数
1		3		2
7		5		4
1		8		6  
7		3		9
为每一个数字进行独热编码：
1-10    3-100	2-1000
7-01    5-010   4-0100
        8-001   6-0010
                9-0001
编码完毕后得到最终经过独热编码后的样本矩阵：
101001000
010100100
100010010
011000001
```

独热编码相关API：

```python
# 创建一个独热编码器
# sparse： 是否使用紧缩格式（稀疏矩阵）
# dtyle：  数据类型
ohe = sp.OneHotEncoder(sparse=是否采用紧缩格式, dtype=数据类型)
# 对原始样本矩阵进行处理，返回独热编码后的样本矩阵。
result = ohe.fit_transform(原始样本矩阵)
```

```python
ohe = sp.OneHotEncoder(sparse=是否采用紧缩格式, dtype=数据类型)
# 对原始样本矩阵进行训练，得到编码字典
encode_dict = ohe.fit(原始样本矩阵)
# 调用encode_dict字典的transform方法 对数据样本矩阵进行独热编码
result = encode_dict.transform(原始样本矩阵)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    [17., 100., 4000],
    [20., 80., 5000],
    [23., 75., 5500]])
# 创建独热编码器
ohe = sp.OneHotEncoder(sparse=False, dtype=int)
# 用独特编码器对原始样本矩阵做独热编码
ohe_dict = ohe.fit(raw_samples)
ohe_samples = ohe_dict.transform(raw_samples)

ohe_samples = ohe.fit_transform(raw_samples)
print(ohe_samples)
```


#### 标签编码

根据字符串形式的特征值在特征序列中的位置，为其指定一个数字标签，用于提供给基于数值算法的学习模型。

标签编码相关API：

```python
# 获取标签编码器
lbe = sp.LabelEncoder()
# 调用标签编码器的fit_transform方法训练并且为原始样本矩阵进行标签编码
result = lbe.fit_transform(原始样本矩阵)
# 根据标签编码的结果矩阵反查字典 得到原始数据矩阵
samples = lbe.inverse_transform(result)
```

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
raw_samples = np.array([
    'audi', 'ford', 'audi', 'toyota',
    'ford', 'bmw', 'toyota', 'ford',
    'audi'])
print(raw_samples)
lbe = sp.LabelEncoder()
lbe_samples = lbe.fit_transform(raw_samples)
print(lbe_samples)
inv_samples = lbe.inverse_transform(lbe_samples)
print(inv_samples)
```

### 线性回归

```
输入		输出
0.5      5.0
0.6      5.5
0.8      6.0
1.1      6.8
1.4      7.0
...
y = f(x)
```

预测函数：y = w<sub>0</sub>+w<sub>1</sub>x
x: 输入
y: 输出
w<sub>0</sub>和w<sub>1</sub>: 模型参数

**所谓模型训练，就是根据已知的x和y，找到最佳的模型参数w<sub>0</sub> 和 w<sub>1</sub>，尽可能精确地描述出输入和输出的关系。**

5.0 = w<sub>0</sub> + w<sub>1</sub> &times; 0.5
5.5 = w<sub>0</sub> + w<sub>1</sub> &times; 0.6

单样本误差：

根据预测函数求出输入为x时的预测值：y' = w<sub>0</sub> + w<sub>1</sub>x，单样本误差为1/2(y' - y)<sup>2</sup>。

总样本误差：

把所有单样本误差相加即是总样本误差：1/2 &Sigma;(y' - y)<sup>2</sup>

损失函数：

loss = 1/2 &Sigma;(w<sub>0</sub> + w<sub>1</sub>x - y)<sup>2</sup>

所以损失函数就是总样本误差关于模型参数的函数，该函数属于三维数学模型，即需要找到一组w<sub>0</sub>  w<sub>1</sub>使得loss取极小值。

案例：画图模拟梯度下降的过程

1. 整理训练集数据，自定义梯度下降算法规则，求出w<sub>0</sub> ， w<sub>1</sub> ，绘制回归线。

```python
import numpy as np
import matplotlib.pyplot as mp
train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])
train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])
test_x = np.array([0.45, 0.55, 1.0, 1.3, 1.5])
test_y = np.array([4.8, 5.3, 6.4, 6.9, 7.3])

times = 1000	# 定义梯度下降次数
lrate = 0.01	# 记录每次梯度下降参数变化率
epoches = []	# 记录每次梯度下降的索引
w0, w1, losses = [1], [1], []
for i in range(1, times + 1):
    epoches.append(i)
    loss = (((w0[-1] + w1[-1] * train_x) - train_y) ** 2).sum() / 2
    losses.append(loss)
    d0 = ((w0[-1] + w1[-1] * train_x) - train_y).sum()
    d1 = (((w0[-1] + w1[-1] * train_x) - train_y) * train_x).sum()
    print('{:4}> w0={:.8f}, w1={:.8f}, loss={:.8f}'.format(epoches[-1], w0[-1], w1[-1], losses[-1]))
    w0.append(w0[-1] - lrate * d0)
    w1.append(w1[-1] - lrate * d1)

pred_test_y = w0[-1] + w1[-1] * test_x
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(train_x, train_y, marker='s', c='dodgerblue', alpha=0.5, s=80, label='Training')
mp.scatter(test_x, test_y, marker='D', c='orangered', alpha=0.5, s=60, label='Testing')
mp.scatter(test_x, pred_test_y, c='orangered', alpha=0.5, s=80, label='Predicted')
mp.plot(test_x, pred_test_y, '--', c='limegreen', label='Regression', linewidth=1)
mp.legend()
mp.show()
```

2. 绘制随着每次梯度下降，w<sub>0</sub>，w<sub>1</sub>，loss的变化曲线。

```python
w0 = w0[:-1]
w1 = w1[:-1]

mp.figure('Training Progress', facecolor='lightgray')
mp.subplot(311)
mp.title('Training Progress', fontsize=20)
mp.ylabel('w0', fontsize=14)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w0, c='dodgerblue', label='w0')
mp.legend()
mp.subplot(312)
mp.ylabel('w1', fontsize=14)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, w1, c='limegreen', label='w1')
mp.legend()

mp.subplot(313)
mp.xlabel('epoch', fontsize=14)
mp.ylabel('loss', fontsize=14)
mp.gca().xaxis.set_major_locator(mp.MultipleLocator(100))
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(epoches, losses, c='orangered', label='loss')
mp.legend()
```

3. 基于三维曲面绘制梯度下降过程中的每一个点。

```python
import mpl_toolkits.mplot3d as axes3d

grid_w0, grid_w1 = np.meshgrid(
    np.linspace(0, 9, 500),
    np.linspace(0, 3.5, 500))

grid_loss = np.zeros_like(grid_w0)
for x, y in zip(train_x, train_y):
    grid_loss += ((grid_w0 + x*grid_w1 - y) ** 2) / 2

mp.figure('Loss Function')
ax = mp.gca(projection='3d')
mp.title('Loss Function', fontsize=20)
ax.set_xlabel('w0', fontsize=14)
ax.set_ylabel('w1', fontsize=14)
ax.set_zlabel('loss', fontsize=14)
ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cstride=10, cmap='jet')
ax.plot(w0, w1, losses, 'o-', c='orangered', label='BGD')
mp.legend()
```

4. 以等高线的方式绘制梯度下降的过程。

```python
mp.figure('Batch Gradient Descent', facecolor='lightgray')
mp.title('Batch Gradient Descent', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.contourf(grid_w0, grid_w1, grid_loss, 10, cmap='jet')
cntr = mp.contour(grid_w0, grid_w1, grid_loss, 10,
                  colors='black', linewidths=0.5)
mp.clabel(cntr, inline_spacing=0.1, fmt='%.2f',
          fontsize=8)
mp.plot(w0, w1, 'o-', c='orangered', label='BGD')
mp.legend()
mp.show()

```

### 线性回归

线性回归相关API：

```python
import sklearn.linear_model as lm
# 创建模型
model = lm.LinearRegression()
# 训练模型
# 输入为一个二维数组表示的样本矩阵
# 输出为每个样本最终的结果
model.fit(输入, 输出) # 通过梯度下降法计算模型参数
# 预测输出  
# 输入array是一个二维数组，每一行是一个样本，每一列是一个特征。
result = model.predict(array)
```

案例：基于线性回归训练single.txt中的训练样本，使用模型预测测试样本。

```python
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
# 采集数据
x, y = np.loadtxt('../data/single.txt', delimiter=',', usecols=(0,1), unpack=True)
x = x.reshape(-1, 1)
# 创建模型
model = lm.LinearRegression()  # 线性回归
# 训练模型
model.fit(x, y)
# 根据输入预测输出
pred_y = model.predict(x)
mp.figure('Linear Regression', facecolor='lightgray')
mp.title('Linear Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, s=60, label='Sample')
mp.plot(x, pred_y, c='orangered', label='Regression')
mp.legend()
mp.show()
```

#### 评估训练结果误差（metrics）

线性回归模型训练完毕后，可以利用测试集评估训练结果误差。sklearn.metrics提供了计算模型误差的几个常用算法：

```python
import sklearn.metrics as sm

# 平均绝对值误差：1/m∑|实际输出-预测输出|
sm.mean_absolute_error(y, pred_y)
# 平均平方误差：SQRT(1/mΣ(实际输出-预测输出)^2)
sm.mean_squared_error(y, pred_y)
# 中位绝对值误差：MEDIAN(|实际输出-预测输出|)
sm.median_absolute_error(y, pred_y)
# R2得分，(0,1]区间的分值。分数越高，误差越小。
sm.r2_score(y, pred_y)
```

案例：在上一个案例中使用sm评估模型误差。

```python
# 平均绝对值误差：1/m∑|实际输出-预测输出|
print(sm.mean_absolute_error(y, pred_y))
# 平均平方误差：SQRT(1/mΣ(实际输出-预测输 出)^2)
print(sm.mean_squared_error(y, pred_y))
# 中位绝对值误差：MEDIAN(|实际输出-预测输出|)
print(sm.median_absolute_error(y, pred_y))
# R2得分，(0,1]区间的分值。分数越高，误差越小。
print(sm.r2_score(y, pred_y))
```

#### 模型的保存和加载

模型训练是一个耗时的过程，一个优秀的机器学习是非常宝贵的。可以模型保存到磁盘中，也可以在需要使用的时候从磁盘中重新加载模型即可。不需要重新训练。

模型保存和加载相关API：

```python
import pickle
pickle.dump(内存对象, 磁盘文件) # 保存模型
model = pickle.load(磁盘文件)  # 加载模型
```

案例：把训练好的模型保存到磁盘中。

```python
# 将训练好的模型对象保存到磁盘文件中
with open('../../data/linear.pkl', 'wb') as f:
    pickle.dump(model, f)
    
# 从磁盘文件中加载模型对象
with open('../../data/linear.pkl', 'rb') as f:
    model = pickle.load(f)
# 根据输入预测输出
pred_y = model.predict(x)
```

#### 岭回归

普通线性回归模型使用基于梯度下降的最小二乘法，在最小化损失函数的前提下，寻找最优模型参数，于此过程中，包括少数异常样本在内的全部训练数据都会对最终模型参数造成程度相等的影响，异常值对模型所带来影响无法在训练过程中被识别出来。为此，岭回归在模型迭代过程所依据的损失函数中增加了正则项，以限制模型参数对异常样本的匹配程度，进而提高模型面对多数正常样本的拟合精度。

```python
import sklearn.linear_model as lm
# 创建模型
model = lm.Ridge(正则强度，fit_intercept=是否训练截距, max_iter=最大迭代次数)
# 训练模型
# 输入为一个二维数组表示的样本矩阵
# 输出为每个样本最终的结果
model.fit(输入, 输出)
# 预测输出  
# 输入array是一个二维数组，每一行是一个样本，每一列是一个特征。
result = model.predict(array)
```

案例：加载abnormal.txt文件中的数据，基于岭回归算法训练回归模型。

```python
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
# 采集数据
x, y = np.loadtxt('../data/single.txt', delimiter=',', usecols=(0,1), unpack=True)
x = x.reshape(-1, 1)
# 创建线性回归模型
model = lm.LinearRegression() 
# 训练模型
model.fit(x, y)
# 根据输入预测输出
pred_y1 = model.predict(x)
# 创建岭回归模型
model = lm.Ridge(150, fit_intercept=True, max_iter=10000) 
# 训练模型
model.fit(x, y)
# 根据输入预测输出
pred_y2 = model.predict(x)

mp.figure('Linear & Ridge', facecolor='lightgray')
mp.title('Linear & Ridge', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75,
           s=60, label='Sample')
sorted_indices = x.T[0].argsort()
mp.plot(x[sorted_indices], pred_y1[sorted_indices],
        c='orangered', label='Linear')
mp.plot(x[sorted_indices], pred_y2[sorted_indices],
        c='limegreen', label='Ridge')
mp.legend()
mp.show()
```

### 多项式回归

若希望回归模型更好的拟合训练样本数据，可以使用多项式回归器。

**一元多项式回归**

y=w<sub>0</sub> + w<sub>1</sub> x + w<sub>2</sub> x<sup>2</sup> + w<sub>3</sub> x<sup>3</sup> + ... + w<sub>d</sub> x<sup>d</sup>

将高次项看做对一次项特征的扩展得到：

y=w<sub>0</sub> + w<sub>1</sub> x<sub>1</sub>  + w<sub>2</sub> x<sub>2</sub>  + w<sub>3</sub> x<sub>3</sub>  + ... + w<sub>d</sub> x<sub>d</sub> 

那么一元多项式回归即可以看做为多元线性回归，可以使用LinearRegression模型对样本数据进行模型训练。

所以一元多项式回归的实现需要两个步骤：

1. 将一元多项式回归问题转换为多元线性回归问题（只需给出多项式最高次数即可）。
2. 将1步骤得到多项式的结果中 w<sub>1</sub>  w<sub>2</sub>  .. 当做样本特征，交给线性回归器训练多元线性模型。

使用sklearn提供的**数据管线**实现两个步骤的顺序执行：

```python
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm

model = pl.make_pipeline(
    sp.PolynomialFeatures(10),  # 多项式特征扩展器
    lm.LinearRegression())      # 线性回归器
```

案例：

```python
import numpy as np
import sklearn.pipeline as pl
import sklearn.preprocessing as sp
import sklearn.linear_model as lm
import sklearn.metrics as sm
import matplotlib.pyplot as mp
# 采集数据
x, y = np.loadtxt('../data/single.txt', delimiter=',', usecols=(0,1), unpack=True)
x = x.reshape(-1, 1)
# 创建模型(管线)
model = pl.make_pipeline(
    sp.PolynomialFeatures(10),  # 多项式特征扩展器
    lm.LinearRegression())      # 线性回归器
# 训练模型
model.fit(x, y)
# 根据输入预测输出
pred_y = model.predict(x)
test_x = np.linspace(x.min(), x.max(), 1000).reshape(-1, 1)
pred_test_y = model.predict(test_x)
mp.figure('Polynomial Regression', facecolor='lightgray')
mp.title('Polynomial Regression', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.scatter(x, y, c='dodgerblue', alpha=0.75, s=60, label='Sample')
mp.plot(test_x, pred_test_y, c='orangered', label='Regression')
mp.legend()
mp.show()
```

过于简单的模型，无论对于训练数据还是测试数据都无法给出足够高的预测精度，这种现象叫做欠拟合。

过于复杂的模型，对于训练数据可以得到较高的预测精度，但对于测试数据通常精度较低，这种现象叫做过拟合。

一个性能可以接受的学习模型应该对训练数据和测试数据都有接近的预测精度，而且精度不能太低。

```
训练集R2   测试集R2
0.3        0.4        欠拟合：过于简单，无法反映数据的规则
0.9        0.2        过拟合：过于复杂，太特殊，缺乏一般性
0.7        0.6        可接受：复杂度适中，既反映数据的规则，同时又不失一般性
```

### 决策树

#### 基本算法原理

核心思想：相似的输入必会产生相似的输出。例如预测某人薪资：

年龄：1-青年，2-中年，3-老年
学历：1-本科，2-硕士，3-博士
经历：1-出道，2-一般，3-老手，4-骨灰
性别：1-男性，2-女性

| 年龄 | 学历 | 经历 | 性别 | ==>  | 薪资        |
| ---- | ---- | ---- | ---- | ---- | ----------- |
| 1    | 1    | 1    | 1    | ==>  | 6000（低）  |
| 2    | 1    | 3    | 1    | ==>  | 10000（中） |
| 3    | 3    | 4    | 1    | ==>  | 50000（高） |
| ...  | ...  | ...  | ...  | ==>  | ...         |
| 1    | 3    | 2    | 2    | ==>  | ?           |

为了提高搜索效率，使用树形数据结构处理样本数据：
$$
年龄=1\left\{
\begin{aligned}
学历1 \\
学历2 \\
学历3 \\
\end{aligned}
\right.
\quad\quad
年龄=2\left\{
\begin{aligned}
学历1 \\
学历2 \\
学历3 \\
\end{aligned}
\right.
\quad\quad
年龄=3\left\{
\begin{aligned}
学历1 \\
学历2 \\
学历3 \\
\end{aligned}
\right.
$$
首先从训练样本矩阵中选择第一个特征进行子表划分，使每个子表中该特征的值全部相同，然后再在每个子表中选择下一个特征按照同样的规则继续划分更小的子表，不断重复直到所有的特征全部使用完为止，此时便得到叶级子表，其中所有样本的特征值全部相同。对于待预测样本，根据其每一个特征的值，选择对应的子表，逐一匹配，直到找到与之完全匹配的叶级子表，用该子表中样本的输出，通过平均(回归)或者投票(分类)为待预测样本提供输出。

随着子表的划分，信息熵（信息的混乱程度）越来越小，信息越来越纯，数据越来越有序。

决策树回归器模型相关API：

```python
import sklearn.tree as st

# 创建决策树回归器模型  决策树的最大深度为4
model = st.DecisionTreeRegressor(max_depth=4)
# 训练模型  
# train_x： 二维数组样本数据
# train_y： 训练集中对应每行样本的结果
model.fit(train_x, train_y)
# 测试模型
pred_test_y = model.predict(test_x)
```

案例：预测波士顿地区房屋价格。

1. 读取数据，打断原始数据集。 划分训练集和测试集。

```python
import sklearn.datasets as sd
import sklearn.utils as su
# 加载波士顿地区房价数据集
boston = sd.load_boston()
print(boston.feature_names)
# |CRIM|ZN|INDUS|CHAS|NOX|RM|AGE|DIS|RAD|TAX|PTRATIO|B|LSTAT|
# 犯罪率|住宅用地比例|商业用地比例|是否靠河|空气质量|房间数|年限|距中心区距离|路网密度|房产税|师生比|黑人比例|低地位人口比例|
# 打乱原始数据集的输入和输出
x, y = su.shuffle(boston.data, boston.target, random_state=7)
# 划分训练集和测试集
train_size = int(len(x) * 0.8)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
```

1. 创建决策树回归器模型，使用训练集训练模型。使用测试集测试模型。

```python
import sklearn.tree as st
import sklearn.metrics as sm

# 创建决策树回归模型
model = st.DecisionTreeRegressor(max_depth=4)
# 训练模型
model.fit(train_x, train_y)
# 测试模型
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
```

#### 工程优化

不必用尽所有的特征，叶级子表中允许混杂不同的特征值，以此降低决策树的层数，在精度牺牲可接受的前提下，提高模型的性能。通常情况下，可以优先选择使<b style='color:red;'>信息熵</b>减少量最大的特征作为划分子表的依据。

#### 集合算法

根据多个不同模型给出的预测结果，利用平均(回归)或者投票(分类)的方法，得出最终预测结果。

基于决策树的集合算法，就是按照某种规则，构建多棵彼此不同的决策树模型，分别给出针对未知样本的预测结果，最后通过平均或投票得到相对综合的结论。

##### 正向激励

首先为样本矩阵中的样本随机分配初始权重，由此构建一棵带有权重的决策树，在由该决策树提供预测输出时，通过加权平均或者加权投票的方式产生预测值。将训练样本代入模型，预测其输出，对那些预测值与实际值不同的样本，提高其权重，由此形成第二棵决策树。重复以上过程，构建出不同权重的若干棵决策树。

正向激励相关API：

```python
import sklearn.tree as st
import sklearn.ensemble as se
# model: 决策树模型（一颗）
model = st.DecisionTreeRegressor(max_depth=4)
# 自适应增强决策树回归模型	
# n_estimators：构建400棵不同权重的决策树，训练模型
model = se.AdaBoostRegressor(model, n_estimators=400, random_state=7)
# 训练模型
model.fit(train_x, train_y)
# 测试模型
pred_test_y = model.predict(test_x)
```

案例：基于正向激励训练预测波士顿地区房屋价格的模型。

```python
# 创建基于决策树的正向激励回归器模型
model = se.AdaBoostRegressor(
	st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
# 训练模型
model.fit(train_x, train_y)
# 测试模型
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
```

**特征重要性**

作为决策树模型训练过程的副产品，根据每个特征划分子表前后的信息熵减少量就标志了该特征的重要程度，此即为该特征重要性指标。训练得到的模型对象提供了属性：feature_importances_来存储每个特征的重要性。

获取样本矩阵特征重要性属性：

```python
model.fit(train_x, train_y)
fi = model.feature_importances_
```

案例：获取普通决策树与正向激励决策树训练的两个模型的特征重要性值，按照从大到小顺序输出绘图。

```python
import matplotlib.pyplot as mp

model = st.DecisionTreeRegressor(max_depth=4)
model.fit(train_x, train_y)
# 决策树回归器给出的特征重要性
fi_dt = model.feature_importances_
model = se.AdaBoostRegressor(
    st.DecisionTreeRegressor(max_depth=4), n_estimators=400, random_state=7)
model.fit(train_x, train_y)
# 基于决策树的正向激励回归器给出的特征重要性
fi_ab = model.feature_importances_

mp.figure('Feature Importance', facecolor='lightgray')
mp.subplot(211)
mp.title('Decision Tree', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_dt.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_dt[sorted_indices], facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, feature_names[sorted_indices], rotation=30)
mp.subplot(212)
mp.title('AdaBoost Decision Tree', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_ab.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_ab[sorted_indices], facecolor='lightcoral', edgecolor='indianred')
mp.xticks(pos, feature_names[sorted_indices], rotation=30)
mp.tight_layout()
mp.show()
```

##### 自助聚合

每次从总样本矩阵中以有放回抽样的方式随机抽取部分样本构建决策树，这样形成多棵包含不同训练样本的决策树，以削弱某些强势样本对模型预测结果的影响，提高模型的泛化特性。

##### 随机森林

在自助聚合的基础上，每次构建决策树模型时，不仅随机选择部分样本，而且还随机选择部分特征，这样的集合算法，不仅规避了强势样本对预测结果的影响，而且也削弱了强势特征的影响，使模型的预测能力更加泛化。

随机森林相关API：

```python
import sklearn.ensemble as se
# 随机森林回归模型	（属于集合算法的一种）
# max_depth：决策树最大深度10
# n_estimators：构建1000棵决策树，训练模型
# min_samples_split: 子表中最小样本数 若小于这个数字，则不再继续向下拆分
model = se.RandomForestRegressor(max_depth=10, n_estimators=1000, min_samples_split=2)
```

案例：分析共享单车的需求，从而判断如何进行共享单车的投放。

```python
import numpy as np
import sklearn.utils as su
import sklearn.ensemble as se
import sklearn.metrics as sm
import matplotlib.pyplot as mp

data = np.loadtxt('../data/bike_day.csv', unpack=False, dtype='U20', delimiter=',')
day_headers = data[0, 2:13]
x = np.array(data[1:, 2:13], dtype=float)
y = np.array(data[1:, -1], dtype=float)

x, y = su.shuffle(x, y, random_state=7)
print(x.shape, y.shape)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], y[:train_size], y[train_size:]
# 随机森林回归器
model = se.RandomForestRegressor( max_depth=10, n_estimators=1000, min_samples_split=2)
model.fit(train_x, train_y)
# 基于“天”数据集的特征重要性
fi_dy = model.feature_importances_
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))

data = np.loadtxt('../data/bike_hour.csv', unpack=False, dtype='U20', delimiter=',')
hour_headers = data[0, 2:13]
x = np.array(data[1:, 2:13], dtype=float)
y = np.array(data[1:, -1], dtype=float)
x, y = su.shuffle(x, y, random_state=7)
train_size = int(len(x) * 0.9)
train_x, test_x, train_y, test_y = \
    x[:train_size], x[train_size:], \
    y[:train_size], y[train_size:]
# 随机森林回归器
model = se.RandomForestRegressor(
    max_depth=10, n_estimators=1000,
    min_samples_split=2)
model.fit(train_x, train_y)
# 基于“小时”数据集的特征重要性
fi_hr = model.feature_importances_
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
```

画图显示两组样本数据的特征重要性：

```python
mp.figure('Bike', facecolor='lightgray')
mp.subplot(211)
mp.title('Day', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_dy.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_dy[sorted_indices], facecolor='deepskyblue', edgecolor='steelblue')
mp.xticks(pos, day_headers[sorted_indices], rotation=30)

mp.subplot(212)
mp.title('Hour', fontsize=16)
mp.ylabel('Importance', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(axis='y', linestyle=':')
sorted_indices = fi_hr.argsort()[::-1]
pos = np.arange(sorted_indices.size)
mp.bar(pos, fi_hr[sorted_indices], facecolor='lightcoral', edgecolor='indianred')
mp.xticks(pos, hour_headers[sorted_indices], rotation=30)
mp.tight_layout()
mp.show()
```

### 人工分类

| 特征1 | 特征2 | 输出 |
| ----- | ----- | ---- |
| 3     | 1     | 0    |
| 2     | 5     | 1    |
| 1     | 8     | 1    |
| 6     | 4     | 0    |
| 5     | 2     | 0    |
| 3     | 5     | 1    |
| 4     | 7     | 1    |
| 4     | -1    | 0    |
| ...   | ...   | ...  |
| 6     | 8     | 1    |
| 5     | 1     | 0    |

案例：

```python
import numpy as np
import matplotlib.pyplot as mp
x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
grid_z = np.piecewise(grid_x, [grid_x>grid_y, grid_x<grid_y], [1, 0])

mp.figure('Simple Classification', facecolor='lightgray')
mp.title('Simple Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
```

### 逻辑分类

通过输入的样本数据，基于多元线型回归模型求出线性预测方程。

y = w<sub>0</sub>+w<sub>1</sub>x<sub>1</sub>+w<sub>2</sub>x<sub>2</sub>

但通过线型回归方程返回的是连续值，不可以直接用于分类业务模型，所以急需一种方式使得把连续的预测值->离散的预测值。   [-oo, +oo]->{0, 1} 
$$
逻辑函数：y = \frac{1}{1+e^{-x}}
$$
该逻辑函数当x>0，y>0.5；当x<0, y<0.5； 可以把样本数据经过线性预测模型求得的值带入逻辑函数的x，即将预测函数的输出看做输入被划分为1类的概率，择概率大的类别作为预测结果，可以根据函数值确定两个分类。这是线性函数非线性化的一种方式。

逻辑回归相关API：

```python
import sklearn.linear_model as lm
# 构建逻辑回归器 
# solver：逻辑函数中指数的函数关系（liblinear为线型函数关系）
# C：参数代表正则强度，为了防止过拟合。正则越大拟合效果越小。
model = lm.LogisticRegression(solver='liblinear', C=正则强度)
model.fit(训练输入集，训练输出集)
result = model.predict(带预测输入集)
```

案例：基于逻辑回归器绘制网格化坐标颜色矩阵。

```python
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
x = np.array([
    [3, 1],
    [2, 5],
    [1, 8],
    [6, 4],
    [5, 2],
    [3, 5],
    [4, 7],
    [4, -1]])
y = np.array([0, 1, 1, 0, 0, 1, 1, 0])`
# 逻辑分类器
model = lm.LogisticRegression(solver='liblinear', C=1)
model.fit(x, y)
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))

grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)
mp.figure('Logistic Classification', facecolor='lightgray')
mp.title('Logistic Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
```

**多元分类**

通过多个二元分类器解决多元分类问题。

| 特征1 | 特征2 | ==>  | 所属类别 |
| ----- | ----- | ---- | -------- |
| 4     | 7     | ==>  | A        |
| 3.5   | 8     | ==>  | A        |
| 1.2   | 1.9   | ==>  | B        |
| 5.4   | 2.2   | ==>  | C        |

若拿到一组新的样本，可以基于二元逻辑分类训练出一个模型判断属于A类别的概率。再使用同样的方法训练出两个模型分别判断属于B、C类型的概率，最终选择概率最高的类别作为新样本的分类结果。

案例：基于逻辑分类模型的多元分类。

```python
import numpy as np
import sklearn.linear_model as lm
import matplotlib.pyplot as mp
x = np.array([
    [4, 7],
    [3.5, 8],
    [3.1, 6.2],
    [0.5, 1],
    [1, 2],
    [1.2, 1.9],
    [6, 2],
    [5.7, 1.5],
    [5.4, 2.2]])
y = np.array([0, 0, 0, 1, 1, 1, 2, 2, 2])
# 逻辑分类器
model = lm.LogisticRegression(solver='liblinear', C=1000)
model.fit(x, y)
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
print(grid_z)
grid_z = grid_z.reshape(grid_x.shape)

mp.figure('Logistic Classification', facecolor='lightgray')
mp.title('Logistic Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
```

### 朴素贝叶斯分类  

朴素贝叶斯分类是一种依据统计概率理论而实现的一种分类方式。观察这组数据：

| 天气情况  | 穿衣风格  | 约女朋友  | ==>  | 心情      |
| --------- | --------- | --------- | ---- | --------- |
| 0（晴天） | 0（休闲） | 0（约了） | ==>  | 0（高兴） |
| 0         | 1（风骚） | 1（没约） | ==>  | 0         |
| 1（多云） | 1         | 0         | ==>  | 0         |
| 0         | 2（破旧） | 1         | ==>  | 1（郁闷） |
| 2（下雨） | 2         | 0         | ==>  | 0         |
| ...       | ...       | ...       | ==>  | ...       |
| 0         | 1         | 0         | ==>  | ？        |

通过上述训练样本如何预测：晴天、穿着休闲、没有约女朋友时的心情？可以整理相同特征值的样本，计算属于某类别的概率即可。但是如果在样本空间没有完全匹配的数据该如何预测？

**贝叶斯定理：P(A|B)=P(B|A)P(A)/P(B)      <==     *P(A, B) = P(A) P(B|A) = P(B) P(A|B)***       

例如：

假设一个学校里有60%男生和4 0%女生.女生穿裤子的人数和穿裙子的人数相等,所有男生穿裤子.一个人在远处随机看到了一个穿裤子的学生.那么这个学生是女生的概率是多少?

```
P(女) = 0.4
P(裤子|女) = 0.5
P(裤子) = 0.6 + 0.2 = 0.8
P(女|裤子) = P(裤子|女) * P(女) / P(裤子) = 0.5 * 0.4 / 0.8 = 0.25
```

根据贝叶斯定理，如何预测：晴天、穿着休闲、没有约女朋友时的心情？

```
P(晴天,休闲,没约,高兴) 
= P(晴天|休闲,没约,高兴) P(休闲,没约,高兴) 
= P(晴天|休闲,没约,高兴) P(休闲|没约,高兴) P(没约,高兴)
= P(晴天|休闲,没约,高兴) P(休闲|没约,高兴) P(没约|高兴)P(高兴)
（ 朴素：条件独立，特征值之间没有因果关系）
= P(晴天|高兴) P(休闲|高兴) P(没约|高兴)P(高兴)
```

由此可得，统计总样本空间中晴天、穿着休闲、没有约女朋友时高兴的概率，与晴天、穿着休闲、没有约女朋友时不高兴的概率，择其大者为最终结果。

高斯贝叶斯分类器相关API：

```python
# 创建高斯分布朴素贝叶斯分类器
model = nb.GaussianNB()
model.fit(x, y)
result = model.predict(samples)
```

案例：

```python
import numpy as np
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp

data = np.loadtxt('../data/multiple1.txt', unpack=False, dtype='U20', delimiter=',')
print(data.shape)
x = np.array(data[:, :-1], dtype=float)
y = np.array(data[:, -1], dtype=float)

# 创建高斯分布朴素贝叶斯分类器
model = nb.GaussianNB()
model.fit(x, y)
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)

mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=y, cmap='brg', s=80)
mp.show()
```

#### 数据集划分

对于分类问题训练集和测试集的划分不应该用整个样本空间的特定百分比作为训练数据，而应该在其每一个类别的样本中抽取特定百分比作为训练数据。sklearn模块提供了数据集划分相关方法，可以方便的划分训练集与测试集数据，使用不同数据集训练或测试模型，达到提高分类可信度。

数据集划分相关API：

```python
import sklearn.model_selection as ms

ms.train_test_split(输入集, 输出集, test_size=测试集占比, random_state=随机种子)
    ->训练输入, 测试输入, 训练输出, 测试输出
```

案例：

```python
import numpy as np
import sklearn.model_selection as ms
import sklearn.naive_bayes as nb
import matplotlib.pyplot as mp
data = np.loadtxt('../data/multiple1.txt', unpack=False, dtype='U20', delimiter=',')
print(data.shape)
x = np.array(data[:, :-1], dtype=float)
y = np.array(data[:, -1], dtype=float)
# 划分训练集和测试集
train_x, test_x, train_y, test_y = \
    ms.train_test_split( x, y, test_size=0.25, random_state=7)
# 朴素贝叶斯分类器
model = nb.GaussianNB()
# 用训练集训练模型
model.fit(train_x, train_y)

l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
n = 500
grid_x, grid_y = np.meshgrid(np.linspace(l, r, n), np.linspace(b, t, n))
samples = np.column_stack((grid_x.ravel(), grid_y.ravel()))
grid_z = model.predict(samples)
grid_z = grid_z.reshape(grid_x.shape)

pred_test_y = model.predict(test_x)
# 计算并打印预测输出的精确度
print((test_y == pred_test_y).sum() / pred_test_y.size)

mp.figure('Naive Bayes Classification', facecolor='lightgray')
mp.title('Naive Bayes Classification', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x, grid_y, grid_z, cmap='gray')
mp.scatter(test_x[:,0], test_x[:,1], c=test_y, cmap='brg', s=80)
mp.show()
```

#### 交叉验证

由于数据集的划分有不确定性，若随机划分的样本正好处于某类特殊样本，则得到的训练模型所预测的结果的可信度将受到质疑。所以需要进行多次交叉验证，把样本空间中的所有样本均分成n份，使用不同的训练集训练模型，对不同的测试集进行测试时输出指标得分。sklearn提供了交叉验证相关API：

```python
import sklearn.model_selection as ms
ms.cross_val_score(模型, 输入集, 输出集, cv=折叠数, scoring=指标名)->指标值数组
```

案例：使用交叉验证，输出分类器的精确度：

```python
# 划分训练集和测试集
train_x, test_x, train_y, test_y = \
    ms.train_test_split(
        x, y, test_size=0.25, random_state=7)
# 朴素贝叶斯分类器
model = nb.GaussianNB()
# 交叉验证
# 精确度
ac = ms.cross_val_score( model, train_x, train_y, cv=5, scoring='accuracy')
print(ac.mean())
#用训练集训练模型
model.fit(train_x, train_y)
```

**交叉验证指标**

1. 精确度(accuracy)：分类正确的样本数/总样本数

2. 查准率(precision_weighted)：针对每一个类别，预测正确的样本数比上预测出来的样本数

3. 召回率(recall_weighted)：针对每一个类别，预测正确的样本数比上实际存在的样本数

4. f1得分(f1_weighted)：

   2x查准率x召回率/(查准率+召回率)

在交叉验证过程中，针对每一次交叉验证，计算所有类别的查准率、召回率或者f1得分，然后取各类别相应指标值的平均数，作为这一次交叉验证的评估指标，然后再将所有交叉验证的评估指标以数组的形式返回调用者。

```python
# 交叉验证
# 精确度
ac = ms.cross_val_score( model, train_x, train_y, cv=5, scoring='accuracy')
print(ac.mean())
# 查准率
pw = ms.cross_val_score( model, train_x, train_y, cv=5, scoring='precision_weighted')
print(pw.mean())
# 召回率
rw = ms.cross_val_score( model, train_x, train_y, cv=5, scoring='recall_weighted')
print(rw.mean())
# f1得分
fw = ms.cross_val_score( model, train_x, train_y, cv=5, scoring='f1_weighted')
print(fw.mean())
```

#### 混淆矩阵

每一行和每一列分别对应样本输出中的每一个类别，行表示实际类别，列表示预测类别。

|       | A类别 | B类别 | C类别 |
| ----- | ----- | ----- | ----- |
| A类别 | 5     | 0     | 0     |
| B类别 | 0     | 6     | 0     |
| C类别 | 0     | 0     | 7     |

上述矩阵即为理想的混淆矩阵。不理想的混淆矩阵如下：

|       | A类别 | B类别 | C类别 |
| ----- | ----- | ----- | ----- |
| A类别 | 3     | 1     | 1     |
| B类别 | 0     | 4     | 2     |
| C类别 | 0     | 0     | 7     |

 查准率 = 主对角线上的值 / 该值所在列的和 

召回率 = 主对角线上的值 / 该值所在行的和

获取模型分类结果的混淆矩阵的相关API：

```python
import sklearn.metrics as sm
sm.confusion_matrix(实际输出, 预测输出)->混淆矩阵
```

案例：输出分类结果的混淆矩阵。

```python
#输出混淆矩阵并绘制混淆矩阵图谱
cm = sm.confusion_matrix(test_y, pred_test_y)
print(cm)
mp.figure('Confusion Matrix', facecolor='lightgray')
mp.title('Confusion Matrix', fontsize=20)
mp.xlabel('Predicted Class', fontsize=14)
mp.ylabel('True Class', fontsize=14)
mp.xticks(np.unique(pred_test_y))
mp.yticks(np.unique(test_y))
mp.tick_params(labelsize=10)
mp.imshow(cm, interpolation='nearest', cmap='jet')
mp.show()
```

#### 分类报告

sklearn.metrics提供了分类报告相关API，不仅可以得到混淆矩阵，还可以得到交叉验证查准率、召回率、f1得分的结果，可以方便的分析出哪些样本是异常样本。

```python
# 获取分类报告
cr = sm.classification_report(实际输出, 预测输出)
```

案例：输出分类报告：

```python
# 获取分类报告
cr = sm.classification_report(test_y, pred_test_y)
print(cr)
```

### 决策树分类

决策树分类模型会找到与样本特征匹配的叶子节点然后以投票的方式进行分类。在样本文件中统计了小汽车的常见特征信息及小汽车的分类，使用这些数据基于决策树分类算法训练模型预测小汽车等级。

| 汽车价格 | 维修费用 | 车门数量 | 载客数 | 后备箱 | 安全性 | 汽车级别 |
| -------- | -------- | -------- | ------ | ------ | ------ | -------- |
|          |          |          |        |        |        |          |

案例：基于决策树分类算法训练模型预测小汽车等级。

1. 读取文本数据，对每列进行标签编码，基于随机森林分类器进行模型训练，进行交叉验证。

```python
import numpy as np
import sklearn.preprocessing as sp
import sklearn.ensemble as se
import sklearn.model_selection as ms

data = np.loadtxt('../data/car.txt', delimiter=',', dtype='U10')
data = data.T
encoders = []
train_x, train_y = [],[]
for row in range(len(data)):
    encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        train_x.append(encoder.fit_transform(data[row]))
    else:
        train_y = encoder.fit_transform(data[row])
    encoders.append(encoder)
train_x = np.array(train_x).T
# 随机森林分类器
model = se.RandomForestClassifier(max_depth=6, n_estimators=200, random_state=7)
print(ms.cross_val_score(model, train_x, train_y, cv=4, scoring='f1_weighted').mean())
model.fit(train_x, train_y)
```

1. 自定义测试集，使用已训练的模型对测试集进行测试，输出结果。

```python
data = [
    ['high', 'med', '5more', '4', 'big', 'low', 'unacc'],
    ['high', 'high', '4', '4', 'med', 'med', 'acc'],
    ['low', 'low', '2', '4', 'small', 'high', 'good'],
    ['low', 'med', '3', '4', 'med', 'high', 'vgood']]

data = np.array(data).T
test_x, test_y = [],[]
for row in range(len(data)):
    encoder = encoders[row]
    if row < len(data) - 1:
        test_x.append(encoder.transform(data[row]))
    else:
        test_y = encoder.transform(data[row])
test_x = np.array(test_x).T
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / pred_test_y.size)
print(encoders[-1].inverse_transform(test_y))
print(encoders[-1].inverse_transform(pred_test_y))
```

### 验证曲线

验证曲线：模型性能 = f(超参数)

验证曲线所需API：

```python
train_scores, test_scores = ms.validation_curve(
    model,		# 模型 
    输入集, 输出集, 
    'n_estimators', 		#超参数名
    np.arange(50, 550, 50),	#超参数序列
    cv=5		#折叠数
)
```

train_scores的结构:

| 超参数取值 | 第一次折叠 | 第二次折叠 | 第三次折叠 | 第四次折叠 | 第五次折叠 |
| ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
| 50         | 0.91823444 | 0.91968162 | 0.92619392 | 0.91244573 | 0.91040462 |
| 100        | 0.91968162 | 0.91823444 | 0.91244573 | 0.92619392 | 0.91244573 |
| ...        | ...        | ...        | ...        | ...        | ...        |

test_scores的结构与train_scores的结构相同。

案例：在小汽车评级案例中使用验证曲线选择较优参数。

```python
# 获得关于n_estimators的验证曲线
model = se.RandomForestClassifier(max_depth=6, random_state=7)
n_estimators = np.arange(50, 550, 50)
train_scores, test_scores = ms.validation_curve(model, train_x, train_y, 'n_estimators', n_estimators, cv=5)
print(train_scores, test_scores)
train_means1 = train_scores.mean(axis=1)
for param, score in zip(n_estimators, train_means1):
    print(param, '->', score)

mp.figure('n_estimators', facecolor='lightgray')
mp.title('n_estimators', fontsize=20)
mp.xlabel('n_estimators', fontsize=14)
mp.ylabel('F1 Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(n_estimators, train_means1, 'o-', c='dodgerblue', label='Training')
mp.legend()
mp.show()
```

```python
# 获得关于max_depth的验证曲线
model = se.RandomForestClassifier(n_estimators=200, random_state=7)
max_depth = np.arange(1, 11)
train_scores, test_scores = ms.validation_curve(
    model, train_x, train_y, 'max_depth', max_depth, cv=5)
train_means2 = train_scores.mean(axis=1)
for param, score in zip(max_depth, train_means2):
    print(param, '->', score)

mp.figure('max_depth', facecolor='lightgray')
mp.title('max_depth', fontsize=20)
mp.xlabel('max_depth', fontsize=14)
mp.ylabel('F1 Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(max_depth, train_means2, 'o-', c='dodgerblue', label='Training')
mp.legend()
mp.show()
```

### 学习曲线

学习曲线：模型性能 = f(训练集大小)

学习曲线所需API：

```python
_, train_scores, test_scores = ms.learning_curve(
    model,		# 模型 
    输入集, 输出集, 
    [0.9, 0.8, 0.7],	# 训练集大小序列
    cv=5		# 折叠数
)
```

train_scores的结构:

案例：在小汽车评级案例中使用学习曲线选择训练集大小最优参数。

```python
# 获得学习曲线
model = se.RandomForestClassifier( max_depth=9, n_estimators=200, random_state=7)
train_sizes = np.linspace(0.1, 1, 10)
_, train_scores, test_scores = ms.learning_curve(
    model, x, y, train_sizes=train_sizes, cv=5)
test_means = test_scores.mean(axis=1)
for size, score in zip(train_sizes, train_means):
    print(size, '->', score)
mp.figure('Learning Curve', facecolor='lightgray')
mp.title('Learning Curve', fontsize=20)
mp.xlabel('train_size', fontsize=14)
mp.ylabel('F1 Score', fontsize=14)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(train_sizes, test_means, 'o-', c='dodgerblue', label='Training')
mp.legend()
mp.show()
```

案例：预测工人工资收入。

读取adult.txt，针对不同形式的特征选择不同类型的编码器，训练模型，预测工人工资收入。

1. 自定义标签编码器，若为数字字符串，则使用该编码器，保留特征数字值的意义。

```python
class DigitEncoder():

    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)
```

1. 读取文件，整理样本数据，对样本矩阵中的每一列进行标签编码。

```python
num_less, num_more, max_each = 0, 0, 7500
data = []

txt = np.loadtxt('../data/adult.txt', dtype='U20', delimiter=', ')
for row in txt:
    if(' ?' in row):
        continue
    elif(str(row[-1]) == '<=50K'):
        num_less += 1
        data.append(row)
    elif(str(row[-1]) == '>50K'):
        num_more += 1
        data.append(row)
   
data = np.array(data).T
encoders, x = [], []
for row in range(len(data)):
    if str(data[row, 0]).isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
```

1. 划分训练集与测试集，基于朴素贝叶斯分类算法构建学习模型，输出交叉验证分数，验证测试集。

```python
x = np.array(x).T
train_x, test_x, train_y, test_y = ms.train_test_split(
    x, y, test_size=0.25, random_state=5)
model = nb.GaussianNB()
print(ms.cross_val_score(
    model, x, y, cv=10, scoring='f1_weighted').mean())
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / pred_test_y.size)
```

1. 模拟样本数据，预测收入级别。

```python
data = [['39', 'State-gov', '77516', 'Bachelors',
         '13', 'Never-married', 'Adm-clerical', 'Not-in-family',
         'White', 'Male', '2174', '0', '40', 'United-States']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(encoders[-1].inverse_transform(pred_y))
```

### 支持向量机(SVM)

#### 支持向量机原理

1. **寻求最优分类边界**

   正确：对大部分样本可以正确地划分类别。

   泛化：最大化支持向量间距。

   公平：与支持向量等距。

   简单：线性，直线或平面，分割超平面。

2. **基于核函数的升维变换**

   通过名为核函数的特征变换，增加新的特征，使得低维度空间中的线性不可分问题变为高维度空间中的线性可分问题。 

   **线性核函数**：linear，不通过核函数进行维度提升，仅在原始维度空间中寻求线性分类边界。

   基于线性核函数的SVM分类相关API：

   ```python
   model = svm.SVC(kernel='linear')
   model.fit(train_x, train_y)
   ```

   案例：对simple2.txt中的数据进行分类。

   ```python
   import numpy as np
   import sklearn.model_selection as ms
   import sklearn.svm as svm
   import sklearn.metrics as sm
   import matplotlib.pyplot as mp
   x, y = [], []
   data = np.loadtxt('../data/multiple2.txt', delimiter=',', dtype='f8')
   x = data[:, :-1]
   y = data[:, -1]
   train_x, test_x, train_y, test_y = \
       ms.train_test_split(x, y, test_size=0.25, random_state=5)
   # 基于线性核函数的支持向量机分类器
   model = svm.SVC(kernel='linear')
   model.fit(train_x, train_y)
   n = 500
   l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
   b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
   grid_x = np.meshgrid(np.linspace(l, r, n),
                        np.linspace(b, t, n))
   flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))    
   flat_y = model.predict(flat_x)
   grid_y = flat_y.reshape(grid_x[0].shape)
   pred_test_y = model.predict(test_x)
   cr = sm.classification_report(test_y, pred_test_y)
   print(cr)
   mp.figure('SVM Linear Classification', facecolor='lightgray')
   mp.title('SVM Linear Classification', fontsize=20)
   mp.xlabel('x', fontsize=14)
   mp.ylabel('y', fontsize=14)
   mp.tick_params(labelsize=10)
   mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
   mp.scatter(test_x[:, 0], test_x[:, 1], c=test_y, cmap='brg', s=80)
   mp.show()
   ```

   **多项式核函数**：poly，通过多项式函数增加原始样本特征的高次方幂
   $$
   y = x_1+x_2 \\
   y = x_1^2 + 2x_1x_2 + x_2^2 \\
   y = x_1^3 + 3x_1^2x_2 + 3x_1x_2^2 + x_2^3
   $$
   案例，基于多项式核函数训练sample2.txt中的样本数据。

   ```python
   # 基于线性核函数的支持向量机分类器
   model = svm.SVC(kernel='poly', degree=3)
   model.fit(train_x, train_y)
   ```

   **径向基核函数**：rbf，通过高斯分布函数增加原始样本特征的分布概率

   案例，基于径向基核函数训练sample2.txt中的样本数据。

   ```python
   # 基于径向基核函数的支持向量机分类器
   # C：正则强度
   # gamma：正态分布曲线的标准差
   model = svm.SVC(kernel='rbf', C=600, gamma=0.01)
   model.fit(train_x, train_y)
   ```

#### 样本类别均衡化

通过类别权重的均衡化，使所占比例较小的样本权重较高，而所占比例较大的样本权重较低，以此平均化不同类别样本对分类模型的贡献，提高模型性能。

样本类别均衡化相关API：

```python
model = svm.SVC(kernel='linear', class_weight='balanced')
model.fit(train_x, train_y)
```

案例：修改线性核函数的支持向量机案例，基于样本类别均衡化读取imbalance.txt训练模型。

```python
... ...
... ...
data = np.loadtxt('../data/imbalance.txt', delimiter=',', dtype='f8')
x = data[:, :-1]
y = data[:, -1]
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=5)
# 基于线性核函数的支持向量机分类器
model = svm.SVC(kernel='linear', class_weight='balanced')
model.fit(train_x, train_y)
... ...
... ...
```

#### 置信概率

根据样本与分类边界的距离远近，对其预测类别的可信程度进行量化，离边界越近的样本，置信概率越低，反之，离边界越远的样本，置信概率高。

获取每个样本的置信概率相关API：

```python
# 在获取模型时，给出超参数probability=True
model = svm.SVC(kernel='rbf', C=600, gamma=0.01, probability=True)
预测结果 = model.predict(输入样本矩阵)
# 调用model.predict_proba(样本矩阵)可以获取每个样本的置信概率矩阵
置信概率矩阵 = model.predict_proba(输入样本矩阵)
```

置信概率矩阵格式如下：

|       | 类别1 | 类别2 |
| ----- | ----- | ----- |
| 样本1 | 0.8   | 0.2   |
| 样本2 | 0.9   | 0.1   |
| 样本3 | 0.5   | 0.5   |

案例：修改基于径向基核函数的SVM案例，新增测试样本，输出每个测试样本的执行概率，并给出标注。

```python
# 整理测试样本
prob_x = np.array([
    [2, 1.5],
    [8, 9],
    [4.8, 5.2],
    [4, 4],
    [2.5, 7],
    [7.6, 2],
    [5.4, 5.9]])
pred_prob_y = model.predict(prob_x)
probs = model.predict_proba(prob_x)
print(probs)

# 绘制每个测试样本，并给出标注
mp.scatter(prob_x[:,0], prob_x[:,1], c=pred_prob_y, cmap='jet_r', s=80, marker='D')
for i in range(len(probs)):
    mp.annotate(
        '{}% {}%'.format(
            round(probs[i, 0] * 100, 2),
            round(probs[i, 1] * 100, 2)),
        xy=(prob_x[i, 0], prob_x[i, 1]),
        xytext=(12, -12),
        textcoords='offset points',
        horizontalalignment='left',
        verticalalignment='top',
        fontsize=9,
        bbox={'boxstyle': 'round,pad=0.6',
              'fc': 'orange', 'alpha': 0.8})
```

#### 网格搜索

获取一个最优超参数的方式可以绘制验证曲线，但是验证曲线只能每次获取一个最优超参数。如果多个超参数有很多排列组合的话，就可以使用网格搜索寻求最优超参数组合。

针对超参数组合列表中的每一个超参数组合，实例化给定的模型，做cv次交叉验证，将其中平均f1得分最高的超参数组合作为最佳选择，实例化模型对象。

网格搜索相关API：

```python
import sklearn.model_selection as ms
model = ms.GridSearchCV(模型, 超参数组合列表, cv=折叠数)
model.fit(输入集，输出集)
# 获取网格搜索每个参数组合
model.cv_results_['params']
# 获取网格搜索每个参数组合所对应的平均测试分值
model.cv_results_['mean_test_score']
# 获取最好的参数
model.best_params_
model.best_score_
model.best_estimator_
```

案例：修改置信概率案例，基于网格搜索得到最优超参数。

```python
# 基于径向基核函数的支持向量机分类器
params = [{'kernel':['linear'], 'C':[1, 10, 100, 1000]},
    {'kernel':['poly'], 'C':[1], 'degree':[2, 3]}, 
    {'kernel':['rbf'], 'C':[1,10,100,1000], 'gamma':[1, 0.1, 0.01, 0.001]}]
model = ms.GridSearchCV(svm.SVC(probability=True), params, cv=5)
model.fit(train_x, train_y)
for p, s in zip(model.cv_results_['params'],
        model.cv_results_['mean_test_score']):
    print(p, s)
# 获取得分最优的的超参数信息
print(model.best_params_)
# 获取最优得分
print(model.best_score_)
# 获取最优模型的信息
print(model.best_estimator_)
```

### 案例：事件预测

加载event.txt，预测某个时间段是否会出现特殊事件。

案例：

```python
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm

class DigitEncoder():
    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)

# 多元分类
data = np.loadtxt('../data/event.txt', delimiter=',', dtype='U10')
data = np.delete(data.T, 1, axis=0)
print(data)
encoders, x = [], []
for row in range(len(data)):
    if data[row][0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=5)
model = svm.SVC(kernel='rbf', class_weight='balanced')
print(ms.cross_val_score( model, train_x, train_y, cv=3, scoring='accuracy').mean())
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print((pred_test_y == test_y).sum() / pred_test_y.size)
data = [['Tuesday', '13:30:00', '21', '23']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x) 
print(encoders[-1].inverse_transform(pred_y))
```

### 案例：交通流量预测(回归)

加载traffic.txt，预测在某个时间段某个交通路口的车流量。

```python
import numpy as np
import sklearn.preprocessing as sp
import sklearn.model_selection as ms
import sklearn.svm as svm
import sklearn.metrics as sm

 class DigitEncoder():
    def fit_transform(self, y):
        return y.astype(int)

    def transform(self, y):
        return y.astype(int)

    def inverse_transform(self, y):
        return y.astype(str)

data = []
# 回归
data = np.loadtxt('../data/traffic.txt', delimiter=',', dtype='U10')
data = data.T
encoders, x = [], []
for row in range(len(data)):
    if data[row][0].isdigit():
        encoder = DigitEncoder()
    else:
        encoder = sp.LabelEncoder()
    if row < len(data) - 1:
        x.append(encoder.fit_transform(data[row]))
    else:
        y = encoder.fit_transform(data[row])
    encoders.append(encoder)
x = np.array(x).T
train_x, test_x, train_y, test_y = \
    ms.train_test_split(x, y, test_size=0.25, random_state=5)
# 支持向量机回归器
model = svm.SVR(kernel='rbf', C=10, epsilon=0.2)
model.fit(train_x, train_y)
pred_test_y = model.predict(test_x)
print(sm.r2_score(test_y, pred_test_y))
data = [['Tuesday', '13:35', 'San Franci', 'yes']]
data = np.array(data).T
x = []
for row in range(len(data)):
    encoder = encoders[row]
    x.append(encoder.transform(data[row]))
x = np.array(x).T
pred_y = model.predict(x)
print(int(pred_y))
```

### 聚类

分类（class）与聚类（cluster）不同，分类是有监督学习模型，聚类属于无监督学习模型。聚类讲究使用一些算法把样本划分为n个群落。一般情况下，这种算法都需要计算欧氏距离。

欧氏距离即欧几里得距离。
$$
P(x_1) - Q(x_2): |x_1-x_2| = \sqrt{(x_1-x_2)^2} \\
P(x_1,y_1) - Q(x_2,y_2): \sqrt{x_1-x_2)^2+(y_1-y_2)^2} \\
P(x_1,y_1,z_1) - Q(x_2,y_2,z_2): \sqrt{(x_1-x_2)^2+(y_1-y_2)^2+(z_1-z_2)^2} \\
$$
用两个样本对应特征值之差的平方和之平方根，即欧氏距离，来表示这两个样本的相似性。

#### K均值算法

第一步：随机选择k个样本作为k个聚类的中心，计算每个样本到各个聚类中心的欧氏距离，将该样本分配到与之距离最近的聚类中心所在的类别中。

第二步：根据第一步所得到的聚类划分，分别计算每个聚类的几何中心，将几何中心作为新的聚类中心，重复第一步，直到计算所得几何中心与聚类中心重合或接近重合为止。

**注意：**

1. 聚类数k必须事先已知。借助某些评估指标，优选最好的聚类数。
2. 聚类中心的初始选择会影响到最终聚类划分的结果。初始中心尽量选择距离较远的样本。

K均值算法相关API：

```python
import sklearn.cluster as sc
# n_clusters: 聚类数
model = sc.KMeans(n_clusters=4)
# 不断调整聚类中心，知道最终聚类中心稳定则聚类完成
model.fit(x)
# 获取训练结果的聚类中心
centers = model.cluster_centers_
```

案例：加载multiple3.txt，基于K均值算法完成样本的聚类。

```python
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
x = np.loadtxt('../data/multiple3.txt', delimiter=',')
# K均值聚类器
model = sc.KMeans(n_clusters=4)
model.fit(x)
centers = model.cluster_centers_
n = 500
l, r = x[:, 0].min() - 1, x[:, 0].max() + 1
b, t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x = np.meshgrid(np.linspace(l, r, n),
                     np.linspace(b, t, n))
flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))    
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_y = model.predict(x)
mp.figure('K-Means Cluster', facecolor='lightgray')
mp.title('K-Means Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=80)
mp.scatter(centers[:, 0], centers[:, 1], marker='+', c='gold', s=1000, linewidth=1)
mp.show()
```

#### 图像量化

KMeans聚类算法可以应用于图像量化领域。通过KMeans算法可以把一张图像所包含的颜色值进行聚类划分，求每一类别的平均值后再重新生成新的图像。可以达到图像降维的目的。这个过程称为图像量化。图像量化可以更好的保留图像的轮廓，降低机器识别图像轮廓的难度。

案例：

```python
import numpy as np
import scipy.misc as sm
import scipy.ndimage as sn
import sklearn.cluster as sc
import matplotlib.pyplot as mp


# 通过K均值聚类量化图像中的颜色
def quant(image, n_clusters):
    x = image.reshape(-1, 1)
    model = sc.KMeans(n_clusters=n_clusters)
    model.fit(x)
    y = model.labels_
    centers = model.cluster_centers_.ravel()
    return centers[y].reshape(image.shape)


original = sm.imread('../data/lily.jpg', True)
quant4 = quant(original, 4)
quant3 = quant(original, 3)
quant2 = quant(original, 2)
mp.figure('Image Quant', facecolor='lightgray')
mp.subplot(221)
mp.title('Original', fontsize=16)
mp.axis('off')
mp.imshow(original, cmap='gray')
mp.subplot(222)
mp.title('Quant-4', fontsize=16)
mp.axis('off')
mp.imshow(quant4, cmap='gray')
mp.subplot(223)
mp.title('Quant-3', fontsize=16)
mp.axis('off')
mp.imshow(quant3, cmap='gray')
mp.subplot(224)
mp.title('Quant-2', fontsize=16)
mp.axis('off')
mp.imshow(quant2, cmap='gray')
mp.tight_layout()
mp.show()
```

#### 均值漂移算法

首先假定样本空间中的每个聚类均服从某种已知的概率分布规则，然后用不同的概率密度函数拟合样本中的统计直方图，不断移动密度函数的中心(均值)的位置，直到获得最佳拟合效果为止。这些概率密度函数的峰值点就是聚类的中心，再根据每个样本距离各个中心的距离，选择最近聚类中心所属的类别作为该样本的类别。

均值漂移算法的特点：

1. 聚类数不必事先已知，算法会自动识别出统计直方图的中心数量。
2. 聚类中心不依据于最初假定，聚类划分的结果相对稳定。
3. 样本空间应该服从某种概率分布规则，否则算法的准确性会大打折扣。

均值漂移算法相关API：

```python
# 量化带宽，决定每次调整概率密度函数的步进量
# n_samples：样本数量
# quantile：量化宽度（直方图一条的宽度）
bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.1)
# 均值漂移聚类器
model = sc.MeanShift(bandwidth=bw, bin_seeding=True)
model.fit(x)
```

案例：加载multiple3.txt，使用均值漂移算法对样本完成聚类划分。

```python
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp

x = np.loadtxt('../data/multiple3.txt', delimiter=',')
# 量化带宽，决定每次调整概率密度函数的步进量
bw = sc.estimate_bandwidth(x, n_samples=len(x), quantile=0.2)
# 均值漂移聚类器
model = sc.MeanShift(bandwidth=bw, bin_seeding=True)
model.fit(x)
centers = model.cluster_centers_
n = 500
l,  r = x[:, 0].min() - 1, x[:, 0].max() + 1
b,  t = x[:, 1].min() - 1, x[:, 1].max() + 1
grid_x = np.meshgrid(np.linspace(l, r, n),
                     np.linspace(b, t, n))
flat_x = np.column_stack((grid_x[0].ravel(), grid_x[1].ravel()))
flat_y = model.predict(flat_x)
grid_y = flat_y.reshape(grid_x[0].shape)
pred_y = model.predict(x)
mp.figure('Mean Shift Cluster', facecolor='lightgray')
mp.title('Mean Shift Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.pcolormesh(grid_x[0], grid_x[1], grid_y, cmap='gray')
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=80)
mp.scatter(centers[:, 0], centers[:, 1], marker='+', c='gold', s=1000, linewidth=1)
mp.show()
```

#### 凝聚层次算法

首先假定每个样本都是一个独立的聚类，如果统计出来的聚类数大于期望的聚类数，则从每个样本出发寻找离自己最近的另一个样本，与之聚集，形成更大的聚类，同时令总聚类数减少，不断重复以上过程，直到统计出来的聚类数达到期望值为止。

凝聚层次算法的特点：

1. 聚类数k必须事先已知。借助某些评估指标，优选最好的聚类数。
2. 没有聚类中心的概念，因此只能在训练集中划分聚类，但不能对训练集以外的未知样本确定其聚类归属。
3. 在确定被凝聚的样本时，除了以距离作为条件以外，还可以根据连续性来确定被聚集的样本。

凝聚层次算法相关API：

```python
# 凝聚层次聚类器
model = sc.AgglomerativeClustering(n_clusters=4)
pred_y = model.fit_predict(x)
```

案例：重新加载multiple3.txt，使用凝聚层次算法进行聚类划分。 

```python
import numpy as np
import sklearn.cluster as sc
import matplotlib.pyplot as mp
x = np.loadtxt('../data/multiple3.txt', delimiter=',')
# 凝聚层次聚类器
model = sc.AgglomerativeClustering(n_clusters=4)
pred_y = model.fit_predict(x)
mp.figure('Agglomerative Cluster', facecolor='lightgray')
mp.title('Agglomerative Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y, cmap='brg', s=80)
mp.show()
```

在确定被凝聚的样本时，除了以距离作为条件以外，还可以根据连续性来确定被聚集的样本。

```python
import numpy as np
import sklearn.cluster as sc
import sklearn.neighbors as nb
import matplotlib.pyplot as mp
n_samples = 500
x = np.linspace(-1, 1, n_samples)
y = np.sin(x * 2 * np.pi)
n = 0.3 * np.random.rand(n_samples, 2)
x = np.column_stack((x, y)) + n
# 无连续性的凝聚层次聚类器
model_nonc = sc.AgglomerativeClustering( linkage='average', n_clusters=3)
pred_y_nonc = model_nonc.fit_predict(x)
# 近邻筛选器
conn = nb.kneighbors_graph( x, 10, include_self=False)
# 有连续性的凝聚层次聚类器
model_conn = sc.AgglomerativeClustering(
    linkage='average', n_clusters=3, connectivity=conn)
pred_y_conn = model_conn.fit_predict(x)
mp.figure('Nonconnectivity', facecolor='lightgray')
mp.title('Nonconnectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y_nonc, cmap='brg', alpha=0.5, s=30)
mp.figure('Connectivity', facecolor='lightgray')
mp.title('Connectivity', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
mp.scatter(x[:, 0], x[:, 1], c=pred_y_conn, cmap='brg', alpha=0.5, s=30)
mp.show()

```

### 聚类

#### 轮廓系数

好的聚类：内密外疏，同一个聚类内部的样本要足够密集，不同聚类之间样本要足够疏远。

轮廓系数计算规则：针对样本空间中的一个特定样本，计算它与所在聚类其它样本的平均距离a，以及该样本与距离最近的另一个聚类中所有样本的平均距离b，该样本的轮廓系数为(b-a)/max(a, b)，将整个样本空间中所有样本的轮廓系数取算数平均值，作为聚类划分的性能指标s。

轮廓系数的区间为：[-1, 1]。 -1代表分类效果差，1代表分类效果好。0代表聚类重叠，没有很好的划分聚类。

轮廓系数相关API：

```python
import sklearn.metrics as sm
# v：平均轮廓系数
# metric：距离算法：使用欧几里得距离(euclidean)
v = sm.silhouette_score(输入集, 输出集, sample_size=样本数, metric=距离算法)
```

案例：输出KMeans算法聚类划分后的轮廓系数。

```python
# 打印平均轮廓系数
print(sm.silhouette_score( x, pred_y, sample_size=len(x), metric='euclidean'))
```

#### DBSCAN算法

从样本空间中任意选择一个样本，以事先给定的半径做圆，凡被该圆圈中的样本都视为与该样本处于相同的聚类，以这些被圈中的样本为圆心继续做圆，重复以上过程，不断扩大被圈中样本的规模，直到再也没有新的样本加入为止，至此即得到一个聚类。于剩余样本中，重复以上过程，直到耗尽样本空间中的所有样本为止。

DBSCAN算法的特点：

1. 事先给定的半径会影响最后的聚类效果，可以借助轮廓系数选择较优的方案。

2. 根据聚类的形成过程，把样本细分为以下三类：

   外周样本：被其它样本聚集到某个聚类中，但无法再引入新样本的样本。

   孤立样本：聚类中的样本数低于所设定的下限，则不称其为聚类，反之称其为孤立样本。

   核心样本：除了外周样本和孤立样本以外的样本。

DBSCAN聚类算法相关API：

```python
# DBSCAN聚类器
# eps：半径
# min_samples：聚类样本数的下限，若低于该数值，则称为孤立样本
model = sc.DBSCAN(eps=epsilon, min_samples=5)
model.fit(x)
```

案例：修改凝聚层次聚类案例，基于DBSCAN聚类算法进行聚类划分，选择最优半径。

```python
import numpy as np
import sklearn.cluster as sc
import sklearn.metrics as sm
import matplotlib.pyplot as mp

x = np.loadtxt('../data/perf.txt', delimiter=',')
epsilons, scores, models = np.linspace(0.3, 1.2, 10), [], []
for epsilon in epsilons:
    # DBSCAN聚类器
    model = sc.DBSCAN(eps=epsilon, min_samples=5)
    model.fit(x)
    score = sm.silhouette_score(
        x, model.labels_, sample_size=len(x), metric='euclidean')
    scores.append(score)
    models.append(model)
scores = np.array(scores)
best_index = scores.argmax()
best_epsilon = epsilons[best_index]
print(best_epsilon)
best_score = scores[best_index]
print(best_score)
best_model = models[best_index]
```

案例：获取核心样本、外周样本、孤立样本。并且使用不同的点型绘图。

```python
best_model = models[best_index]
pred_y = best_model.fit_predict(x)
core_mask = np.zeros(len(x), dtype=bool)
core_mask[best_model.core_sample_indices_] = True
offset_mask = best_model.labels_ == -1
periphery_mask = ~(core_mask | offset_mask)
mp.figure('DBSCAN Cluster', facecolor='lightgray')
mp.title('DBSCAN Cluster', fontsize=20)
mp.xlabel('x', fontsize=14)
mp.ylabel('y', fontsize=14)
mp.tick_params(labelsize=10)
labels = best_model.labels_
mp.scatter(x[core_mask][:, 0], x[core_mask][:, 1], c=labels[core_mask], 
           cmap='brg', s=80, label='Core')
mp.scatter(x[periphery_mask][:, 0], x[periphery_mask][:, 1], alpha=0.5,
           c=labels[periphery_mask], cmap='brg', marker='s', s=80, label='Periphery')
mp.scatter(x[offset_mask][:, 0], x[offset_mask][:, 1],
           c=labels[offset_mask], cmap='brg', marker='x', s=80, label='Offset')
mp.legend()
mp.show()
```

### 推荐引擎

推荐引擎意在把最需要的推荐给用户。

在不同的机器学习场景中通常需要分析相似样本。而统计相似样本的方式可以基于欧氏距离分数，也可基于皮氏距离分数。

**欧氏距离分数**
$$
欧氏距离分数 = \frac{1}{1+欧氏距离}
$$
计算所得欧氏距离分数区间处于：[0, 1]，越趋于0样本间的欧氏距离越远，样本越不相似；越趋于1，样本间的欧氏距离越近，越相似。

构建样本之间的欧氏距离得分矩阵：
$$
\left[
 \begin{array}{c}
  	  & a & b & c & d & .. \\
  	a & 1 & 0.2 & 0.3 & 0.4 & .. \\
  	b & 0.2 & 1 & x & x & .. \\
  	c & 0.3 & x & 1 & x & .. \\
  	d & 0.4 & x & x & 1 & .. \\
  	.. & .. & .. & .. & .. & .. \\

  \end{array}
  \right]
$$
案例：解析ratings.json，根据每个用户对已观看电影的打分计算样本间的欧氏距离，输出欧氏距离得分矩阵。

```python
import json
import numpy as np

with open('../data/ratings.json', 'r') as f:
    ratings = json.loads(f.read())
users, scmat = list(ratings.keys()), []
for user1 in users:
    scrow = []
    for user2 in users:
        movies = set()
        for movie in ratings[user1]:
            if movie in ratings[user2]:
                movies.add(movie)
        if len(movies) == 0:
            score = 0
        else:
            x, y = [], []
            for movie in movies:
                x.append(ratings[user1][movie])
                y.append(ratings[user2][movie])
            x = np.array(x)
            y = np.array(y)
            score = 1 / (1 + np.sqrt(((x - y) ** 2).sum()))
        scrow.append(score)
    scmat.append(scrow)
users = np.array(users)
scmat = np.array(scmat)
for scrow in scmat:
    print('  '.join('{:.2f}'.format(score) for score in scrow)) 
```

**皮尔逊相关系数**

```
A = [1,2,3,1,2] 
B = [3,4,5,3,4] 
m = np.corrcoef(A, B)
```

皮尔逊相关系数 = 协方差 / 标准差之积

相关系数处于[-1, 1]区间。越靠近-1代表两组样本反相关，越靠近1代表两组样本正相关。

案例：使用皮尔逊相关系数计算两用户对一组电影评分的相关性。

```python
score = np.corrcoef(x, y)[0, 1]
```

**按照相似度从高到低排列每个用户的相似用户**

```python
# scmat矩阵中每一行为 每一个用户对所有用户的皮尔逊相关系数
for i, user in enumerate(users):
    # 拿到所有相似用户与相似用户所对应的皮尔逊相关系数
    sorted_indices = scmat[i].argsort()[::-1]
    sorted_indices = sorted_indices[sorted_indices != i]
    similar_users = users[sorted_indices]
    similar_scores = scmat[i, sorted_indices]
    print(user, similar_users, similar_scores, sep='\n')
```

**生成推荐清单**

1. 找到所有皮尔逊系数正相关的用户
2. 遍历当前用户的每个相似用户，拿到相似用户看过但是当前用户没有看过的电影作为推荐电影
3. 多个相似用户有可能推荐同一部电影，则取每个相似用户对该电影的评分得均值作为推荐度。
4. 可以把相似用户的皮尔逊系数作为权重，皮尔逊系数越大，推荐度越高。

```python
    # 找到所有皮尔逊系数正相关的用户
    positive_mask = similar_scores > 0
    similar_users = similar_users[positive_mask]
    # 相似用户对应的皮尔逊相关系数
    similar_scores = similar_scores[positive_mask]
    #存储对于当前用户所推荐的电影以及电影的推荐度(推荐电影的平均分)
    recomm_movies = {}
    #遍历当前用户的每个相似用户
    for i, similar_user in enumerate(similar_users):
        #拿到相似用户看过但是当前用户没有看过的电影
        for movie, score in ratings[similar_user].items():
            if (movie not in ratings[user].keys()):
                if movie not in recomm_movies:
                    recomm_movies[movie] = []
                else:
                    recomm_movies[movie].append(score)
                    
    print(user)
    movie_list = sorted(recomm_movies.items(), key=lambda x:np.average(x[1]), reverse=True)
    print(movie_list)
```



### 自然语言处理（NLP）

Siri的工作流程：1. 听  2.懂  3.思考  4.组织语言   5.回答

1. 语音识别
2. 自然语言处理 - 语义分析
3. 逻辑分析 - 结合业务场景与上下文
4. 自然语言处理 - 分析结果生成自然语言文本
5. 语音合成

自然语言处理的常用处理过程：

先针对训练文本进行分词处理（词干提取、原型提取），统计词频，通过词频-逆文档频率算法获得该词对样本语义的贡献，根据每个词的贡献力度，构建有监督分类学习模型。把测试样本交给模型处理，得到测试样本的语义类别。

自然语言工具包 - NLTK

#### 文本分词

分词处理相关API：

```python
import nltk.tokenize as tk
# 把样本按句子进行拆分  sent_list:句子列表
sent_list = tk.sent_tokenize(text)
# 把样本按单词进行拆分  word_list:单词列表
word_list = tk.word_tokenize(text)
#  把样本按单词进行拆分 punctTokenizer：分词器对象
punctTokenizer = tk.WordPunctTokenizer() 
word_list = punctTokenizer.tokenize(text)
```

案例：

```python
import nltk.tokenize as tk
doc = "Are you curious about tokenization? " \
      "Let's see how it works! " \
      "We need to analyze a couple of sentences " \
      "with punctuations to see it in action."
print(doc)	
tokens = tk.sent_tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
print('-' * 15)
tokens = tk.word_tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
print('-' * 15)
tokenizer = tk.WordPunctTokenizer()
tokens = tokenizer.tokenize(doc)
for i, token in enumerate(tokens):
    print("%2d" % (i + 1), token)
```

#### 词干提取

文本样本中的单词的词性与时态对于语义分析并无太大影响，所以需要对单词进行词干提取。

词干提取相关API：

```python
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

stemmer = pt.PorterStemmer() # 波特词干提取器，偏宽松
stemmer = lc.LancasterStemmer() # 朗卡斯特词干提取器，偏严格
stemmer = sb.SnowballStemmer('english') # 思诺博词干提取器，偏中庸
r = stemmer.stem('playing') # 提取单词playing的词干
```

案例：

```python
import nltk.stem.porter as pt
import nltk.stem.lancaster as lc
import nltk.stem.snowball as sb

words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']
pt_stemmer = pt.PorterStemmer()
lc_stemmer = lc.LancasterStemmer()
sb_stemmer = sb.SnowballStemmer('english')
for word in words:
    pt_stem = pt_stemmer.stem(word)
    lc_stem = lc_stemmer.stem(word)
    sb_stem = sb_stemmer.stem(word)
    print('%8s %8s %8s %8s' % (
        word, pt_stem, lc_stem, sb_stem))
```

#### 词性还原

与词干提取的作用类似，词性还原更利于人工二次处理。因为有些词干并非正确的单词，人工阅读更麻烦。词性还原可以把名词复数形式恢复为单数形式，动词分词形式恢复为原型形式。

词性还原相关API：

```python
import nltk.stem as ns
# 获取词性还原器对象
lemmatizer = ns.WordNetLemmatizer()
# 把单词word按照名词进行还原
n_lemma = lemmatizer.lemmatize(word, pos='n')
# 把单词word按照动词进行还原
v_lemma = lemmatizer.lemmatize(word, pos='v')
```

案例：

```python
import nltk.stem as ns
words = ['table', 'probably', 'wolves', 'playing',
         'is', 'dog', 'the', 'beaches', 'grounded',
         'dreamt', 'envision']
lemmatizer = ns.WordNetLemmatizer()
for word in words:
    n_lemma = lemmatizer.lemmatize(word, pos='n')
    v_lemma = lemmatizer.lemmatize(word, pos='v')
    print('%8s %8s %8s' % (word, n_lemma, v_lemma))
```

#### 词袋模型

一句话的语义很大程度取决于某个单词出现的次数，所以可以把句子中所有可能出现的单词作为特征名，每一个句子为一个样本，单词在句子中出现的次数为特征值构建数学模型，称为词袋模型。

The brown dog is running. The black dog is in the black room. Running in the room is forbidden.

1 The brown dog is running
2 The black dog is in the black room
3 Running in the room is forbidden

| the  | brown | dog  | is   | running | black | in   | room | forbidden |
| ---- | ----- | ---- | ---- | ------- | ----- | ---- | ---- | --------- |
| 1    | 1     | 1    | 1    | 1       | 0     | 0    | 0    | 0         |
| 2    | 0     | 1    | 1    | 0       | 2     | 1    | 1    | 0         |
| 1    | 0     | 0    | 1    | 1       | 0     | 1    | 1    | 1         |

词袋模型化相关API：

```python
import sklearn.feature_extraction.text as ft

# 构建词袋模型对象
cv = ft.CountVectorizer()
# 训练模型，把句子中所有可能出现的单词作为特征名，每一个句子为一个样本，单词在句子中出现的次数为特征值。
bow = cv.fit_transform(sentences).toarray()
print(bow)
# 获取所有特征名
words = cv.get_feature_names()
```

案例：

```python
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
print(sentences)
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)

```

#### 词频（TF）

单词在句子中出现的次数除以句子的总词数称为词频。即一个单词在一个句子中出现的频率。词频相比单词的出现次数可以更加客观的评估单词对一句话的语义的贡献度。词频越高，对语义的贡献度越大。对词袋矩阵归一化即可得到词频。

案例：对词袋矩阵进行归一化

```python
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft
import sklearn.preprocessing as sp
doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
print(sentences)
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)
tf = sp.normalize(bow, norm='l1')
print(tf)
```

#### 文档频率（DF）

含有某个单词的文档样本数/总文档样本数

#### 逆文档频率（IDF）

总样本数/含有某个单词的样本数

#### 词频-逆文档频率(TF-IDF)

词频矩阵中的每一个元素乘以相应单词的逆文档频率，其值越大说明该词对样本语义的贡献越大，根据每个词的贡献力度，构建学习模型。

获取词频逆文档频率（TF-IDF）矩阵相关API：

```python
# 获取词袋模型
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()
# 获取TF-IDF模型训练器
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
```

案例：获取TF_IDF矩阵：

```python
import nltk.tokenize as tk
import sklearn.feature_extraction.text as ft

doc = 'The brown dog is running. ' \
      'The black dog is in the black room. ' \
      'Running in the room is forbidden.'
print(doc)
sentences = tk.sent_tokenize(doc)
print(sentences)
cv = ft.CountVectorizer()
bow = cv.fit_transform(sentences).toarray()
print(bow)
words = cv.get_feature_names()
print(words)
tt = ft.TfidfTransformer()
tfidf = tt.fit_transform(bow).toarray()
print(tfidf)
```

#### 文本分类(主题识别)

使用给定的文本数据集进行主题识别训练，自定义测试集测试模型准确性。

案例：

```python
import sklearn.datasets as sd
import sklearn.feature_extraction.text as ft
import sklearn.naive_bayes as nb

train = sd.load_files('../data/20news', encoding='latin1',
    shuffle=True, random_state=7)
# 20news 下的文件夹名即是相应子文件的主题类别名
# train.data 返回每个文件的字符串内容
# train.target 返回每个文件的父目录名（主题类别名）
train_data = train.data
train_y = train.target
categories = train.target_names
cv = ft.CountVectorizer()
train_bow = cv.fit_transform(train_data)
tt = ft.TfidfTransformer()
train_x = tt.fit_transform(train_bow)
model = nb.MultinomialNB()
model.fit(train_x, train_y)
test_data = [
    'The curveballs of right handed pitchers tend to curve to the left',
    'Caesar cipher is an ancient form of encryption',
    'This two-wheeler is really good on slippery roads']
test_bow = cv.transform(test_data)
test_x = tt.transform(test_bow)
pred_test_y = model.predict(test_x)
for sentence, index in zip(test_data, pred_test_y):
    print(sentence, '->', categories[index])

```

#### 性别识别

使用nltk提供的分类器对语料库中英文男名与女名文本进行性别划分训练，最终进行性别验证。

nltk提供的语料库及分类方法相关API：

```python
import nltk.corpus as nc
import nltk.classify as cf

# 读取语料库中names文件夹里的male.txt文件，并且进行分词
male_names = nc.names.words('male.txt')

'''
train_data的格式不再是样本矩阵，nltk要求的数据格式如下：
[ ({'age': 15, 'score1': 95, 'score2': 95}, 'good'),
  ({'age': 15, 'score1': 45, 'score2': 55}, 'bad') ]
'''
# 基于朴素贝叶斯分类器训练测试数据 
model = cf.NaiveBayesClassifier.train(train_data)
# 使用测试数据计算分类器精确度得分（测试数据格式与训练数据一致）
ac = cf.accuracy(model, test_data)
# 对具体的某个样本进行类别划分
feature = {'age': 15, 'score1': 95, 'score2': 95}
gender = model.classify(feature)
```

案例：

```python
import random
import numpy as np
import nltk.corpus as nc
import nltk.classify as cf
male_names = nc.names.words('male.txt')
female_names = nc.names.words('female.txt')

data = []
for male_name in male_names:
    feature = {'feature': male_name[-2:].lower()}
    data.append((feature, 'male'))
for female_name in female_names:
    feature = {'feature': female_name[-2:].lower()}
    data.append((feature, 'female'))
random.seed(7)
random.shuffle(data)
train_data = data[:int(len(data) / 2)]
test_data = data[int(len(data) / 2):]
model = cf.NaiveBayesClassifier.train(train_data)
ac = cf.accuracy(model, test_data)

names, genders = ['Leonardo', 'Amy', 'Sam', 'Tom', 'Katherine', 'Taylor', 'Susanne'], []
for name in names:
    feature = {'feature': name[-2:].lower()}
    gender = model.classify(feature)
    genders.append(gender)
for name, gender in zip(names, genders):
    print(name, '->', gender)

```

### 自然语言处理（NLP）

#### nltk分类器

nltk提供了朴素贝叶斯分类器方便的处理自然语言相关的分类问题，并且可以自动处理词袋，完成IFIDF矩阵的整理，完成模型训练，最终实现类别预测。使用方法如下：

```python
import nltk.classify as cf
import nltk.classify.util as cu
'''
train_data的格式不再是样本矩阵，nltk要求的数据格式如下：
[ ({'age': 15, 'score1': 95, 'score2': 95}, 'good'),
  ({'age': 15, 'score1': 45, 'score2': 55}, 'bad') ]
'''
# 基于朴素贝叶斯分类器训练测试数据 
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)
```

#### 情感分析

分析语料库中movie_reviews文档，通过正面及负面评价进行自然语言训练，实现情感分析。

```python
import nltk.corpus as nc
import nltk.classify as cf
import nltk.classify.util as cu
pdata = []

# pos文件夹中的每个文件的路径
fileids = nc.movie_reviews.fileids('pos')
# 整理所有正面评论单词，存入pdata列表
for fileid in fileids:
    sample = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        sample[word] = True
    pdata.append((sample, 'POSITIVE'))
# 整理所有正面评论单词，存入ndata列表
ndata = []
fileids = nc.movie_reviews.fileids('neg')
for fileid in fileids:
    sample = {}
    words = nc.movie_reviews.words(fileid)
    for word in words:
        sample[word] = True
    ndata.append((sample, 'NEGATIVE'))

# 拆分测试集与训练集数量（80%作为训练集）
pnumb, nnumb = int(0.8 * len(pdata)), int(0.8 * len(ndata))
train_data = pdata[:pnumb] + ndata[:nnumb]
test_data = pdata[pnumb:] + ndata[nnumb:]
# 基于朴素贝叶斯分类器训练测试数据 
model = cf.NaiveBayesClassifier.train(train_data)
ac = cu.accuracy(model, test_data)
print(ac)

# 模拟业务场景
reviews = [
    'It is an amazing movie.',
    'This is a dull movie. I would never recommend it to anyone.',
    'The cinematography is pretty great in this movie.',
    'The direction was terrible and the story was all over the place.']
sents, probs = [], []
for review in reviews:
    sample = {}
    words = review.split()
    for word in words:
        sample[word] = True
    pcls = model.classify(sample)
    print(review, '->', pcls)
```

#### 主题抽取

经过分词、单词清洗、词干提取后，基于TF-IDF算法可以抽取一段文本中的核心主题词汇，从而判断出当前文本的主题。属于无监督学习。gensim模块提供了主题抽取的常用工具 。

主题抽取相关API：

```python
import gensim.models.ldamodel as gm
import gensim.corpora as gc

# 把lines_tokens中出现的单词都存入gc提供的词典对象，对每一个单词做编码。
line_tokens = ['hello', 'world', ...]
dic = gc.Dictionary(line_tokens)
# 通过字典构建词袋
bow = dic.doc2bow(line_tokens) 

# 构建LDA模型
# bow: 词袋
# num_topics: 分类数
# id2word: 词典
# passes: 每个主题保留的最大主题词个数
model = gm.LdaModel(bow, num_topics=n_topics, id2word=dic, passes=25)
# 输出每个类别中对类别贡献最大的4个主题词
topics = model.print_topics(num_topics=n_topics, num_words=4)
```

案例：

```python
import nltk.tokenize as tk
import nltk.corpus as nc
import nltk.stem.snowball as sb
import gensim.models.ldamodel as gm
import gensim.corpora as gc
doc = []
with open('../data/topic.txt', 'r') as f:
    for line in f.readlines():
        doc.append(line[:-1])
tokenizer = tk.WordPunctTokenizer() 
stopwords = nc.stopwords.words('english')
signs = [',', '.', '!']
stemmer = sb.SnowballStemmer('english')
lines_tokens = []
for line in doc:
    tokens = tokenizer.tokenize(line.lower())
    line_tokens = []
    for token in tokens:
        if token not in stopwords and token not in signs:
            token = stemmer.stem(token)
            line_tokens.append(token)
    lines_tokens.append(line_tokens)
# 把lines_tokens中出现的单词都存入gc提供的词典对象，对每一个单词做编码。
dic = gc.Dictionary(lines_tokens)
# 遍历每一行，构建词袋列表
bow = []
for line_tokens in lines_tokens:
    row = dic.doc2bow(line_tokens)
    bow.append(row)
n_topics = 2
# 通过词袋、分类数、词典、每个主题保留的最大主题词个数构建LDA模型
model = gm.LdaModel(bow, num_topics=n_topics, id2word=dic, passes=25)
# 输出每个类别中对类别贡献最大的4个主题词
topics = model.print_topics(num_topics=n_topics, num_words=4)
print(topics)
```

### 语音识别

声音的本质是震动，震动的本质是位移关于时间的函数，波形文件(.wav)中记录了不同采样时刻的位移。

通过傅里叶变换，可以将时间域的声音函数分解为一系列不同频率的正弦函数的叠加，通过频率谱线的特殊分布，建立音频内容和文本的对应关系，以此作为模型训练的基础。

案例：

```python
import numpy as np
import numpy.fft as nf
import scipy.io.wavfile as wf
import matplotlib.pyplot as mp

sample_rate, sigs = wf.read('../data/freq.wav')
print(sample_rate)
print(sigs.shape, sigs.dtype)
sigs = sigs / 2 ** 15
times = np.arange(len(sigs)) / sample_rate
freqs = nf.fftfreq(sigs.size, 1 / sample_rate)
ffts = nf.fft(sigs)
pows = np.abs(ffts)
mp.figure('Audio', facecolor='lightgray')
mp.subplot(121)
mp.title('Time Domain', fontsize=16)
mp.xlabel('Time', fontsize=12)
mp.ylabel('Signal', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(times, sigs, c='dodgerblue', label='Signal')
mp.legend()
mp.subplot(122)
mp.title('Frequency Domain', fontsize=16)
mp.xlabel('Frequency', fontsize=12)
mp.ylabel('Power', fontsize=12)
mp.tick_params(labelsize=10)
mp.grid(linestyle=':')
mp.plot(freqs[freqs >= 0], pows[freqs >= 0], c='orangered', label='Power')
mp.legend()
mp.tight_layout()
mp.show()
```

#### 语音识别

梅尔频率倒谱系数(MFCC)通过与声音内容密切相关的13个特殊频率所对应的能量分布，可以使用梅尔频率倒谱系数矩阵作为语音识别的特征。基于隐形马尔科夫模型进行模式识别，找到测试样本最匹配的声音模型，从而识别语音内容。

梅尔频率倒谱系数相关API：

```python
import scipy.io.wavfile as wf
import python_speech_features as sf

sample_rate, sigs = wf.read('../data/freq.wav')
mfcc = sf.mfcc(sigs, sample_rate)
```

案例：

```python -m pip install python_speech_features```

```python

```

隐马尔科夫模型相关API：

```python
import hmmlearn.hmm as hl
# n_components: 用几个高斯分布函数拟合样本数据
# covariance_type: 相关矩阵的辅对角线进行相关性比较
# n_iter: 最大迭代上限
model = hl.GaussianHMM(n_components=4, covariance_type='diag', n_iter=1000)
model.fit(mfccs)
# 使用模型匹配测试mfcc矩阵的分值
score = model.score(test_mfccs)
```

案例：

```python

```

#### 声音合成

根据需求获取某个声音的模型频域数据，根据业务需要可以修改模型数据，逆向生成时域数据，完成声音的合成。

案例：

```python
import json
import numpy as np
import scipy.io.wavfile as wf
with open('../data/12.json', 'r') as f:
    freqs = json.loads(f.read())
tones = [
    ('G5', 1.5),
    ('A5', 0.5),
    ('G5', 1.5),
    ('E5', 0.5),
    ('D5', 0.5),
    ('E5', 0.25),
    ('D5', 0.25),
    ('C5', 0.5),
    ('A4', 0.5),
    ('C5', 0.75)]
sample_rate = 44100
music = np.empty(shape=1)
for tone, duration in tones:
    times = np.linspace(0, duration, duration * sample_rate)
    sound = np.sin(2 * np.pi * freqs[tone] * times)
    music = np.append(music, sound)
music *= 2 ** 15
music = music.astype(np.int16)
wf.write('../data/music.wav', sample_rate, music)
```

### 图像识别

#### OpenCV基础

OpenCV是一个开源的计算机视觉库。提供了很多图像处理常用的工具。

案例：

```python
import numpy as np
import cv2 as cv
# 读取图片并显示
original = cv.imread('../data/forest.jpg')
cv.imshow('Original', original)
# 显示图片某个颜色通道的图像
blue = np.zeros_like(original)
blue[:, :, 0] = original[:, :, 0]  # 0 - 蓝色通道
cv.imshow('Blue', blue)
green = np.zeros_like(original)
green[:, :, 1] = original[:, :, 1]  # 1 - 绿色通道
cv.imshow('Green', green)
red = np.zeros_like(original)
red[:, :, 2] = original[:, :, 2]  # 2 - 红色通道
cv.imshow('Red', red)
# 图像裁剪
h, w = original.shape[:2]
l, t = int(w / 4), int(h / 4)
r, b = int(w * 3 / 4), int(h * 3 / 4)
cropped = original[t:b, l:r]
cv.imshow('Cropped', cropped)
#图像缩放 interpolation=线型插值
scaled1 = cv.resize(original, (int(w / 4), int(h / 4)),
    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled1', scaled1)
scaled2 = cv.resize(
    scaled1, None, fx=4, fy=4,
    interpolation=cv.INTER_LINEAR)
cv.imshow('Scaled2', scaled2)
cv.waitKey()
# 图像文件保存
cv.imwrite('../../data/blue.jpg', blue)
cv.imwrite('../../data/green.jpg', green)
cv.imwrite('../../data/red.jpg', red)
cv.imwrite('../../data/cropped.jpg', cropped)
cv.imwrite('../../data/scaled1.jpg', scaled1)
cv.imwrite('../../data/scaled2.jpg', scaled2)
```

#### 边缘检测

物体的边缘检测是物体识别常用的手段。边缘检测常用亮度梯度方法。通过识别亮度梯度变化最大的像素点从而检测出物体的边缘。

常用边缘检测算法相关API：

```python
# 索贝尔边缘识别
# cv.CV_64F：卷积运算使用数据类型为64位浮点型（保证微分的精度）
# 1：水平方向索贝尔偏微分
# 0：垂直方向索贝尔偏微分
# ksize：卷积核为5*5的方阵
cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
# 拉普拉斯边缘识别
cv.Laplacian(original, cv.CV_64F)
# Canny边缘识别
# 50:水平方向阈值  240:垂直方向阈值
cv.Canny(original, 50, 240)
```

案例：

```python
import cv2 as cv

original = cv.imread( '../data/chair.jpg', cv.IMREAD_GRAYSCALE)
cv.imshow('Original', original)
hsobel = cv.Sobel(original, cv.CV_64F, 1, 0, ksize=5)
cv.imshow('H-Sobel', hsobel)
vsobel = cv.Sobel(original, cv.CV_64F, 0, 1, ksize=5)
cv.imshow('V-Sobel', vsobel)
sobel = cv.Sobel(original, cv.CV_64F, 1, 1, ksize=5)
cv.imshow('Sobel', sobel)
laplacian = cv.Laplacian(original, cv.CV_64F)
cv.imshow('Laplacian', laplacian)
canny = cv.Canny(original, 50, 240)
cv.imshow('Canny', canny)
cv.waitKey()

```

#### 亮度提升

OpenCV提供了直方图均衡化的方式实现亮度提升，更有利于边缘识别与物体识别模型的训练。

OpenCV直方图均衡化相关API：

```python
# 彩色图转为灰度图
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
# 直方图均衡化
equalized_gray = cv.equalizeHist(gray)
```

案例：

```python
import cv2 as cv

original = cv.imread('../../data/sunrise.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
equalized_gray = cv.equalizeHist(gray)
cv.imshow('Equalized Gray', equalized_gray)
# YUV：亮度，色度，饱和度
yuv = cv.cvtColor(original, cv.COLOR_BGR2YUV)
yuv[..., 0] = cv.equalizeHist(yuv[..., 0])
equalized_color = cv.cvtColor(yuv, cv.COLOR_YUV2BGR)
cv.imshow('Equalized Color', equalized_color)
cv.waitKey()
```

#### 角点检测

平直棱线的交汇点（颜色梯度方向改变的像素点的位置）

OpenCV提供的角点检测相关API：

```python
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
# Harris角点检测器
# 边缘水平方向、垂直方向颜色值改变超过阈值7、5时即为边缘
# 边缘线方向改变超过阈值0.04弧度即为一个角点。
corners = cv.cornerHarris(gray, 7, 5, 0.04)
```

案例：

```python
import cv2 as cv

original = cv.imread('../data/box.png')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
corners = cv.cornerHarris(gray, 7, 5, 0.04)
mixture = original.copy()
mixture[corners > corners.max() * 0.01] = [0, 0, 255]
cv.imshow('Corner', mixture)
cv.waitKey()
```

### 图像识别

#### 特征点检测

常用特征点检测有：STAR特征点检测 / SIFT特征点检测

特征点检测结合了边缘检测与角点检测从而识别出图形的特征点。

STAR特征点检测相关API如下：

```python
import cv2 as cv
# 创建STAR特征点检测器
star = cv.xfeatures2d.StarDetector_create()
# 检测出gray图像所有的特征点
keypoints = star.detect(gray)
# drawKeypoints方法可以把所有的特征点绘制在mixture图像中
cv.drawKeypoints(original, keypoints, mixture,
    			 flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
```

案例：

```python
import cv2 as cv
original = cv.imread('../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
star = cv.xfeatures2d.StarDetector_create()
keypoints = star.detect(gray)
mixture = original.copy()
cv.drawKeypoints(
    original, keypoints, mixture,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
```

SIFT特征点检测相关API：

```python
import cv2 as cv

# 创建SIFT特征点检测器
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
```

案例：

```python
import cv2 as cv

original = cv.imread('../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
mixture = original.copy()
cv.drawKeypoints(original, keypoints, mixture,
    flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)
cv.imshow('Mixture', mixture)
cv.waitKey()
```

#### 特征值矩阵

图像特征值矩阵（描述）记录了图像的特征点以及每个特征点的梯度信息，相似图像的特征值矩阵也相似。这样只要有足够多的样本，就可以基于隐马尔科夫模型进行图像内容的识别。

特征值矩阵相关API：

```python
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
_, desc = sift.compute(gray, keypoints)
```

案例：

```python
import cv2 as cv

import matplotlib.pyplot as mp
original = cv.imread('../data/table.jpg')
cv.imshow('Original', original)
gray = cv.cvtColor(original, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)
sift = cv.xfeatures2d.SIFT_create()
keypoints = sift.detect(gray)
_, desc = sift.compute(gray, keypoints)
print(desc.shape)
mp.matshow(desc, cmap='jet', fignum='Description')
mp.title('Description', fontsize=20)
mp.xlabel('Feature', fontsize=14)
mp.ylabel('Sample', fontsize=14)
mp.tick_params(which='both', top=False, labeltop=False, labelbottom=True, labelsize=10)
mp.show()
```

#### 物体识别

```python
import os
import numpy as np
import cv2 as cv
import hmmlearn.hmm as hl

def search_files(directory):
    directory = os.path.normpath(directory)

    objects = {}
    for curdir, subdirs, files in os.walk(directory):
        for file in files:
            if(file.endswith('.jpg')):
                label = curdir.split(os.path.sep)[-1]
                if label not in objects:
                    objects[label] = []
                path = os.path.join(curdir, file)
                objects[label].append(path)
    return objects
	
#加载训练集样本数据，训练模型，模型存储
train_objects = search_files('../data/objects/training')
train_x, train_y = [], []
for label, filenames in train_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        #范围缩放，使特征描述矩阵样本数量一致
        h, w = gray.shape[:2]
        f = 200 / min(h, w)
        gray = cv.resize(gray, None, fx=f, fy=f)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    train_x.append(descs)
    train_y.append(label)
models = {}
for descs, label in zip(train_x, train_y):
    model = hl.GaussianHMM(n_components=4, covariance_type='diag', n_iter=100)
    models[label] = model.fit(descs)


#测试模型
test_objects = search_files('../data/objects/testing')
test_x, test_y = [], []
for label, filenames in test_objects.items():
    descs = np.array([])
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        sift = cv.xfeatures2d.SIFT_create()
        keypoints = sift.detect(gray)
        _, desc = sift.compute(gray, keypoints)
        if len(descs) == 0:
            descs = desc
        else:
            descs = np.append(descs, desc, axis=0)
    test_x.append(descs)
    test_y.append(label)

# 遍历所有测试样本  使用model匹配测试样本查看每个模型的匹配分数
for descs, test_label in zip(test_x, test_y):
    for pred_label, model in models.items():
        score = model.score(descs)
        print(test_label, '->', pred_label, score)
```

### 人脸识别

人脸识别与图像识别的区别在于人脸识别需要识别出两个人的不同点。 

#### 视频捕捉

通过OpenCV访问视频捕捉设备（视频头），从而获取图像帧。

视频捕捉相关API：

```python
import cv2 as cv

# 获取视频捕捉设备
video_capture = cv.VideoCapture(0)
# 读取一帧
frame = video_capture.read()[1]
cv.imshow('VideoCapture', frame)
# 释放视频捕捉设备
video_capture.release()
# 销毁cv的所有窗口
cv.destroyAllWindows()
```

案例：

```python
import cv2 as cv
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()
cv.destroyAllWindows()
```

#### 人脸定位

哈尔级联人脸定位

```python
import cv2 as cv
# 通过特征描述文件构建哈尔级联人脸识别器
fd = cv.CascadeClassifier('../data/haar/face.xml')
# 从一个图像中识别出所有的人脸区域
# 	1.3：为最小的人脸尺寸
# 	5：最多找5张脸
# 返回：
# 	faces: 抓取人脸（矩形区域）列表 [(l,t,w,h),(),()..]
faces = fd.detectMultiScale(frame, 1.3, 5)
face = faces[0] # 第一张脸
# 绘制椭圆
cv.ellipse(
    face, 				# 图像
    (l + a, t + b), 	# 椭圆心
    (a, b), 			# 半径
    0, 					# 椭圆旋转角度
    0, 360, 			# 起始角, 终止角
    (255, 0, 255), 		# 颜色
    2					# 线宽
)
```

案例：

```python
import cv2 as cv
# 哈尔级联人脸定位器
fd = cv.CascadeClassifier('../../data/haar/face.xml')
ed = cv.CascadeClassifier('../../data/haar/eye.xml')
nd = cv.CascadeClassifier('../../data/haar/nose.xml')
vc = cv.VideoCapture(0)
while True:
    frame = vc.read()[1]
    faces = fd.detectMultiScale(frame, 1.3, 5)
    for l, t, w, h in faces:
        a, b = int(w / 2), int(h / 2)
        cv.ellipse(frame, (l + a, t + b), (a, b), 0, 0, 360, (255, 0, 255), 2)
        face = frame[t:t + h, l:l + w]
        eyes = ed.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in eyes:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 0), 2)
        noses = nd.detectMultiScale(face, 1.3, 5)
        for l, t, w, h in noses:
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(face, (l + a, t + b), (a, b), 0, 0, 360, (0, 255, 255), 2)
    cv.imshow('VideoCapture', frame)
    if cv.waitKey(33) == 27:
        break
vc.release()
cv.destroyAllWindows()
```

#### 人脸识别

简单人脸识别：OpenCV的LBPH(局部二值模式直方图)

```python
# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import os
import numpy as np
import cv2 as cv
import sklearn.preprocessing as sp
fd = cv.CascadeClassifier('../../data/haar/face.xml')


def search_faces(directory):
    directory = os.path.normpath(directory)

    faces = {}
    for curdir, subdirs, files in os.walk(directory):
        for jpeg in (file for file in files
                     if file.endswith('.jpg')):
            path = os.path.join(curdir, jpeg)
            label = path.split(os.path.sep)[-2]
            if label not in faces:
                faces[label] = []
            faces[label].append(path)
    return faces


train_faces = search_faces(
    '../../data/faces/training')
codec = sp.LabelEncoder()
codec.fit(list(train_faces.keys()))
train_x, train_y = [], []
for label, filenames in train_faces.items():
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(gray, 1.1, 2,
                                    minSize=(100, 100))
        for l, t, w, h in faces:
            train_x.append(
                gray[t:t + h, l:l + w])
            train_y.append(
                codec.transform([label])[0])
train_y = np.array(train_y)
# 局部二值模式直方图人脸识别分类器
model = cv.face.LBPHFaceRecognizer_create()
model.train(train_x, train_y)
test_faces = search_faces(
    '../../data/faces/testing')
test_x, test_y, test_z = [], [], []
for label, filenames in test_faces.items():
    for filename in filenames:
        image = cv.imread(filename)
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = fd.detectMultiScale(gray, 1.1, 2,
                                    minSize=(100, 100))
        for l, t, w, h in faces:
            test_x.append(
                gray[t:t + h, l:l + w])
            test_y.append(
                codec.transform([label])[0])
            a, b = int(w / 2), int(h / 2)
            cv.ellipse(image, (l + a, t + b),
                       (a, b), 0, 0, 360,
                       (255, 0, 255), 2)
            test_z.append(image)
test_y = np.array(test_y)
pred_test_y = []
for face in test_x:
    pred_code = model.predict(face)[0]
    pred_test_y.append(pred_code)
escape = False
while not escape:
    for code, pred_code, image in zip(
            test_y, pred_test_y, test_z):
        label, pred_label = \
            codec.inverse_transform([code, pred_code])
        text = '{} {} {}'.format(
            label,
            '==' if code == pred_code else '!=',
            pred_label)
        cv.putText(image, text, (10, 60),
                   cv.FONT_HERSHEY_SIMPLEX, 2,
                   (255, 255, 255), 6)
        cv.imshow('Recognizing...', image)
        if cv.waitKey(1000) == 27:
            escape = True
            break
```



# 数据分析DAY01

## 机器学习与数学

语音识别领域：如何判断一个音频的内容是“橘子”还是“橙子”？

图像识别领域：如何判断一张图像是“橘子”还是“橙子”？

机器学习的流程：

1. 使用一组数据描述一件事物。	
2. 把这组数据数学模型化。     【线性代数】
3. 根据某些机器学习算法计算这组数据更加接近某一类事物。 【信息论，高等数学】
4. 根据最终的统计结果，得到结论。  【概率论】

## 线型代数

### 标量与向量

**标量**：一个标量就是一个单独的数或者字符，一般用小写的变量名称表示。

**向量**：一个向量就是一组数，这些数是有序排列的。可以按照索引的序列确定每个单独的数。在几何空间中可以代表一个“点”，也可表示为空间坐标系原点到这个点的有向线段。


$$
c = 
\left[
\begin{array}{c}
红色\\
橙色\\
黄色\\
\end{array}
\right]
\quad\quad\quad
w = 
\left[
\begin{array}{c}
7.5\\
6.8\\
5.2\\
\end{array}
\right]
\quad\quad\quad
h = 
\left[
\begin{array}{c}
7.1\\
7.4\\
10.3\\
\end{array}
\right]
$$

### 矩阵

把上述多个列向量沿水平方向合并在一起，就形成了m行n列的“数据表”。称为m行n列的“矩阵”。矩阵属于二维数据结构。
$$
h = 
\left[
\begin{array}{c}
红色 & 7.5 & 7.1\\
橙色 & 6.8 & 7.4\\
黄色 & 5.2 & 10.3\\
\end{array}
\right]
$$
**标签编码**

字符串不能直接参与运算，所以可以把字符串按照一定的编码规则转为相对应的数字。从而构建纯数字的矩阵。

#### 矩阵的运算

考虑以下问题：

1. 如何使样本每个值统一增大或减小？【矩阵的标量的加法与减法】
2. 如何判断行向量 **[橙色, 6.8, 7.4]** 与矩阵中存储的哪个样本最接近？【矩阵的减法】
3. 如何使每个样本的特征值统一统一乘以相应系数？

**矩阵的加法**
$$
10 + 
\left[
\begin{array}{c}
1 & 2\\
4 & 5\\
7 & 8\\
\end{array}
\right]
= 
\left[
\begin{array}{c}
11 & 12\\
14 & 15\\
17 & 18\\
\end{array}
\right]

\quad\quad\quad

\left[
\begin{array}{c}
1 & 2\\
3 & 4\\
5 & 6\\
\end{array}
\right]
+ 
\left[
\begin{array}{c}
1 & 2\\
3 & 4\\
5 & 6\\
\end{array}
\right]
= 
\left[
\begin{array}{c}
2 & 4\\
6 & 8\\
10 & 12\\
\end{array}
\right]
$$
**矩阵的减法**
$$
10 - 
\left[
\begin{array}{c}
1 & 2\\
3 & 4\\
5 & 6\\
\end{array}
\right]
= 
\left[
\begin{array}{c}
9 & 8\\
7 & 6\\
5 & 4\\
\end{array}
\right]

\quad\quad\quad\quad

\left[
\begin{array}{c}
1 & 2\\
3 & 4\\
5 & 6\\
\end{array}
\right]
-
\left[
\begin{array}{c}
1 & 1\\
\end{array}
\right]
= 
\left[
\begin{array}{c}
0 & 1\\
2 & 3\\
4 & 5\\
\end{array}
\right]
$$
**矩阵的乘法**
$$
10 \times 
\left[
\begin{array}{c}
1 & 2\\
4 & 5\\
7 & 8\\
\end{array}
\right]
= 
\left[
\begin{array}{c}
10 & 20\\
40 & 50\\
70 & 80\\
\end{array}
\right]

\quad\quad\quad
$$
**两个矩阵相乘**
$$
\left[
\begin{array}{c}
1 & 2 & 3\\
4 & 5 & 6\\
\end{array}
\right]
\times 
\left[
\begin{array}{c}
1 & 2\\
3 & 4\\
5 & 6\\
\end{array}
\right]
= 
\left[
\begin{array}{c}
22 & 28\\
49 & 64\\
\end{array}
\right]
$$

### 特殊矩阵

**方阵：** 行数与列数相等的矩阵为方阵。
$$
\left[
\begin{array}{c}
1 & 2\\
3 & 4\\
\end{array}
\right]
\quad\quad\quad
\left[
\begin{array}{c}
1 & 2 & 2\\
3 & 4 & 4\\
3 & 4 & 4\\
\end{array}
\right]
$$
**零矩阵：** 矩阵中每个元素都为0。
$$
\left[
\begin{array}{c}
0 & 0 & 0\\
0 & 0 & 0\\
0 & 0 & 0\\
\end{array}
\right]
$$
**对角矩阵：**    主对角线之外的元素都是0的矩阵。
$$
\left[
\begin{array}{c}
1 & 0 & 0\\
0 & 2 & 0\\
0 & 0 & 3\\
\end{array}
\right]
$$

**单位矩阵：** 主对角线元素都是1的对角矩阵。
$$
\left[
\begin{array}{c}
1 & 0 & 0\\
0 & 1 & 0\\
0 & 0 & 1\\
\end{array}
\right]
$$

### 距离算法

1. 曼哈顿距离
   $$
   𝑑_{12}=|𝑥_1−𝑥_2 |+|𝑦_1−𝑦_2|
   $$

2. 欧式距离
   $$
   𝑑_{12}=\sqrt{(𝑥_1−𝑥_2)^2+(𝑦_1−𝑦_2)^2}
   $$

3. 闵可夫斯基距离（欧式距离的推广）
   $$
   𝑑_{12}=
   \sqrt[p]{
   \sum_{k=1}^n (x_{1k} - x_{2k})^p
   }
   $$

4. 夹角余弦相似度

$$
𝑐𝑜𝑠\theta=\frac{\vec{a} × \vec{b}}{|\vec{a}||\vec{b}|}=\frac{𝑥_1 𝑥_2+𝑦_1 𝑦_2}{\sqrt{𝑥_1^2+𝑦_1^2}\sqrt{𝑥_2^2+𝑦_2^2 } }
$$



#### 距离算法对比

**欧氏距离能够体现个体数值特征的绝对差异**

1. 更多的用于需要从维度的数值大小中体现差异的分析

2. 如使用用户行为指标分析用户价值的相似度或差异

**余弦距离更多的是从方向上区分差异，而对绝对的数值不敏感**

1. 更多的用于使用用户对内容评分来区分兴趣的相似度和差异

2. 修正了用户间可能存在的度量标准不统一的问题



## 概率论与数理统计

### 概率论

尝试解决以下问题：

1. 已知近几年10月1日的天气情况，如何预测今年10月1日的天气？
2. 如何判断一个邮件是垃圾邮件？

概率论与数理统计是研究**随机现象**的规律性的数学科学。

**随机现象**则是指在基本条件不变的情况下，每一次试验或观察前，不能肯定会出现哪种结果，呈现出偶然性。随机现象的实现和对它的观察称为随机试验。随机试验的每一可能结果称为一个基本事件，一个或一组基本事件统称随机事件，或简称事件。典型的随机试验有掷骰子、扔硬币等。事件的概率是衡量该事件发生的可能性的量度。虽然在一次随机试验中某个事件的发生是带有偶然性的，但那些可在相同条件下大量重复的随机试验却往往呈现出明显的数量规律。

案例：

| 课程难度（diff） | 学生智力（intel） | 学生评级（grade） |
| ---------------- | ----------------- | ----------------- |
| 简单             | 不聪明            | 中                |
| 一般             | 聪明              | 优                |
| 难               | 不聪明            | 中                |
| 非常难           | 不聪明            | 差                |
| 简单             | 不聪明            | 优                |
| 一般             | 不聪明            | 中                |
| 难               | 聪明              | 优                |
| 非常难           | 聪明              | 优                |
| 简单             | 聪明              | 优                |

总样本数=9，则：
$$
P(diff=简单) = \frac{3}{9} \quad \quad 
P(intel=聪明) = \frac{4}{9} \quad \quad 
P(grade=优) = \frac{5}{9} \quad \quad
$$

#### 联合概率

在上述样本环境下，不聪明的优等生出现的概率：
$$
P(grade=优, intel=不聪明) = \frac{5}{9} \times \frac{5}{9} = \frac{25}{81}
$$


#### 条件概率

在上述样本环境下，学生智力不聪明的条件下，能得优的概率：
$$
P(grade=优 | intel=不聪明) = \frac{1}{5}
$$
条件概率就是事件B在另外一个事件A已经发生条件下的发生概率。条件概率表示为P(B│A)，读作“在A条件下B的概率”。

#### 贝叶斯定理

$$
P(A, B) = P(A) P(B|A) = P(B) P(A|B)	\\
\Downarrow \\
P(A|B)=P(B|A)P(A)/P(B)
$$

例如：

假设一个学校里有60%男生和4 0%女生.女生穿裤子的人数和穿裙子的人数相等,所有男生穿裤子.一个人在远处随机看到了一个穿裤子的学生.那么这个学生是女生的概率是多少?

```
P(女) = 0.4
P(裤子|女) = 0.5
P(裤子) = 0.6 + 0.2 = 0.8
P(女|裤子) = P(裤子|女) * P(女) / P(裤子) = 0.5 * 0.4 / 0.8 = 0.25
```

### 数理统计

 数理统计是数学的一个分支，它以概率论为基础，研究大量随机现象的统计规律性的一门科学。

设有一组学生成绩数据：

```
极差-1  差-2  及格-3  良好-4  优秀-5
[3, 5, 2, 3, 2, 3, 2, 3, 2, 5, 4, 4, 2, 1, 3, 3, 3, 4, 3, 2]
```

看似没有规律，但经过统计发现及格的概率比其他概率高。所以若有一个新的学生成绩，则其大概率为[良好]。

#### 随机变量*

随机变量（random variable）表示随机试验各种结果的实值单值函数。随机事件不论与数量是否直接有关，都可以数量化，即都能用数量化的方式表达。



离散型随机变量：

连续型随机变量：



#### 数理统计的常见指标

设有一组学生成绩数据：

```
极差-1  差-2  及格-3  良好-4  优秀-5
[3, 5, 2, 3, 2, 3, 2, 3, 2, 5, 4, 4, 2, 1, 3, 3, 3, 4, 3, 2]
```

##### 期望

在概率论与数理统计中，数学期望是试验中每次可能结果的概率乘以其结果的总和。
$$
X=X(e)=\left\{
\begin{array}{l}
 1 \quad \quad e=极差  \quad \quad P(e=1)=0.05\\  
 2 \quad \quad e=差   \quad \quad \quad P(e=2)=0.3\\
 3 \quad \quad e=及格  \quad \quad P(e=3)=0.4\\  
 4 \quad \quad e=良好   \quad \quad P(e=4)=0.15\\
 5 \quad \quad e=优秀  \quad \quad P(e=5)=0.1\\  
\end{array} \right.  
\quad \\ 
\quad\\
\quad\\
𝐸(𝑋)=1×0.05 + 2×0.3 + 3×0.4 + 4×0.15 + 5×0.1 = 2.95
$$



假设X是一个离散型随机变量，其可能取值有：{x<sub>1</sub>，x<sub>2</sub>，⋯，x<sub>n</sub>}，各取值对应的概率取值为P(x<sub>k</sub>)，k=1,2,⋯,n，则其数学期望被定义为：
$$
\begin{equation*}
𝐸(𝑋)=\sum_{k=1}^nx_kP(x_k)
\end{equation*}
$$


##### 方差

概率论与数理统计中，是各个样本数据分别与其平均数之差的平方和的平均数。
$$
𝑉𝑎𝑟(X)=𝐸{[X−𝐸(X)]^2 }=𝐸(X^2)−[𝐸(X)]^2
$$




##### 协方差

**对于二维随机变量（X,Y）讲，求其数学期望，可以体现什么？**

反映了X与Y各自的平均值。

**若求其方差，可以体现什么？**

反映了X与Y各自离开平均值的偏离程度。

**如何反映X与Y之间的相互关系？**

在概率论与数理统计中，协方差衡量两个随机变量X和Y之间的总体误差。
$$
𝐶𝑜𝑣(𝑋,𝑌)=𝐸[(𝑋−𝐸[𝑋])(𝑌−𝐸[𝑌])]=𝐸[𝑋𝑌]−𝐸[𝑋]𝐸[𝑌]
$$


#### 随机变量及其分布

随机变量随着试验的结果而取不同的值，在试验之前虽然不能确切知道它取什么值，但随机变量的取值客观上有一定的统计规律性，这种规律性称为随机变量的概率分布。

##### 离散型随机变量及其分布律

1. 0-1分布

   0-1分布是单个二值型离散随机变量的分布，亦称“两点分布”、“伯努利分布”。

   示例：随机扔硬币，0为反， 1为正。 扔10次。

   ```
   [0, 1, 0, 0, 0, 1, 0, 1, 1, 1]
   ```

   概率分布律：
   $$
   𝑃\{𝑋=1\}=𝑝 \quad \quad \quad \quad \quad  𝑃\{𝑋=0\}=1−𝑝
   $$

2. 二项分布

   各次试验之间都相互独立，并且每次试验中只有两种可能的结果。二项分布即重复n次伯努利试验，亦称“n重伯努利试验”。

   示例：随机扔硬币，每轮扔10次，记录每次正面出现的个数。

   ```
   [5, 6, 4, 3, 7, 3, 4, 5, 4, 5]
   ```

   概率分布律：
   $$
   𝑃\{𝑋=𝑘\}=𝐶_𝑛^𝑘 𝑝^𝑘 (1−𝑝)^{𝑛−𝑘}
   $$

3. 几何分布

   在n次伯努利试验中，试验k次才得到第一次成功的几率。	

   示例：随机扔硬币，一直扔，直到第一次出现正面时，记录扔硬币的次数。

   ```
   [2, 3, 1, 2, 1, 1, 4, 1, 2, 1]
   ```

   概率分布律：
   $$
   𝑃\{𝑋=𝑘\}=(1−𝑝)^{𝑘−1}𝑝
   $$





##### 连续型随机变量及其概率密度



**随机变量的分布函数**

对于非离散型随机变量X，由于其可能的取值不能一一列举，所以不能像离散型随机变量那样可以用分布律描述它。因而我们研究随机变量所取的值落在一个区间 ( x<sub>1</sub>, x<sub>2</sub> ] 的概率：

设X是一个随机变量，x是任意实数，则函数：
$$
F(x) = P\{ X \leq x \}, -\infty < x < \infty
$$
称为X的**分布函数**。

对于任意实数x<sub>1</sub>, x<sub>2</sub> ( x<sub>1</sub> < x<sub>2</sub> )，有：
$$
P \{ x_1 \lt X \leq x_2 \} = P\{X \leq x_2 \} - P\{X \leq x_1 \} 
=F(x_2) - F(x_1)
$$
因此，若已知X的分布函数，就可以算出X落在任意区间(x<sub>1</sub>, x<sub>2</sub>]上的概率。所以分布函数可以完整的描述随机变量统计的规律性。



**例：** 一个靶子是半径为2m的圆盘，设击中靶上任一同心圆盘上的点的概率与该圆盘的面积成正比，并设每次射击都能中靶，以X表示弹着点与圆心的距离，试求随机变量X的分布函数。

解：

若x < 0, 则\{X<= x\}是不可能事件，于是：
$$
F(x)=P\{X\leq x\}=0
$$
若 0 <= x <= 2, 由题意, P\{0 <= x <= 2\}=kx^2,k是某常数，当x=2时，P\{0 <= x <= 2\}=1，求得k=1/2，于是：
$$
F(x)=P\{0\leq X\leq 2\}=\frac{x^2}{4}
$$
若x >= 2, 由题意\{X <= x\}是必然事件，于是：
$$
F(x)=P(X\leq x)=1
$$
综上所述，即得X的分布函数为：
$$
F(x)=
\begin{equation}
\begin{cases}
0 & x<0\\
\frac{x^2}{4} & 0\leq x \lt 2\\
1 & x \geq 2\\

\end{cases}
\end{equation}
$$
函数图像如下：

![F(x)](images\F(x).png)

容易看出本例中分布函数F(x)，对于任一的x可以写成形式：
$$
F(x) = \int^x_{-\infty}f(t)dx
$$
其中：
$$
f(t) = 
\begin{equation}
\begin{cases}
\frac{t}{2}, & 0<t<2, \\
0, & 其他
\end{cases}
\end{equation}
$$
这就是说，F(x)恰好是非负函数f(t)在区间(-∞,x] 上的积分。

对于随机变量X的分布函数F(x)， 若存在非负可积函数f(t)，使对于任意实数x有：
$$
F(x) = \int^x_{-\infty}f(t)dx
$$
则称X为**连续型随机变量**， f(x)称为X的**概率密度函数**, 简称**概率密度**。



1. 均匀分布

   在区间(a, b)上服从均匀分布的随机变量X，落在区间(a, b)中任一等长度的子区间内的可能性是相同的。



均匀分布概率密度函数：
$$
f(x) = 
\begin{equation}
\begin{cases}
\frac{1}{b-a}, & a<x<b, \\
0, & 其他
\end{cases}
\end{equation}
$$
对概率密度函数求积分得分布函数：
$$
F(x) = 
\begin{equation}
\begin{cases}
0, & x<a\\
\frac{x-a}{b-a}, & a \leq x <b \\
1, &x\geq b
\end{cases}
\end{equation}
$$


![](images\u.png)



2. 高斯分布（正态分布）

   高斯分布又叫正态分布，其曲线呈钟型，两头低，中间高，左右对称。

   高斯分布数学期望为μ，标准差为σ ，我们将其记为N(μ，σ<sup>2</sup>)， N(0, 1)称为标准正太分布。



   高斯分布概率密度函数：

$$
f(x)=\frac{1}{\sqrt{2\pi}\sigma} e^{-\frac{(x-\mu)^2}{2\sigma^2}}, -∞<x<+∞
$$




   ![高斯分布密度函数](images\高斯分布密度函数.png)



   期望值μ决定了正态分布的位置，其标准差σ决定了正太分布的幅度。























