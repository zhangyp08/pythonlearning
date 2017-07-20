#!/usr/bin/python
# encoding:utf-8

class MyQueue(object):
    def __init__(self):
        self.MyList = []

    def put(self,data):
        self.MyList.append(data)

    def get(self):
        data=self.MyList[0]  # get the first value and return
        for i in xrange(len(self.MyList)-1):
            self.MyList[i]=self.MyList[i+1]
        self.MyList.pop()
        return data

    def queueLen(self):
        return self.MyList.__len__()

    def queuePrint(self):
        for data in self.MyList:
            print data

    def queueToStr(self,sep=''):
        s=''
        for data in xrange(len(self.MyList)-1):
            s+=str(self.MyList[data])
            s+=sep
        s=s+str(self.MyList[data+1])
        return s


testQueue=MyQueue()
testQueue.put(1)
testQueue.put(2)
testQueue.put(3)
testQueue.put('a')
testQueue.put('b')
testQueue.queuePrint()
print "The queue length is: ", testQueue.queueLen()
getData=testQueue.get()
print "Pop data is: ", getData
testQueue.queuePrint()
print "Turn Queue to str: ", testQueue.queueToStr('#')
