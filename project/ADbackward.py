# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 20:49:54 2020

@author: duola
"""
import numpy as np
from enum import Enum
from time import *
import matplotlib.pyplot as plt
begin_time = time()
class CGraph:
    def __init__(self):
        self.Nodec = 0
        self.NodeList = []

    def connect(self):
        Node.cgraph = self
        return self

    def append(self, node):
        self.Nodec += 1
        self.NodeList.append(node)

    def compute_gradient(self, seedID):
        for node in self.NodeList:
            node.derivative = 0.0
        self.NodeList[seedID].derivative = 1.0
        for node in self.NodeList[-1::-1]:
            if node.op is Node.operators.add:
                self.NodeList[node.arg1].derivative += node.derivative
                self.NodeList[node.arg2].derivative += node.derivative
            elif node.op is Node.operators.sub:
                self.NodeList[node.arg1].derivative += node.derivative
                self.NodeList[node.arg2].derivative += -node.derivative
            elif node.op is Node.operators.mul:
                self.NodeList[
                    node.arg1].derivative += node.derivative * self.NodeList[
                        node.arg2].value
                self.NodeList[
                    node.arg2].derivative += node.derivative * self.NodeList[
                        node.arg1].value
            elif node.op is Node.operators.truediv:
                self.NodeList[
                    node.arg1].derivative += node.derivative / self.NodeList[
                        node.arg2].value
                self.NodeList[
                    node.arg2].derivative += -node.derivative * self.NodeList[
                        node.arg1].value / (self.NodeList[node.arg2].value)**2
            elif node.op is Node.operators.sin:
                self.NodeList[
                    node.arg1].derivative += node.derivative * np.cos(
                        self.NodeList[node.arg1].value)
            elif node.op is Node.operators.cos:
                self.NodeList[
                    node.arg1].derivative += -node.derivative * np.sin(
                        self.NodeList[node.arg1].value)


class Node:
    cgraph = None
    operators = Enum('operators', ('add', 'sub', 'mul', 'truediv',
                                   'sin', 'cos'))

    def __init__(self,
                 value=np.NaN,
                 derivative=0.0,
                 op=None,
                 arg1=None,
                 arg2=None,
                 name=None):
        self.value = value
        self.derivative = derivative
        self.op = op
        self.arg1 = arg1
        self.arg2 = arg2
        self.name = name
        if Node.cgraph is not None:
            self.ID = Node.allocate_ID()
            Node.cgraph.append(self)

    @classmethod
    def allocate_ID(cls):
        if cls.cgraph is not None:
            return cls.cgraph.Nodec
        else:
            return None

    @classmethod
    def tome(cls, x):
        if isinstance(x, cls):
            return x
        else:
            return cls(x, op='constant')

    def __add__(self, other):
        other = Node.tome(other)
        return Node(
            self.value + other.value,
            op=Node.operators.add,
            arg1=self.ID,
            arg2=other.ID)

    def __sub__(self, other):
        other = Node.tome(other)
        return Node(
            self.value - other.value,
            op=Node.operators.sub,
            arg1=self.ID,
            arg2=other.ID)

    def __mul__(self, other):
        other = Node.tome(other)
        return Node(
            self.value * other.value,
            op=Node.operators.mul,
            arg1=self.ID,
            arg2=other.ID)

    def __truediv__(self, other):
        other = Node.tome(other)
        return Node(
            self.value / other.value,
            op=Node.operators.truediv,
            arg1=self.ID,
            arg2=other.ID)

    def __radd__(self, other):
        other = Node.tome(other)
        return Node(
            other.value + self.value,
            op=Node.operators.add,
            arg1=other.ID,
            arg2=self.ID)

    def __rsub__(self, other):
        other = Node.tome(other)
        return Node(
            other.value - self.value,
            op=Node.operators.sub,
            arg1=other.ID,
            arg2=self.ID)

    def __rmul__(self, other):
        other = Node.tome(other)
        return Node(
            other.value * self.value,
            op=Node.operators.mul,
            arg1=other.ID,
            arg2=self.ID)

    def __rtruediv__(self, other):
        other = Node.tome(other)
        return Node(
            other.value / self.value,
            op=Node.operators.truediv,
            arg1=other.ID,
            arg2=self.ID)



    def sin(self):
        return Node(np.sin(self.value), op=Node.operators.sin, arg1=self.ID)

    def cos(self):
        return Node(np.cos(self.value), op=Node.operators.cos, arg1=self.ID)

 
graph = CGraph()
graph.connect()
def function(x):
    a=Node()
    b=Node()
    a.value=1
    b.value=1
    for i in range(len(x)):
        y=b*0.4+Node.sin(a)*0.3
        z=x[i]+Node.cos(b)*0.3+a*0.1
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
def diff(x):
    temp=[]
    for i in range(len(x)):
        tempnode=Node()
        tempnode.value=x[i]
        temp.append(tempnode)
    return temp
def h(x,d):
    temp=diff(x)
    y=function(temp)
    matrix=[]
    truematrix=[]
    for i in range(len(y)):
        temprow=[]
        graph.compute_gradient(y[i].ID)
        for j in range(len(x)):
            temprow.append(temp[j].derivative)
        matrix.append(temprow)
    for i in range(len(y)):
        temprow=[]
        m=i
        for j in range(len(x)):
            temp=0
            for k in range(len(y)):
                temp+=d[m][k]*matrix[k][j]
            temprow.append(temp)
        truematrix.append(temprow)                
    return truematrix 
x=[]
for i in range(2020):
    x.append(1)
d=[[1,0],[0,1]]
result=h(x,d)
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