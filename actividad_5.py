import os
from actividad_4 import Registro

with open("registros.txt", "r") as fich_regs:
    if os.path.exists("registros.txt"):
        codigo_buscar = int(input("Ingrese el codigo a buscar: "))
        linea = fich_regs.readline().split(",")
        reg = Registro(int(linea[0]), linea[1], linea[2])
        if reg.get_codigo() == codigo_buscar:
            print(reg.__str__())
        else:
            print("Registro no encontrado")
    else:
        print("Fichero no existente")