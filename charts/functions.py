import matplotlib.pyplot as plt 
import numpy as np 


def sen(x):
    return np.sin(x)

def tan(x):
    return np.tan(x)

x = np.linspace(0,10,100)
y= sen(x)

fig, axes =plt.subplots()

axes.plot(x,y)
plt.savefig("fig.jpg")

y=tan(x)

axes.plot(x,y)
plt.savefig("tang.jpg")