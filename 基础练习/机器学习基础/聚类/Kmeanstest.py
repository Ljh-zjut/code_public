#!usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#从磁盘读经纬度表数据
X = []
f = open(r'C:\study&work\codes\study python\基础练习\city.txt')
for V in f:
    X.append([float(V.split(',')[1]), float(V.split(',')[2])])

#转换数组
X = np.array(X)

#设定类簇数量
n_clusters = 5

#把数据和对应分类数放入聚类函数进行聚类
cls = KMeans(n_clusters).fit(X)

#X中没想所属分类的一个列表
cls.labels_

#绘图
markers = ['^','x','o','*','+']
for i in range(n_clusters):
    members = cls.labels_ == i
    plt.scatter(X[members,0],X[members,1],s=60,marker=markers[i],c='b',alpha=0.5)
plt.title('')
plt.show()