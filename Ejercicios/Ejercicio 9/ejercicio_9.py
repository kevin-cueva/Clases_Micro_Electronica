"""Escriba una función que solicite tres números como parámetros y
devuelva el valor mediano de los tres.
Nota: El valor mediano es el medio de los tres valores cuando se
ordenan en orden ascendente."""

def mediano(a:float,b:float,c:float)->float:
    lista = []
    lista.append(a)
    lista.append(b)
    lista.append(c)
    lista.sort()
    return lista[1]

print("\nAcontinuacion digite tres numeros para buscar el mediano")
try:
    a = float(input("#: "))
    b= float(input("#: "))
    c = float(input("#: "))
    print(f'mediano:{mediano(a,b,c)}')
except:
    print("Error de digitacion")
