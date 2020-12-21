from die import Die
from collections import Counter
import pygal

die = Die()

results = []

for i in range(1000):
    result = die.roll()
    results.append(result)

# 计算每个点数出现的频率
# print(Counter(results))  # or....
frequencies = []

for value in range(1, die.num_sides+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# 对结果进行可视化处理
hist = pygal.Bar()

hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [str(x) for x in range(1, die.num_sides+1)]
hist.x_title = "Result"
hist._y_title = "Frequency of Result"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')

