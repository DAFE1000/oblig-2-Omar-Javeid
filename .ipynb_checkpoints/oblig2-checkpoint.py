import math
def f(x):
    return math.exp(-x/4) * math.atan(x)

def deriver(f,x,h=0.1):
    return (f(x + h) - f(x - h)) / (2*h)

# deriverte av e^-x/4 * tan^-1 x
def g(x):
    return math.atan(x) - 4/(1 + x**2)

def newton(g, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        gx = g(x)
        dgx = deriver(g, x)
        x_new = x - gx/dgx
        if abs(x_new -x) < tol:
            return x_new
        x = x_new
    return x

x_topp = newton(g, 1)
print(x_topp)

y_topp = f(x_topp)
print(y_topp)

import matplotlib.pyplot as plt

x_vals = np.linspace(0, 5, 100)
y_vals = [f(x) for x in x_vals]

plt.plot(x_vals, y_vals)
plt.scatter(x_topp, y_topp)  # marker toppunkt
plt.title("Graf av f(x)")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid()
plt.show()

