# 练习:记录一个函数fun01的执行次数.
#      画出内存图

# def fun01():
#     pass
#
# fun01()
# fun01()
# fun01()
# fun01()
# fun01()
# print("调用?次")


count = 0


def fun01():
    global count
    count += 1


fun01()
fun01()
fun01()
fun01()
fun01()
print("调用" + str(count) + "次")
