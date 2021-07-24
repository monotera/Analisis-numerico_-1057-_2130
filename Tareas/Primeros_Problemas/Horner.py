"""
Created on Fri Jul 23 18:02:49 2021

@author: Nelson Mosquera (Monotera)
"""

#Valor de x
valorX=4;
#Coeficientes del polinomio
coeficientes=[1,-2,4/3,-8/27]

def horner (coeficientes, valorX):
    resultado = coeficientes[0]
    cont = 0
    #Recorrer los coeficientes
    for i in range(1,len(coeficientes)):
    	#Multiplicar al valor parcial el valor de x más el coeficiente
        resultado= resultado * valorX + coeficientes[i]
        cont += 1
    return resultado, cont	

resultado, cont = horner(coeficientes, valorX)


print("Resultado:"+str(resultado))

#Se llega a la conclucion de que el numero de operaciones es igual al grado 
print("Numero de multiplicaciones:"+str(cont))
print("Numero de diviciones:"+str(cont))