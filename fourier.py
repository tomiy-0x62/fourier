import numpy as np
from matplotlib import pyplot

import function as fn

x = np.linspace(-np.pi * 5, np.pi * 5, 100)  #-5πから5πまでの範囲を100分割したnumpy配列
y = np.array([])
z = np.array([])

n = 1000

for i in x:
    y = np.append(y, fn.f(i, n))
    z = np.append(z, fn.g(i, n))

pyplot.grid()
pyplot.plot(x, y)
pyplot.plot(x, z)
pyplot.show()