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