import os

if os.path.exists('actividad_3.txt'):
    contador = 0
    with open('actividad_3.txt', 'r') as archivo:
        caracter = archivo.read(1)
        while caracter != "":
            contador += 1
            caracter = archivo.read(1)
    print("Numero de caracteres:", contador)
else:
    print("El archivo no existe")

