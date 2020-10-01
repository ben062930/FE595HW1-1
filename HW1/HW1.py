import matplotlib.pyplot as plt
import numpy as np

# set the period of 2*pi
x = np.arange(0,2*np.pi,0.01)
y_sin = np.sin(x)
y_cos = np.cos(x)
y_tan = np.tan(x)
# plot the curves
plt.plot(x,y_sin)
plt.plot(x,y_cos)
plt.plot(x,y_tan)

plt.ylim(-1.1, 1.1)
plt.show()

#The below is a revised version
if __name__ == "__main__":
    x = np.arange(0, 2 * np.pi, 0.001*np.pi)
    #to make plot smoother
    y_sin = np.sin(x)
    y_cos = np.cos(x)
    y_tan = np.tan(x)
    # plot the curves
    plt.plot(x, y_sin, color = "green", label = "sin")
    plt.plot(x, y_cos, color = "blue", label = "cos")
    plt.plot(x, y_tan, color = "red", label = "tan")

    plt.ylim(-1.1, 1.1)
    plt.show()  
