
"""
La mayoría de los números de tarjetas de pago tienen 16 dígitos. Los 6 dígitos más a la izquierda
 representan un número de identificación único para el banco que emitió la tarjeta. 
 Los siguientes 2 dígitos determinan el tipo de tarjeta (por ejemplo, débito, crédito, regalo). 
 Los dígitos del 9 al 15 son el número de serie de la tarjeta, y el último dígito se usa como dígito 
de control para verificar si el número de la tarjeta es válido. Por lo tanto, si alguien ingresa
el número de la tarjeta incorrectamente, existe una alta probabilidad de que un software de pago 
pueda determinarlo fácilmente.
La mayoría de las tarjetas utilizan un algoritmo inventado por Hans Peter Luhn, un buen compañero de IBM.
De acuerdo con el algoritmo de Luhn, puede determinar si un número de tarjeta de crédito
es (sintácticamente) válido de la siguiente manera:

1.Dobla cada segundo dígito de derecha a izquierda. Si esta "duplicación" 
da como resultado un número de dos dígitos, réstale 9 y obtendrás un solo dígito.
2.Ahora agregue todos los números de un solo dígito del paso 1.
3.Agregue todos los dígitos en los lugares impares de derecha a izquierda en el número
de tarjeta de crédito.
4. Sume los resultados de los pasos 2 y 3.
5.Si el resultado del paso 4 es divisible por 10, el número de tarjeta es válido; 
de lo contrario, no es válido.
por ejemplo:
"""


"""
2
4556 7375 8689 9855
4024 0071 0902 2143
"""
import sys
import math
import re
# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
def funcion_paso1(a:list)->list:
    lista = []
    for i in a:
        value = i-9
        if(value<0):
            value = value+9
        lista.append(value)
    return lista
def es_valido(paso1:list, paso2:list)->str:
    a = (sum(paso1)+sum(paso2))%10
    if(a==0):
        return 'YES'
    return 'NO'
datos = []
n = int(input())
for i in range(n):
    card = input()
    datos.append(card)
for i in datos:
    card = re.sub(" ","",i)
    tarj = list(card)
    tarjeta = [int(x) for x in tarj]
    rev = list(reversed(tarjeta))
    var = [(y*2) for x,y in enumerate(rev) if x%2!=0]
    paso1 = funcion_paso1(var)
    paso2 = [y for x,y in enumerate(rev) if (x+1)%2!=0]
    print(es_valido(paso1,paso2))
    

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


