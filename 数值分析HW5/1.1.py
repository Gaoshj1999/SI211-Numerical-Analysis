# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:22:54 2020

@author: duola
"""
import math
from sympy import *
import matplotlib.pyplot as plt
x = symbols('x')
true=integrate(math.e**x, (x, 0, 4))
#print(true)
result=[]
length=4
N=[]
for i in range(100):
    N.append(i+1)
    sum=0
    interval=length/(i+1)
    #print("interval:",interval)
    a=0
    b=-interval/2
    sum+=interval/6*(math.e**0+math.e**4)
    if i>0:
        for j in range(i):
            a+=interval
            #print("a:",a)
            sum+=interval/6*2*math.e**a
    for j in range(i+1):
        b+=interval
        #print("b:",b)
        sum+=interval/6*4*math.e**b
    result.append(true-sum)
#print(result)
plt.plot(N,result)
plt.show()