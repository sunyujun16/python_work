from die import Die
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
print(frequencies)

# # 对结果进行可视化处理
hist = pygal.Bar()

hist.title = "Results of rolling two D6s 1000 times"
hist.x_labels = [str(x) for x in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('diff_dice_visual.svg')

