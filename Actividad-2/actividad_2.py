import os

if os.path.exists("actividad_2.txt"):
    with open('actividad_2.txt', 'r') as archivo:
        for line in archivo:
            print(line, end="")
else:
    print("El archivo no existe")
