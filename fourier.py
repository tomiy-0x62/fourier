import numpy as np
from matplotlib import pyplot

import function as fn

T = 2 * np.pi
x = np.linspace(-T * 2, T * 2, 100)  #-5πから5πまでの範囲を100分割したnumpy配列
y = np.array([])
z = np.array([])

n = 1000

for i in x:
    y = np.append(y, fn.k(i, n))
    #z = np.append(z, fn.h_o(i))

pyplot.grid()
pyplot.plot(x, y)
#pyplot.plot(x, z)
pyplot.show()
