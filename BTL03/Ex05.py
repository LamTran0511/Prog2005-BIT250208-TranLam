import math
import matplotlib.pyplot as plt

x1 = list(range(-10, 11))
y1 = [x ** 2 for x in x1]

x2 = list(range(0, 11))
y2 = [math.sqrt(x) for x in x2]

plt.figure(figsize=(10, 4))

plt.subplot(1, 2, 1)
plt.plot(x1, y1)
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(1, 2, 2)
plt.plot(x2, y2)
plt.title("y = sqrt(x)")
plt.xlabel("x")
plt.ylabel("y")

plt.tight_layout()
plt.show()