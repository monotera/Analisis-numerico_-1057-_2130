"""
Septiembre 20 de 2021
Punto 9. Taller 2 Analisis Numérico.
@author: Diana Sofía Carrillo
La función gradienteConjugado() fue hecha basándose en los siguientes códigos:
    https://sophiamyang.medium.com/descent-method-steepest-descent-and-conjugate-gradient-in-python-85aa4c4aac7b
    https://gist.github.com/sfujiwara/b135e0981d703986b6c2

"""

import numpy as np
from scipy.sparse.linalg import cg
import time


def gradienteConjugado(A, b, x=None):
    n = len(b)
    if not x:
        x = np.ones(n) #Vector inicial inicializado en unos
    r = np.dot(A, x) - b
    p = - r
    r_k_norm = np.dot(r, r)
    for i in range(2*n):
        Ap = np.dot(A, p)
        alpha = r_k_norm / np.dot(p, Ap)
        x += alpha * p
        r += alpha * Ap
        r_kplus1_norm = np.dot(r, r)
        beta = r_kplus1_norm / r_k_norm
        r_k_norm = r_kplus1_norm
        if r_kplus1_norm < 1e-5:
            print ('Iteraciones:', i)
            break
        p = beta * p - r
    return x

if __name__ == '__main__':
    n = 1000
    P = np.random.normal(size=[n, n])
    A = np.dot(P.T, P) #producto punto entre la transpuesta de P y P, para tener una matriz definida positiva y simetrica.
    b = np.zeros(n) #tambien se puede llenar con unos pero demora más, aunque tiene el beneficio de mostrar un valor diferente a cero en el tiempo de ejecución del tercer método
    
    np.set_printoptions(precision = 10)
    
    t1 = time.time()
    print ('Metodo 1.') #Metodo implementado aquí, no incluye una matriz dispersa
    x = gradienteConjugado(A, b)
    t2 = time.time()
    print ("tiempo: ",t2 - t1)
    print ('\nMetodo 2.') #Metodo de librería que soluciona sistemas de ecuaciones, no usa gradiente conjugado
    x2 = np.linalg.solve(A, b)
    t3 = time.time()
    print ("tiempo: ",t3 - t2)
    print ('\nMetodo 3.') #Metodo de librería que soluciona sistemas de ecuaciones usando gradente conjugado, también usa una matriz dispersa
    x3 = cg(A, b)
    t4 = time.time()
    print ("tiempo: ",t4 - t3)  