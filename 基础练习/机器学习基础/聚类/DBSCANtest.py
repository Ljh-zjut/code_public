#! usr/bin/env python3
#-*-coding: utf-8-*-

import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt

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

#将数据通过分类器进行训练
cls = DBSCAN(eps=2000, min_samples=1).fit(X)

#类簇数量
n_clusters = len(set(cls.labels_))

#X中每项所属分类的一个列表
cls.labels_
print(cls.labels_)

#绘图
markers = ['^','x','o','*','+']
for i in range(n_clusters):
    my_members = cls.labels_ == i
    plt.scatter(X[my_members, 0], X[my_members, 1], s=60, marker=markers[i], c='b', alpha=0.5)

plt.title('dbscan')
plt.show()