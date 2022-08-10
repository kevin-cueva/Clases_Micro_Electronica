
def fahrenheit_a_celsius()->float:
    """
    Con la Letra F 
    """
    data = float(input("Ingrese los Grados Fahrenheit °F :"))
    res = (5/9)*(data-32)
    return res

def celsius_a_fahrenheit()->float:
    """
    Con la Letra C 
    """
    data = float(input("Ingrese los Grados Celcios °C :"))
    res = (9/5)*data+32
    return res
letra = input("""\nC: Para convertir de Celsius(°C) a Fahrenheit (°F)\n
F: Para convertir Fahrenheit (°F) a Celsius(°C)\nElección: """)

letra = letra.upper()

if(letra == 'C' or letra == 'F'):
    if(letra == 'F'):
        print(f"En Grados Celcios: {round(fahrenheit_a_celsius(),2)}°C")
    elif(letra == 'C'):
        print(f"En Grados Fahrenheit: {round(celsius_a_fahrenheit(),2)}°")
else:
    print("La eleccion no corresponde a los parametros establecidos")