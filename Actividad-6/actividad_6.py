import os
from registro import Registro

if os.path.exists("actividad_6.txt"):
    with open("actividad_6.txt", "a") as registros:
        agregar = input("¿Agregar un registro? (S/N): ").upper()
        reg_agregados = 0
        while agregar == "S":
            try:  # La excepcion es para el codigo (tiene que ser numerico)
                reg = Registro(int(input("Código: ")), input("Nombre: "), input("Carrera: "))  # Se crea un objeto con
                # los datos obtenidos
                registros.write(reg.to_file() + "\n")  # Se escribe el objeto en el archivo con el metodo to_file
            except Exception as ex:
                print("\nOcurrio una excepcion de tipo Exception:", ex)
            else:
                reg_agregados += 1  # Si no se lanzo la excepcion se suma 1 al contador de registros
            agregar = input("\n¿Agregar un registro? (S/N): ").upper()
        else:
            print(f"Registros agregados: {reg_agregados}")
else:
    print("\nFichero no encontrado\n")
