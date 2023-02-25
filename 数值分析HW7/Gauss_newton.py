# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 16:51:24 2020

@author: duola
"""

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
    return [[400*x1**2+1,-200*x1],[-200*x1,101]]

def Newton_method(x,y):
    n=0
    x1,x2=x,y
    X=[]
    X.append((x1,x2))
    grad=gradient(x1,x2)
    H=[]
    hessi=np.mat(hessian(x1,x2)).I.tolist()
    c=math.sqrt(grad[0]**2+grad[1]**2)
    while c>10**(-3):
        H.append(hessi)
        x1-=(hessi[0][0]*grad[0]+hessi[0][1]*grad[1])
        x2-=(hessi[1][0]*grad[0]+hessi[1][1]*grad[1])
        X.append((x1,x2))
        grad=gradient(x1,x2)
        c=math.sqrt(grad[0]**2+grad[1]**2)
        hessi=np.mat(hessian(x1,x2)).I.tolist()
        n+=1
    return X,n,H
X,n,H=Newton_method(-1,-1)
Z=[(-1, -1), (-0.9901713894525808, 0.9706364147575852), (-0.41845495959900203, -0.150252596981703), (-0.39503621074968104, 0.1539655148572266), (0.3502329348954381, -0.4284782086783501), (0.3552877727595019, 0.12495430701641136), (0.6720539454679152, 0.3478373242046091), (0.6604578301678583, 0.43175255003958746), (0.5966252948900571, 0.3484031187551048), (0.5922464842427587, 0.3472640832823994), (0.5910802198735299, 0.34591531302293216)]
x=[]
y=[]
x1=[]
y1=[]
z=[]
print(H)
for i in range(n):
    x.append(X[i][0])
    y.append(X[i][1])
    z.append(i)
for i in range(len(Z)):
    x1.append(Z[i][0])
    y1.append(Z[i][1])
plt.plot(x,y)
plt.plot(x1,y1)
plt.show()