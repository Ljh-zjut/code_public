#! usr/bin/env python3
#-*- coding:utf-8 -*-

import numpy as np
from math import log
import operator

#‘年龄’， ‘身高’， ‘年收入’， ‘学历’
dataInit = [
    [25,179,15,0,0],
    [33,190,19,0,1],
    [28,180,18,2,1],
    [25,178,18,2,1],
    [46,100,100,2,0],
    [40,170,170,1,0],
    [34,173,20,2,1],
    [36,181,55,1,0],
    [35,170,25,2,1],
    [30,180,35,1,1],
    [28,174,30,1,0],
    [29,176,36,1,1]
]
labelInit = ['age','height','income','education']

#是否相亲 0：N 1：Y
Y = np.array([0,1,1,1,0,0,1,0,1,1,0,1])

#计算数据集的信息熵 （信息熵即指类别标签的混乱程度，值越小越好）
def calcshan(dataSet):
    lenDataSet = len(dataSet)
    p = {}
    H = 0.0
    for data in dataSet:
        currentLabel = data[-1]             #获取类别标签 
        if currentLabel not in p.keys():    #dict.keys(): 以列表返回一个字典所有的键。 若字典中不存在该类别标签，即创建  
            p[currentLabel] = 0
        p[currentLabel] += 1                #递增类别标签的值
    for key in p:
        px=float(p[key])/float(lenDataSet)  #计算某个标签的概率
        H-=px*log(px,2)                     #计算信息熵
    return H

#根据某一特征分类数据集
def splitData(dataSet, axis, value):        #dataSet为要划分的数据集,axis为给定的特征，value为给定特征的具体值
    subDataSet = []
    for data in dataSet:
        subData = []
        if data[axis]==value:
            subData = data[:axis]           #取出data中第0到axis-1个数进subData
            subData.extend(data[axis+1:])   #取出data中第axis+1到最后一个数进subData;这两行代码相当于把第axis个数从数据集中剔除掉
            subDataSet.append(subData)
    return subDataSet

#选择最好的数据集划分方式，遍历所有特征，选择信息熵最小的特征，即为最好的分类特征
def chooseBestFeature(dataSet):
    lenFeature=len(dataSet[0]) - 1          #计算特征维度时要把类别标签那一列去掉
    shanInit = calcshan(dataSet)            #计算原始数据集的信息熵
    feature = []
    inValue = 0.0
    bestFeature = 0
    for i in range(lenFeature):
        shanCarry=0.0
        feature=[example[i] for example in dataSet] #提取第i个特征的所有数据 
        feature=set(feature)                #得到第i个特征所有的分类值，如'0'和'1'
        for feat in feature:
            subData=splitData(dataSet, i, feat) #先对数据集按照分类值分类
            prob = float(len(subData))/float(len(dataSet))
            shanCarry += prob*calcshan(subData) #计算第i个特征的信息熵
        outValue = shanInit - shanCarry     #原始数据信息熵与循环中的信息熵的差
        if(outValue>inValue):
            inValue=outValue                #将信息熵与原始熵相减后的值赋给inValue，方便下一个循环的信息熵差值与其比较
            bestFeature=i
    return bestFeature


# 用于找出出现次数最多的分类名称的函数
def majorityCnt(classList):  
    classCount={}  
    for vote in classList:  
        if vote not in classCount.keys(): classCount[vote] = 0  
        classCount[vote] += 1  
    sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)  
    return sortedClassCount[0][0]

#创建分类决策树

def createTree(dataSet, label):
    classList=[example[-1] for example in dataSet]  #classList是指当前数据集的类别标签
    if classList.count(classList[0]) == len(classList): #计算classList中某个类别标签的数量，若只有一类，则数量与它的数据长度相等
        return classList[0]
    if len(dataSet[0]) == 1:                        #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    featBest = chooseBestFeature(dataSet)
    feature = [example[featBest] for example in dataSet]
    featValue = set(feature)
    newLabel = label[featBest]
    del(label[featBest])
    Tree = {newLabel:{}}
    for value in featValue:
        subLabel = label[:]                         #copy all of labels, so trees don't mess up existing labels
        Tree[newLabel][value]=createTree(splitData(dataSet, featBest, value), subLabel)
    return Tree

print(createTree(dataInit, labelInit))