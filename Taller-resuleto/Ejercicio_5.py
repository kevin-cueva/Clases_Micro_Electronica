"""Escriba un programa que solicite el mes, representado por enteros positivos desde
1 hasta 12 y el año, representado por una cifra positiva de cuatro números. El
programa debe imprimir el nombre del mes y la cantidad de dı́as que este posee,
debe tener en cuenta si un año es bisiesto o no para mostrar los dı́as correctos del
mes de febrero."""

import math
def bisiesto(a:int)->bool:
    if(math.fmod(a,4)==0 and a%100!=0 and a%400!=0):
        return True
    return False

meses = ['Enero','Febrero','Marzo','Abrir','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Nobiembre','Diciembre']
dias_meses = [31,28,31,30,31,30,31,31,30,31,30,31]
mes = int(input("Ingrese el numero del mes ej: marzo ->3: "))
year = int(input("Ingrese el año: "))

if(bisiesto(year)==True):
    dias_meses[1] = 29
print(f"Mes: {meses[mes-1]} - Dias: {dias_meses[mes-1]}")

    
