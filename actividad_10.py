class Node:
    def __init__(self, data=None):
        self.data = data
        self._next_node = None
        self._prev_node = None

    @property
    def prev_node(self):
        return self._prev_node

    @prev_node.setter
    def prev_node(self, prev_node):
        if isinstance(prev_node, Node) or prev_node is None:
            self._prev_node = prev_node

    @property
    def next_node(self):
        return self._next_node

    @next_node.setter
    def next_node(self, next_node):
        if isinstance(next_node, Node) or next_node is None:
            self._next_node = next_node

    def __str__(self):
        return str(self.data)


class SLList:
    def __init__(self):
        self._anchor = None
        self._size = 0

    def empty(self):
        return self._anchor is None

    def size(self):
        return self._size

    def _last_node(self):
        temp = self._anchor
        while temp.next_node:
            temp = temp.next_node
        return temp

    def _prev_node_of(self, node):
        temp = self._anchor
        prev = None
        while temp.next_node:
            if node is temp:
                break
            prev = temp
            temp = temp.next_node
        return prev

    def push_front(self, data):
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            new_node.next_node = self._anchor
            self._anchor = new_node
        self._size += 1

    def push_back(self, data):
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            self._last_node().next_node = new_node
        self._size += 1

    def insert(self, data, index=0):
        if 0 <= index < self._size:
            new_node = Node(data)
            temp = self.get_node(index)
            new_node.next_node = temp.next_node
            temp.next_node = new_node
            self._size += 1

    def pop_front(self):
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            self._anchor = self._anchor.next_node
        self._size -= 1

    def pop_back(self):
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            prev = self._prev_node_of(self._last_node())
            prev.next_node = None
        self._size -= 1

    def remove(self, index=0):
        if 0 <= index < self._size:
            index_temp = self.get_node(index)
            prev_temp = self._prev_node_of(index_temp)
            if self.empty():
                return
            elif index == 0 and prev_temp is None:
                self._anchor = self._anchor.next_node
            else:
                prev_temp.next_node = index_temp.next_node
            self._size -= 1

    def search_for(self, data):
        temp = self._anchor
        found = False
        times = 0
        while temp:
            if temp.data is data:
                times += 1
                found = True
            temp = temp.next_node
        return found, times

    def get_node(self, index):
        if 0 <= index < self._size:
            temp = self._anchor
            i = 0
            while temp.next_node:
                if i is index:
                    break
                temp = temp.next_node
                i += 1
            return temp


class DLList:
    def __init__(self):
        self._anchor = None
        self._size = 0

    def empty(self):
        return self._anchor is None

    def size(self):
        return self._size

    def _last_node(self):
        temp = self._anchor
        while temp.next_node:
            temp = temp.next_node
        return temp

    def push_front(self, data):
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            new_node.next_node = self._anchor
            self._anchor.prev_node = new_node
            self._anchor = new_node
        self._size += 1

    def push_back(self, data):
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            last = self._last_node()
            last.next_node = new_node
            new_node.prev_node = last
        self._size += 1

    def insert(self, data, index=0):
        if 0 <= index < self._size:
            new_node = Node(data)
            temp = self.get_node(index)
            if temp is self._last_node():
                new_node.prev_node = temp
                temp.next_node = new_node
            else:
                new_node.next_node = temp.next_node
                temp.next_node.prev_node = new_node
                temp.next_node = new_node
                new_node.prev_node = temp
            self._size += 1

    def pop_front(self):
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            self._anchor = self._anchor.next_node
            self._anchor.prev_node = None
        self._size -= 1

    def pop_back(self):
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            temp = self._last_node()
            temp.prev_node.next_node = None
            temp.prev_node = None
        self._size -= 1

    def remove(self, index=0):
        if 0 <= index < self._size:
            index_temp = self.get_node(index)
            if self.empty():
                return
            if index == 0 and index_temp.prev_node is None:
                self._anchor = self._anchor.next_node
            elif index is self._size - 1 and index_temp.next_node is None:
                index_temp.prev_node.next_node = None
            else:
                index_temp.prev_node.next_node = index_temp.next_node
                index_temp.next_node.prev_node = index_temp.prev_node
            self._size -= 1

    def search_for(self, data):
        temp = self._anchor
        found = False
        times = 0
        while temp:
            if temp.data is data:
                times += 1
                found = True
            temp = temp.next_node
        return found, times

    def get_node(self, index):
        if 0 <= index < self._size:
            temp = self._anchor
            i = 0
            while temp.next_node:
                if i is index:
                    break
                temp = temp.next_node
                i += 1
            return temp
