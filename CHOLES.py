# -*- coding: utf-8 -*-
"""
Created on Tue Feb 16 17:01:39 2021

@author: USER
"""

import numpy as np
#a=np.array([[25,15,-5,-10],[15,10,1,-7],[-5,1,21,4],[-10,-7,4,18]]).astype(float)
#L=np.zeros((4,4)).astype(float)
a=np.array([[1,1,-1,2,2],[1,5,-3,4,6],[-1,-3,3,-2,-3],[2,4,-2,10,9],[2,6,-3,9,19]])
L=np.zeros((5,5)).astype(float)
su=0
#k=0#0,1,2
p=0
q=0
su_1=1
for t in range(1,2*len(a[1])):
    if t%2!=0:
        m=0
        for k in range(0,p):
            inicial=(L[p][k])**2
            m=m+inicial
        L[p][p]=(a[p][p]-m)**(1/2) 
        p=p+1
#        for j_1 in range(su,len(a[1])):
#            m=0
#            for s in range(0,k):
#                p=l[k][s] * u[s][j_1]
#                m=m+p
#            u[k][j_1]=a[k][j_1]-m
#        su=su+1
#        k=k+1
    else:
        for p_1 in range(su_1,len(a[1])):
            m_1=0
            for k_1 in range(0,q):
                inicial_1=(L[p_1][k_1])*(L[q][k_1])
                m_1=m_1+inicial_1
            L[p_1][q]=(a[p_1][q]-m_1)/L[q][q]
        q=q+1
        su_1=su_1+1
print(a)
print(L)
print(np.transpose(L))
#        for k_1 in range(su_1,len(a[1])):
#            m_1=0
#            for s_1 in range(0,j):
#                p=l[k_1][s_1]*u[s_1][j]
#                m_1=m_1+p
#            l[k_1][j]=(a[k_1][j]-m_1)/u[j][j]
#        j=j+1
#        su_1=su_1+1