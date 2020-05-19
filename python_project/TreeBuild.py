# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:26:12 2020

@author: 丘卓栩

part2: 树的建立/关系的存储

v2.0
BasicInfo中dataframe的结构应增属性：亲属rela_idx, 关系rela_ship，根节点中两者为-1
"""
import BasicInfo as bs

family = []#存储每一个member类，用索引来访问
root = 0#根节点在family中索引，默认为0，开始访问

class member:
    def __init__(self,idx=-1,kids=[],spouse=-1):
        self.idx = idx
        self.kids = kids#member类索引list
        self.spouse = spouse#member类索引

def buildTree(alist):
    global root
    for i in range(len(alist)):
        temp = member(i)
        rela_idx = find_rela(alist[i]['亲属'],root)
        if(rela_idx != None or i == 0):#输入根节点或者找到亲属可输入
            family.append(temp)
            n = len(family)-1
            j = alist[i]['关系']#根据关系连接节点
            if j == 0:
                family[rela_idx].spouse = n
                family[-1].spouse = rela_idx
                family[-1].kids = family[rela_idx]
                continue
            elif j == 1:
                family[rela_idx].kids.append(n)#子节点也会新增元素?
                continue
            elif j == 2:
                family[-1].kids.append(root)
                if(rela_idx == root):
                    root = n    
                continue
               
def find_rela(rela_idx,rt):#根据alist索引找到family索引
    if(rela_idx == -1):
        return None
    else:
        for i in range(len(family)):
            if(family[i].idx == rela_idx):
                return i        
    print("相关亲属不存在。")    
    return None

def search_parent(idx,sex):
    tmp = []
    if(idx == root):
        print("找不到此人在这一代的父代亲属，查询失败。")
        return
    for i in range(family):
        if(idx in family[i].kids):
            tmp.append(i)
    flag1 = input("查询到父代亲属，请问是否继续往上查询：1.是 2.否")
    flag1 = int(flag1)
    if(flag1 == 1):
        flag2 = input("请选择进行父系查询或母系查询：1.父系查询 2.母系查询")
        flag2 = int(flag2)
        if(flag2 == 1):
            for i in tmp:
                if(bs.alist[family[i].idx]['性别'] == '男'):
                    search_parent(i,sex)
                    return
            print("找不到父系亲属，查询失败。")
        else:
            for i in tmp:
                if(bs.alist[family[i].idx]['性别'] == '女'):
                    search_parent(i,sex)
                    return
            print("找不到母系亲属，查询失败。")
    else:
        print("您所查询的亲属信息：")
        for i in tmp:
            if(sex == 1 and bs.alist[family[i].idx]['性别'] == '男'):
                print(bs.alist[i])
            if(sex == 2 and bs.alist[family[i].idx]['性别'] == '女'):
                print(bs.alist[i])
        
def search_child(idx,sex):
    tmp = family[idx].kids
    if(len(tmp) == 0):
        print("找不到此人在这一代的子代亲属，查询失败。")
        return
    flag = input("查询到子代亲属，请问是否继续往下查询：1.是 2.否")
    flag = int(flag)
    if(flag == 1):
        for i in tmp:
            search_child(i, sex)
    else:
        print("您所查询的亲属信息：")
        for i in tmp:
            print(bs.alist[family[i].idx])
            
def search_spouse(idx):
    tmp = family[idx].spouse
    if(tmp == -1):
        print("找不到此人配偶，查询失败。")
        return
    print("您所查询的亲属信息：")
    print(bs.alist[tmp])
    
def search_rela_info(idx,sex):
    print("->已选择 查询亲戚关系：")
    man = input("请输入要查询的成员名字：")
    result = bs.circle("姓名",man)
    if result == -1:
        print("您所查询的成员不存在。")
    else:
        if len(result) > 1:
            print("查询到多位成员，请输入其对应的编号以选择成员：")
            for i in result:
                print(i + ' ' + bs.alist[i])
            idx = input("显示完毕，请选择：")
            idx = int(idx)
        else:
            idx = result[0]
        rela_idx = find_rela(idx,root)
        sex = input("请选择要查询亲属的性别：0.不限 1.男 2.女")
        sex = int(sex)
        choc = input("请输入要查询的成员亲属关系：1.父代查询 2.子代查询 3.配偶查询 0.退出功能")
        choc = int(choc)
        if choc == 0:
            print("已结束查询。")
            return
        elif choc == 1:
            search_parent(rela_idx,sex)
        elif choc == 2:
            search_child(rela_idx,sex)
        elif choc == 3:
            search_spouse(rela_idx,sex)
    return
        
bs.read_file()
buildTree(bs.alist)
