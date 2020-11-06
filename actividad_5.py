import os
from registro import Registro

with open("registros.txt", "r") as fich_regs:
    if os.path.exists("registros.txt"):
        codigo_buscar = int(input("Codigo a buscar: "))
        bandera = False
        reg = Registro(0, "", "")
        linea = fich_regs.readline()
        while linea:
            reg.from_file(linea.split(","))
            if reg.get_codigo() == codigo_buscar:
                bandera = True
                break
            linea = fich_regs.readline()
        if bandera:
            print(reg.__str__())
        else:
            print("Registro no encontrado")
    else:
        print("Fichero no existente")