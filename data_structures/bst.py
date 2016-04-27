class BinarySearchTree:
    class Node:
        def __init__(self, key, data, left=None, right=None, parent=None):
            self.key = key
            self.data = data
            self.left = left
            self.right = right
            self.parent = parent

        def child_count(self):
            if self.left and self.right:
                return 2
            elif self.left or self.right:
                return 1
            else:
                return 0

        def is_left_child(self):
            return self.parent and self.parent.left is self

        def is_right_child(self):
            return self.parent and not self.is_left_child()

        def children(self):
            return [c for c in (self.left, self.right) if c is not None]

        def __repr__(self):
            return 'key:%s,\tvalue:%s' % (str(self.key), str(self.data))

        def __eq__(self, other):
            if isinstance(other, BinarySearchTree.Node):
                return self.key == other.key and self.data == other.data
            else:
                return False

        def __ne__(self, other):
            return not self.__eq__(other)

        def __hash__(self):
            return hash(self.__repr__())

    def __init__(self):
        self.__root = None
        self.__length = 0

    def add(self, key, data):
        if self.__root is None:
            self.__root = BinarySearchTree.Node(key, data)
        else:
            self._add(key, data, self.__root)
        self.__length += 1

    def _add(self, key, data, current):
        if key < current.key:
            if current.left is None:
                current.left = BinarySearchTree.Node(key, data, parent=current)
            else:
                self._add(key, data, current.left)
        elif key > current.key:
            if current.right is None:
                current.right = BinarySearchTree.Node(key, data, parent=current)
            else:
                self._add(key, data, current.right)
        else:
            current.data = data

    def in_order(self):
        def _rec(current):
            if current.left:
                _rec(current.left)

            print('key:%s,\tvalue:%s' % (str(current.key), str(current.data)))

            if current.right:
                _rec(current.right)

        if self.__root:
            _rec(self.__root)

    def bfs(self):
        if self.__root:
            visited = set()
            from data_structures import queue
            q = queue.Queue()
            q.enqueue(self.__root)

            while not q.empty():
                curr = q.dequeue()
                if curr.key not in visited:
                    print('key:%s,\tvalue:%s' % (str(curr.key), str(curr.data)))
                    visited.add(curr.key)
                    for c in curr.children():
                        if c not in visited:
                            q.enqueue(c)

    def get(self, key):
        res = self._get(key, self.__root)
        if res:
            return res.data

    def _get(self, key, current):
        if current is None:
            return None
        elif key == current.key:
            return current
        elif key < current.key:
            return self._get(key, current.left)
        else:
            return self._get(key, current.right)

    def empty(self):
        return self.__root is None

    def delete(self, key):
        to_remove = self._get(key, self.__root)

        if to_remove:
            if to_remove.child_count() == 0 or to_remove.child_count() == 1:
                self._remove(to_remove)
            elif to_remove.child_count() == 2:
                right_min = self._find_min(to_remove.right)
                to_remove.key = right_min.key
                to_remove.data = right_min.data
                self._remove(right_min)
            self.__length -= 1

    def _remove(self, to_remove):
        if to_remove.child_count() == 0:
            if to_remove.is_left_child():
                to_remove.parent.left = None
            else:
                to_remove.parent.right = None
        elif to_remove.child_count() == 1:
            to_remove_child = to_remove.left if to_remove.left else to_remove.right
            if to_remove.is_left_child():
                to_remove.parent.left = to_remove_child
            else:
                to_remove.parent.right = to_remove_child

    def _find_min(self, current):
        if current.left:
            return self._find_min(current.left)
        else:
            return current

    def depth(self):
        return self._depth(0, self.__root)

    def _depth(self, cnt, current):
        if current:
            d1 = self._depth(cnt + 1, current.left)
            d2 = self._depth(cnt + 1, current.right)
        else:
            return cnt

        return d1 if d1 > d2 else d2

    def is_balanced(self):
        if self._check_balanced(self.__root) == -1:
            return False
        else:
            return True

    def _check_balanced(self, current):
        if current is None:
            return 0

        l_depth = self._check_balanced(current.left)
        if l_depth == -1:
            return -1
        r_depth = self._check_balanced(current.right)
        if r_depth == -1:
            return -1

        diff = abs(l_depth - r_depth)
        return -1 if diff > 1 else max([l_depth, r_depth]) + 1

    def __contains__(self, key):
        return self._get(key, self.__root)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self.__length
