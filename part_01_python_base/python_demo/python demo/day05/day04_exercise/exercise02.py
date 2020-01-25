"""
4.　在控制台中获取一个整数作为边长．
　　根据边长打印矩形．
   例如：４
       ****
       *  *
       *  *
       ****

       6
       ******
       *    *
       *    *
       *    *
       *    *
       ******
"""

number = int(input("请输入整数:"))  # 4

print("*" * number)

for item in range(number - 2):  #
    print("*" + " " * (number - 2) + "*")

print("*" * number)
