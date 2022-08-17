"""Escriba un programa que lea un número entero ingresado por el
usuario. Y luego, muestre un mensaje que indique si el número
entero es par o impar."""

a = int(input("Digite un numero entero: "))
if(a%2==0):
    print("Entero es Par")
else:
    print("Entero es Impar")