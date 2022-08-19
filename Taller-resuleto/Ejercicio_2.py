"""
Escriba un programa que solicite cuatro números, muestre la suma de estos inclu-
yendo los números ingresados:
Ejemplo: (1.5) + (-4) + (65.34) + (9) = 71.84.
"""
lista = []
for n in range(4):
    a = float(input(f"Ingrese el #{n+1}: "))
    lista.append(a)

print(f"({lista[0]}) + ({lista[1]}) + ({lista[2]}) + ({lista[3]}) = {sum(lista)} ")