"""
Created on Fri Jul 23 18:02:49 2021

@author: Nelson Mosquera (Monotera)
"""

# Problema 1
import math
import numpy as np


def sqrt(n, E, x):
    if(x <= 0 or n < 0):
        raise ValueError("El valor de n y/o x no puede ser negativo")
    elif n == 0:
        return 0
    y = np.longdouble(1/2*(x + (n/x)))
    while abs(x-y) > E:
        x = y
        y = np.longdouble(1/2*(x + (n/x)))
        print(round(y, int(str(E).split('-')[1])))
    return round(y, int(str(E).split('-')[1]))


print("Raiz cuadrarda de 7 con una tolerancia de 10^-8 ", sqrt(7, 10**-8, 1))
print("Raiz cuadrarda de 7 con una tolerancia de 10^-16 ", sqrt(7, 10**-16, 1))
print("Raiz cuadrarda de 7 utilizando funcion de python sqrt ",  math.sqrt(7))
