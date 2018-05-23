#! usr/bin/env python3
#-*- coding: utf-8 -*-

from sklearn.naive_bayes import GaussianNB
import numpy as np

#0：晴， 1：阴，2：降水，3：多云
#当天的天气
X = [[0],[1],[2],[1],[2],[0],[0],[3],[1]]
y = [1,2,1,2,0,0,3,1,1]
clf = GaussianNB().fit(X,y)
p = [[0]]
label_test = np.array([1])
accurancy = clf.score(p, label_test)
print(accurancy)