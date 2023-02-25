# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 15:26:35 2020

@author: duola
"""
from numpy import *
import matplotlib.pyplot as plt
x0=float(input("please enter the start point:"))
h=float(input("please enter h:"))
N=int(input("please enter N:"))
matrix=[]
x=[]
fx=[]
for i in range(N):
    x.append(x0+i*h)
print("please enter fx:")
for i in range(N):
    fx.append(float(input()))
r=[]
for i in range(N-2):
    r.append(3*(fx[i+2]-2*fx[i+1]+fx[i]))
r.insert(0,0)
r.insert(N-1,0)
a=[]
for i in range(N):
    temp=[]
    if i==0:
        for j in range(N):
            if j==0:
                temp.append(1)
            else:
                temp.append(0)
    elif i==N-1:
        for j in range(N):
            if j==N-1:
                temp.append(1)
            else:
                temp.append(0)
    else:
        for j in range(N):
            if j==i-1:
                temp.append(h)
            elif j==i:
                temp.append(4*h)
            elif j==i+1:
                temp.append(h)
            else:
                temp.append(0)
    a.append(temp)
A=mat(a)
A1=A.I
R=mat(r)
C=(A1*(R.T)).tolist()#矩阵形式的向量
c=[]
for i in range(N):
    c.append(C[i][0])
b=[]
for i in range(N-1):
    b.append((fx[i+1]-fx[i])/h-h*(c[i+1]+2*c[i])/3)
d=[]
for i in range(N-1):
    d.append((c[i+1]-c[i])/(3*h))
outputx=[]
outputfx=[]
for i in range(N-1):
    m=linspace(x[i],x[i+1],1000)
    for k in m:
        outputx.append(k)
        n=fx[i]+b[i]*(k-x[i])+c[i]*(k-x[i])**2+d[i]*(k-x[i])**3
        outputfx.append(n)
plt.plot(outputx,outputfx)
plt.show()