from matplotlib import pyplot as plt

products = ['A', 'B', 'C', 'D', 'E']
values = [30, 25, 15, 20, 10]

plt.pie(values, labels=products)
plt.title('Doanh so 5 sp')
plt.show()