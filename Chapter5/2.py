import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-5, 5, 400)
y = x**2
z = x**3
plt.plot(x, y, color='blue', label='y = x^2')
plt.plot(x, z, color='red', label='y = x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.title('dt y = x^2 va y = x^3')
plt.legend()
plt.show()