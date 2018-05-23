#! usr/bin/env python3
# -*- coding: utf-8 -*-

import numpy as np
from sklearn.cluster import KMeans

#国家人口面积
X = [
    [9670250, 1392358258],
    [2980000, 1247923065],
    [9629091, 317408015],
    [8514877, 201032714],
    [377873, 127270000],
    [7692024, 23540571],
    [9984670, 34591000],
    [17075400, 143551289],
    [513115, 67041000],
    [181035, 14805358],
    [99600, 50400000],
    [120538, 24052231]
]

#转换数组
X = np.array(X)

#归一化
a = X[ : , :1 ]/17075400.0*10000
b = X[ : , 1: ]/1392358258.0*10000
X = np.concatenate((a, b), axis=1)

#设定类簇数量
n_clusters = 3

#把数据和对应分类数放入聚类函数进行聚类
cls = KMeans(n_clusters).fit(X)

#X中没想所属分类的一个列表
cls.labels_

#曼哈顿距离函数
def manhattan_distance(x,y):
    print(min(np.sum(abs(x-y), axis=1)))
    return min(np.sum(abs(x-y), axis=1))

distance_sum = 0
for i in range(n_clusters):
    group = cls.labels_ == i
    members = X[group, :]
    for v in members:
        distance_sum += manhattan_distance(np.array(v), cls.cluster_centers_)
        #print(np.array(v), cls.cluster_centers_)
print(distance_sum)