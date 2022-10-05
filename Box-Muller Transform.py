

# Box-Muller Transform


import numpy as np
import matplotlib.pyplot as plt
from numpy.random import random
import seaborn as sb

n=1000000

x1=np.random.random(n)
x2=np.random.random(n)

r=np.sqrt(-2*np.log(x1))
theta=2*np.pi*x2
z1=r*np.cos(theta)
z2=r*np.sin(theta)

#plt.plot(z1,z2,label='Joint plot')
#plt.xlabel('z1')
#plt.ylabel('z2')
#sb.distplot(z1)
#sb.distplot(z2)
#sb.distplot(z2,color='yellow',label='z2')
plt.hist(z1,bins=50,color='crimson',label='z1',ec='blue')
plt.hist(z2,bins=50,color='darkorange',label='z2',ec='blue')
plt.legend()
plt.show()
