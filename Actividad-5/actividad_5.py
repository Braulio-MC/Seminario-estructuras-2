import os

if os.path.exists("actividad_5.txt"):
    with open("actividad_5.txt", "r") as archivo:
        cifrado = ""  # Variable que contendra la cadena de caracteres cifrada
        descifrado = ""  # Variable que contendra la cadena de caracteres descifrada
        caracter = archivo.read(1)
        while caracter != "":
            if caracter.islower():  # Si el caracter es minuscula se cifrara
                cifrado += chr(ord(caracter) + 1)  # Calcula el numero ascii del caracter y le suma 1 despues
                # lo castea a char y lo concatena a la variable cifrado
            else:
                cifrado += caracter  # Si es mayuscula solo se concatena el caracter
            caracter = archivo.read(1)
    print(cifrado)
    print("--------------------------------------------------------------------")
    with open("cif_act_5.txt", "w") as archivo:
        archivo.write(cifrado)  # Escribimos la cadena cifrada al archivo cif_act_5.txt
    with open("cif_act_5.txt", "r") as archivo:
        caracter = archivo.read(1)
        while caracter != "":
            if caracter.islower():  # Si el caracter es minuscula se descifrara
                descifrado += chr(ord(caracter) - 1)  # Calcula el numero ascii del caracter y le resta 1 despues
                # lo castea a char y lo concatena a la variable descrifrado
            else:
                descifrado += caracter  # Si es mayuscula solo se concatena el caracter
            caracter = archivo.read(1)
    print(descifrado)
else:
    print("El archivo no existe")