# DataStruction
Data Struction team work

# API Document

## 家谱

### Description

- 属性

### Parameters

| Parameter  | Description |
| ---------- | ----------- |
| name       | 姓名        |
| sex        | 性别        |
| born_place | 出生地      |
| born_date  | 出生日期    |
| dead_date  | 死亡日期    |
| height     | 身高        |
| edu_bg     | 学历        |
| pos        | 职业        |
| top_pos    | 最高职务    |

以上是一个家庭成员的所有基本信息

## 曾一鸿

负责家庭成员基本信息的录入以及存储，查询家庭任一成员的基本信息
整个程序都要用到的一些元素：1.class Info，这个类存储家庭成员基本信息变量
2.alist,blist,这两个list，前者存储csv文件中存储的成员信息，后者录入程序要新添加的成员信息
3.默认的存储文件地址：data.csv
实现思路：

- 输入家庭成员基本信息：定义add函数，输入新成员信息进Info类，一个家庭成员建立一个Info类，再将这个类加到blist中
- 关于文件存储：信息存储在csv文件中，呈表格形式。在程序中，选择将新添的家庭成员信息存储进文件后，blist中的信息将追加至csv文件中
- 关于将文件里的信息写入到程序里：引入pandas库，将csv文件里的信息转成DataFrame再操作
