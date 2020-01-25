from linklist import *
import time

l = []
for i in range(999999):
    l.append(i)

link = LinkList()
link.init_list(l)

tm = time.time()
# for i in l:
#     print(i)　　#　列表
# link.show()  #　链表

# l.append(8866)
# link.append(8866) #　尾插入

# l.insert(0,8866)
# link.head_insert(8866) #　头插

# link.insert(100,9999)

# link.delete(1) #删除
l.remove(1)

# link.show()
# print(link.get_index(-1))

print("time: ",time.time()-tm)
