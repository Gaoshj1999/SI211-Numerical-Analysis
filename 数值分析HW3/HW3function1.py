# -*- coding: utf-8 -*-
"""
Created on Sun Oct 18 16:17:15 2020

@author: duola
"""
import math
from sympy import *
import matplotlib.pyplot as plt
from numpy import *
#HW3function
h=1
N=11
matrix=[]
x=[]
fx=[]
for i in range(N):
    x.append(i-5)
for i in range(N):
    fx.append(1.0/(1+(i-5)**2))
r=[]
for i in range(N-2):
    r.append(3*(fx[i+2]-2*fx[i+1]+fx[i])/h)
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
#HW2function
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
a = linspace(-5, 5, 1000)
b = [fx.evalf(subs={x:t}) for t in a]
c = [1.0/(1+t*t) for t in a]
plt.plot(outputx,outputfx)
plt.plot(a, b)
plt.show()