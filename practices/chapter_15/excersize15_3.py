from matplotlib import pyplot as plt
from random_walk.random_walk import RandomWalk

rw = RandomWalk(50000)
rw.fill_walk()

point_nums = list(range(rw.num_points))
plt.plot(rw.x_values, rw.y_values, linewidth=1)
plt.scatter(0, 0, c='green', s=100)
plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', s=100)

# 隐藏坐标轴
plt.axes().get_xaxis().set_visible(False)
plt.axes().get_yaxis().set_visible(False)

plt.figure(dpi=256, figsize=(20, 6))

plt.show()












