"""Escriba un programa que solicite una letra del alfabeto e indique sí es
una vocal o una consonante, si no es ninguna de las dos, entonces
debe indicar que ese carácter no es válido"""

import string
letra = input("\nDigite una letra del alfabeto: ")
letra = letra.lower()
lista = list(string.ascii_lowercase) #Lista con el alfabeto

if(letra in lista):
    if(letra=='a' or letra=='e' or letra == 'i' or letra == 'o' or letra=='u'):
        print("Vocal")
    else:
        print("Consonate")
else:
    print("El caracter no es valido")
