
#Funciones
def fun1(n:float)->float:
    return n*n
def fun2(n:float)->float:
    return fun1(n)+1000*n
def fun3(n:float)->float:

    if(n<=0):
        return 10
    elif(n>1 and n<5):
        return fun1(n)-n+1
    elif(n>=5):
        return 2*n-1
    else:
        return None;

num = "0"
try:
    num = float(input("Introduzca un numero decimal: "))
except:
    nun = "0"
if(type(num)==float):
    elegir = int(input("""
    ELiga\n1: f(n) = n^2\n2:f(n) = n^2+1000n\n3:f(n)=10 si n<=0, n^2-n+1 si 1<n<5, 2n-1 si n>=5\n Opcion: """
    ))

    if (elegir == 1):
        print(f"El numero es {num} y el resultado: {fun1(num)}")
    elif(elegir == 2):
        print(f"El numero es {num} y el resultado: {fun2(num)}")
    elif(elegir == 3):
        print(f"El numero es {num} y el resultado: {fun3(num)}")
    else:
        print("El dato elegida no coincide con las opciones sugeridas ...")
else:
    print("El dato de entrada no coincide con el tipo requerido...")