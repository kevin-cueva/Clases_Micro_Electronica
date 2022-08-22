import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
lista = []
n = int(input())
dato = 100
for i in range(n):
    pi = int(input())
    lista.append(pi)

lista.sort()
tam = len(lista)
for i in range(tam-1):
    if(lista[i+1]-lista[i]<dato):
        dato = lista[i+1]-lista[i]       

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(f"{dato}")
