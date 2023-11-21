import numpy as np 
import matplotlib.pyplot as plt 
from math import *
import sympy

def fx(x): 
    return np.cos(2*np.pi*x)+x**2
def der(x):
    return -2*np.pi*np.sin(2*np.pi*x)+2*x
     
def der_graph():
    x = np.linspace(-2,2,2001)
    plt.plot(x,fx(x),x,der(x))
    plt.xlim(x[[0,-1]])
    plt.grid()
    plt.show()
    
    local_min= -0.001
    learning_rate=0.01
    training_epochs=100
    
    for i in range (training_epochs): 
        grad = der(local_min)
        local_min = local_min - learning_rate*grad
        if abs(grad)<0.01:
            break
    print(local_min)
    
der_graph()   