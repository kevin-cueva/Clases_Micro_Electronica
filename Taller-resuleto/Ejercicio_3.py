""""Un triángulo se puede clasificar en: equilátero, isósceles o escaleno. Escriba un pro-
grama que solicite los valores de los ángulos de un triángulo y muestre un mensaje
en donde indique qué tipo de triángulo es."""

a = float(input("Introduzca el lado a: "))
b = float(input("Introduzca el lado b: "))
c = float(input("Introduzca el lado c: "))

lista = [a,b,c]
set = set(lista) # Este  tipo de dato no permite valores repetidos
#Triángulo equilátero: tiene los tres lados iguales.
if(len(set)==1):
    print("Triangulo equilatero")

#Triángulo isósceles: tiene dos lados iguales.
if(len(set) == 2):
    print("Triangulo Isósceles")

#Triángulo escaleno: tiene los tres lados distintos.
if(len(set)==3):
    print("Triangulo Escaleno")


