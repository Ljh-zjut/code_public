#！ usr/bin/env python3
#-*- coding: utf-8 -*-
import math

education = (2.0/12, 5.0/12, 5.0/12)
junior_college = (1.0/2, 1.0/2)
undergraduate = (3.0/5, 2.0/5)
master = (4.0/5, 1.0/5)
date_per = (junior_college, undergraduate, master)

def info_date(p):
    info = 0 
    for v in p:
        info += v * math.log(v, 2)
    return info

def infoA():
    info = 0
    for i in range(len(education)):
        info += -education[i] * info_date(date_per[i])
    return info

print(infoA())

age = [25,25,28,28,29,30,33,34,36,40,46]
#是否相亲，1：是， 0：否
date = [0,1,1,0,1,1,1,1,1,0,0,0]

#从年龄28，29中间分开
#左右分类数量占总数百分比
split_per = (4.0/12, 8.0/12)

#左边分类中相亲比例
date_left = (1.0/2, 1.0/2)

#右边分类中的相亲比例
date_right = (5.0/8, 3.0/8)

#左右各分类中相亲占比
date_per2 = (date_left, date_right)

def infoB():
    info = 0
    for i in range(len(split_per)):
        info += -split_per[i] * info_date(date_per2[i])
    return info
print(infoB())