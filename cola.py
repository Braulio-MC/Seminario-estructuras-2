class Queue:
    def __init__(self):
        self.__queue = []
        self.__size = 0

    def front(self):
        try:
            return self.__queue.__getitem__(0)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def end(self):
        try:
            return self.__queue.__getitem__(self.__size - 1)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def push(self, obj):
        self.__queue.append(obj)
        self.__size = self.__size + 1

    def pop(self):
        try:
            self.__queue.pop(0)
            self.__size = self.__size - 1
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def size(self):
        return self.__size

    def get(self, index):
        try:
            return self.__queue.__getitem__(index)
        except IndexError as exc:
            print("Se ha producido una excepcion en IndexError:", exc)

    def print(self):
        print(self.__queue)
