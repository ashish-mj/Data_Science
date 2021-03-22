#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 18:03:47 2021

@author: ashish
"""

import numpy as np

####################################################### Basic operation 
a= [10,2,3,4,10,6,7,8,9,10]

b=np.array(a,dtype=str,ndmin=3)
print(b)

b=np.array(a,dtype=float)
print(b)

b=np.array(a,dtype=complex)
print(b)

b=np.array(a,dtype=int)
print(b)

print(b[0]+b[5])
print(sum(b))
b.sort()
print(b)


##########################################################User Defined Structure data type

dt = np.dtype([("Name",'S20'),("Age",int),("Salary",float)]) 
b= [("Ashish",21,40000.8),("Adithya",28,20000.50),("pavan",21,15000.2)]
a = np.array(b, dtype = dt) 
print("Name - "+str(a["Name"])+"\nAge - "+str(a["Age"])+"\nSalary - "+str(a["Salary"]))

for i in a:
    print("-------------------------------------------------\n")
    print("Name - "+str(i[0])+"\nAge - "+str(i[1])+"\nSalary - "+str(i[2]))
    print("-------------------------------------------------\n")

##########################################################Array attributes
    
a = np.array([[1,2,3],[4,5,6]],dtype=float)
print(a)
print(a.shape)
a.shape=(3,2)
print(a)
b=a.reshape(2,3)
print(b)
print(b.ndim)
print(b.itemsize)
print(b.flags)

a=np.arange(1,100,7)
print(a)
    
##########################################################Array creations

a=np.empty((3,3),dtype=complex)
print(a)

a=np.zeros((3,3),dtype=int)
print(a)

a=np.ones((3,3),dtype=float)
print(a)

dt=np.dtype([("Age",int),("Salary",float)])
a=np.ones((3,3),dtype=dt)
print(a)
#############################################################