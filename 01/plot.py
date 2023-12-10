import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

X, Y = np.loadtxt("01\pizza.txt", skiprows=1, unpack=True)

#print(X[0:5])
#print(Y[0:5])

sns.set()
plt.axis([0,50,0,50])
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
plt.xlabel("Reservations", fontsize=30)
plt.ylabel("Pizzas", fontsize=30)
X, Y = np.loadtxt("01\pizza.txt", skiprows=1, unpack=True)
plt.plot(X, Y, "bo")
plt.show()