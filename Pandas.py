#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 24 12:11:42 2021

@author: ashish
"""
import pandas as pd


########################################################Series
a=["a","B","c","D","e"]
print(pd.Series())
print(pd.Series(a))
print(pd.Series(a,index=[100,101,102,103,104]))

data={'a':200,'b':201,'c':202}
print(pd.Series(data))
print(pd.Series(data,index=["b","c","a"]))

print(pd.Series(5,index=[1,2,3,4,5]))

data={'a':200,'b':201,'c':202}
c = pd.Series(data)
print(c[0])
print(c["a"])

########################################################