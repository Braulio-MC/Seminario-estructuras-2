class Registro:
    def __init__(self, codigo, nombre, carrera):
        self.__codigo = codigo
        self.__nombre = nombre
        self.__carrera = carrera

    def set_codigo(self, codigo):
        self.__codigo = codigo

    def get_codigo(self):
        return self.__codigo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    def get_nombre(self):
        return self.__nombre

    def set_carrera(self, carrera):
        self.__carrera = carrera

    def get_carrera(self):
        return self.__carrera

    def to_file(self):  # Metodo que regresa una cadena de caracteres con los campos separados con coma para escribir
        # a un archivo
        return str(self.__codigo) + ", " + self.__nombre + ", " + self.__carrera

    def from_file(self, split_stream):  # Metodo que recibe una cadena de caracteres contenedora de los campos
        # codigo, nombre y carrera para despues ser asignados a las variables del objeto
        self.__init__(int(split_stream[0]), split_stream[1], split_stream[2])

    def __cmp__(self, other):
        return self.__codigo == other.get_codigo() \
               and self.__nombre == other.get_nombre() \
               and self.__carrera == other.get_carrera()

    def __str__(self):
        return "Codigo: " + str(self.__codigo) + ", Nombre: " + self.__nombre + ", Carrera: " + self.__carrera