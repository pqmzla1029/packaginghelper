from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt

from itertools import product, combinations

fig = plt.figure()
ax = plt.axes(projection="3d")
length=[0,2]
breadth=[0,3]
height=[0,5]
for s, e in combinations(np.array(list(product(length, breadth, height))), 2):
    giv=np.abs(s-e)
    if (np.sum(np.abs(s-e)) <= height[1]-height[0]):
        ax.plot3D(*zip(s, e), color="b")

"""
# draw cube
r = [-1, 1]
for s, e in combinations(np.array(list(product(r, r, r))), 2):
    if np.sum(np.abs(s-e)) == r[1]-r[0]:
        ax.plot3D(*zip(s, e), color="b")
"""
"""
points = np.array([[-1, -1, -1],
                  [1, -1, -1 ],
                  [1, 1, -1],
                  [-1, 1, -1],
                  [-1, -1, 1],
                  [1, -1, 1 ],
                  [1, 1, 1],
                  [-1, 1, 1]])
xline=points[:,0]
yline=points[:,1]
zline=points[:,2]
print(xline)
print(yline)
print(zline)
ax.plot3D(xline, yline, zline, 'gray')
"""
plt.show()
