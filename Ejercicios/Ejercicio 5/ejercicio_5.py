"""Cree un programa que lea la longitud y el ancho del campo de un
agricultor del usuario en pies. Mostrar el área del campo en acres.
43.560 pies cuadrados en un acre."""

print("\nIngrese el ancho y largo del Campo en pies")
a = float(input("Ancho: "))
l = float(input("Largo: "))

acres = lambda ancho,largo:((ancho*largo)/43560)
print(f"Area en Acres: {round(acres(a,l),4)} acres\u00b2")
