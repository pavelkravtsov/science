from math import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from math import pi
import matplotlib.pyplot as plt
import numpy as np


fig = plt.figure()
ax = fig.gca(projection='3d')
# eta = \Delta \eta
eta = np.arange(-1.5, 1.5, 0.02)
# phi = \Delta \phi
phi = np.arange(-1.5, 4.5, 0.05)
eta, phi = np.meshgrid(eta, phi)
    
y = 0.5 * np.cos(phi)
tmp = np.sqrt(1 - y * y)
phi_N = (3/(8 * pi)) * (tmp - y * np.arccos(y)) / (tmp * tmp * tmp)

ones = eta ** 0
size = 0.6
eta_N = ones + np.exp(- (eta + ones) * (eta + ones) / (size * size * 2)) + \
        np.exp(- (eta - ones) * (eta - ones) / (size * size * 2))
N = phi_N * eta_N

surf = ax.plot_surface(eta, phi, N, rstride=1, cstride=1, cmap=cm.gist_rainbow_r,
                       linewidth=0, antialiased=False)
ax.set_zlim3d(0.0, 2.0)
ax.set_xlabel(r"$\Delta \eta$")
ax.set_ylabel(r"$\Delta \phi$")
ax.set_zlabel(r"")
plt.show()
