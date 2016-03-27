class Stack(object):
    """ Stack implementation """

    class Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    top = None

    def empty(self):
        return not self.top

    def push(self, d):
        self.top = Stack.Node(d, self.top)

    def pop(self):
        if not self.empty():
            d = self.top.data
            self.top = self.top.next
            return d

    def peek(self):
        if not self.empty():
            return self.top.data
