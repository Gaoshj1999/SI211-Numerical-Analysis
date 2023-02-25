# -*- coding: utf-8 -*-
"""
Created on Sat Oct 24 14:51:50 2020

@author: duola
"""
import math
from time import *
import matplotlib.pyplot as plt
begin_time = time()
def function(x):
    a=1
    b=1
    for i in range(len(x)):
        y=b*0.4+math.sin(a)*0.3
        z=x[i]+math.cos(b)*0.3+a*0.1
        a=y
        b=z    
    return [a,b]
row1=[]
row2=[]
matrix=[]
originx=[]
origin=[]
for i in range(2020):
    originx.append(1)
origin=function(originx)
for i in range(len(originx)):
    x=[]
    for j in range(len(originx)):
        h=1*10**-8
        if i==j:
            x.append(1+h)
        else:
            x.append(1)
    temp=function(x)
    row1.append((temp[0]-origin[0])/h)
    row2.append((temp[1]-origin[1])/h)
matrix.append(row1)
matrix.append(row2)
end_time = time()
run_time = end_time-begin_time
print(run_time)
print(matrix)
'''
xp=[]
for i in range(100):
    xp.append(i+1920)
showmatrix1=[]
showmatrix2=[]
for i in range(100):
    showmatrix1.append(matrix[0][1920+i])
for i in range(100):
    showmatrix2.append(matrix[1][1920+i])
showmatrix=[]
showmatrix.append(showmatrix1)
showmatrix.append(showmatrix2)
plt.plot(xp,showmatrix[0])
plt.plot(xp,showmatrix[1])
plt.show()
'''