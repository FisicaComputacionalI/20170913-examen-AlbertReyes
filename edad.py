import numpy as np
import matplotlib.pyplot as plt
x = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
y = x+1994
pl.title('Reyes Ramirez Luis Alberto')
pl.xlabel('edad')
pl.ylabel('anio')
pl.plot(x,y)
pl.savefig('temp.png')
pl.show()