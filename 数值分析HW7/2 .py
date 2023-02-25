# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 18:03:19 2020

@author: duola
"""

from sympy import *
import numpy as np
import matplotlib.pyplot as plt
import mpl_toolkits.axisartist as axisartist\
    
def function(x):
    return x**3-2*x+2

def gradient(x):
    return 3*x**2-2
   
def Newton_method(x):
    n=1
    d=[]
    f=function(x)
    X=[]
    grad=gradient(x)
    while f!=0 and n<=100:
        x-=f/grad
        X.append(x)
        d.append(f/grad)
        f=function(x)
        grad=gradient(x)
        n+=1
    return X,d
X,d=Newton_method(0)
n=[]
for i in range(100):
    n.append(i+1)
#plt.plot(n,X)
plt.plot(n,d)
plt.show()