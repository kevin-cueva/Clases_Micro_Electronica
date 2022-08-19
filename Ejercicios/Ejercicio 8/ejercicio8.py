#Ejercicio #8 de la diapositiva 2   
with open('matriz.txt','w') as f:
    
    for i in range(1, 11): #1 al 10
        for j in range(1,11):
            if(i<10 and j<10):
                f.write(f"|{i}   {j} | {i*j}\n")
                continue
            elif(i>9 and j<10 or j>9 and i<10):
                f.write(f"|{i}   {j}| {i*j}\n")
                continue
            else:
                f.write(f"|{i}  {j}| {i*j}\n")

          