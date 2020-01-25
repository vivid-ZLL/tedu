"""
初始化动画图像
"""
import numpy as np
import matplotlib.pyplot as mp
import matplotlib.animation as ma

n = 100
balls = np.zeros(100, dtype=[
    ('position', float, 2),  # 位置
    ('size', float,),  # 大小
    ('growth', float,),  # 生长速度
    ('color', float, 4),  # 颜色RGBA
])

# for ball in balls:
#     print(ball)
# 初始化balls数组每个字段的属性值
balls['position'] = np.random.uniform(0, 1, (n, 2))
# for ball in balls:
#     print(ball)
# ...

balls['size'] = np.random.uniform(50, 70, n)
balls['growth'] = np.random.uniform(10, 20, n)
balls['color'] = np.random.uniform(0, 1, (n, 4))

mp.figure('Animation', facecolor='lightgray')  # 画图
mp.title('Animation', fontsize=16)
# 取消坐标轴的刻度
mp.xticks([])
mp.yticks([])

sc = mp.scatter(balls['position'][:, 0], balls['position'][:, 1], s=balls['size'], color=balls['color'])


def update(number):
    # 选择一个点
    index = number % 100
    # 重新修改index位置元素的属性
    balls['position'][index] = np.random.uniform(0, 1, (1, 2))
    balls['size'][index] = np.random.uniform(50, 70)

    balls['size'] += balls['growth']
    # 重新绘制
    sc.set_sizes(balls['size'])


# 制作动画
res = ma.FuncAnimation(mp.gcf(), update, interval=30)

mp.show()
