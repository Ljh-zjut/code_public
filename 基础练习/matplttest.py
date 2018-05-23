#-*- coding : utf-8 -*-
import numpy as np

def main():
    #line
    import matplotlib.pyplot as plt
    x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
    c,s= np.cos(x), np.sin(x)
    plt.figure(1)
    plt.plot(x,c, color="blue", linewidth=1.0, linestyle="-",label="COS", alpha=0.5) #alpha透明度
    plt.plot(x,s,"r*", label = "SIN")
    ax = plt.gca()
    ax.spines["right"].set_color("none")  #把右边和顶部的线设置为透明
    ax.spines["top"].set_color("none")
    ax.spines["left"].set_position(("data",0)) #把左边和底部的线移动到0坐标
    ax.spines["bottom"].set_position(("data",0))
    ax.xaxis.set_ticks_position("bottom") #以底部的线为x轴，左边的线为y轴
    ax.yaxis.set_ticks_position("left")
    plt.xticks([-np.pi, -np.pi/2,0,np.pi/2,np.pi],[r'$-\pi$',r'$-\pi/2$',r'$0$',r'$+\pi/2$',r'$+\pi$'])
    plt.yticks(np.linspace(-1,1,5,endpoint=True))
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_fontsize(16)
        label.set_bbox(dict(facecolor="white", edgecolor="None",alpha=0.2))

    plt.title("cos &  sin")
    plt.show()

if __name__ == "__main__":
    main()