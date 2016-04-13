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

    __root = None
    __length = 0

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
        else:
            if current.right is None:
                current.right = BinarySearchTree.Node(key, data, parent=current)
            else:
                self._add(key, data, current.right)

    def pre_order(self):
        def _rec(current):
            if current.left:
                _rec(current.left)

            print('key:%s,\tvalue:%s' % (str(current.key), str(current.data)))

            if current.right:
                _rec(current.right)

        if self.__root:
            _rec(self.__root)

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

    def is_balanced(self):
        dl = self._depth(0, self.__root.left)
        dr = self._depth(0, self.__root.right)
        return abs(dl - dr) <= 1

    def _depth(self, cnt, current):
        if current:
            d1 = self._depth(cnt + 1, current.left)
            d2 = self._depth(cnt + 1, current.right)
        else:
            return cnt

        return d1 if d1 > d2 else d2

    def __contains__(self, key):
        return self._get(key, self.__root)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self.__length

t = BinarySearchTree()

assert len(t) == 0

t.add(4, 'a')
t.add(15, 'b')
t.add(32, 'c')
t.add(6, 'd')
t.add(13, 'e')
t.add(48, 'f')
t.add(2, 'g')

assert t.depth() == 4
assert t.is_balanced() == False
assert len(t) == 7

t.delete(15)
t.delete(2)
assert 15 not in t
assert 2 not in t
assert len(t) == 5

t.pre_order()
