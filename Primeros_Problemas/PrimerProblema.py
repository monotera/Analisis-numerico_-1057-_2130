# Problema 1
import math

def sqrt(n, E, x):
    if(x < 0 or n < 0):
        raise ValueError("El valor de n y/o x no puede ser negativo")
    elif n == 0:
        return 0
    y = 1/2*(x + (n/x))
    while abs(x-y) > E:
        x = y
        y = 1/2*(x + (n/x))
    return y


print("Raiz cuadrarda de 7 con una tolerancia de 10^-8 ", sqrt(7, pow(10, -8), 2))
print("Raiz cuadrarda de 7 con una tolerancia de 10^-16 ", sqrt(7, pow(10, -16), 2))
print("Raiz cuadrarda de 7 utilizando funcion de python sqrt ",  math.sqrt(7))
