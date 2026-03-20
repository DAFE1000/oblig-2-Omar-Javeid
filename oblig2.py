import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

f = lambda x: np.exp(-x/4)*np.arctan(x)

g = lambda x: np.arctan(x) - 4/(x**2 + 1)

x0 = 1.7
x_topp = fsolve(g, x0)[0]
y_topp = f(x_topp)

print(x_topp, y_topp)

# plot
x = np.linspace(0,5,100)
y = f(x)

plt.plot(x,y)
plt.scatter(x_topp, y_topp)
plt.title("Graf til f(x)")
plt.show()