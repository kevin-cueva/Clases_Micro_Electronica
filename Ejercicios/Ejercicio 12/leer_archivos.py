from crear_archivos import Crear_archivo

p = Crear_archivo()
p.archivo()

numeros_pares = set()
try:
    with open ('primero.txt', 'r') as f:
        lista = list(f.read().split(','))
        for i in lista:
            numeros_pares.add(int(i))
        del lista
                
    with open ('segundo.txt', 'r') as f:
        lista = list(f.read().split(','))
        for i in lista:
            numeros_pares.add(int(i))
        del lista
except:
    print("Ocurrioun error\n")


lista = list([x for x in numeros_pares if x %2 == 0 ])
lista.sort(reverse=True)
print(lista)
del numeros_pares

with open ('organizados.txt','w') as f:
            for i in lista:   
                f.write(f'{str(i)},')
                    

