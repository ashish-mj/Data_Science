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


##########################################################


