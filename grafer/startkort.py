import matplotlib.pyplot as plt
import random
import numpy as np

deck = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]
x = []
N = 100000
n = 0

while n < N:
    n += 1
    choices = random.choices(deck, k=2)
    s = sum(choices)
    x.append(s)


plt.hist(x, bins=37, density=True)
plt.xticks(np.arange(3, 21, 1))
plt.xlabel("Sum av tall")
plt.ylabel("Prosent sjanse %")
plt.show()
