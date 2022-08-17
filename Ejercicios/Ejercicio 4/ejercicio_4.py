
print("\nDigite los valores de ancho y largo en metros Para hallar el Area")
a = float(input("Digite el Ancho: "))
b = float(input("Digite el Largo: "))

area_metro = lambda ancho,largo:(ancho*largo)
area_pie = lambda ancho,largo:(ancho*largo*3.281)
print(f"El area :{area_metro(a,b)} m\u00b2 - {area_pie(a,b)} pies\u00b2")

