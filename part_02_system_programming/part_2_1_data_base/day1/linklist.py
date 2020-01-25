"""
    功能: 实现单链表的构建和功能操作
    重点代码
"""
from list_helper import *


# 创建节点类

class Node:
    def __init__(self, val, next=None):
        self.val = val  # 有用数据
        self.next = next  # 获取下一个节点关系


class LinkList:
    def __init__(self):
        self.head = Node(None)
        # 默认head的索引为-1

    def init_list(self, list_):
        p = self.head

        for item in list_:
            p.next = Node(item)
            p = p.next

    def show(self):
        """
        遍历链表
        """
        p = self.head.next
        while p is not None:
            yield p.val
            p = p.next

    def is_empty(self):
        """
            判断链表为空
        """
        if self.head.next is None:
            return True
        return False

    def clear(self):
        """
        清空链表
        """
        self.head.next = None

    def append(self, val):
        """
            尾部插入
        """
        p = self.head
        while p.next is not None:
            p = p.next
        p.next = Node(val)

    def head_insert(self, val):
        """
            头部插入
        """
        node = Node(val)
        node.next = self.head.next
        self.head.next = node

    def insert(self, index, val):
        """
            指定插入位置
        """
        p = self.head
        for i in range(index):
            # 超出位置最大范围,结束循环
            if p.next is None:
                break
            p = p.next
        node = Node(val)
        node.next = p.next
        p.next = node

    def delete(self, x):
        p = self.head
        # 短路逻辑,避免p.next.val报错
        while p.next and p.next.val != x:
            p = p.next
        if p.next is None:
            raise ValueError("x not in linklist")
        else:
            p.next = p.next.next

    def get_index(self, index):
        """
            获取指定位置的数据
        """
        p = self.head.next
        if index < 0:
            raise IndexError("Index out of range hah")
        for i in range(index):
            if p.next is None:
                raise IndexError("index out of range oh yeah")
            p = p.next
        return p.val

    def merge(l1, l2):
        # 将l2合并到l1中
        p = l1.head
        q = l2.head.next
        while p.next is not None:
            if p.next.val < q.val:
                p = p.next
            else:
                tmp = p.next
                p.next = q
                p = p.next
                q = tmp
        p.next = q


    print("==================")

