# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 22:41:12 2020

@author: duola
"""

from numpy import *
n=[[1,math.sin(0),math.cos(0)],[1,math.sin(0.25),math.cos(0.25)],[1,math.sin(0.5),math.cos(0.5)]]
N=mat(n)
NI=N.I
n1=[0.5-0,math.cos(0)-math.cos(0.5),math.sin(0.5)-math.sin(0)]
N1=mat(n1)
fx=[math.sin(9/10*0),math.sin(9/10*0.25),math.sin(9/10*0.5)]
FX=mat(fx)
FXT=FX.T
matrix=N1*NI*FXT
mlist=array(matrix)
print(mlist[0][0])