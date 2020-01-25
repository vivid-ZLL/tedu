"""
    函数式编程 语法
"""

def fun01():
    print("fun01执行喽")

# 调用方法,执行方法体
re1 = fun01()
print(re1)

# 将函数赋值给变量
re2 = fun01
# 通过变量,调用函数
re2()

def fun02():
    print("fun02执行喽")

# 将函数作为函数的参数进行传递
# 将一个函数的代码(fun02/fun01),注入到另外一个函数中(fun03).
def fun03(func):
    print("fun03执行喽")
    func()

fun03(fun01)
fun03(fun02)









