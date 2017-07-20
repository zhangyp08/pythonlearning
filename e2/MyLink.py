#!/usr/bin/python
# encoding=utf-8
from Node import Node


class MyLink(object):
    def __init__(self):                  ## init a empty link
        self.head=None
        self.tail=None
        self.len=0

    def append(self,data):               ## append data to last one
        node=Node(data)
        if self.head is None:
            self.head=node
            self.tail=node
        else:
            self.tail.next=node
            self.tail=node
        self.len += 1

    def insert(self,index,data):            ## insert data
        if 1 <= index <= self.len:
            node=Node(data)
            if index == 1:
                if self.head is None:           #在空链表插入
                    self.head = node
                    self.tail = node
                else:                           #在第一个插入，且链表不为空的情况下
                    node.next = self.head.next
                    self.head.next = node
            else:
                cur_index = 0
                cur = self.head
                while cur_index < (index-1):      #cur为索引的上一个
                    cur = cur.next
                    cur_index += 1
                node.next = cur.next
                cur.next = node
                if node.next is None:              #尾部情况
                    self.tail = node
            self.len += 1
        else:
            raise Exception("The index is not valid!")

    def iter(self):                     # iterate link
        if not self.head:
            return
        current=self.head
        yield current.data              # return an iterate object
        while current.next:
            current=current.next
            yield current.data

    def remove(self,index):             ## remove index link data
        if self.head is None:
           raise Exception("The link is empty")
        if 1 <= index <= self.len:
            cur_index = 0
            cur = self.head
            if self.len == 1 and index == 1 :           #链表只有一个值，并且index=1，则清空链表
                self.head = None
                self.tail = None
            elif index == 1 and self.len > 1:               #删除链表的第一个值
                self.head=cur.next

            else:
                while cur_index < (index - 1):  # cur为索引的上一个
                    cur = cur.next
                    cur_index += 1
                node = cur.next
                cur.next=node.next
            self.len-=1
            print self.len
        else:
            raise Exception("The index is invalid or largen than link length")

    def size(self):                     ## return link size
        return self.len

    def is_empty(self):                 ##if the link is empty
        return self.head is None

###test

mylink = MyLink()           #init
mylink.append(10)
mylink.append(11)
mylink.insert(1,9)
mylink.insert(2,8)
mylink.remove(2)
mylink.remove(1)
mylink.remove(1)
mylink.remove(1)
l=mylink.iter()
for i in l:
    print i