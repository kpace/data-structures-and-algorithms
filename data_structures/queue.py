class Queue(object):
    """ "Linked" Queue implementation """

    class Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    def __init__(self):
        self.__first = None
        self.__last = None

    def enqueue(self, d):
        if self.empty():
            self.__first = self.__last = Queue.Node(d)
        else:
            self.__last.next = Queue.Node(d)
            self.__last = self.__last.next

    def dequeue(self):
        if self.empty():
            raise ValueError("Queue is empty")
        d = self.__first.data
        if self.__first == self.__last:
            self.__first = self.__last = None
        else:
            self.__first = self.__first.next
        return d

    def empty(self):
        return self.__first is None
