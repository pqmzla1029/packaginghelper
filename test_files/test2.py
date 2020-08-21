
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure ()
ax = Axes3D (fig)
#ax.set_xlim ([0,150])
#ax.set_ylim ([0,800])
#ax.set_zlim ([0,7.0])
countbottles=0
debugmode=2
way="stand"
casebb=2
casesb=2
offl=0
offb=0
offh=0

if casebb==1:
    bl=140
    bb=440
    bh=240

if casesb==1:
    sl=30
    sb=40
    sh=100
    gap=5

if casebb==2:
    bl=24
    bb=20
    bh=24

if casesb==2:
    tol=0.06
    sl=2.709+tol
    sb=2.709+tol
    sh=7.886+tol

    gap=0.05

if casebb==3:
    bl=19
    bb=13
    bh=15

if casesb==3:
    sl=30
    sb=40
    sh=100
    gap=5

if casebb==4:
    bl=19
    bb=13
    bh=20

if casebb==5:
    bl=23
    bb=15
    bh=29

alpha=0.05
volume_box=sl*sb*sh
volume_filled=0
#ax.bar3d (20, 40, 1, 90, 400, 2.4, color=(0, 0, 1, 0),edgecolor='black',alpha=alpha)
ax.bar3d (offl, offb, offh, bl,bb,bh, color='brown',edgecolor='black',alpha=alpha)
if(debugmode==1):
    ax.bar3d (offl, offb, offh, sl,sb,sh, color='red',edgecolor='black')
if(debugmode==2):
    if(way=="stand"):
        l=int(bl/(sl+gap))
        b=int(bb/(sb+gap))
        h=int(bh/(sh+gap))
        #print(l)
        #print(b)
        #print(h)
        for i in range(l):
            for j in range(b):
                for k in range(h):
                    basel=offl+i*(sl+gap)
                    baseb=offb+j*(sb+gap)
                    baseh=offh+k*(sh+gap)
                    ax.bar3d (basel,baseb,baseh,sl,sb,sh, color='red',edgecolor='black')
                    countbottles=countbottles+1


    if(way=="fall"):
        temp=sb
        sb=sh
        sh=temp

        l=int(bl/(sl+gap))
        b=int(bb/(sb+gap))
        h=int(bh/(sh+gap))
        #print(l)
        #print(b)
        #print(h)
        for i in range(l):
            for j in range(b):
                for k in range(h):
                    basel=offl+i*(sl+gap)
                    baseb=offb+j*(sb+gap)
                    baseh=offh+k*(sh+gap)
                    ax.bar3d (basel,baseb,baseh,sl,sb,sh, color='red',edgecolor='black')
                    countbottles=countbottles+1

    if(way=="sleep"):
        temp=sl
        sl=sh
        sh=temp

        l=int(bl/(sl+gap))
        b=int(bb/(sb+gap))
        h=int(bh/(sh+gap))
        #print(l)
        #print(b)
        #print(h)
        for i in range(l):
            for j in range(b):
                for k in range(h):
                    basel=offl+i*(sl+gap)
                    baseb=offb+j*(sb+gap)
                    baseh=offh+k*(sh+gap)
                    ax.bar3d (basel,baseb,baseh,sl,sb,sh, color='red',edgecolor='black')
                    countbottles=countbottles+1
volume_bottle=(sh+gap)*(sl+gap)*(sb+gap)
volume_filled=countbottles*volume_bottle
ax.margins(0.1)
print(countbottles)
#print(volume Unused="")
plt.show()
ax.view_init(azim=0, elev=90)
fig.savefig("view_top.png")
plt.show()
ax.view_init(azim=90, elev=0)
fig.savefig("view_front.png")
plt.show()
ax.view_init(azim=0, elev=0)
fig.savefig("view_side.png")
plt.show()
