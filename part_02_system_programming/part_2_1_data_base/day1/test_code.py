from linklist import *

# test code
l = LinkList()
l01 = LinkList()
l02 = LinkList()
l.init_list([0, 1, 2, 3, 4, 5])

l01.init_list([0, 1, 3, 5])
l02.init_list([2, 3, 4, 5, 6])

l01.show()
l02.show()

re = l01.merge(l01, l02)
linklist_result = LinkList()
linklist_result.init_list(re)

for item in linklist_result.show():
    print(item)


