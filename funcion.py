import numpy as np
import matplotlib.pyplot as plt
def f(x):
    return 5*np.cos(2*np.pi*x)+2012
x = np.arange(2012, 2018, 100)
plt.plot(x, f(x))
plt.savefig('temp.png')
plt.show()
