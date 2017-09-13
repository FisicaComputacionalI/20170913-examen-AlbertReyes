import numpy as np
import matplotlib.pyplot as plt
x1 = ([0:1:23])
y1 = x+1994
plt.title('Reyes Ramirez Luis Alberto')
plt.xlabel('edad')
plt.ylabel('anio')
x2 = ([2012:100:2018])
y2 = 5*np.cos(2*np.pi*x)+2012
plt.plot(x1, y1, x2, y2, ,'r')
plt.savefig('temp.png')
plt.show()
