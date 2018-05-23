import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
import math

#original datas
T = np.linspace(1960,1968,9)
S = [29.72,30.61,31.51,32.13,32.34,32.85,33.56,34.20,34.83]

xdata = np.array(T)
ydata = np.log(np.array(S))

def func(x,a,b):
    return a*x+b

#使用非线性最小二乘法拟合函数
popt,pcov = curve_fit(func,xdata,ydata)[0]
print(popt,pcov)

#绘图
#plt.plot(xdata,ydata,'ko',label="Original Noised Data")
#plt.plot(xdata,func(xdata,popt,pcov),'r',label="Fitted Curve")
#plt.show()

print(math.e**(popt*1964+pcov))