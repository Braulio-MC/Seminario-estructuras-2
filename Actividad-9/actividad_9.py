class Queue:
    def __init__(self):
        self.__queue = []
        self.__size = 0  # Tamaño en objetos de la cola

    def empty(self):
        return self.__size == 0

    def front(self):  # Metodo para regresar el frente de la cola
        try:
            return self.__queue.__getitem__(0)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def end(self):  # Metodo para regresar el final de la cola
        try:
            return self.__queue.__getitem__(self.__size - 1)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def push(self, obj):  # Metodo para encolar
        self.__queue.append(obj)
        self.__size = self.__size + 1

    def pop(self):  # Metodo para desencolar
        try:
            popped = self.__queue.pop(0)
            self.__size = self.__size - 1
            return popped
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def size(self):
        return self.__size

    def get(self, index):  # Metodo para retornar un objeto de la cola por indice
        try:
            return self.__queue.__getitem__(index)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def __contains__(self, item):
        for i in self.__queue:
            if i is item:
                return True
        return False

    def print(self):
        print(self.__queue)


"""q = Queue()
q.push("Hola")
q.push(123)
q.push('C')
print(q.front())  # "Hola"
q.pop()           # pop a "Hola"
print(q.size())   # 2
print(q.front())  # 123
q.pop()           # pop a 123
print(q.front())  # 'C'
q.push("Adios")
print(q.size())   # 2
q.print()         # ['C', 'Adios']"""
