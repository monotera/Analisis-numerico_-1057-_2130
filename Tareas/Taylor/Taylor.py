import numpy as np
np.seterr(divide='ignore', invalid='ignore') #para ignorar el error de dividir por 0
import matplotlib.pyplot as plt

# Orden
n_terms = 5

# valores de x
x_vals = np.linspace(0,1,100)

# valores de y
y_vals = np.zeros([n_terms,len(x_vals)])

for n in range(n_terms):
    #Para orden 0
    if n == 0:
        y_vals[n,:] = np.ones(len(x_vals))
    else:
        new_term = 1**n * (x_vals**n)
        y_vals[n,:] = y_vals[n-1,:] + new_term

# Graficar los valores de los terminos
for n in range(n_terms):
    #if n == 25:
        label = str(n) + " order"
        plt.plot(x_vals,y_vals[n,:], label=label)

# grafica la funcion real   
plt.plot(x_vals, 1/(1-x_vals), label="$1/(1-x)$")
plt.xlabel("x")
plt.ylabel("y")
plt.ylim([0,25])
plt.legend()