"""
https://www.codingame.com/training/easy/substitution-encoding

Desea codificar y decodificar mensajes fácilmente con un método simple y personalizado.
 Para ello, utilizará un método de sustitución.

El principio es simple, tienes una tabla de comparación como esta:

A B
C D

y un mensaje para codificar escrito con los caracteres disponibles en tu tabla:

CBA

Vas a tomar cada uno de los caracteres que componen el mensaje y reemplazarlos 
por su posición en la tabla:

C => 10 (row 1 column 0)
B => 01 (row 0 column 1)
A => 00 (row 0 column 0)

The message becomes: 100100
"""


import sys
import math


# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def codificacion(lista:list, message:str)->str:
    cadena = ''
    for letra in message:
        for posicion,valor in enumerate(lista):
            for i,k in enumerate(valor):
                if(letra==k):
                    cadena = cadena+str(posicion)+str(i)
    return cadena
cadena =''
lista=[]
lista_row = []
rows = int(input())
for i in range(rows):
    row = input()
    lista_row = row.split(' ')
    lista.append(lista_row)
message = input()

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

print(codificacion(lista,message))


