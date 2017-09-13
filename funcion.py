import numpy as np
import pylab as pl
x=([2012:0.01:2018])
y=5*np.cos(2*np.pi*x)+2012
plt.plot(x,y)
plt.savefig('temp.png')
plt.show()
