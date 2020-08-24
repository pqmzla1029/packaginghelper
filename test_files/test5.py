import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
fig = plt.figure ()
ax = Axes3D (fig)

offl=0
offb=0
offh=0
gap=0

bx=3
by=2
bz=2



l=5
iex=3
iey=1
isx=2
isy=2
nextbase=0
alpha=0.9

for k in range(l):
    if ((k+1)%2==0):


        for i in range(iex):
            for j in range(iey):
                basel=offl+i*(by+gap)
                baseb=offb+j*(bx+gap)
                nextbase=baseb+bx+gap
                baseh=offh+k*(bz+gap)
                ax.bar3d (basel,baseb,baseh,by,bx,bz, color='brown',edgecolor='black',alpha=alpha)


        #break
        #print(nextbase)
        for i in range(isx):
            for j in range(isy):
                basel=offl+i*(bx+gap)
                baseb=offb+j*(by+gap)+nextbase

                baseh=offh+k*(bz+gap)
                ax.bar3d (basel,baseb,baseh,bx,by,bz, color='brown',edgecolor='black',alpha=alpha)
                #print(basel)
                #print(baseb)

    else:
        for i in range(isx):
            for j in range(isy):
                basel=offl+i*(bx+gap)
                baseb=offb+j*(by+gap)
                nextbase=baseb+(by+gap)
                baseh=offh+k*(bz+gap)
                ax.bar3d (basel,baseb,baseh,bx,by,bz, color='brown',edgecolor='black',alpha=alpha)
        #print(nextbase)
        for i in range(iex):
            for j in range(iey):
                basel=offl+i*(by+gap)
                baseb=offb+j*(bx+gap)+nextbase
                baseh=offh+k*(bz+gap)
                ax.bar3d (basel,baseb,baseh,by,bx,bz, color='brown',edgecolor='black',alpha=alpha)
    #break
ax.margins(0.1)
ax.view_init(azim=90, elev=0)
plt.show()
ax.view_init(azim=0, elev=90)
fig.savefig("view_box_top.png")
plt.show()
ax.view_init(azim=90, elev=0)
fig.savefig("view_box_front.png")
plt.show()
ax.view_init(azim=0, elev=0)
fig.savefig("view_box_side.png")
plt.show()
