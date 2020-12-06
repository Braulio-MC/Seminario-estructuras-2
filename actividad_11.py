from actividad_9 import Queue


class Node:
    def __init__(self, identifier, data=None, father=None):
        self._identifier = identifier
        self.data = data
        self._father = father
        self._next_node = None
        self._prev_node = None

    @property
    def identifier(self):
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        self._identifier = identifier

    @property
    def father(self):
        return self._father

    @father.setter
    def father(self, father):
        self._father = father

    def is_leaf(self):
        return self is not None and self.prev_node is self.next_node

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

    def __cmp__(self, other):
        if self.data and self.identifier is other.data and other.identifier:
            return 0
        elif self.data and self.identifier > other.data and other.identifier:
            return 1
        elif self.data and self.identifier < other.data and other.identifier:
            return -1

    def __str__(self):
        return str(self.data)


class Tree:
    def __init__(self):
        self._root = None
        self._identifiers = []

    def _get_identifiers(self, root):
        if root is None:
            return
        self._identifiers.append(root.identifier)
        if root.prev_node:
            self._get_identifiers(root.prev_node)
        if root.next_node:
            self._get_identifiers(root.next_node)

    def _add(self, root, data, identifier):
        if identifier < root.identifier:
            if root.prev_node:
                self._add(root.prev_node, data, identifier)
            else:
                root.prev_node = Node(identifier, data, root)
        else:
            if root.next_node:
                self._add(root.next_node, data, identifier)
            else:
                root.next_node = Node(identifier, data, root)

    @staticmethod
    def _replace(old, new):
        if old is old.father.prev_node:
            old.father.prev_node = new
        elif old is old.father.next_node:
            old.father.next_node = new
        if new:
            new.father = old.father

    def _get_by_id(self, root, identifier):
        if root is None:
            return None
        if identifier == root.identifier:
            return root
        if identifier < root.identifier:
            return self._get_by_id(root.prev_node, identifier)
        else:
            return self._get_by_id(root.next_node, identifier)

    def _exists(self, root, identifier):
        if root is None:
            return False
        if identifier == root.identifier:
            return True
        if identifier < root.identifier:
            return self._get_by_id(root.prev_node, identifier)
        else:
            return self._get_by_id(root.next_node, identifier)

    @staticmethod
    def _breadth_first(root):
        queue = Queue()
        if queue and root:
            queue.push(root)
            while not queue.empty():
                popped = queue.pop()
                print(popped)
                if popped.prev_node:
                    queue.push(popped.prev_node)
                if popped.next_node:
                    queue.push(popped.next_node)

    def _height(self, root):
        if root is None:
            return 0
        left_height = self._height(root.prev_node)
        right_height = self._height(root.next_node)
        return (left_height if left_height > right_height else right_height) + 1

    def _get_the_lowest(self, tree):
        if tree is None or tree.prev_node is None:
            return tree
        return self._get_the_lowest(tree.prev_node)

    def _get_the_highest(self, tree):
        if tree is None or tree.next_node is None:
            return tree
        return self._get_the_highest(tree.next_node)

    def _preorder(self, root):
        if root is None:
            return
        print(root.data)
        self._preorder(root.prev_node)
        self._preorder(root.next_node)

    def _inorder(self, root):
        if root is None:
            return
        self._inorder(root.prev_node)
        print(root.data)
        self._inorder(root.next_node)

    def _postorder(self, root):
        if root is None:
            return
        self._postorder(root.prev_node)
        self._postorder(root.next_node)
        print(root.data)

    def empty(self):
        return self._root is None

    def identifiers(self):
        self._identifiers = []
        self._get_identifiers(self._root)
        print(self._identifiers)

    def add(self, data, identifier):
        if self.empty():
            self._root = Node(data, identifier)
        else:
            self._add(self._root, data, identifier)

    def remove(self, identifier):
        try:
            root = self._get_by_id(self._root, identifier)
            if root is self._root:
                if self._root.is_leaf():
                    self._root = None
                elif root.prev_node and not root.next_node:
                    self._root = self._root.prev_node
                    self._root.prev_node = None
                elif root.next_node and not root.prev_node:
                    self._root = self._root.next_node
                    self._root.next_node = None
                elif root.prev_node and root.next_node:
                    lowest = self._get_the_lowest(self._root.next_node)
                    self._root.data = lowest.data
                    self.remove(lowest.identifier)
            if root.father:
                if root.is_leaf():
                    self._replace(root, None)
                elif root.prev_node and not root.next_node:
                    self._replace(root, root.prev_node)
                elif root.next_node and not root.prev_node:
                    self._replace(root, root.next_node)
                elif root.prev_node and root.next_node:
                    lowest = self._get_the_lowest(root.next_node)
                    root.data = lowest.data
                    self.remove(lowest.identifier)
        except Exception as ex:
            ex.__init__("Identificador no existente: {}".format(identifier))
            print("Ocurrio una excepcion de tipo Exception:", ex)

    def get_by_id(self, identifier):
        return self._get_by_id(self._root, identifier)

    def exists(self, identifier):
        return self._exists(self._root, identifier)

    def get_the_highest(self):
        self._get_the_highest(self._root)

    def get_the_lowest(self):
        self._get_the_lowest(self._root)

    def height(self):
        return self._height(self._root)

    def breadth_first(self):
        self._breadth_first(self._root)

    def preorder(self):
        self._preorder(self._root)

    def inorder(self):
        self._inorder(self._root)

    def postorder(self):
        self._postorder(self._root)

    def __contains__(self, identifier):
        if self.exists(identifier):
            return True
        return False

    def __setitem__(self, identifier, data):
        if self.empty():
            self._root = Node(identifier, data)
        else:
            self._add(self._root, data, identifier)

    def __delitem__(self, identifier):
        self.remove(identifier)

    def __getitem__(self, identifier):
        return self.get_by_id(identifier)


t = Tree()
t[1] = 12345
t[2] = "Hola"
t[3] = (1, 2, 3)
t[4] = 3.1416
t[5] = "Adios"
t[6] = [4, 5, 6]
t[7] = {1: "Uno", 2: "Dos", 3: "Tres"}
print("breadth first")
t.breadth_first()
print("\npreorder")
t.preorder()
print("\ninorder")
t.inorder()
print("\npostorder")
t.postorder()
print("\nidentifiers")
t.identifiers()
