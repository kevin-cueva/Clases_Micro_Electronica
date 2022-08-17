"""Escriba un programa que le pida al usuario que ingrese el ancho y el
largo de una habitación. Una vez leídos los valores, su programa
debería calcular y mostrar el área de la habitación. La longitud y el
ancho se ingresarán como números de punto flotante. Incluya
unidades en su mensaje de solicitud y salida; pies o metros."""

print("\nEn que formato ingresara los datos")
print("m : metros")
print("p : pies")
eleccion = input("Eleccion: ")
a = float(input("Digite el Ancho: "))
b = float(input("Digite el Largo: "))
if(eleccion == 'm'):
    area = lambda ancho,largo:(ancho*largo)
    print(f"El area : {area(a,b)} m\u00b2")

elif (eleccion == 'p'):
    area = lambda ancho,largo:(ancho*largo*3.281)
    print(f"El area : {area(a,b)} pies\u00b2")


