#! usr/bin/env python
#-*- coding:utf-8 -*-

import numpy as np
a = np.arange(15).reshape(3, 5)
a.ravel()[1] = 100
a.resize((5,3))
b = np.array([[1],[2],[3],[4],[5]])
c = np.hstack((a, b))
d = np.hsplit(c,(2,3))
a.max(axis = 0)
a.max(axis = 1)
a.mean(axis = 0)
a.flatten()
np.ravel(a)
e = np.repeat(7,4)
f = np.zeros((5,4,3),dtype=np.uint8)
f.astype(np.float)
g = np.arange(10)
h = np.linspace(0,7,5)
np.save('g.npy', g)
i = np.load('g.npy')
j = np.arange(24).reshape((2,3,4))
k = j[:, 2, :]
j[..., 1]
j[:, 1:, 1:-1]
l = np.split(j, 2)
l0 = g.reshape((2,5))
l1 = np.arange(2,12).reshape(2,5)
m = np.vstack((l0,l1))
m1 = np.hstack((l1,l0))
m2 = np.concatenate((l0,l1))
m3 = np.concatenate((l0,l1), axis=-1)
m4 = np.stack((l0,l1))
n = m4.transpose((2,0,1))
n1 = m4[0].transpose()
o = np.rot90(n1, 3)
o1 = np.fliplr(n1)
o2 = np.flipud(n1)
o3 = np.roll(n1, 1)
o4 = np.roll(n1,1,axis=1)
p = np.exp(3)
q = np.arange(1,6)
q1 = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
q2 = np.array([1, 0, 1])
q3 = np.dot(q2,q1)

import numpy.random as random
r = random.seed(42)
r1 = random.rand(2,4)
r2 = random.random((3,3))
r3 = random.uniform(1,7,5)
r4 = random.normal(size = (5,2))
r5 = random.binomial(n=2, p=0.5, size=6)
s = random.choice(q,3)
s1 = random.choice(q, 3, replace=False)
s2 = random.permutation(q)
random.shuffle(q)
s3 = random.bytes(7)
print(s3)