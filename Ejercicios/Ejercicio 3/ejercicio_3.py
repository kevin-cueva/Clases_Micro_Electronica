
def normalizar(lista:list, a, b)->list:
    x_max = max(lista)
    x_min = min(lista)
    if (x_min == x_max):
        return lista
    res = []
    for i in lista:
        data = a+(((i-x_min)*(b-a))/(x_max-x_min))
        res.append(round(data,5))
    
    return res


def funcion(lista):
    x = []
    for i in lista:
        x.append(i*i+i+1)
    return x
    


landa = [k for k in range(1,21) if k <= 20]
x = funcion(landa)

print(normalizar(x,-1,1))
print("\n")
print(normalizar(x,1,10))
print("\n")
print(normalizar(x,0.5,1))

