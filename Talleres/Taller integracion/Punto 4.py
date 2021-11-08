# -*- coding: utf-8 -*-
"""
Created on Sun Nov  7 17:47:17 2021

@author: Usuario
"""
from pylab import*
import numpy as np

def euler(f, g, x, y, z, h, m):
    u = []
    v = []
    w = []
    
    for i in range(m):
        k1y=h*f(x, y, z)
        k1z=h*g(x, y, z)
        k2y=h*f(x+h,y+k1y,z+k1z)
        k2z=h*g(x+h,y+k1y,z+k1z)
        y=y+0.5*(k1y+k2y)
        z=z+0.5*(k1z+k2z)
        x=x+h
        u=u+[x]
        v=v+[y]
        w=w+[z]
    return [u, v, w]

def f(x, y, z): return 0.4*y-0.018*y*z
def g(x, y, z): return -0.8*z+0.023*y*z
[u,v,w] = euler(f,g,-1,30,4,1,22) #inicialmente x debería de ser igual a 0, pero lo cambiamos a -1 para indicar que el experimento inicio en año anterior al 0.

#datos reales
anio = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 20, 21]
linces = [4, 6.1, 9.8, 35.2, 59.4, 41.7, 19, 13, 8.3, 9.1, 7.4, 8, 12.3, 19.5, 45.7, 51.1, 29.7, 15.8, 9.7, 10.1, 8.6]
conejos = [30, 47.2, 70.2, 77.4, 36.3, 20.6, 18.1, 21.4, 22, 25.4, 27.1, 40.3, 57, 76.6, 52.3, 19.5, 11.2, 7.6, 14.6, 16.2, 24.7]

#graficar
plot(anio, linces, color = 'pink', label = "Datos Linces")
plot(anio, conejos, color = 'mediumpurple', label = "Datos Conejos")
plot(u,w,'*k', color = 'pink', label = "Aproximación Linces")
plot(u,v,'sk', color = 'mediumpurple', label = "Aproximación Conejos")
legend(bbox_to_anchor = (1.05, 0.6))
xlabel("Año (1900-1921)")
ylabel("Índice de Capturas")
grid(True)
show()


#error
def relative_error(y_true, y_pred):
    relative_error = []
    for i in range (size(y_true)):
        relative_error += [np.abs(y_true[i] - y_pred[i]) / y_true[i]]
    return relative_error

errorConejos = relative_error(conejos, v)
errorLinces = relative_error(linces, w)


np.set_printoptions(4)
print("El error promedio de la aproximación hacia la cacería de conejos es: ", np.average(errorConejos))
print("\nEl error máximo de la aproximación hacia la cacería de conejos es: ", max(errorConejos), " en el año: ", u[np.argmax(errorConejos)]+1900)
print("\nEl error promedio de la aproximación hacia la cacería de linces es: ", np.average(errorLinces))
print("\nEl error máximo de la aproximación hacia la cacería de linces es: ", max(errorLinces), " en el año: ", u[np.argmax(errorLinces)]+1900)


