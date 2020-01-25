import time


def time_count(func):
    def wrapper(*args, **kwargs):
        a = time.time()

        func(*args, **kwargs)

        b = time.time()
        c = b - a
        print("程序执行了%f秒"%c)
    return wrapper

@time_count
def fun01():
    time.sleep(2)
    print("over")


@time_count
def fun02(a):
    time.sleep(1)
    print("over,参数是",a)

fun01()
print("---------------------")
fun02(998)
