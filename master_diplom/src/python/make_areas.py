import os
import os.path
import numpy as np
import numpy.random as random
import matplotlib.pyplot as plt
import ipywidgets as widgets

from matplotlib import figure
from math import *

image_folder = "../../build/areas/"

def rnd(N=10000):
    return random.random(N)

def sq(x):
    return x * x

def generate_k_xz():
    phi = 2 * np.pi * rnd()
    r = np.cbrt(rnd())
    
    cos_t = 2 * rnd() - 1    
    sin_t = np.sin(np.arccos(cos_t))
    cos_p = np.cos(phi)
    sin_p = np.sin(phi)
    
    sx = r * sin_t * cos_p 
    sy = r * sin_t * sin_p
    sz = r * cos_t
    
    #sx = np.abs(sx)
    return sx, sz

def draw(x_coord, y_coord, xlabel, ylabel, filename):
    p = plt.figure(figsize=(8,5))
    d = (np.max(x_coord)-np.min(x_coord))
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.scatter(x_coord, y_coord, s=5*d, alpha=0.3)
    plt.savefig(os.path.join(image_folder, filename))

np.random.seed(123)
os.mkdir(image_folder)

M = 0.775
m = 0.140
R = 2.3000
k = sqrt(M * M / 4 - m * m)

sx, sz = generate_k_xz()
kx = sx * k
kz = sz * k
x = sq(kx * R / M) + sq(k) - sq(kz) - sq(R) / 4
a = sq(k) + sq(M) / 4 - x
b = kz * np.sqrt(sq(R) + sq(M))
Y = (a + b) / (a - b)
F = - (1 / x) * np.sqrt((sq(R) + sq(M)) * (sq(k) - sq(kz)) - sq(M) * x - sq(M * R) / 4)
F_ = np.clip(F, -100,100)
Dphi = np.arctan(F)
Dphi_ = np.array([x if x > 0 else x + np.pi for x in Dphi])
Dy = 0.5 * np.log(Y)

draw(Dy, Dphi_, "$\Delta y$", "$\Delta \phi$", "5")
draw(Y, F_, "$Y$", "$\Phi$", "4")
draw(Y, x, "$Y$", "$x$", "3")
draw(kz, x, "$k_z$", "$x$", "2")
draw(kz, kx, "$k_z$", "$k_x$", "1")