import numpy as np
import matplotlib.pyplot as plt
#original data
x = [1,2,3,4,5,6,7,8,9]
y = [0.199,0.389,0.580,0.783,0.980,1.177,1.380,1.575,1.771]

#A = np.vstack([x,np.ones(len(x))]).T

#a,b = np.linalg.lstsq(A,y)[0]

t1 = t2 = t3 = t4 = 0
n = len(x)
for i in range(n):
    t1 += y[i] #求和y
    t2 += x[i] #求和x
    t3 += x[i]*y[i]
    t4 += x[i]**2

a = (t1*t2/n - t3)/(t2*t2/n - t4)
b = (t1 - a*t2)/n

x = np.array(x)
y = np.array(y)

plt.plot(x,y,'o',label='Original data',markersize=10)
plt.plot(x,a*x+b,'r',label='Fitted line')
plt.show()