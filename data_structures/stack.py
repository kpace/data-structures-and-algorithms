class Stack(object):
    """ "Linked" Stack implementation """

    class Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next
    def __init__(self):
        self.__top = None

    def push(self, d):
        self.__top = Stack.Node(d, self.__top)

    def pop(self):
        if self.empty():
            raise ValueError("Stack is empty")
        d = self.__top.data
        self.__top = self.__top.next
        return d

    def peek(self):
        if self.empty():
            raise ValueError("Stack is empty")
        return self.__top.data

    def empty(self):
        return not self.__top
