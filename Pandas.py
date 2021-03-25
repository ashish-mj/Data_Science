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
x=pd.Series(a,index=[100,101,102,103,104])
print(x)

data={'a':200,'b':201,'c':202}
print(pd.Series(data))
print(pd.Series(data,index=["b","c","a"]))

print(pd.Series(5,index=[1,2,3,4,5]))

data={'a':200,'b':201,'c':202}
c = pd.Series(data)
print(c[0])
print(c["a"])
c['d']=203
print(c)

########################################################Dataframe

data=[1,2,3,4,5,6]
print(pd.DataFrame())
print(pd.DataFrame(data))

data = [[1,"Ashish",20,50000],[2,"Akshay",26,30000],[3,"Rajeev",50,150000]]
print(pd.DataFrame(data,columns=["ID","Name","Age","Salary"],dtype=float))

data={"Name":["Ashish","Girish","Pavan"],"Age":[21,24,28]}

print(pd.DataFrame(data,index=["rank1","rank2","rank3"]))

data = [[1,"Ashish",20,50000],[2,"Akshay",26,30000],[3,"Rajeev",50,150000]]
table = pd.DataFrame(data,columns=["ID","Name","Age","Salary"],dtype=float)

print(table)
print("Name : "+str(table["Name"]))
print(table.iloc[1,2])
print(table["Age"])

table["Dept"]=['IS','CS',"EC"]
print(table)

t1=table.append({"ID":4,"Name":"Pavan","Age":44,"Salary":20000,"Dept":"IS"},ignore_index = True)
temp = pd.Series([5,"Ajay",30,40000,"EE"],t1.columns)
t1=t1.append(temp,ignore_index = True)
print(t1)

t1.pop("Dept")
print(t1)

t1=t1.drop(t1.index[0:3])
print(t1)


