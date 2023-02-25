# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 16:26:19 2020

@author: duola
"""

from numpy import *
n=[[1,math.sin(0),math.cos(0)],[1,math.sin(0.5),math.cos(0.5)],[1,math.sin(1),math.cos(1)]]
N=mat(n)
NI=N.I
n1=[1-0,math.cos(0)-math.cos(1),math.sin(1)-math.sin(0)]
N1=mat(n1)
fx=[0,0.5**3,1]
FX=mat(fx)
FXT=FX.T
matrix=N1*NI*FXT
mlist=array(matrix)
print(mlist[0][0])