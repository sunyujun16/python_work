from matplotlib import pyplot as plt
from dice.die import Die
from collections import Counter
import pygal

die_1 = Die()
die_2 = Die(10)

results = []

times = 50000
for i in range(times):
    result_1 = die_1.roll()
    result_2 = die_2.roll()
    results.append(result_1 + result_2)

# 计算每个点数出现的频率
# counts = Counter(results)
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)
# print(frequencies)

x_labels = list(range(2, max_result+1))
# print(x_labels)
# plt.plot(x_labels, frequencies)
plt.scatter(x_labels, frequencies, c='red', edgecolors='None', s=5)
plt.title("D6 + D10, 50000 times", fontsize=24)

plt.show()













