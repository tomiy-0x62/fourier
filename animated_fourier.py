import numpy as np
import matplotlib.pyplot as plt
import time

import function as fn


ax, fig = plt.subplots()

x = np.linspace(-np.pi * 5, np.pi * 5, 100)  #-5πから5πまでの範囲を100分割したnumpy配列
y = np.array([])

while True:
    for n in range(1, 1000):
        for i in x:
            y = np.append(y, fn.f(i, n))
        fig.grid()
        fig.plot(x, y)
        fig.set_title("n = {}".format(n), loc="center")
        plt.pause(0.5)
        fig.cla()
        y = np.array([])

    time.sleep(3)
    plt.close()
