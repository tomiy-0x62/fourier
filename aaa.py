import numpy as np

tmp = 0
for i in range(10000000):
    tmp += 1/(2*i-1)**4

print(tmp)
print(np.pi**4/96)
