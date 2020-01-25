"""
    身份运算符
"""

a = 800
b = 1000
# id函数，可以获取变量存储的对象地址。
print(id(a))
print(id(b))
# flase
print(a is b)  # is 的本质就是通过ｉｄ函数进行判断的

c = a
print(id(c))
print(c is a)

d = 1000
print(d is b)
