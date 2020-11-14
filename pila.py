class Stack:
    def __init__(self):
        self.__stack = []
        self.__size = 0

    def top(self):
        try:
            return self.__stack.__getitem__(self.__size - 1)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def push(self, obj):
        self.__stack.append(obj)
        self.__size = self.__size + 1

    def pop(self):
        try:
            self.__stack.pop(self.__size - 1)
            self.__size = self.__size - 1
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def size(self):
        return self.__size

    def get(self, index):
        try:
            return self.__stack.__getitem__(index)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def print(self):
        print(self.__stack)
