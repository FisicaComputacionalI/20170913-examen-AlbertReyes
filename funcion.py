import numpy as np
import pylab as plt
x = np.arrange(2012, 2018, 100)
y = 5*np.cos(2*np.pi*x)+2012
plt.plot(x,y)
plt.savefig('temp.png')
plt.show()