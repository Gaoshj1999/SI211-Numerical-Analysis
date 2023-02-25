# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 19:06:18 2020

@author: duola
"""

import math
from sympy import *
import matplotlib.pyplot as plt
import numpy as np
quotient=[[],[],[],[],[],[],[],[],[],[]]
x=[]
y=[]
for i in range(11):
    y.append(1.0/(1+(i-5)**2))
for i in range(11):
    x.append(i-5)
for i in range(10):
    for j in range(11):
        quotient[i].append(0)
i=0
while i < 10:
    j = 10
    while j > i:
        if i == 0:
            quotient[i][j]=((y[j]-y[j-1])/(x[j]-x[j-1]))
        else:
            quotient[i][j] = (quotient[i-1][j]-quotient[i-1][j-1])/(x[j]-x[j-1-i])
        j -= 1
    i += 1
x=symbols("x")  # 符号x，自变量
fx=y[0]+quotient[0][1]*(x+5)+quotient[1][2]*(x+5)*(x+4)+quotient[2][3]*(x+5)*(x+4)*(x+3)+quotient[3][4]*(x+5)*(x+4)*(x+3)*(x+2)+quotient[4][5]*(x+5)*(x+4)*(x+3)*(x+2)*(x+1)+quotient[5][6]*(x+5)*(x+4)*(x+3)*(x+2)*(x+1)*x+quotient[6][7]*(x+5)*(x+4)*(x+3)*(x+2)*(x+1)*x*(x-1)+quotient[7][8]*(x+5)*(x+4)*(x+3)*(x+2)*(x+1)*x*(x-1)*(x-2)+quotient[8][9]*(x+5)*(x+4)*(x+3)*(x+2)*(x+1)*x*(x-1)*(x-2)*(x-3)+quotient[9][10]*(x+5)*(x+4)*(x+3)*(x+2)*(x+1)*x*(x-1)*(x-2)*(x-3)*(x-4)
y1=fx.evalf(subs={x:5})
a = np.linspace(-5, 5, 1000)
b = [fx.evalf(subs={x:t}) for t in a]
c = [1.0/(1+t*t) for t in a]
plt.plot(a, c)
plt.plot(a, b)
plt.show()

