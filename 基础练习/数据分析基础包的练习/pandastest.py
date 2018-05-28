#! usr/bin/env python3
#-*- coding: utf-8 -*-

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#生成一个固定频率的时间索引，从5月9号到5月14号
dates = pd.date_range('20180509', periods=6)
#创建一个类似表格的数据结构，索引包括列索引和行索引，index为行索引（这里是日期），columns是列索引（这里是‘ABCD’）
df = pd.DataFrame(np.random.randn(6,4), index=dates, columns=list('ABCD'))
#筛选日期大于5月10号小于5月12号的数据
rows = df[(df.index >= '2018-05-10')&(df.index <= '2018-05-12')]
#筛选A列数据大于0的数据
rows2 = df[df['A'] > 0]

#用一维数组生成series
s = pd.Series([1,1,2,3,5])
#创建一个新的列
df['sumAB'] = pd.Series(df['A']+df['B'], index=df.index)
df['10A'] = pd.Series(df['A']*10, index=df.index)
#设置A为新的行
df1 = df.set_index('A')
df['bool'] = (df.A > 1)
#重新设置列索引顺序
df = df.reindex(columns=['C','B','A'])

#使用字典生成DataFrame，key为列名字
data = {'state':['ok','ok','good','bad'],
'year':[2000,2001,2002,2003],
'pop':[3.7,3.6,2.4,0.9]}

df2 = pd.DataFrame(data)
df2 = df2.reindex(columns=['year','state','pop','debt'])
df2l = df2['year'] #返回一个名为state的Series,也可以直接df2.year进行列索引
#df2h = df2.ix[0] #用.ix[]来区分[]进行行索引,ix中可以有两个参数，第一个是行索引，第二个是列索引
df2['debt'] = 11.25 #修改整列的数据
#用Series修改元素，没有指定的默认数据用NaN
val = pd.Series([-1.2, -1.5, -1.7,0], index = [0,1,4,5]) 
df2.debt = val

#DataFrame转置
df2T = df2.T

#使用切片初始化数据,未被匹配的数据为NaN
pdata = {'state':df2['state'][0:3], 'pop':df2['pop'][0:2]}
newdf2 = pd.DataFrame(pdata)

#指定索引和列的名称
newdf2.index.name='序号'
newdf2.columns.name='信息'

#fill_value 指定不存在元素NaN的默认值
df3 = newdf2.reindex(columns=['pop','state','year'], fill_value=2018)

#重新指定索引并指定填充NaN的方法,ffill指前向填充值,bfill指后向填充值
df4 = pd.Series(['blue', 'purple'], index = [0, 2]).reindex(range(4), method='ffill')

#删除（丢弃）整一行/列的元素：drop函数
df5 = df3.drop(0) #默认删除行
df5 = df3.drop('pop', axis=1) #删除列

#DataFrame算术:不重叠部分为NaN,重叠部分元素运算
x = pd.DataFrame(np.arange(9.).reshape((3, 3)),
                columns = ['A','B','C'],
                index = ['a', 'b', 'c'])
y = pd.DataFrame(np.arange(12).reshape((4, 3)),
                columns = ['A','B','C'],
                index = ['a', 'b', 'c', 'd'])
sum = x+y

#对x与y的不重叠部分填充，不是对结果NaN填充
sum2 = sum.add(y, fill_value = 0)

#DataFrame与Series运算：每行/列进行运算
series = y.ix[0]
sub = y-series #按行运算，每一行都会减

series2 = pd.Series(range(4), index = ['A','B','C','D'])
sub2 = y+series2

series3 = y['A']
sub3 = y.sub(series3, axis=0) #按列进行减法运算

#numpy函数应用与映射
sqr = np.square(y)#平方

#lambda(匿名函数)以及应用
max1 = y.max() #求每一列最大值

f=lambda x: x.max()-x.min()
fun1 = y.apply(f) #作用于每一列
fun2 = y.apply(f, axis = 1 ) #作用于每一行

#applymap(func)和map(func)指将函数作用到每一个元素
_format = lambda x: '%.2f' % x #保留两位小数
fun3 = y.applymap(_format) #applymap只针对dataframe
fun4 = y['A'].map(_format) #map只针对series

print(fun4)
