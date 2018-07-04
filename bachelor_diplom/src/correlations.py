import math
import numpy
import random
from correlations_api import *
from numpy import pi
from functools import partial


def rand_angle():
    return (2 *random.random() - 1) * pi


def gauss_momentum_component(q0):
    return random.normalvariate(0.0, q0 / math.sqrt(2))

    
def gauss_momentum(q0):
    qx = gauss_momentum_component(q0)
    qy = gauss_momentum_component(q0)
    return math.sqrt(qx * qx + qy * qy)


def laplace_momentum(q0):
    return random.gammavariate(2.0, q0)
    

def const_theory_alpha_distribution(a):
    if a <= pi:
        return a / (pi * pi)
    elif pi < a <= 2 * pi:
        return (2 * pi - a) / (pi * pi)
    return 0.0

    
def const_theory_momentum_distribution(p):
    rho = p / (2 * q0)
    if rho >= 1.0:
        return numpy.nan
    return (2 / pi) * (1 / (2 * q0)) * (1 / math.sqrt(1.0 -  rho * rho))


def gauss_theory_alpha_distribution(a):
    y = math.cos(a)
    c = math.sqrt(1 - y * y / 4)
    return (3 / (8 * pi)) * (c - (y / 2) * math.acos(y / 2)) / (c ** 3)


def get_alpha_const():
    f1 = rand_angle()
    f2 = rand_angle()
    f3 = rand_angle()
    f = 1 if (f3 - f2) * (f2 - f1) >= 0 else 0  
    alpha = (2 * f - 1) * abs(f3 - f1) / 2 + (1 - f) * pi
    alpha = pi + random.choice((-1, 1)) * (pi -alpha)
    return alpha


def get_momentum_const(q0):
    f1 = rand_angle()
    f2 = rand_angle()
    return 2 * q0 * abs(math.cos((f2 - f1) / 2.0))


def get_momentum_gauss(q0):
    q1 = gauss_momentum(q0)
    q2 = gauss_momentum(q0)
    f1 = rand_angle()
    f2 = rand_angle()
    return math.sqrt(q1 * q1 + q2 * q2 - 2 * q1 * q2 * math.cos(f2 - f1))


def get_alpha_gauss(q0):
    q1x = gauss_momentum_component(q0)
    q2x = gauss_momentum_component(q0)
    q3x = gauss_momentum_component(q0)
    q1y = gauss_momentum_component(q0)
    q2y = gauss_momentum_component(q0)
    q3y = gauss_momentum_component(q0)
    p1x = q2x - q1x
    p2x = q3x - q2x
    p1y = q2y - q1y
    p2y = q3y - q2y
    p1 = math.sqrt(p1x * p1x + p1y * p1y)
    p2 = math.sqrt(p2x * p2x + p2y * p2y)
    alpha = math.acos((p1x * p2x + p1y  * p2y) / (p1 * p2))
    alpha = pi + random.choice((-1, 1)) * (pi -alpha)
    return alpha


def get_momentum_laplace(q0):
    q1 = laplace_momentum(q0)
    q2 = laplace_momentum(q0)
    f1 = rand_angle()
    f2 = rand_angle()
    return math.sqrt(q1 * q1 + q2 * q2 - 2 * q1 * q2 * math.cos(f2 - f1))


def get_alpha_laplace(q0):
    q1 = laplace_momentum(q0)
    q2 = laplace_momentum(q0)
    q3 = laplace_momentum(q0)
    f1 = rand_angle()
    f2 = rand_angle()
    f3 = rand_angle()
    q1x = q1 * math.cos(f1)
    q2x = q2 * math.cos(f2)
    q3x = q3 * math.cos(f3)
    q1y = q1 * math.sin(f1)
    q2y = q2 * math.sin(f2)
    q3y = q3 * math.sin(f3)
    p1x = q2x - q1x
    p2x = q3x - q2x
    p1y = q2y - q1y
    p2y = q3y - q2y
    p1 = math.sqrt(p1x * p1x + p1y * p1y)
    p2 = math.sqrt(p2x * p2x + p2y * p2y)
    alpha = math.acos((p1x * p2x + p1y  * p2y) / (p1 * p2))
    alpha = pi + random.choice((-1, 1)) * (pi -alpha)
    return alpha

for n in [10000, 100000]:
    q0 = 1.0
    plot_distribution = partial(plot_distribution, N=n,
                                calculate_function=lambda: 0,
                                theory_function=lambda x: numpy.nan)
    plot_alpha_distribution = partial(plot_distribution, string_name=r"\Delta \phi",
                                      left_bound=0, right_bound=2 * pi, da=2*pi/50)
    plot_momentum_distribution = partial(plot_distribution, string_name=r"p",
                                         left_bound=0.0, right_bound=2*q0, da=2*q0/25)

    ## CONST
    plot_alpha_distribution(calculate_function=get_alpha_const,
                            theory_function=const_theory_alpha_distribution,
                            picture_name="const_alpha")         

    plot_momentum_distribution(calculate_function=partial(get_momentum_const, q0),
                               theory_function=const_theory_momentum_distribution,
                               picture_name="const_momentum")


    ## GAUSS
    plot_momentum_distribution(calculate_function=partial(get_momentum_gauss, q0),
                               theory_function=lambda p: p * math.exp(-(p * p) / (2 * q0 * q0)) / q0 /q0,
                               right_bound=4*q0,
                               picture_name="gauss_momentum")

    plot_alpha_distribution(calculate_function=partial(get_alpha_gauss, q0),
                            theory_function=gauss_theory_alpha_distribution,
                            picture_name="gauss_alpha")

    ## LAPLACE
##    plot_alpha_distribution(calculate_function=partial(get_alpha_laplace, q0),
##                            picture_name="laplace_alpha")
##    plot_momentum_distribution(calculate_function=partial(get_momentum_laplace, q0),
##                               right_bound=4*q0*math.sqrt(2),
##                               picture_name="laplace_momentum")
