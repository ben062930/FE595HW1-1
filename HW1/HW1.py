import matplotlib.pyplot as plt
import numpy as np

# set the period of 2*pi
x = np.arange(0,2*np.pi,0.01)
y_sin = np.sin(x)
y_cos = np.cos(x)

# plot the curves
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.show()

