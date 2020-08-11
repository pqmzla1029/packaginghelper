
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure ()
ax = Axes3D (fig)
#ax.set_xlim ([0,150])
#ax.set_ylim ([0,800])
#ax.set_zlim ([0,7.0])
debugmode=2

offl=20
offb=40
offh=100

bl=140
bb=440
bh=240

sl=30
sb=40
sh=100
gap=5

alpha=0.05

#ax.bar3d (20, 40, 1, 90, 400, 2.4, color=(0, 0, 1, 0),edgecolor='black',alpha=alpha)
ax.bar3d (offl, offb, offh, bl,bb,bh, color='brown',edgecolor='black',alpha=alpha)
if(debugmode==1):
    ax.bar3d (offl, offb, offh, sl,sb,sh, color='red',edgecolor='black')
if(debugmode==2):
    l=int(bl/(sl+gap))
    b=int(bb/(sb+gap))
    h=int(bh/(sh+gap))
    #print(l)
    #print(b)
    #print(h)
    for i in range(l):
        for j in range(b):
            for k in range(h):
                basel=20+i*(sl+gap)
                baseb=40+j*(sb+gap)
                baseh=100+k*(sh+gap)
                ax.bar3d (basel,baseb,baseh,sl,sb,sh, color='red',edgecolor='black')

plt.show ()
