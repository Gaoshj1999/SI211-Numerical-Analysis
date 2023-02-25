# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:12:40 2020

@author: duola
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 17:07:20 2020

@author: duola
"""


from sympy import *
import numpy as np
import math
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist\
    
def function(x1,x2):
    return 0.5*(x1-1)**2+50*(x2-x1**2)**2+0.5*x2**2

def gradient(x1,x2):
    return 200*x1**3-200*x1*x2+x1-1,-100*x1**2+101*x2

def hessian(x1,x2):
    return [[600*x1**2-200*x2+1,-200*x1],[-200*x1,101]]

def Newton_method(x,y):
    n=0
    x1,x2=x,y
    X=[]
    X.append((x1,x2))
    grad=gradient(x1,x2)
    hessi=np.mat(hessian(x1,x2)).I.tolist()
    c=math.sqrt(grad[0]**2+grad[1]**2)
    while c>10**(-3):
        x1-=(hessi[0][0]*grad[0]+hessi[0][1]*grad[1])
        x2-=(hessi[1][0]*grad[0]+hessi[1][1]*grad[1])
        X.append((x1,x2))
        grad=gradient(x1,x2)
        c=math.sqrt(grad[0]**2+grad[1]**2)
        hessi=np.mat(hessian(x1,x2)).I.tolist()
        n+=1
    return X,n
X,n=Newton_method(-1,-1)
x=[]
y=[]
z=[]
for i in range(n):
    x.append(X[i][0])
    y.append(X[i][1])
    z.append(i)
plt.plot(x,y)
plt.show()