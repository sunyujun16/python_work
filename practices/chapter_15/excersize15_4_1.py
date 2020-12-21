import pygal
from matplotlib import pyplot as plt
from random_walk.random_walk import RandomWalk


# while True:
#     keep_running = input('continue or not? y/n')
#     if keep_running == 'n':
#         break

times =1000
rw = RandomWalk(times)
rw.fill_walk()

point_nums = list(range(1, rw.num_points+1))

# 用pygal实现可视化
hist = pygal.Bar()

hist.title = "Random walk in Pygal"
hist.x_labels = [str(i) for i in point_nums]
hist.x_title = "steps"
hist.y_title = "xy_values"

hist.add('Random walk x', rw.x_values)
hist.add('Random Walk y', rw.y_values)
hist.render_to_file('excersize15_4_1.svg')


















