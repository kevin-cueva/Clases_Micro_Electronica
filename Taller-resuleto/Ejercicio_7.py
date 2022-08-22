import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.
result = 0
n = int(input())  # the number of temperatures to analyse
tem = []
ban1 =0
ban2 =0
lista_positiva = []
lista_negativa = []
ban_n = 0
ban_p = 0
menor_positivo = 0
menor_negativo = 0

for i in input().split():
    # t: a temperature expressed as an integer ranging from -273 to 5526
    t = int(i)
    tem.append(t)

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)

for i in tem:
  if(i<0):
    lista_negativa.append(i)
    ban_n = 1
  else:
    lista_positiva.append(i)
    ban_p = 1
    
if(lista_positiva):
  menor_positivo = min(lista_positiva)
if(lista_negativa):
  menor_negativo = max(lista_negativa) #Aqui es el mayor de los negativos


if(menor_negativo<0 and menor_negativo>=-273 and n>0 and menor_positivo>0 and menor_positivo<=5526 and ban_n==1 and ban_p ==1):
  #Primer caso
  if(menor_negativo*-1 < menor_positivo and n>0):
    result = menor_negativo
  #Segundo caso
  elif(menor_negativo*-1 == menor_positivo and n>0):
    result = menor_positivo
  
  #Tercer caso
  elif(menor_negativo*-1 > menor_positivo and n>0):
    result = menor_positivo
  
elif(n<=0 and ban_p==0 and ban_n ==0):
        result = 0
elif(menor_negativo <= -274 or menor_positivo>5526):
  result = 0
elif(ban_n==1 and ban_p == 0 and menor_negativo > -274 ):
  result = menor_negativo
elif(ban_p==1 and ban_n == 0 and menor_positivo<5527 ):
  result = menor_positivo

print(result)
