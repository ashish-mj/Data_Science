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

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2,ignore_index=True)
print(df)
df = df.drop(0)
print(df)

############################################Practice Dataframes

data = [[1,"Ashish","MI"],[2,"Dhoni","CSK"],[3,"Virat","RCB"],[4,"Warner","SRH"],[5,"Rahul","KP"],[6,"Dinesh","KKR"],[7,"Iyer","DC"],[8,"Samson","RR"]]
data = pd.DataFrame(data,columns=["ID","Player_Name","Team"])
print(data)

data["Salary"]="$2000"
print(data)
titles ={"MI":5,"CSK":3,"KKR":2,"SRH":2,"RR":1,"RCB":0,"DC":0,"KP":0}
data["Titles"]=data["Team"].map(titles)
print(data)

net_worth=[]

for i in data["Titles"]:
    if i==5:
        net_worth.append("$1200000")
    elif i==3:
        net_worth.append("$900000")
    elif i==2:
        net_worth.append("$500000")
    else:
        net_worth.append("$350000")

data["Net_worth"]=net_worth
print(data)

data.loc[data["Titles"]>=3,"Salary"]="$4000"
print(data)

del data["ID"]
print(data)

print(data[:4])
print(data.loc[data["Player_Name"]!=""])
temp = pd.Series(["Smith","RPSG","$2000",0,"$35000"],data.columns)
data=data.append(temp,ignore_index=True)
print(data)
data=data.drop(8)
print(data)

data=data.drop([1,4])

############################################Basic Functionality

data = pd.Series([1,2,3,4,5,6,7,8,9])
data1 = [[1,"Ashish","MI"],[2,"Dhoni","CSK"],[3,"Virat","RCB"],[4,"Warner","SRH"],[5,"Rahul","KP"],[6,"Dinesh","KKR"],[7,"Iyer","DC"],[8,"Samson","RR"]]
data1 = pd.DataFrame(data1,columns=["ID","Player_Name","Team"])
print(data)
print(data1)

print(data.axes)
print(data1.axes)

print(data.dtype)
print(data1.dtypes)     #dtypes for dataframes

print(data.empty)
print(data1.empty)

print(data.head(4))
print(data1.head(4))

print(data.tail(7))
print(data1.tail(7))

print(data.values)
print(data1.values)

print(data1.T)



############################################






