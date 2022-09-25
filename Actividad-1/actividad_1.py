class NumCom:
    def __init__(self, p_real, p_ima):
        self.__p_real = p_real
        self.__p_ima = p_ima

    def set_p_real(self, p_real):
        self.__p_real = p_real

    def get_p_real(self):
        return self.__p_real

    def set_p_ima(self, p_ima):
        self.__p_ima = p_ima

    def get_p_ima(self):
        return self.__p_ima

    def __add__(self, other):  # a + c, bi + di
        temp = NumCom(self.__p_real + other.get_p_real(), self.__p_ima + other.get_p_ima())
        return temp

    def __sub__(self, other):  # a - c, bi - di
        temp = NumCom(self.__p_real - other.get_p_real(), self.__p_ima - other.get_p_ima())
        return temp

    def __mul__(self, other):
        lis_res = [                              # Propiedad distributiva
            self.__p_real * other.get_p_real(),  # a * c   =   w
            self.__p_real * other.get_p_ima(),   # a * di  =   x
            self.__p_ima * other.get_p_real(),   # bi * c  =   y
            self.__p_ima * other.get_p_ima()     # bi * di =   z
        ]                                        # Multiplicacion de numeros complejos
        lis_res[1] += lis_res[2]                 # = x + y
        lis_res[2] = lis_res[3] * -1             # = z * -1
        lis_res[0] += lis_res[2]                 # = w + (z * -1)
        lis_res.pop(2)                           # Se eliminan los posiciones innecesarias [2] y [3]
        temp = NumCom(lis_res[0], lis_res[1])    # = w + (z * -1), x + y
        return temp

    def __str__(self):
        return str(self.__p_real) + " " + str(self.__p_ima) + "i"


num1 = NumCom(2, 4)
num2 = NumCom(3, -2)
print("Suma:", num1 + num2)            # 5, 2i
print("Resta:", num1 - num2)           # -1, 6i
print("Multiplicacion:", num1 * num2)  # 14, 8i
