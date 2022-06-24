import numpy as np

def f(t, n_max):
    # [-π,π)でf(t)=tとなる周期2πのノコギリ波
    tmp = 0
    for n in range(1, n_max):
        tmp += (-2/n) * (-1)**n * np.sin(n*t)
    return tmp

def g(t, n_max):
     # [-π,π)でf(t)={1 (0<=t<π), -1 (-π<=t<0)}となる周期2πの矩形波
    tmp = 0
    for n in range(1, n_max):
        tmp += (-2/(n*np.pi)) * ((-1)**n -1) * np.sin(n*t)
    return tmp

def h_o(t):
    a = 0.6
    t = abs(t)
    t = t - int(t)
    if (t <= a):
        return 1
    else:
        return 0

def h(t, n_max):
    a = 0.6
    tmp = a
    for n in range(1, n_max):
        tmp += 2 * np.sin(np.pi*a*n) * np.cos(np.pi*n*t) / (n * np.pi)
    return tmp

def i(t, n_max):
    tmp = 2 * np.pi**2 / 3
    for n in range(1, n_max):
        tmp += 4 * (-1)**n * np.cos(n*t) / n**2
    return tmp

def j(t, n_max):
    tmp = 0
    for n in range(1, n_max):
        tmp += 4* (np.sin(n*np.pi) - np.sin(n*np.pi/2)) * np.sin(n*t) / (n**2 * np.pi)
    return tmp

def k(t, n_max):
    tmp = 0
    for n in range(-n_max, n_max):
        tmp += -1 * ( (-1)**n -1 ) / ( 2*np.pi*n )
