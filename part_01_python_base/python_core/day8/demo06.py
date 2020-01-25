"""
    函数参数
        形式参数
"""

"""
# 缺省(默认)参数:如果实参不提供,可以使用默认值
def fun01(a=None, b=None, c=0, d=0):
    print(a)
    print(b)
    print(c)
    print(d)

    # 关键字实参 + 缺省形参 : 调用者可以灵活传递参数


fun01(a=1)


# 位置形参
def fun01(a, b, c, d):
    print(a)
    print(b)
    print(c)
    print(d)


# 3.星号元组形参: *将所有实参合并为一个元组
# 作用:让实参个数无限制
def fun03(*args):
    print(args)


fun03(1,12321,6548,654564,321,87 )



# 命名关键字形参:在星号元组形参以后的位置形参
# 目的:要求实参必须使用关键字实参
def fun04(a, *args, b):
    print(a)
    print(args)
    print(b)


fun04(534564, b=6548)
fun04(4564,54564,321231,2313,b=2123)



# 5. 字典形参:实参可以传递数量无限的关键字实参
#            目的:将实参合并为字典
def fun06(**a):
print(a)

fun06(a=1, b=3, cc=22)

"""
