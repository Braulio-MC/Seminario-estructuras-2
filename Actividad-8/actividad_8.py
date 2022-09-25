class Stack:
    def __init__(self):
        self.__stack = []
        self.__size = 0  # Tamaño en objetos de la pila

    def top(self):  # Metodo para regresar el tope de la pila
        try:
            return self.__stack.__getitem__(self.__size - 1)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def push(self, obj):  # Metodo para apilar
        self.__stack.append(obj)
        self.__size = self.__size + 1  # Se suma 1 al tamaño cada que se apila

    def pop(self):  # Metodo para desapilar
        try:
            self.__stack.pop(self.__size - 1)
            self.__size = self.__size - 1  # Se resta 1 al tamaño cada que se desapila
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def size(self):
        return self.__size

    def get(self, index):  # Metodo para retornar un objeto de la pila por indice
        try:
            return self.__stack.__getitem__(index)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def print(self):
        print(self.__stack)


s = Stack()
s.push("Hola")
s.push(123)
s.push('C')
print(s.top())  # 'C'
s.pop()  # pop a 'C'
print(s.size())  # 2
print(s.top())  # 123
s.push("Adios")
print(s.top())  # "Adios"
print(s.size())  # 3
s.print()  # ['Hola', 123, 'Adios']
