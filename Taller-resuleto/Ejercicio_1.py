"""
"""
import math
a = float(input("Digite  el numero A: "))
b = float(input("Digite  el numero B: "))

print(f"La suma a+b: {a+b}")
print(f"La diferencia cuando b se resta de a: {b-a}")
print(f"El producto entre a y b: {a*b}")
print(f"El resultado de log 10 (a): {round(math.log10(a),5)}")
print(f"El resultado de a^b: {round(math.pow(a,b),5)}")
print(f"El resultado de e^a: {round(math.pow(math.e,a),5)}")
print(f"El resultado de b√a: {round(a*(1/b),5)}")

