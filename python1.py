import numpy as np
import matplotlib.pyplot as plt

def python1(n):
    
	if n <= 9:
        
		return (n**2)-7
    
	elif n>=10:
        
		return ((n**2)-7)-10  

ya = np.vectorize(python1)

x = np.arange(0,100)
y = ya(x)
    
plt.stem(x,y)