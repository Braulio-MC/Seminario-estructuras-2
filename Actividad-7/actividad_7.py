import os
from registro import Registro

if os.path.exists("actividad_7.txt"):
    with open("actividad_7.txt", "r") as fich_regs:
        codigo_buscar = int(input("Codigo a buscar: "))
        bandera = False
        reg = Registro(0, "", "")  # Se inicializa el objeto donde se almacenaran los datos del registro
        for linea in fich_regs:
            reg.from_file(linea.split(","))  # Se divide la cadena en campos para despues asignarlos al objeto
            if reg.get_codigo() == codigo_buscar:  # Se comparan los codigos
                bandera = True  # Se implementa una bandera para saber si existe el registro
                break
        if bandera:  # Si el registro existe se imprime
            print(reg.__str__())
        else:  # Si no existe se le pregunta al usuario si desea agregarlo
            with open("actividad_7.txt", "a") as fich_regs_append:
                agregar = input("Registro no encontrado, ¿desea agregarlo? (S/N): ").upper()
                if agregar == 'S':
                    try:  # La excepcion es para el codigo (tiene que ser numerico)
                        print("Codigo:", codigo_buscar)
                        reg = Registro(codigo_buscar, input("Nombre: "), input("Carrera: "))  # Se crea
                        # un objeto con los datos obtenidos
                        fich_regs_append.write(reg.to_file() + "\n")  # Se escribe el objeto en el archivo
                        # con el metodo to_file
                    except Exception as ex:
                        print("\nOcurrio una excepcion de tipo Exception:", ex)
else:
    print("Fichero no existente")
