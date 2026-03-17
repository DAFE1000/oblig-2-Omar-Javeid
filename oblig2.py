import math
import numpy as np

def f(x):
    return math.exp(-x/4) * math.atan(x)

def deriver(f,x,h=0.1):
            return (f(x + h) - f(x - h)) / (2*h)

print(deriver(f,0))