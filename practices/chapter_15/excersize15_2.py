from matplotlib import pyplot as plt

x_values = list(range(1, 5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.PuBu, edgecolors='None', s=10)
plt.title("Cube", fontsize=20)
plt.xlabel("Value", fontsize=14)
plt.axis([0, 5100, 0, 126000000000])

plt.show()



