# Bisection Method and it's plotting

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

def function(x):
    return x**3 - x - 2

def bisection(a, b, tolerance):
    
    if function(a)*function(b) > 0:
        print("Root does not exist for this interval.")
    
    else:
        while abs(a-b) >= tolerance:
            c = (a+b)/2
            product = function(a)*function(c)
            
            if function(c) == 0:
                print("Root is: ",c)
                
            elif product > tolerance:
                a = c

            elif product < tolerance:
                b = c

        return c

a = float(input("Enter the value of a: "))
b = float(input("Enter the value of b: "))
tolerance = float(input("What should be the tolerance: "))

print("Bisection method gives root at x =", bisection(a,b,tolerance))

x = np.linspace(a,b, 100)
plt.plot(x,function(x))
plt.grid()
plt.show()
            
