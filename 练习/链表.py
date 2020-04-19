#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Author:Richard_Kong
"""
链表的节点实现 和 链表的实现  链表的增删改查 插入 遍历头部插入 尾部插入 任意位置插入
"""

class SingleNode(object):
    """单链表的节点的实现"""

    def __init__(self, item):
        # item 是存放数据元素的
        self.item = item
        # next 是下一个节点的标识
        self.next = None


class SingleLinkList(object):
    """
    单向链表的实现,链表中的元素是node 结点 不是item
    """

    def __init__(self):
        # head 指向链表头结点的地址
        self.head = None

    def is_empty(self):
        """
        判断链表是否为空
        :return: 判断头结点的标志是否为None  如果是 那么就为空
        """
        return self.head is None

    def length(self):
        """
        计算链表的长度
        :return:返回链表的长度
        """
        # head 指向链表头结点的地址 所以cur 就是链表的节点
        cur = self.head
        count = 0

        while cur is not None:
            # cur是链表的节点 所以可以调用 item、 和 next
            cur = cur.next
            count += 1

        return count

    def travel(self):
        """
        遍历链表
        :return:
        """
        cur = self.head
        while cur.next is not None:
            print(cur.item, " ")
            cur = cur.next
        print(cur.item)


    def add(self,item):
        """
        在链表的头部添加元素
        :param item:
        :return:
        """
        # 创建一个保存item的节点
        node = SingleNode(item)
        # 在头部添加元素 将新添加元素的next指向 现有的头结点，将现有的头结点指向新添加的元素
        node.next = self.head
        self.head = node

    def append(self,item):
        """
        尾部添加元素,思想：当链表为空时 直接self.head = node 当 链表部位空时 要找到最后一个元素
        将最后一个元素的next指向 node
        :param item:
        :return:
        """
        node  = SingleNode(item)
        if self.head is None:
            self.head = node
        else:
            cur  = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self,pos,item):
        """
        在指定位置添加元素，那么传入的参数就应该有两个，一个是位置，一个是元素
        首先要找到插入的位置，就好办
        首先 要判断插入的位置 和链表的长度的关系 其次再决定怎么插入
        :param pos: 插入元素的位置
        :param item: 插入的元素
        :return:
        """
        # 如果 指定的位置pos在第一个元素之前 那么执行头部插入
        if pos <= 0:
            self.append(item)
        # 如果指定的位置 大于链表的长度 则执行尾部插入
        elif pos >= (self.length() -1):
            self.append(item)
        # 其他情况要找到指定位置进行插入
        else:
            node = SingleNode(item)
            count = 0
            # pre用来指向指定位置pos的前一个位置pos-1，初始从头结点开始移动到指定位置
            pre = self.head

            while count < (pos - 1):
                count += 1
                pre = pre.next
            # 将新节点的next指向插入位置的节点
            node.next = pre.next
            # 将插入位置的前一个节点的next指向新节点
            pre.next = node

    def remove(self,item):
        """
        删除指定的节点，首先要在表中找到此节点才能删除
        :param item: 传入要删除的节点
        :return:
        """
        cur = self.head
        pre = None

        while cur.next is not None:
            # 找到指定元素
            if cur.item == item:
                # 如果第一个就是要删除的节点
                if not pre:
                    self.head = cur.next
                else:
                    # 将删除位置前一个节点的next指向删除位置的后一个节点
                    pre.next = cur.next
                break
            else:
                # 如果不相等 那就继续按照链表后移
                pre = cur
                cur = cur.next

    def search(self,item):
        """
        在链表中所有item元素是否存在，并返回True or False
        :param item:
        :return:存在返回True 不存在返回False
        """
        cur = self.head
        while cur != None:
            if cur.item == item:
                return True
            cur = cur.next
        return False


if __name__ == '__main__':
    linkList = SingleLinkList()
    linkList.add(12)
    linkList.append(31)
    print(linkList.length())
    linkList.insert(1,43)
    print(linkList.is_empty())
    print(linkList.length())
    linkList.travel()
    print(linkList.search(12))
    linkList.remove(12)
    linkList.travel()
    print(linkList.length())
