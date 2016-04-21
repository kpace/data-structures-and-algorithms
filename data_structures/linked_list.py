class LList(object):
    """ Singly linked list implementation """

    class Node(object):
        def __init__(self, data, next=None):
            self.data = data
            self.next = next

    __first = None
    __length = 0

    def __len__(self):
        return self.__length

    def __iter__(self):
        current = self.__first
        while current is not None:
            yield current.data
            current = current.next

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

    def partition(self, x):
        """
        Partition the list around a value x, such that all elements less than
        x come before it, all nodes greater than or equal come after it.
        """
        self.pop(x)
        current = self.__first
        smaller_first = smaller_last = None
        greater_first = greater_last = None

        while current:
            if current.data < x:
                if smaller_first is None:
                    smaller_first = smaller_last = LList.Node(current.data)
                else:
                    smaller_last.next = LList.Node(current.data)
                    smaller_last = smaller_last.next
            else:
                if greater_first is None:
                    greater_first = greater_last = LList.Node(current.data)
                else:
                    greater_last.next = LList.Node(current.data)
                    greater_last = greater_last.next
            current = current.next
        if smaller_last is None:
            self.__first = LList.Node(x, greater_first)
        else:
            smaller_last.next = LList.Node(x, greater_first)
            self.__first = smaller_first

    def beginning_of_cycle(self):
        """
            Returns the first element of cycle, if there is such,
            otherwise returns None.
        """
        slow = fast = self.__first
        while slow.next and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                # cycle found
                # point slow to the first and move both pointers
                # at equal pace until they meet
                slow = self.__first
                while slow != fast:
                    slow = slow.next
                    fast = fast.next
                return fast.data
        return None

    def is_palindrome(self):
        st = []
        p = self.__first
        while p:
            st.append(p.data)
            p = p.next

        p = self.__first
        m = len(st) / 2
        while len(st) >= m:  # iterate only through half of the stack
            if p.data != st.pop():
                return False
            p = p.next
        return True
