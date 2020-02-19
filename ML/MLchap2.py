import numpy as np
import matplotlib.pylab as plt

def step_function(x):
    y = x > 0
    return y.astype(np.int)

x = np.array([-1.0, 1.0, 2.0])
print(x)
y=x>0
print(y)
y = y.astype(np.int)
print(y)


def step_function2(x):
    return np.array(x>0,dtype=np.int)

x = np.arange(-5.0, 5.0, 0.1)
y = step_function2(x)
plt.plot(x, y)
plt.ylim(-0.1, 1.1)
plt.show()

def sigmoid(x):
    return 1/(1+np.exp(-x))

x = np.array([-1.0,1.0,2.0])
print(sigmoid(x))

print(1.0 + x)
print(1.0 / x)

x2 = np.arange(-5.0, 5.0 , 0.1)
y2 = sigmoid(x2)
plt.plot(x2, y2)
plt.ylim(-0.1,1.1)
plt.show()