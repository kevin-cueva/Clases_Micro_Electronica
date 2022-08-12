from ast import Delete


lista = []
print("\n\nIngrese Los numeros que desea almacenar en la lista\npara salir presione el 0\n")
while(True):
    try:
        num = float(input("#: "))
    except:
        num ="error"
    if(num == 0):
        break
    elif(type(num)==float):
        lista.append(num)
    else:
        input("Lo ingresado no corresponde a un numero...")

if(lista):
    print(lista)
else:
    print("No hay ningun valor guardado")
    del lista
        