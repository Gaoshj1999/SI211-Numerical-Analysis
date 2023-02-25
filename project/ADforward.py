# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 10:24:37 2020

@author: duola
"""

import math
from sympy import *
from time import *
import matplotlib.pyplot as plt
begin_time = time()
#print(math.log(10,10))
class adv:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __add__(self,other):
        if type(other)==adv:
            return adv(self.a+other.a,self.b+other.b)
        if type(other)==float:
            return adv(self.a+other,self.b)
        if type(other)==int:
            return adv(self.a+other,self.b)
    def __sub__(self,other):
        if type(other)==adv:
            return adv(self.a-other.a,self.b-other.b)
        if type(other)==float:
            return adv(self.a-other,self.b)
        if type(other)==int:
            return adv(self.a-other,self.b)
    def __mul__(self,other):
        if type(other)==adv:
            u=self.a*other.a
            v=other.a*self.b+other.b*self.a
        if type(other)==float:
            u=other*self.a
            v=other*self.b
        if type(other)==int:
            u=other*self.a
            v=other*self.b
        return adv(u,v)
    def __truediv__(self,other):
        if type(other)==adv:
            u=self.a/other.a
            v=(self.b*other.a-self.a*other.b)/(other.a**2)
            return adv(u,v)
        if type(other)==float:
            u=self.a/other
            v=self.b/other
            return adv(u,v)
        if type(other)==int:
            u=self.a/other
            v=self.b/other
            return adv(u,v)   
    def __neg__(self):
        u=-self.a 
        v=-self.b
        return adv(u,v)
    def sin(self):
        u=math.sin(self.a)
        v=math.cos(self.a)*self.b
        return adv(u,v)
    def ln(self):
        u=math.log(self.a)
        v=self.b/self.a
        return adv(u,v)
    def cos(self):
        u=math.cos(self.a)
        v=-math.sin(self.a)*self.b
        return adv(u,v)
    def __str__(self):
        return '('+str(self.a)+' ,'+str(self.b)+')'
def sin(x):
    return x.sin()
def cos(x):
    return x.cos()
def ln(x):
    return x.ln()      
def diff(x,d):
    temp=[]
    for i in range(len(x)):
        temp.append(adv(x[i],d[i]))
    return temp
def function(x):
    a=adv(1,0)
    b=adv(1,0)
    for i in range(len(x)):
        y=b*0.4+sin(a)*0.3
        z=x[i]+cos(b)*0.3+a*0.1
        a=y
        b=z    
    return [a,b]
'''
example for other function:
    def function(x):  
    return [x[0]*x[0]+x[1]*x[1]]
with
d=[[1,0],[0,1]]
x=[2,5]
'''
def getdiff(x):
    temp=[]
    for i in range(len(x)):
        temp.append(x[i].b)
    return temp
def g(x,d):
    matrix=[]
    for i in range(len(x)):
        y=diff(x,d[i])
        answer=getdiff(function(y))
        if len(matrix)==0:
            for i in range(len(answer)):
                matrix.append([])
        for j in range(len(answer)):
            matrix[j].append(answer[j])
    return matrix
d=[]
for i in range(2020):
    temp=[]
    for j in range(2020):
        if i==j:
            temp.append(1)
        else:
            temp.append(0)
    d.append(temp)
x=[]
for i in range(2020):
    x.append(1)
result=g(x,d)
end_time = time()
run_time = end_time-begin_time
print(run_time)
print(result)
'''
xp=[]
for i in range(100):
    xp.append(i+1920)
showmatrix1=[]
showmatrix2=[]
for i in range(100):
    showmatrix1.append(result[0][1920+i])
for i in range(100):
    showmatrix2.append(result[1][1920+i])
showmatrix=[]
showmatrix.append(showmatrix1)
showmatrix.append(showmatrix2)
plt.plot(xp,showmatrix[0])
plt.plot(xp,showmatrix[1])
plt.show()
'''