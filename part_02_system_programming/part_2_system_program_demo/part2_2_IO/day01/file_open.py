"""
file_open.py
文件打开方式训练
"""

#　打开文件
try:
    # fd = open('a.py','r') #　以只读打开
    # fd = open('a.py','w') # 以只写方式打开
    # fd = open('a.py','a') #　追加方式

    """
    普通的文本文件　
    既可以使用文本方式打开也可以使用二进制方式打开
    二进制文件则必须以二进制方式打开
    """
    fd = open('a.py','rb') #　二进制方式
    print(fd)
except Exception as e:
    print(e)

# 读写文件

# 关闭文件
fd.close()
