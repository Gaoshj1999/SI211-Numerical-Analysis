# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 21:38:27 2020

@author: duola
"""
def returnLRmatrix(A):
    n=len(A)
    U=[]#上三角矩阵
    L=[]#下三角矩阵
    for i in range(n):
        U.append([])
        L.append([])
        for j in range(n):
            U[i].append(0)
            if i==j:
                L[i].append(1)
            else:
                L[i].append(0)
    for r in range(n):
        if r==0:
            U[0][0]=A[0][0]
            for i in range(n-1):
                U[r][i+1]=A[0][i+1]
                L[i+1][r]=A[i+1][0]/U[0][0]
        elif r<n-1:
            temp=0
            for k in range(r):
                temp+=L[r][k]*U[k][r]
            U[r][r]=A[r][r]-temp
            for i in range(n-r-1):
                temp=0
                for k in range(r):
                    temp+=L[r][k]*U[k][r+i+1]
                U[r][i+r+1]=A[r][i+r+1]-temp
                temp=0
                for k in range(r):
                    temp+=L[r+i+1][k]*U[k][r]
                L[i+r+1][r]=(A[i+r+1][r]-temp)/U[r][r]
        else:
            temp=0
            for k in range(r):
                temp+=L[r][k]*U[k][r] 
            U[r][r]=A[r][r]-temp
    return L,U
def useLRtosolution(A,b):
    L,U=returnLRmatrix(A)
    n=len(L)
    y=[]
    x=[]
    for i in range(n):
        y.append(0)
        x.append(0)
    for i in range(n):
        if i==0:
            y[i]=b[i]
        else:
            temp=0
            for k in range(i):
                temp+=L[i][k]*y[k]
            y[i]=b[i]-temp
    x[n-1]=y[n-1]/U[n-1][n-1]
    for i in range(n-1):
        temp=0
        for k in range(n-i):
            temp+=U[n-2-i][i+k]*x[i+k]
        x[n-2-i]=(y[n-2-i]-temp)/U[n-2-i][n-2-i]
    return x,y      
A=[[1,-2,1],[2,1,-3],[4,-7,1]]
b=[0,5,-1]
x,y=useLRtosolution(A,b)
print(y)
print(x)