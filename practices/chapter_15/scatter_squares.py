import matplotlib.pyplot as plt

# x_values = [1, 2, 3, 4, 5]
# y_values = [1, 4, 9, 16, 25]
x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]

# plt.scatter(x_values, y_values, edgecolor='none', s=10, c='darkred')  # s是点的大小
# plt.scatter(x_values, y_values, edgecolor='none', s=10, c=(0, 0, 0.8))
plt.scatter(x_values, y_values, edgecolor='none', s=10, c=y_values, cmap=plt.cm.Blues)

# 设置图表标题并加轴标签
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Squares of Value", fontsize=14)

# 刻度标记
plt.tick_params(axis='both', which='major', labelsize=14)

# 设置每个坐标轴的取值范围
plt.axis([0, 1100, 0, 1100000])

plt.savefig('scatter_squares.png', bbox_inches='tight')