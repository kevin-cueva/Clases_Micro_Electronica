#https://trinket.io/embed/python3/a5bd54189b
import numpy as np
M = int(input("Numero de filas: "))
N = int(input("Numero de columnas "))

#Matriz 1
m1 = [[np.random.randint(1,10) for j in range(M)] for i in range(N)]
m_np1 = np.array(m1) 

#Matriz 2
m2 = [[np.random.randint(1,10) for j in range(M)] for i in range(N)]
m_np2 = np.array(m2) 

size_matris = m_np1.shape #Filas y columnas de la matriz
print("\nMatriz 1:")
print(m_np1)
print("\nMatriz 2:")
print(m_np2)
print("\nSuma de M1 + M2")
suma = m_np1 + m_np2
print(suma)
print("\nMultiplicacion")
multi=m_np1 * m_np2
print(multi)
print("\nDeterminante M1")
print(np.linalg.det(m_np1))
print("\nDeterminante M2")
print(np.linalg.det(m_np2))
print("\nInversa de la Matriz 1:")
print(np.linalg.inv(m_np1))
print("\nInversa de la Matriz 2:")
print(np.linalg.inv(m_np2))

