import numpy as np
from PIL import Image
import scipy.ndimage as sn
import matplotlib.pyplot as mp

# 读取文件
original = Image.open('lily.jpg').convert('L') # 转为灰度图
"""
‘L’（8位像素，黑白）
‘P’（8位像素，使用调色板映射到任何其他模式）
‘RGB’（3x8位像素，真彩色）
‘RGBA’（4x8位像素，带透明蒙版的真彩色）
‘CMYK’（4x8位像素，分色）
‘YCbCr’（3x8位像素，彩色视频格式）
‘I’（32位有符号整数像素）
‘F’（32位浮点像素）
"""
# 高斯模糊
median = sn.median_filter(original, 21)
# 角度旋转
rotate = sn.rotate(original, 45)
# 边缘识别
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
