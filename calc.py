import numpy as np
import matplotlib.pyplot as plt


k = np.arange(0, 1, 0.001)
k = np.delete(k, 0)

z = np.arange(0, 1, 0.001)
z = np.delete(z, 0)
solved = []
temp = 0

for i in range(len(k)):
    for c in range(len(z)):
        temp = k[i]**-2 + z[c]**-2
        if (temp > 15.9999) and (temp < 16.0001):
            solved.append('[' + str(k[i]) + ', ' + str(z[c]) + ']' + ' -> ' + str(temp))

for yes in range(len(solved)):
    print(solved[yes])         
  
            