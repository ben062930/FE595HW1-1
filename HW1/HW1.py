import matplotlib.pyplot as plt
import numpy as np

def hw1():
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

#The below is a revised version
if __name__ == "__main__":
 hw1()
