# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 09:00:23 2021

@author: USER
"""
import numpy as np
a=np.array([[1,2,3,4],[2,1,4,3],[3,3,9,6],[4,17,22,30]]).astype(float)
#u=np.array([[1,1,1,1],[0,1,1,1],[0,0,1,1],[0,0,0,1]]).astype(float)
#l=np.array([[1,0,0,0],[1,1,0,0],[1,1,1,0],[1,1,1,1]]).astype(float)
#a=np.zeros((6,6)).astype(int)
#B=np.zeros(6).astype(int)
#suma=0
###############
#for m in [1,2,3,4,5,6]:
#    suma=suma+m**5
#    B[m-1]=suma
#    a[m-1,:]=[m,m**2,m**3,m**4,m**5,m**6]
#print(B)
#print(A)
u=np.zeros(a.shape).astype(float)
l=(np.zeros(a.shape).astype(float)+np.eye(4).astype(float))
su=0
k=0#0,1,2
j=0
su_1=1
for t in range(1,2*len(a[1])):
    if t%2!=0:
        for j_1 in range(su,len(a[1])):
            m=0
            for s in range(0,k):
                p=l[k][s] * u[s][j_1]
                m=m+p
            u[k][j_1]=a[k][j_1]-m
        su=su+1
        k=k+1
    else:
        for k_1 in range(su_1,len(a[1])):
            m_1=0
            for s_1 in range(0,j):
                p=l[k_1][s_1]*u[s_1][j]
                m_1=m_1+p
            l[k_1][j]=(a[k_1][j]-m_1)/u[j][j]
        j=j+1
        su_1=su_1+1
print(a)
print(u)
print(l)