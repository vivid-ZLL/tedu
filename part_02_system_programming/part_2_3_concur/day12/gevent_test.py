import gevent

def foo(a,b):
    print("running foo ...",a,b)
    print("Foo again...")

f = gevent.spawn(foo,1,2)