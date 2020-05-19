import pandas as pd


alist = []
blist = []
title = ["姓名", "出生地", "出生日期", "死亡日期", "身高", "学历", "职业", "最高职务", "亲属", "关系", "性别"]
pd.set_option("display.max_rows", None)
cur_filename = "data.csv"
#df = pd.read_csv("data.csv", encoding="utf-8")


class Info:
    def __init__(self, name, born_place, born_date, dead_date, height, edu_bg, pos, top_pos, born_rela, rela_ship, sex):
        self.name = name
        self.born_place = born_place
        self.born_date = born_date
        self.dead_date = dead_date
        self.height = height
        self.edu_bg = edu_bg
        self.pos = pos
        self.top_pos = top_pos
        self.born_rela = born_rela
        self.rela_ship = rela_ship
        self.sex = sex
        self.datas = {"姓名": name, "出生地": born_place, "出生日期":born_date, "死亡日期":dead_date, "身高":height, "学历":edu_bg, "职业":pos, "最高职务":top_pos, "性别":sex, "亲属":born_rela, "关系":rela_ship}
        #丘：改动x1 5.10
        
    def edit(self):
        pass

    def print_info(self):
        print("{}: {}".format(self.name, self.born_place))
        pass


def add(): #将新增的信息存入list中，但还没有存入txt文件中
    print("->已选择 增加成员记录")
    name = input("请输入姓名：")
    born_place = input("请输入出生地：")
    born_date = input("请输入出生日期：")
    dead_date = input("请输入死亡日期：")
    height = input("请输入身高：")
    edu_bg = input("请输入学历（1.小学2.初中3.高中4.本科生5.研究生6.博士生）：")
    #上面这里阿暄修改一下，也是改得让用户可以明白要输入什么格式的内容，如果输入文字的话，你统计的时候就把文字改成数字，如果输入数字的话，就在查询显示的地方把数字转成文字显示
    pos = input("请输入当前职业：")
    top_pos = input("请输入最高职务：")
    born_rela = input("请输入亲属名字：")#这里小丘改一下描述，改得让用户可以明白要输入什么格式的内容
    rela_ship = input("请输入与上面输入的那位亲属的关系（）：")
    sex = input("请输入性别：")
    person = Info(name, born_place, born_date, dead_date, height, edu_bg, pos, top_pos, born_rela, rela_ship, sex)
    add_in_list(blist, person.datas)
    print("信息添加成功")
    #return blist


def read_file():#将文件里面的信息读取出来存到list里面
    print("->已选择 读取文件")
    print("请输入相应序号进行操作：")
    print("当前默认文件：", cur_filename)
    func = input("1.使用默认文件名读取存储文件 2.使用自定义文件名读取存储文件 0.退出功能")
    if(func == "1"):
        df = pd.read_csv(cur_filename, encoding="utf-8")
        csv_to_list(df)
    elif(func == "2"):
        f = input("请输入要读取的文件名：")
        filename = "{}.csv".format(f)
        df = pd.read_csv(filename, encoding="utf-8")
        csv_to_list(df)
    elif(func == "0"):
        return


def csv_to_list(df):
    length = len(df)
    i = 0
    while i < length:
        tmp = Info(df.loc[i, "姓名"], df.loc[i, "出生地"], df.loc[i, "出生日期"], df.loc[i, "死亡日期"], df.loc[i, "身高"], df.loc[i, "学历"], df.loc[i, "职业"], df.loc[i, "最高职务"],df.loc[i, "亲属"], df.loc[i, "关系"], df.loc[i, "性别"])
        alist.append(tmp.datas) #丘：改动x2 5.10
        i += 1
    print(alist)


def save_file(li):
    print("->已选择 存储文件")
    func = input("1.使用默认文件名存储文件 2.使用自定义文件名存储文件 0.退出功能")
    if (func == "1"):
        dataframe = pd.DataFrame(li)
        dataframe.to_csv(cur_filename, mode='a', header=False, index=False)
    elif (func == "2"):
        f = input("请输入要读取的文件名：")
        filename = "{}.csv".format(f)
        dataframe = pd.DataFrame(li)
        dataframe.to_csv(filename, mode='a', header=False, index=False)
    elif (func == "0"):#丘：此处有bug，在主程序中return后按顺序执行查询函数
        return


def add_in_list(li, person):
    li.append(person)


def search_basic():
    print("->已选择 查询基本信息")
    func = input("1.“姓名”查询 2.“出生地”查询 3.“出生日期”查询 0.退出功能")
    func = int(func)
    if func == 0:
        return
    str = "请输入要查询的{}：".format(title[func - 1])
    tmp = input(str)
    result = circle(title[func - 1], tmp)
    if result == -1:
        print("您所查询的成员不存在哦")
    else:
        print("您所查询的成员信息：")
        for i in result:
            print(alist[i])


def circle(str, tmp):
    tmp_list = []
    for i in range(len(alist)):#丘：此处修改至保存索引，便于part2中引用
        if alist[i][str] == tmp:
            tmp_list.append(i)
    if len(tmp_list) != 0:
        return tmp_list
    else:
        return -1

#read_file()
#search_basic()


