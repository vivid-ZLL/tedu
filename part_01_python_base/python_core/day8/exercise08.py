count = 0


def fun01():
    print("alice")
    global count
    count += 1


fun01()
fun01()
fun01()
fun01()
fun01()
fun01()
print("调用了%d次" % count)
