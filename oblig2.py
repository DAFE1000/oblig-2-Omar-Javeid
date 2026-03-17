import math


# deriverte av e^-x/4 * tan^-1 x
def g(x):
    return math.atan(x) - 4/(1 + x**2)