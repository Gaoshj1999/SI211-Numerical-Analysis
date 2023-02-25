# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 20:13:09 2020

@author: duola
"""

import math
from sympy import *
import matplotlib.pyplot as plt
r=[]
N=[]
for i in range(100):
    N.append(i+1)
    sum=0
    for j in range(i+1):
        sum+=16/(45*((i+1)**5))*(math.e**(4*(j+1)/(i+1)))
    r.append(sum)
plt.plot(N,r)
plt.show()