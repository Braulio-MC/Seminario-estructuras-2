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

    def empty(self):  # Metodo para saber si la lista esta vacia
        return self._anchor is None

    def size(self):  # Metodo que retorna el tamaño en objetos de la lista
        return self._size

    def _last_node(self):  # Metodo que devuelve el ultimo nodo de la lista
        temp = self._anchor
        while temp.next_node:
            temp = temp.next_node
        return temp

    def _prev_node_of(self, node):  # Metodo que devuelve el nodo previo al nodo pasado por parametro
        temp = self._anchor
        prev = None
        while temp.next_node:
            if node is temp:
                break
            prev = temp
            temp = temp.next_node
        return prev

    def push_front(self, data):  # Metodo para insertar al frente
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            new_node.next_node = self._anchor
            self._anchor = new_node
        self._size += 1

    def push_back(self, data):  # Metodo para insertar al final
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            self._last_node().next_node = new_node
        self._size += 1

    def insert(self, data, index=0):  # Metodo para insertar delante del indice dado
        if 0 <= index < self._size:
            new_node = Node(data)
            temp = self.get_node(index)
            new_node.next_node = temp.next_node
            temp.next_node = new_node
            self._size += 1

    def pop_front(self):  # Metodo para eliminar el nodo del frente
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            self._anchor = self._anchor.next_node
        self._size -= 1

    def pop_back(self):  # Metodo para eliminar el nodo del final
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            prev = self._prev_node_of(self._last_node())
            prev.next_node = None
        self._size -= 1

    def remove(self, index=0):  # Metodo para eliminar el nodo del indice dado
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

    def search_for(self, data):  # Metodo que devuelve si un dato fue encontrado y cuantas veces lo encontro
        temp = self._anchor
        found = False
        times = 0
        while temp:
            if temp.data is data:
                times += 1
                found = True
            temp = temp.next_node
        return found, times

    def get_node(self, index):  # Metodo para obtener un nodo de la lista
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

    def empty(self):  # Metodo para saber si la lista esta vacia
        return self._anchor is None

    def size(self):  # Metodo que retorna el tamaño en objetos de la lista
        return self._size

    def _last_node(self):  # Metodo que devuelve el ultimo nodo de la lista
        temp = self._anchor
        while temp.next_node:
            temp = temp.next_node
        return temp

    def push_front(self, data):  # Metodo para insertar al frente
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            new_node.next_node = self._anchor
            self._anchor.prev_node = new_node
            self._anchor = new_node
        self._size += 1

    def push_back(self, data):  # Metodo para insertar al final
        new_node = Node(data)
        if self.empty():
            self._anchor = new_node
        else:
            last = self._last_node()
            last.next_node = new_node
            new_node.prev_node = last
        self._size += 1

    def insert(self, data, index=0):  # Metodo para insertar delante del indice dado
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

    def pop_front(self):  # Metodo para eliminar el nodo del frente
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            self._anchor = self._anchor.next_node
            self._anchor.prev_node = None
        self._size -= 1

    def pop_back(self):  # Metodo para eliminar el nodo del final
        if self.empty():
            return
        elif self._anchor.next_node is None:
            self._anchor = None
        else:
            temp = self._last_node()
            temp.prev_node.next_node = None
            temp.prev_node = None
        self._size -= 1

    def remove(self, index=0):  # Metodo para eliminar el nodo del indice dado
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

    def search_for(self, data):  # Metodo que devuelve si un dato fue encontrado y cuantas veces lo encontro
        temp = self._anchor
        found = False
        times = 0
        while temp:
            if temp.data is data:
                times += 1
                found = True
            temp = temp.next_node
        return found, times

    def get_node(self, index):  # Metodo para obtener un nodo de la lista
        if 0 <= index < self._size:
            temp = self._anchor
            i = 0
            while temp.next_node:
                if i is index:
                    break
                temp = temp.next_node
                i += 1
            return temp


print("----------Lista simplemente--------------")
sll = SLList()
sll.push_front(1)
sll.push_back("Hola")
sll.insert(3.1416, )  # Despues del indice 0
sll.insert("Adios", 2)  # Despues del indice 2
for item in range(sll.size()):
    print(sll.get_node(item))
print("--------------Eliminacion---------------")
sll.pop_front()  # Elimina 1
sll.pop_back()  # Elimina "Adios"
sll.remove()  # Elimina 3.1416
for item in range(sll.size()):
    print(sll.get_node(item))
print("----------Lista doblemente--------------")
dll = DLList()
dll.push_front(1)
dll.push_back("Hola")
dll.insert(3.1416, )  # Despues del indice 0
dll.insert("Adios", 2)  # Despues del indice 2
for item in range(dll.size()):
    print(dll.get_node(item))
print("--------------Eliminacion---------------")
dll.pop_front()  # Elimina 1
dll.pop_back()  # Elimina "Adios"
dll.remove()  # Elimina 3.1416
for item in range(dll.size()):
    print(dll.get_node(item))
