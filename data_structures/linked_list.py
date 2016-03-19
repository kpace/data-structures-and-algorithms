class LList(object):
    class Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    __first = None
    __length = 0

    def __len__(self):
        return self.__length

    def empty(self):
        return not self.__first

    def append(self, data):
        n = LList.Node(data)
        if self.__first:
            last = self.__first
            while last.next:
                last = last.next
            last.next = n
        else:
            self.__first = n
        self.__length += 1

    def prepend(self, data):
        self.__first = LList.Node(data, self.__first)
        self.__length += 1

    def pop_first(self):
        if self.empty():
            raise ValueError("List is empty")
        res = self.__first
        self.__first = self.__first.next
        self.__length -= 1
        return res.data

    def _find_prev(self, data):
        prev = self.__first
        while prev.next:
            if prev.next.data == data:
                return prev
            else:
                prev = prev.next

    def pop(self, data):
        if self.empty():
            raise ValueError("List is empty")
        if self.__first.data == data:
            return self.pop_first()
        else:
            prev = self._find_prev(data)
            if prev:
                res = prev.next.data
                prev.next = prev.next.next
                self.__length -= 1
                return res
            else:
                return None

    def remove_duplicates(self):
        current = self.__first
        while current:
            runner = current
            while runner.next:
                if runner.next.data == current.data:
                    runner.next = runner.next.next
                    self.__length -= 1
                else:
                    runner = runner.next
            current = current.next

    def kth_to_last(self, k):
        """ Returns the kth to last element. """
        current = front = self.__first
        for _ in range(k):
            front = front.next

        while front.next:
            front = front.next
            current = current.next
        return current.data