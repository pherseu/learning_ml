import numpy as np

X, Y = np.loadtxt("01\pizza.txt", skiprows=1, unpack=True)

print(X[0:5])
print(Y[0:5])