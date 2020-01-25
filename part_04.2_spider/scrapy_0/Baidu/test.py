def func():
    for i in range(12):
        yield i


res = func()
for i in res:
    print(i)

print(res.__next__())