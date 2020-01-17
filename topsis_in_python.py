# -*- coding: utf-8 -*-
"""
Created on Sat Jan 18 02:12:58 2020


"""
import numpy as np
import math
def topsis(matrix,weight,feat):
    b=[]
    for i in range(n):
        sum=0
        for j in range(m):
            sum=sum+matrix[j][i]**2
        b.append(math.sqrt(sum))
                  
    for i in range(m):
        for j in range(n):
            matrix[i][j]= (matrix[i][j]/b[j])
        
    for i in range(m):
        for j in range(n):
            matrix[i][j]=matrix[i][j]*weight[j]
  
#res = [min(column) for column in zip(*matrix)] 
#res1 = [max(column) for column in zip(*matrix)] 

#result=[]
#s=0
#for i in range(m):
 #   for j in range(n):
  #      s=s+matrix[i][j]
   # result.append(s)
        
    vpos=[]
    vneg=[]

    maximum=np.max(matrix,axis=0)
    minimum=np.min(matrix,axis=0)
    for i in range(n):
        if feat[i]==0:
            vpos.append(minimum[i])
            vneg.append(maximum[i])
        else:
            vpos.append(maximum[i])
            vneg.append(minimum[i])
    spos=[]
    sneg=[]
    for i in range(m):
        addi=0
        mini=0
        for j in range(n):
            addi=addi+(matrix[i][j]-vpos[j])**2
            mini=mini+(matrix[i][j]-vneg[j])**2
        spos.append(math.sqrt(addi))
        sneg.append(math.sqrt(mini))   

    perscore=[]
    for j in range(m):
        d=sneg[j]/(spos[j]+sneg[j])
        perscore.append(d)
    
    final=perscore.index(max(perscore))  
    return final+1
