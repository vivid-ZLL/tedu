"""
sort.py 排序算法训练
"""

#　冒泡
def bubble(list_):
    n = len(list_)
    # 　外层表示比较多少轮
    for i in range(n - 1):
        #  表示每轮两两比较的次数
        for j in range(n - 1 - i):
            # 从小到大排序
            if list_[j] > list_[j + 1]:
                list_[j],list_[j + 1] = list_[j + 1],list_[j]

#　完成一轮交换
    #快速排序
def sub_sort(list_,low,high):
    #　选定基准
    x = list_[low]
    #　low向后　ｈｉｇｈ向前
    while low < high:
        #　后面的数往前放
        while list_[high] >= x and high > low:
            high -= 1
        list_[low] =  list_[high]
        # 前面的数往后放
        while list_[low] < x and low < high:
            low += 1
        list_[high] = list_[low]

    list_[low] = x
    return low


def quick(list_,low,high):
    #　low 表示列表第一个元素索引，high表示最后一个元素索引
    if low < high:
        key = sub_sort(list_,low,high)
        quick(list_,low,key - 1)
        quick(list_, key + 1,high)



l = [4,9,3,1,2,5,8,4]
# bubble(l)
quick(l,0,len(l)-1)
print(l)

