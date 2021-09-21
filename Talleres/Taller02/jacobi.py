# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 08:56:07 2021

@author: Diana Sofía Carrillo
"""
from numpy import *

def jacobi(a, b, x):
    n = len(x)
    t = x.copy()
    for i in range(n):
        s = 0
        for j in range(n):
            if i != j:
                s = s + a[i][j]*t[j]
        x[i] = (b[i] - s)/a[i][i]
    return x

def jacobiiteraciones(a, b, x, e, m):
    n = len(x)
    t = x.copy()
    for k in range(m):
        x = jacobi(a, b, x)
        d = linalg.norm(array(x)-array(t), inf)
        if d < e:
            return [x, k]
        else:
            t= x.copy()
    return [[], m]

a = [[5, 2, 0],[0, -13, 5],[1, 1, 7]]
b = [45.34, -44.66, 16.2]
x = [1, 1, 1]
e = 10E-6
m = 20 #Num máximo de iteraciones
[x, k]=jacobiiteraciones(a, b, x, e, m)
print("Solución:", x)
print("Iteraciones:", k)

def error_relativo(v_obtenido, a, b):
    v_real = linalg.solve(a, b)
    rta = linalg.norm(v_obtenido - v_real) / linalg.norm(v_real)
    return rta

print ("Error relativo:", error_relativo(x, a, b))