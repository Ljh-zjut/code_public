#! usr/bin/env python3
#-*-coding: utf-8-*-

import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

import sys

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

K = range(1, 10)
a = []
for k_number in K:
    cls = KMeans(n_clusters=k_number).fit(X)
    value = sum(np.min(cdist(X, cls.cluster_centers_, 'euclidean'), axis=1))/X.shape[0] #axis = 1指每一行的最小值，这里得到的是每一个向量和对应类簇中心点的欧式距离，求和后再求平均值。
    print(k_number, value)
    #print(cdist(X, cls.cluster_centers_, 'euclidean'))
    a.append(value)

cha = [a[i] - a[i+1] for i in range(len(a)-1)]
a_value = a[cha.index(max(cha)) + 1] #因为肘方法的下一个值最优，所以+1
index = a.index(a_value)+1 #因为索引从0开始，所以求簇类数量还要+1
print(max(cha), a_value, index)