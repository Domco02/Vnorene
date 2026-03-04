import numpy as np
import matplotlib.pyplot as plt
 
from mpl_toolkits.mplot3d import Axes3D
 
def plot_frame(ax, R, o, label, length=0.5):
    x_axis = o + R.dot(np.array([length, 0, 0]))
    y_axis = o + R.dot(np.array([0, length, 0]))
    z_axis = o + R.dot(np.array([0, 0, length]))
    
    ax.quiver(o[0], o[1], o[2], x_axis[0]-o[0], x_axis[1]-o[1], x_axis[2]-o[2],
              color='r', arrow_length_ratio=0.1)
    ax.quiver(o[0], o[1], o[2], y_axis[0]-o[0], y_axis[1]-o[1], y_axis[2]-o[2],
              color='g', arrow_length_ratio=0.1)
    ax.quiver(o[0], o[1], o[2], z_axis[0]-o[0], z_axis[1]-o[1], z_axis[2]-o[2],
              color='b', arrow_length_ratio=0.1)
    
    ax.text(o[0], o[1], o[2], label, fontsize=12, color='k')
    
def quat_to_rot(q):
    eta, x, y, z = q
    return np.array([
        [2*(eta**2 + x**2) - 1, 2*(x*y - eta*z), 2*(x*z + eta*y)],
        [2*(x*y + eta*z), 2*(eta**2 + y**2) - 1, 2*(y*z - eta*x)],
        [2*(x*z - eta*y), 2*(y*z + eta*x), 2*(eta**2 + z**2) - 1]
    ])

