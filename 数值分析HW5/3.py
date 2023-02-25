# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 21:37:03 2020

@author: duola
"""

import math
from sympy import *
import matplotlib.pyplot as plt
I=[]
for i in range(1000):
    I.append((1+i*0.01)*math.sin((1+i*0.01)*math.pi/4))
I1=[]
for i in range(1000):
    I1.append(math.pi/8*(math.cos(math.pi/8*(i*0.01+1)*(1-1/math.sqrt(3)))+math.cos(math.pi/8*(i*0.01+1)*(1+1/math.sqrt(3)))))
result=[]
for i in range(1000):
    if I[i]>I1[i]:
        result.append(I[i]-I1[i])
    else:
        result.append(I1[i]-I[i])
#print(result[0])
N=[]
for i in range(1000):
    N.append(1+i*0.01)
plt.plot(N,result)
plt.show()