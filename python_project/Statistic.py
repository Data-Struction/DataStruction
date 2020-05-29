#!/usr/bin/env python
# coding: utf-8

# In[1]:


"""
@author: 桂引暄

part4: 统计
"""
import pandas as pd
import BasicInfo as bs
from TreeBuild import *

global Elist
Elist=["小学", "初中", "高中", "本科", "研究生", "博士"]
#最大公约数
def gcd(a,b):
    if a<b:
        a,b=b,a
    while(a%b != 0):
        c = a%b
        a=b
        b=c
    return b

#平均身高
def avg_height():
    df = pd.read_csv('data.csv')
    h = df['身高'].mean()
    return round(h,1)
    
#平均学历、最高学历、最低学历
def avg_edu_bg():
    df = pd.read_csv('data.csv')
    e = round(df['学历'].mean())
    return Elist[e-1]
#     if e==1:
#         print("平均学历：小学")
#     elif e==2:
#         print("平均学历：初中")
#     elif e==3:
#         print("平均学历：高中")
#     elif e==4:
#         print("平均学历：本科")
#     elif e==5:
#         print("平均学历：研究生")
#     elif e==6:
#         print("平均学历：博士")
def lowest_edu_bg():
    df = pd.read_csv('data.csv')
    arr = list(df['学历'])
    arr.sort()
    low = int(arr[0])
    return Elist[low-1]

def highest_edu_bg():
    df = pd.read_csv('data.csv')
    arr = list(df['学历'])
    arr.sort()
    high = int(arr[-1])
    return Elist[high-1]
        
#男女比例
def male_female():
    df = pd.read_csv('data.csv')
    sum_male = 0
    sum_female = 0
    arr1 = list(df['性别'])
    for item in arr1:
        if item=='女':
            sum_female+=1
        if item=='男':
            sum_male+=1
    n = gcd(sum_female, sum_male)
    male = int(sum_male/n)
    female = int(sum_female/n)
    s=str(male)+":"+str(female)
    return s
    
#平均寿命
def avg_age():
    df = pd.read_csv('data.csv')
    j = 0
    sum = 0
    df['寿命'] = df['出生日期'] - df['死亡日期']
    arr2 = list(df['寿命'])
    age = []
    for item in arr2:
        if(item<0):
            age.append(-round(item/10000)) 
    for i in range(len(age)):
        sum+=age[i]
    s=str(round(sum/len(age)))+"岁"
    return s

global plist
plist={}
def get_p(parent,layer):
    if parent.spouse!=-1 or len(parent.kids)!=0:
        plist[layer] = 1
        if parent.spouse != -1:
            plist[layer] +=1
#         print(plist)
        if len(parent.kids) == 0:
            return 
        k = 1
        for kid in parent.kids:
            plist[layer] += 1
            get_p(family[kid],layer+k)
            k+=1
    else:
        return

def avg_people():#计算平均人口
    get_p(family[root], 0)
#     print(plist)
    sum = 0
    for i in range(len(plist)):
        sum+=plist[i]
    return round(sum/len(plist))
            
    
            



