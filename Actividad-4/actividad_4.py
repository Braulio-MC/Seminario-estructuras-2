import os

if os.path.exists("actividad_4.txt"):
    with open("actividad_4.txt", "r") as archivo:
        cifrado = ""  # Variable que contendra la cadena de caracteres cifrada
        caracter = archivo.read(1)
        while caracter != "":
            if caracter.islower():  # Si el caracter es minuscula se cifrara
                cifrado += chr(ord(caracter) + 1)  # Calcula el numero ascii del caracter y le suma 1 despues
                # lo castea a char y lo concatena a la variable cifrado
            else:
                cifrado += caracter  # Si es mayuscula solo se concatena el caracter
            caracter = archivo.read(1)
    print(cifrado)
else:
    print("El archivo no existe")
