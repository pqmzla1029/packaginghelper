#import os
#print(os.getcwd())
#path_parent = os.path.dirname(os.getcwd())
#os.chdir(path_parent)
#print(os.getcwd())

#import sys
# insert at 1, 0 is the script path (or '' in REPL)
#sys.path.append(path_parent)


from container_packing.shortcuts import pack_products_into_restrictions
print("imported")
boxes = [{
  'x': 10,
  'y': 20,
  'z': 30,
  'quantity': 2
}, {
  'x': 20,
  'y': 30,
  'z': 50,
  'quantity': 4
}]

conataner_max_sizes = (60, 60, 70)

container_x, container_y, container_z = pack_products_into_restrictions(boxes,conataner_max_sizes)

def test():
    from mpl_toolkits import mplot3d

    import numpy as np
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = plt.axes(projection="3d")

    plt.show()
