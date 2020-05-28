# -*- coding: utf-8 -*-
"""
Created on Tue May  5 11:26:12 2020

@author: 丘卓栩

part2: 树的建立/关系的存储

BasicInfo中dataframe的结构应增属性：亲属rela_name, 关系rela_ship，根节点中前者为null，后者为-1
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
        if(i == 0):
            alist[i]['亲属'] = 'default'
            alist[i]['关系'] = -1
        temp = member(i,[])
        rela_idx = find_rela(alist[i]['亲属'])
        if(rela_idx != None or i == 0):#输入根节点或者找到亲属可输入
            family.append(temp)
            n = len(family)-1
            j = alist[i]['关系']#根据关系连接节点
            if j == 0:
                family[rela_idx].spouse = n
                family[-1].spouse = rela_idx
                family[-1].kids = family[rela_idx].kids
            elif j == 1:
                family[rela_idx].kids.append(n)
            elif j == 2:
                family[-1].kids.append(root)
                if(rela_idx == root):#关于根节点得变化一个疑问：新增根节点配偶的父节点，是否变化？
                    root = n    
                    

               
def find_rela(rela_name):#根据alist索引找到family索引
    if(rela_name == 'default'):
        return None
    else:
        for i in range(len(family)):
            if(bs.alist[family[i].idx]['姓名'] == rela_name):
                #if(i == root):
                    
                return i        
    print("相关亲属不存在。")    
    return None

def search_parent(idx, p3, p4):
#     limt = input("请输入目标查询亲属与目标成员的相隔代数:")
    limt = p3
    limt = int(limt)
    str2 = sch_p_cir(idx, 1, limt, p4)
    return str2
def sch_p_cir(idx, time, limt, p4):#注：家谱属性都为父系
    tmp = []
    for i in range(len(family)):
        if(idx in family[i].kids):
            tmp.append(i)
    if(tmp == []):
#         print("没有满足条件的父代亲属，查询失败。")
        str1 = "没有满足条件的父代亲属，查询失败。"
        return str1
    if(time == limt):
#         sex = input("请选择要查询亲属的性别：0.不限 1.男 2.女")
        sex = p4
        sex = int(sex)
#         print("您所查询的亲属信息：")
        for i in tmp:
            if(sex == 1 and bs.alist[family[i].idx]['性别'] == '男'):
#                 print(bs.alist[i])
                str0 = str(bs.alist[i])
                str1 = "您所查询的亲属信息\n"+str0+"\n查询结束"
                return str1
            elif(sex == 2 and bs.alist[family[i].idx]['性别'] == '女'):
                str0 = str(bs.alist[i])
                str1 = "您所查询的亲属信息\n"+str0+"\n查询结束"
                return str1
            elif(sex == 0):
                str0 = str(bs.alist[i])
                str1 = "您所查询的亲属信息\n"+str0+"\n查询结束"
                return str1
#         print("查询结束。")
    else:
        for i in tmp:
            if(bs.alist[family[i].idx]['性别'] == '男'):
                sch_p_cir(i, time+1, limt)
                
def search_child(idx, p3, p4):
#     limt = input("请输入目标查询亲属与目标成员的相隔代数:")
    limt = p3
    limt = int(limt)
    tmp = sch_c_cir(idx, 1, limt)
    if(tmp == []):
#         print("没有满足条件的子代亲属，查询失败。")
        str1 = "没有满足条件的子代亲属，查询失败。"
        return str1
    else:
#         sex = input("请选择要查询亲属的性别：0.不限 1.男 2.女")
        sex = p4
        sex = int(sex)
#         print("您所查询的亲属信息：")
        for i in tmp:
            if(sex == 1 and bs.alist[family[i].idx]['性别'] == '男'):
                str0 = str(bs.alist[i])
                str1 = "您所查询的亲属信息\n"+str0+"\n查询结束"
                print(str1)
                return str1
            elif(sex == 2 and bs.alist[family[i].idx]['性别'] == '女'):
                str0 = str(bs.alist[i])
                str1 = "您所查询的亲属信息\n"+str0+"\n查询结束"
                print(str1)
                return str1
            elif(sex == 0):
                str0 = str(bs.alist[i])
                str1 = "您所查询的亲属信息\n"+str0+"\n查询结束"
                print(str1)
                return str1
#         print("查询结束。")
def sch_c_cir(idx, time, limt):
    childs = []
    tmp = family[idx].kids
    if(time == limt):        
        if(tmp == []):
            return []
        else:
            childs = childs + tmp
    else:
        for i in tmp:
            childs = childs + sch_c_cir(i, time+1, limt)
    return childs

def search_spouse(idx):
    tmp = family[idx].spouse
    if(tmp == -1):
        str1 = "找不到此人配偶，查询失败。"
        return str1
#     print("您所查询的亲属信息：")
    str0 = str(bs.alist[tmp])
    str1 = "您所查询的亲属信息：\n"+str0+"\n查询结束"
    print(str1)
    return str1
    
def search_rela_info(p1, p2, p3, p4): #p1.成员姓名 p2.查询关系序号 p3.查询相隔代数 p4.亲属性别序号
    print("->已选择 查询亲戚关系：")
#     man = input("请输入要查询的成员名字：")
    man = p1
    rela_idx = find_rela(man)
    if(rela_idx == None):
        str1 = "已结束查询。"
        return str1
    else:
#         choc = input("请输入要查询的成员亲属关系：1.父代查询 2.子代查询 3.配偶查询 0.退出功能")
        choc = p2
        choc = int(choc)
        if choc == 0:
            str1 = "已结束查询。"
            return str1
        elif choc == 1:
            str2 = search_parent(rela_idx, p3, p4)
            return str2
        elif choc == 2:
            str2 = search_child(rela_idx, p3, p4)
            return str2
        elif choc == 3:
            str2 = search_spouse(rela_idx)
            return str2
    return
        
# bs.read_file()#三行测试功能函数，可删除
# buildTree(bs.alist)
# search_rela_info()