import numpy as np 
import matplotlib.pyplot as plt 

def fx(x): 
    return 3*x**2-3*x+4
def der(x):
    return 6*x-3

def der_graph():
    x = np.linspace(-10,10,2001)
    plt.plot(x,fx(x),x,der(x))
    plt.xlim(x[[0,-1]])
    plt.grid
    #plt.show()
    
    local_min= np.random.choice(x,1)
    learning_rate=0.01
    training_epochs=10000
    
    for i in range (training_epochs): 
        grad = der(local_min)
        local_min = local_min - learning_rate*grad
        if abs(grad)<0.01:
            break
    print(local_min)
    
der_graph()    