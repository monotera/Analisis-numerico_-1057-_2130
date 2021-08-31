"""
@Author=Monotera
"""

import numpy as np

"""
 2x + y   =  7
-5x + 11y = -1
"""


"""
Fucnion de python: 
    
Pre-condiciones
la matriz de coeficientes debe ser cuadrada y de rango completo, es decir, 
todas las filas (o, de manera equivalente, las columnas) deben ser linealmente .
independientes; si no es cierto, use lstsq para la mejor “solución” de mínimos 
cuadrados del sistema / ecuación.
"""
def python_solution():
    a = np.array([[2,1],[-5,11]]) 
    b = np.array([7,-1])
    
    x = np.linalg.solve(a,b);
    
    #np.dot = producto de dos array
    print(x)
    print(np.allclose(np.dot(a,x),b));
    
"""
Permite resolver para una sola incognita
"""
def cramer_solution():
    A = np.array([[2,1],[-5,11]]) 
    b = np.array([7,-1]) 
    D = np.linalg.det(A)
    N = len(b)
    x = np.zeros(N)
    
    for i in range(0,N):
        Ai = A.copy()
        Ai.T[i] = b
        Di = np.linalg.det(Ai)
        x[i] = Di/D

    print("Solucion: ", x)
    print("Numero de iteraciones: ", N)
    
    
def gauss_jordan_solution():
# Método de Gauss-Jordan
# Solución a Sistemas de Ecuaciones
# de la forma A.X=B

# INGRESO
    A = np.array([[2,1],[-5,11]]) 

    B = np.array([[7.0],[-1.0]])

# Evitar truncamiento en operaciones
    A = np.array(A,dtype=float) 

# Matriz aumentada
    AB = np.concatenate((A,B),axis=1)
    AB0 = np.copy(AB)

# Pivoteo parcial por filas
    tamano = np.shape(AB)
    n = tamano[0]
    m = tamano[1]

    # Para cada fila en AB
    for i in range(0,n-1,1):
        # columna desde diagonal i en adelante
        columna = abs(AB[i:,i])
        dondemax = np.argmax(columna)
    
    # dondemax no está en diagonal
        if (dondemax !=0):
            # intercambia filas
            temporal = np.copy(AB[i,:])
            AB[i,:] = AB[dondemax+i,:]
            AB[dondemax+i,:] = temporal
        
    AB1 = np.copy(AB)
    

# eliminacion hacia adelante
    for i in range(0,n-1,1):
        pivote = AB[i,i]
        adelante = i + 1
        for k in range(adelante,n,1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
    AB2 = np.copy(AB)

# elimina hacia atras
    ultfila = n-1
    ultcolumna = m-1
    for i in range(ultfila,0-1,-1):
        pivote = AB[i,i]
        atras = i-1 
        for k in range(atras,0-1,-1):
            factor = AB[k,i]/pivote
            AB[k,:] = AB[k,:] - AB[i,:]*factor
            # diagonal a unos
        AB[i,:] = AB[i,:]/AB[i,i]
    X = np.copy(AB[:,ultcolumna])
    X = np.transpose([X])


# SALIDA
    print('Matriz aumentada:')
    print(AB0)
    print('Pivoteo parcial por filas')
    print(AB1)
    print('eliminacion hacia adelante')
    print(AB2)
    print('eliminación hacia atrás')
    print(AB)
    print('solución de X: ')
    print(X)


    

python_solution()
cramer_solution()
gauss_jordan_solution()


