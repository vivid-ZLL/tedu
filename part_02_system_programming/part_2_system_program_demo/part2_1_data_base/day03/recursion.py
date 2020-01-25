"""
求一个数的阶乘
递归实现
"""

def recursion(num):
    if num <= 1:
        return 1
    return num * recursion(num - 1)

print("n! = ",recursion(5))